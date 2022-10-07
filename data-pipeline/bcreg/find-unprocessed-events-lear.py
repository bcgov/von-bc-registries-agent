#!/usr/bin/python
import psycopg2
import datetime
import os
import logging

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type
from bcreg.bcreg_batch_utils import find_unprocessed_events
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


MAX_CORPS = 10000
CRAZY_MAX_CORPS = 100000

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)
LOGGER = logging.getLogger(__name__)


try:
    with EventProcessor() as event_processor:
        with BCReg_Lear() as bc_registries_lear:
            find_unprocessed_events(event_processor, bc_registries_lear, lear_system_type)
except Exception as e:
    LOGGER.error("Exception: " + str(e))
    log_error("find-unpocessed-events processing exception: " + str(e))
    raise
