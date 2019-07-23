#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries


with BCRegistries() as bc_registries:
    # run this query against BC Reg database:
    sql1 = """
    select corp.corp_typ_cd,
           op_state.op_state_typ_cd,
           count(*)
    from bc_registries.corporation corp, 
          bc_registries.corp_state state,
       bc_registries.corp_op_state op_state,
           bc_registries.corp_type ctype
    where state.corp_num = corp.corp_num
      and state.end_event_id is null
      and op_state.state_typ_cd = state.state_typ_cd
      and corp.corp_typ_cd = ctype.corp_typ_cd
    group by corp.corp_typ_cd, op_state.op_state_typ_cd
    order by corp.corp_typ_cd, op_state.op_state_typ_cd;
    """

    print("Get corp stats from BC Registries DB", datetime.datetime.now())
    bc_reg_stats = bc_registries.get_bcreg_sql("corp_stats", sql1, cache=False)
    #print(bc_reg_stats)


with EventProcessor() as event_processor:
    # run this query against Event Processor database:
    sql2 = """
    select corp_typ_cd, corp_state, count(*)
    from (
    SELECT record_id, corp_num, corp_state, corp_json->>'corp_typ_cd' as corp_typ_cd, entry_date, process_date 
    FROM corp_history_log ch1
    WHERE record_id = (SELECT MAX(record_id) FROM corp_history_log ch2 WHERE ch1.corp_num = ch2.corp_num and process_date is not null)
    ORDER BY corp_num, record_id
    ) as foo group by corp_typ_cd, corp_state
    order by corp_typ_cd, corp_state;
    """

    print("Get corp stats from Event Processor DB", datetime.datetime.now())
    event_proc_inbound_stats = event_processor.get_event_proc_sql("inbound_stats", sql2)
    #print(event_proc_inbound_stats)

    # run this query against Event Processor database:
    sql3 = """
    select corp_typ_cd, corp_state, count(*)
    from (
    SELECT record_id, corp_num, credential_json->>'entity_status' as corp_state, credential_json->>'entity_type' as corp_typ_cd, entry_date, process_date 
    FROM credential_log cl1
    WHERE record_id = (SELECT MAX(record_id) FROM credential_log cl2 WHERE cl1.corp_num = cl2.corp_num and process_date is not null and credential_type_cd = 'REG')
    ORDER BY corp_num, record_id
    ) as foo group by corp_typ_cd, corp_state
    order by corp_typ_cd, corp_state;
    """

    print("Get corp stats from Event Processor DB", datetime.datetime.now())
    event_proc_outbound_stats = event_processor.get_event_proc_sql("outbound_stats", sql3)
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
        select corp_typ_cd, corp_state, count(*)
        from (
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
        group by credential_id
        ) as foo group by corp_typ_cd, corp_state
        order by corp_typ_cd, corp_state;
        """

        print("Get corp stats from OrggBook DB", datetime.datetime.now())
        cursor = conn.cursor()
        cursor.execute(sql4)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        rows = [dict(zip(column_names, row))  
            for row in cursor]
        cursor.close()
        cursor = None
        orgbook_stats = rows
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


stats_dict = {}
def add_stats_to_dict(key, type, value):
    if not key in stats_dict:
        stats_dict[key] = {'bc_reg': 0, 'event_proc_inbound': 0, 'event_proc_outbound': 0, 'orgbook': 0}
    stats_dict[key][type] = value


# convert all stats into dicts based on company type and status
for bc_reg_stat in bc_reg_stats:
    key = bc_reg_stat['corp_typ_cd'] + ',' + bc_reg_stat['op_state_typ_cd']
    add_stats_to_dict(key, 'bc_reg', bc_reg_stat['count'])

for event_proc_inbound_stat in event_proc_inbound_stats:
    key = event_proc_inbound_stat['corp_typ_cd'] + ',' + event_proc_inbound_stat['corp_state']
    add_stats_to_dict(key, 'event_proc_inbound', event_proc_inbound_stat['count'])

for event_proc_outbound_stat in event_proc_outbound_stats:
    key = event_proc_outbound_stat['corp_typ_cd'] + ',' + event_proc_outbound_stat['corp_state']
    add_stats_to_dict(key, 'event_proc_outbound', event_proc_outbound_stat['count'])

for orgbook_stat in orgbook_stats:
    key = orgbook_stat['corp_typ_cd'] + ',' + orgbook_stat['corp_state']
    add_stats_to_dict(key, 'orgbook', orgbook_stat['count'])

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
    if 0 < (value['bc_reg'] - value['orgbook']):
        print(key + ',' + str(value['bc_reg']) + ',' + str(value['orgbook']) + ',' + str(value['bc_reg'] - value['orgbook']))
print("===========================")

