#!/usr/bin/python
 
import psycopg2
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor

 
with EventProcessor() as event_processor:
    event_processor.create_tables()
    print("Created event processor tables")
