#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries


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


stats_dict = {}
def add_stats_to_dict(key, type, value):
    if not key in stats_dict:
        stats_dict[key] = {'event_proc_inbound': 0, 'event_proc_outbound': 0}
    stats_dict[key][type] = value


# convert all stats into dicts based on company type and status
for event_proc_inbound_stat in event_proc_inbound_stats:
    key = event_proc_inbound_stat['corp_typ_cd'] + ',' + event_proc_inbound_stat['corp_state']
    add_stats_to_dict(key, 'event_proc_inbound', event_proc_inbound_stat['count'])

for event_proc_outbound_stat in event_proc_outbound_stats:
    key = event_proc_outbound_stat['corp_typ_cd'] + ',' + event_proc_outbound_stat['corp_state']
    add_stats_to_dict(key, 'event_proc_outbound', event_proc_outbound_stat['count'])

print("Overall stats:")
print(json.dumps(stats_dict))
print("===========================")
print("Company Type,Company Status,bc_reg,event_proc_inbound,event_proc_outbound,orgbook")
for key, value in stats_dict.items():
    print(key + ',' + str(value['event_proc_inbound']) + ',' + str(value['event_proc_outbound']))
print("===========================")
print("Incomplete data in Event Processor:")
print("===========================")
print("Company Type,Company Status,event_proc_inbound,event_proc_outbound,event_proc_diff")
for key, value in stats_dict.items():
    if 0 < (value['event_proc_inbound'] - value['event_proc_outbound']):
        print(key + ',' + str(value['event_proc_inbound']) + ',' + str(value['event_proc_outbound']) + ',' + str(value['event_proc_inbound'] - value['event_proc_outbound']))
print("===========================")

