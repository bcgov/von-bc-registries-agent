#!/usr/bin/python
import psycopg2
import datetime
import os
import logging

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor, LEAR_CORP_TYPES_IN_SCOPE
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


specific_corps = []


with BCReg_Lear() as bc_registries:
    # get 5 corps for each type in scope (in addition to the above list)
    for corp_type in LEAR_CORP_TYPES_IN_SCOPE:
        print(corp_type)
        sql = """
               select identifier as corp_num
               from businesses
               where legal_type = '""" + corp_type + """'
               order by identifier desc
              """
        corps = bc_registries.get_bcreg_sql("corps_by_type", sql, cache=False)
        n_corps = min(len(corps), 5)
        for i in range(n_corps):
           specific_corps.append(corps[i]['corp_num'])

    with EventProcessor() as event_processor:
        print("Get last processed event")
        prev_event_id = 0

        print("Get last max event")
        max_event_date = bc_registries.get_max_event_date()
        max_event_id = bc_registries.get_max_event(max_event_date)
        print(">>> max event:", max_event_id, max_event_date)
        
        # get specific test corps (there are about 6)
        print("Get specific corps")
        corps = bc_registries.get_specific_corps(specific_corps)
        print(">>> corps:", corps)

        print("Find unprocessed events for each corp")
        last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
        max_event_dt = bc_registries.get_event_effective_date(max_event_id)
        corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id, max_event_dt, corps)
        
        print("Update our queue")
        event_processor.update_corp_event_queue(lear_system_type, corps, max_event_id, max_event_date)