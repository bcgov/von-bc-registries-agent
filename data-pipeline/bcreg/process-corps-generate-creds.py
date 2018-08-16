#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor


with EventProcessor() as event_processor:
    event_processor.process_corp_event_queue_and_generate_creds(True)


