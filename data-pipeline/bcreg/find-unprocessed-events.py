#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type


with BCRegistries() as bc_registries:
    with EventProcessor() as event_processor:
        print("Get last processed event")
        prev_event_date = event_processor.get_last_processed_event_date(system_type)
        if prev_event_date is not None:
            prev_event_id = event_processor.get_last_processed_event(prev_event_date, system_type)
        else:
            prev_event_id = 0
        
        print("Get last max event")
        max_event_date = bc_registries.get_max_event_date()
        max_event_id = bc_registries.get_max_event(max_event_date)
        
        # get unprocessed corps (there are about 2700)
        print("Get unprocessed corps")
        last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
        max_event_dt = bc_registries.get_event_effective_date(max_event_id)
        corps = bc_registries.get_unprocessed_corps(prev_event_id, last_event_dt, max_event_id, max_event_dt)
        
        print("Find unprocessed events for each corp")
        corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id, max_event_dt, corps)
        
        print("Update our queue")
        event_processor.update_corp_event_queue(system_type, corps, max_event_id, max_event_date)


