#!/usr/bin/python

from bcreg.bcregistries import MIN_START_DATE, system_type
from bcreg.eventprocessor import EventProcessor

with EventProcessor() as event_processor:
    # insert last event
    event_processor.insert_last_event(system_type, 0, MIN_START_DATE)

    print("Seeded initial event processor data")
