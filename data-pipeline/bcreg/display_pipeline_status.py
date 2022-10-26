#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal

from bcreg.bcregistries import system_type
from bcreg.bcreg_lear import lear_system_type
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor


with EventProcessor() as event_processor:
    event_processor.display_event_processing_status(system_type_cd=system_type)

    event_processor.display_event_processing_status(system_type_cd=lear_system_type)

