#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor


with EventProcessor() as event_processor:
	event_processor.process_corp_generate_creds()

