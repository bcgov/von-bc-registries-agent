#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor, CORP_TYPES_IN_SCOPE
from bcreg.bcregistries import BCRegistries
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


"""
This script will populate an audit table (CORP_AUDIT_LOG) in the event processor database to identify
corporations inputted from BC Registries (CORP_HISTORY_LOG) but with no Registration credential
posted to OrgBook (CREDENTIAL_LOG table).

    ./run-step.sh bcreg/populate_audit_table.py

Once this job completes, run the following sql to see how many companies are 'missed':

    select count(*) from CORP_AUDIT_LOG where LAST_CREDENTIAL_ID is null;

To force re-process of these companies, run the following sql's:

    update corp_history_log
    set process_success = null, process_date = null, process_msg = null
    where process_success is not null
    and corp_num in
    (select corp_num from CORP_AUDIT_LOG where LAST_CREDENTIAL_ID is null);

    commit;

Then run the following script to re-generate the credentials (note this runs on cached data and does not
re-query the BC Reg database):

    ./run-step.sh bcreg/generate-creds.py

Once this completes, re-run this script:

    ./run-step.sh bcreg/populate_audit_table.py

Re-run the 'select count(*) ...' query again and the numbers should now balance.
"""

QUERY_LIMIT = '200000'
REPORT_COUNT = 10000
ERROR_THRESHOLD_COUNT = 5

bc_reg_count = 0
with BCRegistries() as bc_registries:
    # run this query against BC Reg database:
    sql1 = """
    select corp.corp_num, corp.corp_typ_cd
    from bc_registries.corporation corp
    where corp.corp_num not in (
        select corp_num from bc_registries.corp_state where state_typ_cd = 'HWT');
    """

    print("Get corp stats from BC Registries DB", datetime.datetime.now())
    bc_reg_recs = bc_registries.get_bcreg_sql("corp_stats", sql1, cache=False)
    for bc_reg_rec in bc_reg_recs:
        if bc_reg_rec['corp_typ_cd'] in CORP_TYPES_IN_SCOPE:
            bc_reg_count = bc_reg_count + 1


with EventProcessor() as event_processor:
    # run this query against Event Processor database:
    sql1a = "select COALESCE(MAX(LAST_CORP_HISTORY_ID), 0) from CORP_AUDIT_LOG"
    sql2 = """
    SELECT record_id, system_type_cd, corp_num, corp_state, corp_json->>'corp_typ_cd' as corp_typ_cd, last_event->>'event_id' as last_event_id, last_event->>'event_date' as last_event_date, entry_date, process_date, process_msg 
    FROM corp_history_log
    WHERE record_id > %s AND process_date is not null
    ORDER BY record_id
    limit """ + QUERY_LIMIT + """;
    """
    continue_loop = True
    i = 0
    while continue_loop:
        print("Get corp history processed rec id", datetime.datetime.now())
        event_proc_inbound_recid = event_processor.get_event_proc_sql("inbound_recid", sql1a)
        print("Get corp history from Event Processor DB", datetime.datetime.now())
        event_proc_inbound_recs = event_processor.get_event_proc_sql("inbound_recs", sql2, (event_proc_inbound_recid[0]['coalesce'],))
        print("... build audit log", datetime.datetime.now())
        continue_loop = 0 < len(event_proc_inbound_recs)
        for inbound_rec in event_proc_inbound_recs:
            if inbound_rec['corp_typ_cd'] in CORP_TYPES_IN_SCOPE and inbound_rec['corp_state'] != 'HWT':
                i = i + 1
                if (i % REPORT_COUNT == 0):
                    print('>>> Processing {} {}.'.format(i, datetime.datetime.now()))

                if inbound_rec['process_msg'] and inbound_rec['process_msg'] == 'Withdrawn':
                    # skip
                    pass
                else:
                    # see if we have a record for this corp yet
                    sql2a = """
                    SELECT RECORD_ID, LAST_CORP_HISTORY_ID, SYSTEM_TYPE_CD, LAST_EVENT_DATE, CORP_NUM, CORP_STATE, CORP_TYPE, ENTRY_DATE
                    FROM CORP_AUDIT_LOG WHERE CORP_NUM = %s;
                    """
                    corp_recs = event_processor.get_event_proc_sql("corp_recs", sql2a, (inbound_rec['corp_num'],))
                    if 0 == len(corp_recs):
                        # if not, add it
                        sql2b = """
                        INSERT INTO CORP_AUDIT_LOG 
                        (LAST_CORP_HISTORY_ID, SYSTEM_TYPE_CD, LAST_EVENT_DATE, CORP_NUM, CORP_STATE, CORP_TYPE, ENTRY_DATE)
                        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;
                        """
                        cur = None
                        try:
                            cur = event_processor.conn.cursor()
                            cur.execute(sql2b, (inbound_rec['record_id'], inbound_rec['system_type_cd'], inbound_rec['last_event_date'], inbound_rec['corp_num'], inbound_rec['corp_state'], inbound_rec['corp_typ_cd'], datetime.datetime.now(),))
                            _record_id = cur.fetchone()[0]
                            event_processor.conn.commit()
                            cur.close()
                            cur = None
                        except (Exception, psycopg2.DatabaseError) as error:
                            print(error)
                            raise
                        finally:
                            if cur is not None:
                                cur.close()
                    else:
                        # if yes, see if we need to update it
                        sql2c = """
                        UPDATE CORP_AUDIT_LOG
                        SET LAST_CORP_HISTORY_ID = %s, LAST_EVENT_DATE = %s, CORP_STATE = %s, CORP_TYPE = %s, ENTRY_DATE = %s
                        WHERE RECORD_ID = %s AND CORP_NUM = %s;
                        """
                        cur = None
                        corp_rec = corp_recs[0]
                        try:
                            cur = event_processor.conn.cursor()
                            cur.execute(sql2c, (inbound_rec['record_id'], inbound_rec['last_event_date'], inbound_rec['corp_state'], inbound_rec['corp_typ_cd'], datetime.datetime.now(), corp_rec['record_id'], corp_rec['corp_num'],))
                            event_processor.conn.commit()
                            cur.close()
                            cur = None
                        except (Exception, psycopg2.DatabaseError) as error:
                            print(error)
                            raise
                        finally:
                            if cur is not None:
                                cur.close()

with EventProcessor() as event_processor:
    # run this query against Event Processor database:
    sql1b = "select COALESCE(MAX(LAST_CREDENTIAL_ID), 0) from CORP_AUDIT_LOG where corp_state = 'ACT'"
    sql1c = "select COALESCE(MAX(LAST_CREDENTIAL_ID), 0) from CORP_AUDIT_LOG where corp_state = 'HIS'"
    sql3s = [
    """
    SELECT record_id, corp_num, credential_json->>'entity_status' as corp_state, credential_json->>'entity_type' as corp_typ_cd, credential_json->>'effective_date' as effective_date, entry_date, process_date 
    FROM credential_log 
    WHERE process_date is not null and credential_type_cd = 'REG'
      AND ((corp_state = 'ACT' and record_id > %s) OR  (corp_state = 'HIS' and record_id > %s))
    ORDER BY record_id
    limit """ + QUERY_LIMIT + """;
    """,
    """
    SELECT record_id, corp_num, credential_json->>'entity_status' as corp_state, credential_json->>'entity_type' as corp_typ_cd, credential_json->>'effective_date' as effective_date, entry_date, process_date 
    FROM credential_log 
    WHERE process_date is not null and credential_type_cd = 'REG'
      AND corp_num in (select corp_num from CORP_AUDIT_LOG where last_credential_id is null)
    ORDER BY record_id
    limit """ + QUERY_LIMIT + """;
    """,
    ]
    for sql3 in sql3s:
        continue_loop = True
        i = 0
        while continue_loop:
            print("Get corp REG processed rec ids", datetime.datetime.now())
            event_proc_outbound_act_recid = event_processor.get_event_proc_sql("outbound_act_recid", sql1b)
            event_proc_outbound_his_recid = event_processor.get_event_proc_sql("outbound_his_recid", sql1c)
            print("Get corp REG credentials from Event Processor DB", datetime.datetime.now())
            event_proc_outbound_recs = event_processor.get_event_proc_sql("outbound_recs", sql3, (event_proc_outbound_act_recid[0]['coalesce'], event_proc_outbound_his_recid[0]['coalesce'],))
            print("... build audit log", datetime.datetime.now())
            continue_loop = 0 < len(event_proc_outbound_recs)
            for outbound_rec in event_proc_outbound_recs:
                if outbound_rec['corp_typ_cd'] in CORP_TYPES_IN_SCOPE:
                    i = i + 1
                    if (i % REPORT_COUNT == 0):
                        print('>>> Processing {} {}.'.format(i, datetime.datetime.now()))
                    # see if we have a record for this corp yet
                    sql3a = """
                    SELECT RECORD_ID, LAST_CORP_HISTORY_ID, SYSTEM_TYPE_CD, LAST_EVENT_DATE, CORP_NUM, CORP_STATE, CORP_TYPE, ENTRY_DATE,
                            LAST_CREDENTIAL_ID, CRED_EFFECTIVE_DATE
                    FROM CORP_AUDIT_LOG WHERE CORP_NUM = %s;
                    """
                    corp_recs = event_processor.get_event_proc_sql("corp_recs", sql3a, (outbound_rec['corp_num'],))
                    if 0 == len(corp_recs):
                        # if not, it's an error
                        # ignore for now
                        print("Error no inbound record found for", outbound_rec['corp_num'])
                        pass
                    else:
                        # if yes, see if we need to update it
                        sql3b = """
                        UPDATE CORP_AUDIT_LOG
                        SET LAST_CREDENTIAL_ID = %s, CRED_EFFECTIVE_DATE = %s
                        WHERE RECORD_ID = %s AND CORP_NUM = %s;
                        """
                        cur = None
                        corp_rec = corp_recs[0]
                        try:
                            cur = event_processor.conn.cursor()
                            cur.execute(sql3b, (outbound_rec['record_id'], outbound_rec['effective_date'], corp_rec['record_id'], corp_rec['corp_num']))
                            event_processor.conn.commit()
                            cur.close()
                            cur = None
                        except (Exception, psycopg2.DatabaseError) as error:
                            print(error)
                            raise
                        finally:
                            if cur is not None:
                                cur.close()

print("Got all corp audits", datetime.datetime.now())

# now check counts
evp_corp_history_count = 0
evp_credential_count = 0
with EventProcessor() as event_processor:
    sql1 = """
    SELECT count(*) FROM CORP_AUDIT_LOG;
    """
    sql2 = """
    SELECT count(*) FROM CORP_AUDIT_LOG WHERE last_credential_id is not null;
    """
    evp_corp_history_count = event_processor.get_sql_record_count(sql1)
    evp_credential_count = event_processor.get_sql_record_count(sql2)

if evp_corp_history_count != bc_reg_count:
    print("Error missing corps in Event Processor", bc_reg_count, evp_corp_history_count)
    if ERROR_THRESHOLD_COUNT < abs(evp_corp_history_count - bc_reg_count):
        log_error("Error missing corps in Event Processor: reg={} evp={}".format(bc_reg_count, evp_corp_history_count))
    else:
        log_warning("Warning missing corps in Event Processor: reg={} evp={}".format(bc_reg_count, evp_corp_history_count))

if evp_credential_count != evp_corp_history_count:
    print("Error missing credentials in Event Processor", evp_corp_history_count, evp_credential_count)
    if ERROR_THRESHOLD_COUNT < abs(evp_credential_count - evp_corp_history_count):
        log_error("Error missing credentials in Event Processor: evp corps={} evp creds={}".format(evp_corp_history_count, evp_credential_count))
    else:
        log_warning("Warning missing credentials in Event Processor: evp corps={} evp creds={}".format(evp_corp_history_count, evp_credential_count))

