#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type


with EventProcessor() as event_processor:
    print("Get last processed event")
    prev_event_date = event_processor.get_last_processed_event_date(lear_system_type)
    if prev_event_date is not None:
        prev_event_id = event_processor.get_last_processed_event(prev_event_date, lear_system_type)
    else:
        prev_event_id = 0

    # if the last event is non-zero then we already ran the initial company load
    if 0 < prev_event_id:
        print("Prev event = " + str(prev_event_id) + ", " + str(prev_event_date) + ", skipping initial corps_data_load ...")
    else:
        with BCReg_Lear() as bc_registries:
            print("Get last max event")
            max_event_date = bc_registries.get_max_event_date()
            max_event_id = bc_registries.get_max_event(max_event_date)
            print(">>> max event --> ", max_event_id, max_event_date)
            
            # get unprocessed corps (there are about 2700)
            print("Get unprocessed corps")
            last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
            max_event_dt = bc_registries.get_event_effective_date(max_event_id)
            print(">>> last/max event --> ", last_event_dt, max_event_dt)
            corps = bc_registries.get_unprocessed_corps_data_load(prev_event_id, last_event_dt, max_event_id, max_event_dt)
            
            print("Update our queue")
            event_processor.update_corp_event_queue(lear_system_type, corps, max_event_id, max_event_date)
