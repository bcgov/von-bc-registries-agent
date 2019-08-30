#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor, CORP_TYPES_IN_SCOPE
from bcreg.bcregistries import BCRegistries

import argparse


"""
This script identifies missing corps based on the BC Registries, Event Processor and OrgBook databases.

Note:  This report runs based on the audit table, populated by the `populate_audit_table.py` script

Note:  For any companies that are identified as "missing" by this report, re-run with "--fixme" to get these
       companies auto-re-queued for processing

1. Stop any scheduled jobs (cron)
2. Run this script with "--fixme"
3. Run the "initial reload" and "post credentials" jobs
4. Re-run the audit report
5. Restart the cron jobs

After step 4 above, try re-running this script to verify the counts are correct.
"""


parser = argparse.ArgumentParser(description='Audit BC Reg vs OrgBook.')
parser.add_argument("--fixme", action='store_true', help="Add missing corps to processing queue", required=False)
args = parser.parse_args()
if args.fixme:
    print("FIX incorrect corps")
else:
    print("DON'T fix incorrect corps")

stats_dict = {}
def add_stats_to_dict(key, type):
    if not key in stats_dict:
        stats_dict[key] = {'bc_reg': 0, 'event_proc_inbound': 0, 'event_proc_outbound': 0, 'orgbook': 0}
    stats_dict[key][type] = stats_dict[key][type] + 1


corps_dict = {}
def add_corp_to_dict(corp_num, key, type):
    if corp_num.startswith('BC'):
        corp_num = corp_num[2:]
    if not corp_num in corps_dict:
        corps_dict[corp_num] = {}
    corps_dict[corp_num][type] = key


with BCRegistries() as bc_registries:
    # run this query against BC Reg database:
    sql1 = """
    select corp.corp_num, 
           corp.corp_typ_cd,
           op_state.op_state_typ_cd
    from bc_registries.corporation corp, 
          bc_registries.corp_state state,
       bc_registries.corp_op_state op_state
    where state.corp_num = corp.corp_num
      and state.end_event_id is null
      and op_state.state_typ_cd = state.state_typ_cd
      and state.state_typ_cd != 'HWT';
    """

    print("Get corp stats from BC Registries DB", datetime.datetime.now())
    bc_reg_recs = bc_registries.get_bcreg_sql("corp_stats", sql1, cache=False)
    for bc_reg_rec in bc_reg_recs:
        if bc_reg_rec['corp_typ_cd'] in CORP_TYPES_IN_SCOPE:
            key = bc_reg_rec['corp_typ_cd'] + ',' + bc_reg_rec['op_state_typ_cd']
            add_stats_to_dict(key, 'bc_reg')
            add_corp_to_dict(bc_reg_rec['corp_num'], key, 'bc_reg')
    #print(bc_reg_stats)


with EventProcessor() as event_processor:
    # run this query against Event Processor database:
    sql2 = """
    SELECT last_corp_history_id, last_event_date, corp_num, corp_type, corp_state, entry_date, last_credential_id, cred_effective_date
    FROM corp_audit_log
    ORDER BY record_id;
    """

    print("Get corp stats from Event Processor DB", datetime.datetime.now())
    processed_inbound_corps = {}
    event_proc_inbound_recs = event_processor.get_event_proc_sql("inbound_recs", sql2)
    for inbound_rec in event_proc_inbound_recs:
        if inbound_rec['corp_type'] in CORP_TYPES_IN_SCOPE and inbound_rec['corp_state'] != 'HWT':
            if not inbound_rec['corp_num'] in processed_inbound_corps.keys():
                key = inbound_rec['corp_type'] + ',' + inbound_rec['corp_state']
                add_stats_to_dict(key, 'event_proc_inbound')
                add_corp_to_dict(inbound_rec['corp_num'], key, 'event_proc_inbound')
                processed_inbound_corps[inbound_rec['corp_num']] = 'Done'

    # run this query against Event Processor database:
    sql3 = """
    SELECT last_corp_history_id, last_event_date, corp_num, corp_type, corp_state, entry_date, last_credential_id, cred_effective_date
    FROM corp_audit_log
    WHERE last_credential_id is not null
    ORDER BY record_id;
    """

    print("Get corp stats from Event Processor DB", datetime.datetime.now())
    processed_outbound_corps = {}
    event_proc_outbound_recs = event_processor.get_event_proc_sql("outbound_recs", sql3)
    for outbound_rec in event_proc_outbound_recs:
        if outbound_rec['corp_type'] in CORP_TYPES_IN_SCOPE:
            if not outbound_rec['corp_num'] in processed_outbound_corps.keys():
                key = outbound_rec['corp_type'] + ',' + outbound_rec['corp_state']
                add_stats_to_dict(key, 'event_proc_outbound')
                add_corp_to_dict(outbound_rec['corp_num'], key, 'event_proc_outbound')
                processed_outbound_corps[outbound_rec['corp_num']] = 'Done'
    #print(event_proc_outbound_stats)

    sql3a = """
    SELECT corp_num from event_by_corp_filing where process_success is null
      and prev_event_id = 0;
    """
    sql3b = """
    SELECT corp_num from event_by_corp_filing where process_success is null;
    """

    print("Get corps still outstanding from Event Processor DB", datetime.datetime.now())
    un_processed_outbound_corps = {}
    event_un_proc_outbound_recs = event_processor.get_event_proc_sql("outbound_un_recs", sql3a)
    for outbound_rec in event_un_proc_outbound_recs:
        un_processed_outbound_corps[outbound_rec['corp_num']] = outbound_rec['corp_num']
    #print(un_processed_outbound_corps)
    semi_processed_outbound_corps = {}
    event_semi_proc_outbound_recs = event_processor.get_event_proc_sql("outbound_semi_recs", sql3b)
    for outbound_rec in event_semi_proc_outbound_recs:
        semi_processed_outbound_corps[outbound_rec['corp_num']] = outbound_rec['corp_num']
    #print(semi_processed_outbound_corps)


# now something to read orgbook:
print("Connect to OrgBook DB")
conn = None
try:
    params = config(section='org_book')
    conn = psycopg2.connect(**params)
except (Exception) as error:
    print(error)
    conn = None
    log_error("OrgBook exception connecting to DB: " + str(error))
    raise

if conn:
    cursor = None
    try:
        # run this query against OrgBook Search database
        sql4 = """
                select 
                  source_id,
                  credential_id, 
                  MAX(CASE WHEN claim_name='entity_type' THEN claim_value END) corp_typ_cd,
                  MAX(CASE WHEN claim_name='entity_status' THEN claim_value END) corp_state
                from (
                select topic.source_id as source_id, claim.credential_id as credential_id, claim.name as claim_name, claim.value as claim_value
                from credential_set, credential, claim, topic
                where credential_set.credential_type_id in (select id from credential_type where description like 'Registration%' or description like 'registration%')
                    and credential.id = credential_set.latest_credential_id
                    and topic.id = credential_set.topic_id
                    and claim.credential_id = credential.id
                    and claim.name in ('registration_id', 'entity_type', 'entity_status')) as foo
                group by source_id, credential_id;
        """

        print("Get corp stats from OrgBook DB", datetime.datetime.now())
        cursor = conn.cursor()
        cursor.execute(sql4)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        orgbook_stats = [dict(zip(column_names, row))  
            for row in cursor]
        cursor.close()
        cursor = None
        for orgbook_stat in orgbook_stats:
            if orgbook_stat['corp_typ_cd'] in CORP_TYPES_IN_SCOPE:
                key = orgbook_stat['corp_typ_cd'] + ',' + orgbook_stat['corp_state']
                add_stats_to_dict(key, 'orgbook')
                add_corp_to_dict(orgbook_stat['source_id'], key, 'orgbook')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        log_error("Event Processor exception reading DB: " + str(error))
        raise 
    finally:
        if cursor is not None:
            cursor.close()
        cursor = None
        if conn:
            conn.close()
    #print(orgbook_stats)

print("Got all stats!!!", datetime.datetime.now())



print("Overall stats:")
print(json.dumps(stats_dict))
print("===========================")
print("Company Type,Company Status,bc_reg,event_proc_inbound,event_proc_outbound,orgbook")
for key, value in stats_dict.items():
    print(key + ',' + str(value['bc_reg']) + ',' + str(value['event_proc_inbound']) + ',' + str(value['event_proc_outbound']) + ',' + str(value['orgbook']))
print("===========================")
print("Incomplete data in OrgBook:")
print("===========================")
print("Company Type,Company Status,bc_reg,orgbook,orgbook_diff")
for key, value in stats_dict.items():
    if 0 != (value['bc_reg'] - value['orgbook']):
        print(key + ',' + str(value['bc_reg']) + ',' + str(value['orgbook']) + ',' + str(value['bc_reg'] - value['orgbook']))
print("===========================")
print("Incomplete data in Event Processor:")
print("===========================")
print("Company Type,Company Status,event_proc_inbound,event_proc_outbound,event_proc_diff")
for key, value in stats_dict.items():
    if 0 != (value['event_proc_inbound'] - value['event_proc_outbound']):
        print(key + ',' + str(value['event_proc_inbound']) + ',' + str(value['event_proc_outbound']) + ',' + str(value['event_proc_inbound'] - value['event_proc_outbound']))
print("===========================")


def add_missing_corps_to_queue(specific_corps):
    system_type = 'BC_REG'
    with BCRegistries() as bc_registries:
        with EventProcessor() as event_processor:
            print("Get last processed event")
            prev_event_id = 0

            print("Get last max event")
            max_event_date = event_processor.get_last_processed_event_date(system_type)
            max_event_id = event_processor.get_last_processed_event(max_event_date, system_type)
            
            # get specific test corps (there are about 6)
            print("Get specific corps")
            corps = bc_registries.get_specific_corps(specific_corps)
            
            print("Find unprocessed events for each corp")
            last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
            max_event_dt = bc_registries.get_event_effective_date(max_event_id)
            corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id, max_event_dt, corps)
            
            print("Update our queue")
            event_processor.update_corp_event_queue(system_type, corps, max_event_id, max_event_date)


MAX_SPECIFIC_CORPS = 500
specific_corps_1 = []
missing_corps = {'bc_reg': 0, 'event_proc_inbound': 0, 'event_proc_outbound': 0, 'orgbook': 0}
specific_corps_2 = []
specific_corps_3 = []
incorrect_corps = {'bc_reg': 0, 'event_proc_inbound': 0, 'event_proc_outbound': 0, 'orgbook': 0}
for corp_num, corp_set in corps_dict.items():
    if corp_num in un_processed_outbound_corps:
        # skip records that are still outstanding
        pass
    elif not 'orgbook' in corp_set:
        # company is missing in orgbook
        missing_corps['orgbook'] = missing_corps['orgbook'] + 1
        # check if company is partly processed
        if 'event_proc_inbound' in corp_set and not 'event_proc_outbound' in corp_set:
            # in the inbound processing queue but no credentials generated
            missing_corps['event_proc_outbound'] = missing_corps['event_proc_outbound'] + 1
            if len(specific_corps_3) < MAX_SPECIFIC_CORPS:
                specific_corps_3.append(corp_num)
        else:
            if len(specific_corps_1) < MAX_SPECIFIC_CORPS:
                specific_corps_1.append(corp_num)
    elif corp_num in semi_processed_outbound_corps:
        # skip records that are still outstanding
        pass
    elif 'bc_reg' in corp_set:
        if corp_set['orgbook'] != corp_set['bc_reg']:
            # company is in orgbook but company type and/or status is wrong
            incorrect_corps['orgbook'] = incorrect_corps['orgbook'] + 1
            if len(specific_corps_2) < MAX_SPECIFIC_CORPS:
                specific_corps_2.append(corp_num)
    else:
        print(corp_num, 'in orgbook but not bc_reg, weird ...')

print("Total of", missing_corps['orgbook'], "corps MISSING in orgbook")
print(specific_corps_1)
print("Total of", missing_corps['event_proc_outbound'], "corps MISSING in event processing outbound queue")
print(specific_corps_3)
print("Total of", incorrect_corps['orgbook'], "corps INCORRECT in orgbook")
print(specific_corps_2)

if args.fixme:
    if 0 < len(specific_corps_1):
        print("Adding MISSING", len(specific_corps_1), "corps to outstanding queue ...")
        #print(specific_corps_1)
        add_missing_corps_to_queue(specific_corps_1)

    if 0 < len(specific_corps_3):
        print("Adding MISSING", len(specific_corps_3), "corps to outstanding queue ...")
        #print(specific_corps_2)
        add_missing_corps_to_queue(specific_corps_3)

    if 0 < len(specific_corps_2):
        print("Adding INCORRECT", len(specific_corps_2), "corps to outstanding queue ...")
        #print(specific_corps_2)
        add_missing_corps_to_queue(specific_corps_2)

