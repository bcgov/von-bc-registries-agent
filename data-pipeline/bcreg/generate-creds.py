#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


try:
    with EventProcessor() as event_processor:
    	event_processor.process_corp_generate_creds()
except Exception as e:
    print("Exception", e)
    log_error("generate_creds processing exception: " + str(e))
    raise

