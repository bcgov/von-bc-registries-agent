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
        stats_dict[key] = {'event_proc_inbound': 0, 'event_proc_outbound': 0}
    stats_dict[key][type] = stats_dict[key][type] + 1

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


print("Got all corp stats", datetime.datetime.now())

print("Overall stats:")
print(json.dumps(stats_dict))
print("===========================")
print("Company Type,Company Status,bc_reg,event_proc_inbound,event_proc_outbound")
for key, value in stats_dict.items():
    print(key + ',' + str(value['event_proc_inbound']) + ',' + str(value['event_proc_outbound']))
print("===========================")
print("Incomplete data in Event Processor:")
print("===========================")
print("Company Type,Company Status,event_proc_inbound,event_proc_outbound,event_proc_diff")
missing_corps = False
for key, value in stats_dict.items():
    if 0 != (value['event_proc_inbound'] - value['event_proc_outbound']):
        print(key + ',' + str(value['event_proc_inbound']) + ',' + str(value['event_proc_outbound']) + ',' + str(value['event_proc_inbound'] - value['event_proc_outbound']))
        missing_corps = True
print("===========================")


#with EventProcessor() as event_processor:
#    if missing_corps:
#        sql5 = """
#        select corp_num from corp_history_log where (process_msg != 'Withdrawn' or process_msg is null) and process_date is not null and corp_num not in
#        (select corp_num from credential_log where credential_type_cd = 'REG' and process_date is not null)
#        """
#
#        event_proc_corps = event_processor.get_event_proc_sql("event_proc_corps", sql5)
#        corp_count = 0
#        for corp in event_proc_corps:
#            #print(corp['corp_num'])
#            corp_count = corp_count + 1
#        print("Missing corps =", corp_count)


