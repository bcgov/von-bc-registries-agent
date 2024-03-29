#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
import os 
import logging

from bcreg.config import config
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type, LEAR_CORP_TYPES_IN_SCOPE
from bcreg.eventprocessor import EventProcessor
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


try:
    with EventProcessor() as event_processor:
        # check for a (comma-delimited) list of corp types to process
        corp_types = os.environ.get('CORP_TYPES_SCOPE')

        if not corp_types or 0 == len(corp_types):
            event_processor.process_corp_event_queue_and_generate_creds(lear_system_type, use_cache=True, corp_types=LEAR_CORP_TYPES_IN_SCOPE)
        else:
            corp_types = corp_types.split(",")
            corp_types_scope = {}
            for corp_type in corp_types:
                if corp_type in LEAR_CORP_TYPES_IN_SCOPE:
                    corp_types_scope[corp_type] = LEAR_CORP_TYPES_IN_SCOPE[corp_type]
            event_processor.process_corp_event_queue_and_generate_creds(lear_system_type, use_cache=True, corp_types=corp_types_scope)                    
except Exception as e:
    print("Exception", e)
    log_error("process_corps_generate_creds processing exception: " + str(e))
    raise


