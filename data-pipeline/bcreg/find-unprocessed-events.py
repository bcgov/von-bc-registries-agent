#!/usr/bin/python
import psycopg2
import datetime
import os
import logging

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

MAX_CORPS = 10000
CRAZY_MAX_CORPS = 100000

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)
LOGGER = logging.getLogger(__name__)


try:
    with BCRegistries() as bc_registries:
        with EventProcessor() as event_processor:
            LOGGER.info("Get last processed event")
            prev_event_date = event_processor.get_last_processed_event_date(system_type)
            if prev_event_date is not None:
                prev_event_id = event_processor.get_last_processed_event(prev_event_date, system_type)
            else:
                prev_event_id = 0
            LOGGER.info("Last processed event is " + str(prev_event_id) + " " + str(prev_event_date))

            LOGGER.info("Get last max event before now")
            max_event_date_before_now = bc_registries.get_max_date_before_now()
            max_event_id_before_now = bc_registries.get_max_event(max_event_date_before_now)
            LOGGER.info("Last max event before now is " + str(max_event_id_before_now) + " " + str(max_event_date_before_now))

            # get unprocessed corps (there are about 2700)
            LOGGER.info("Get unprocessed corps")
            if prev_event_id == 0:
                last_event_dt = datetime.datetime(datetime.MINYEAR, 1, 1)
            else:
                last_event_dt = prev_event_date # bc_registries.get_event_effective_date(prev_event_id)
            max_event_dt_before_now = max_event_date_before_now # bc_registries.get_event_effective_date(max_event_id)
            corps = bc_registries.get_unprocessed_corps(prev_event_id, last_event_dt)
            LOGGER.info("Unprocessed corps count is " + str(len(corps)))

            LOGGER.info("Find unprocessed events for each corp")
            corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id_before_now, max_event_dt_before_now, corps)
            LOGGER.info("Unprocessed corps events count is " + str(len(corps)))

            # do some reasonability checks before we update the queue
            cur_year = int(datetime.datetime.now().year)
            if prev_event_id == 0:
                raise Exception('no previous event id found: {}'.format(prev_event_id))
            if prev_event_date.year < (cur_year-10) or prev_event_date.year > (cur_year+10):
                raise Exception('previous event date unreasonable: {}'.format(prev_event_date))
            if max_event_id_before_now == 0:
                raise Exception('no max event id before now found: {}'.format(max_event_id_before_now))
            if max_event_dt_before_now.year < (cur_year-10) or max_event_dt_before_now.year > (cur_year+10):
                raise Exception('max event date before now unreasonable: {}'.format(max_event_dt_before_now))

            # reasonability test on the number of outstanding records
            if CRAZY_MAX_CORPS < len(corps):
                log_error("find-unpocessed-events More than cRaZy MaX corps: " + str(len(corps)))
            elif MAX_CORPS < len(corps):
                log_warning("find-unpocessed-events More than max corps: " + str(len(corps)))

            LOGGER.info("Update our queue")
            event_processor.update_corp_event_queue(system_type, corps, max_event_id_before_now, max_event_date_before_now)

            # process any corps listed as "outstanding" in the audit table
            # create events in our processing queue
            LOGGER.info("Check audit report for outstanding/unprocessed corps")
            audit_corps = event_processor.get_outstanding_audit_corps()
            LOGGER.info("Unprocessed corps audit count is " + str(len(audit_corps)))

            # reasonability test on the number of outstanding records
            if CRAZY_MAX_CORPS < len(audit_corps):
                log_error("find-unpocessed-events More than cRaZy MaX corps: " + str(len(audit_corps)))
            elif MAX_CORPS < len(audit_corps):
                log_warning("find-unpocessed-events More than max corps: " + str(len(audit_corps)))

            LOGGER.info("Update our queue")
            event_processor.update_corp_audit_event_queue(system_type, audit_corps)

except Exception as e:
    LOGGER.error("Exception: " + str(e))
    log_error("find-unpocessed-events processing exception: " + str(e))
    raise
