#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor, CORP_TYPES_IN_SCOPE
from bcreg.bcregistries import BCRegistries

"""
This script identifies missing corps based on the Event Processor database, comparing input corporations
and output (staged) credentials.

Note:  This report runs based on the audit table, populated by the `populate_audit_table.py` script

Note:  For any companies that are identified as "missing" by this report, run the following query to 
       reset the status in the Event Processor database to force reprocess of these companies:

update corp_history_log
set process_success = null, process_date = null, process_msg = null
where process_success is not null
and corp_num not in
(select corp_num from credential_log where credential_type_cd = 'REG');

commit;

1. Stop any scheduled jobs (cron)
2. Run the above query
3. Run the "initial reload" and "post credentials" jobs
4. Re-run the audit report
5. Restart the cron jobs
"""

stats_dict = {}
def add_stats_to_dict(key, type):
    if not key in stats_dict:
        stats_dict[key] = {'event_proc_inbound': 0, 'event_proc_outbound': 0}
    stats_dict[key][type] = stats_dict[key][type] + 1


corps_dict = {}
def add_corp_to_dict(corp_num, key, type):
    if corp_num.startswith('BC'):
        corp_num = corp_num[2:]
    if not corp_num in corps_dict:
        corps_dict[corp_num] = {}
    corps_dict[corp_num][type] = key


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


