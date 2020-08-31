#!/usr/bin/python
import psycopg2
import datetime
import os
import logging

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor, bn_credential
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


try:
    with EventProcessor() as event_processor:
        event_processor.generate_credential_type(system_type, bn_credential)
except Exception as e:
    print("Exception", e)
    log_error("process-corps-generate-bn-creds processing exception: " + str(e))
    raise
