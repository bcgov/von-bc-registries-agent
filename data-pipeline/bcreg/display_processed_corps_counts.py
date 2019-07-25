#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries


stats_dict = {}
def add_stats_to_dict(key, type):
    if not key in stats_dict:
        stats_dict[key] = {'bc_reg': 0, 'event_proc_inbound': 0, 'event_proc_outbound': 0, 'orgbook': 0}
    stats_dict[key][type] = stats_dict[key][type] + 1


with BCRegistries() as bc_registries:
    # run this query against BC Reg database:
    sql1 = """
    select corp.corp_num, 
           corp.corp_typ_cd,
           op_state.op_state_typ_cd
    from bc_registries.corporation corp, 
          bc_registries.corp_state state,
       bc_registries.corp_op_state op_state,
           bc_registries.corp_type ctype
    where state.corp_num = corp.corp_num
      and state.end_event_id is null
      and op_state.state_typ_cd = state.state_typ_cd
      and corp.corp_typ_cd = ctype.corp_typ_cd;
    """

    print("Get corp stats from BC Registries DB", datetime.datetime.now())
    bc_reg_recs = bc_registries.get_bcreg_sql("corp_stats", sql1, cache=False)
    for bc_reg_rec in bc_reg_recs:
        key = bc_reg_rec['corp_typ_cd'] + ',' + bc_reg_rec['op_state_typ_cd']
        add_stats_to_dict(key, 'bc_reg')
    #print(bc_reg_stats)


with EventProcessor() as event_processor:
    # run this query against Event Processor database:
    sql2 = """
    SELECT record_id, corp_num, corp_state, corp_json->>'corp_typ_cd' as corp_typ_cd, entry_date, process_date 
    FROM corp_history_log
    WHERE process_date is not null and (process_msg != 'Withdrawn' or process_msg is null)
    ORDER BY record_id desc;
    """

    print("Get corp stats from Event Processor DB", datetime.datetime.now())
    processed_inbound_corps = {}
    event_proc_inbound_recs = event_processor.get_event_proc_sql("inbound_recs", sql2)
    for inbound_rec in event_proc_inbound_recs:
        if not inbound_rec['corp_num'] in processed_inbound_corps.keys():
            key = inbound_rec['corp_typ_cd'] + ',' + inbound_rec['corp_state']
            add_stats_to_dict(key, 'event_proc_inbound')
            processed_inbound_corps[inbound_rec['corp_num']] = 'Done'

    # run this query against Event Processor database:
    sql3 = """
    SELECT record_id, corp_num, credential_json->>'entity_status' as corp_state, credential_json->>'entity_type' as corp_typ_cd, entry_date, process_date 
    FROM credential_log 
    WHERE process_date is not null and credential_type_cd = 'REG'
    ORDER BY record_id desc;
    """

    print("Get corp stats from Event Processor DB", datetime.datetime.now())
    processed_outbound_corps = {}
    event_proc_outbound_recs = event_processor.get_event_proc_sql("outbound_recs", sql3)
    for outbound_rec in event_proc_outbound_recs:
        if not outbound_rec['corp_num'] in processed_outbound_corps.keys():
            key = outbound_rec['corp_typ_cd'] + ',' + outbound_rec['corp_state']
            add_stats_to_dict(key, 'event_proc_outbound')
            processed_outbound_corps[outbound_rec['corp_num']] = 'Done'
    #print(event_proc_outbound_stats)


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
          credential_id, 
          MAX(CASE WHEN claim_name='entity_type' THEN claim_value END) corp_typ_cd,
          MAX(CASE WHEN claim_name='entity_status' THEN claim_value END) corp_state
        from (
        select claim.credential_id as credential_id, claim.name as claim_name, claim.value as claim_value
        from credential_set, credential, claim
        where credential_set.credential_type_id in (select id from credential_type where description = 'Registration')
            and credential.id = credential_set.latest_credential_id
            and claim.credential_id = credential.id
            and claim.name in ('registration_id', 'entity_type', 'entity_status')) as foo
        group by credential_id;
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
            key = orgbook_stat['corp_typ_cd'] + ',' + orgbook_stat['corp_state']
            add_stats_to_dict(key, 'orgbook')
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

