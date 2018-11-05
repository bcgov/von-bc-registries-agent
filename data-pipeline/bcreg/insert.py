#!/usr/bin/python
 
import psycopg2
import datetime
import json
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.eventprocessor import corp_credential, corp_schema, corp_version
from bcreg.eventprocessor import addr_credential, addr_schema, addr_version
from bcreg.eventprocessor import dba_credential, dba_schema, dba_version
from bcreg.bcregistries import system_type, MIN_START_DATE


with EventProcessor() as event_processor:
    # insert last event
    event_processor.insert_last_event(system_type, 0, MIN_START_DATE)
    
    print("Seeded initial event processor data")

