#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


try:
    with EventProcessor() as event_processor:
        event_processor.process_corp_event_queue_and_generate_creds(True)
except Exception as e:
    print("Exception", e)
    log_error("process_corps_generate_creds processing exception: " + str(e))
    raise


