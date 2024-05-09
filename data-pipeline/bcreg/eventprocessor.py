#!/usr/bin/python
 
import psycopg2
import datetime
import pytz
import json
import time
import hashlib
import traceback
import logging
import random
import os
import csv

from bcreg.config import config
from bcreg.bcregistries import BCRegistries, CustomJsonEncoder, event_dict, is_data_conversion_event, system_type, CORP_TYPES_IN_SCOPE
from bcreg.bcreg_core import CORP_WITHDRAWN_STATE
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type, LEAR_CORP_TYPES_IN_SCOPE
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


EXTRA_DEMO_CREDS = os.environ.get("EXTRA_DEMO_CREDS")
if EXTRA_DEMO_CREDS is not None and EXTRA_DEMO_CREDS.upper() == "TRUE":
    # setup environment to process "extra" cred types
    print("Generating extra 'demo' credentials")
    GENERATE_EXTRA_DEMO_CREDS = True

    try:
        with open('./bcreg/tests/names-2018.txt', 'r') as f:
            reader = csv.reader(f)
            names_list = list(reader)
    except:
        names_list = None
else:
    # default - setup environment to process only "core" cred types
    GENERATE_EXTRA_DEMO_CREDS = False
    names_list = None

corp_credential = 'REG'
corp_schema = 'registration.registries.ca'
corp_version = '1.0.42'

addr_credential = 'ADDR'
addr_schema = 'address.registries.ca'
addr_version = '1.0.42'

dba_credential = 'REL'
dba_schema = 'relationship.registries.ca'
dba_version = '1.0.42'

# the next 4 cred types will only be generated in "demo" mode
bn_credential = 'BNC'
bn_schema = 'business_number.registries.ca'
bn_version = '1.0.42'

vp_credential = 'VPC'
vp_schema = 'demo.verified_person.registries.ca'
vp_version = '1.0.42'

vp_rel_credential = 'VPR'
vp_rel_schema = 'demo.person_relationship.registries.ca'
vp_rel_version = '1.0.42'

org_rel_credential = 'OGR'
org_rel_schema = 'demo.org_relationship.registries.ca'
org_rel_version = '1.0.42'

CORP_BATCH_SIZE = 3000
FALLBACK_CORP_BATCH_SIZE = 300

MIN_START_DATE = datetime.datetime(datetime.MINYEAR+1, 1, 1)
MIN_VALID_DATE = datetime.datetime(datetime.MINYEAR+10, 1, 1)
MAX_END_DATE   = datetime.datetime(datetime.MAXYEAR-1, 12, 31)

# for now, we are in PST time
timezone = pytz.timezone("PST8PDT")

MIN_START_DATE_TZ = timezone.localize(MIN_START_DATE)
MIN_VALID_DATE_TZ = timezone.localize(MIN_VALID_DATE)
MAX_END_DATE_TZ   = timezone.localize(MAX_END_DATE)

LOGGER = logging.getLogger(__name__)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            try:
                tz_aware = timezone.localize(o)
                return tz_aware.astimezone(pytz.utc).isoformat()
            except (Exception) as error:
                if o.year <= datetime.MINYEAR+1:
                    return MIN_START_DATE_TZ.astimezone(pytz.utc).isoformat()
                elif o.year >= datetime.MAXYEAR-1:
                    return MAX_END_DATE_TZ.astimezone(pytz.utc).isoformat()
                return o.isoformat()
        return json.JSONEncoder.default(self, o)


def event_json(event):
    return json.dumps(event, cls=CustomJsonEncoder, sort_keys=True)

def event_dict_from_json(event_json):
    return json.loads(event_json)


# interface to Event Processor database
class EventProcessor:
    def __init__(self):
        try:
            params = config(section='event_processor')
            self.conn = psycopg2.connect(**params)
        except (Exception) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            self.conn = None
            log_error("EventProcessor exception connecting to DB: " + str(error))
            raise

    def __del__(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
 
    # create our base processing tables
    def do_create_tables(self, commands):
        cur = None
        try:
            cur = self.conn.cursor()
            for command in commands:
                cur.execute(command)
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception initializing DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # create our base processing tables
    def create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS LAST_EVENT (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                EVENT_ID INTEGER NOT NULL,
                EVENT_DATE TIMESTAMP NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL
            )
            """,
            """
            CREATE INDEX IF NOT EXISTS le_stc ON LAST_EVENT 
            (SYSTEM_TYPE_CD);
            """,
            """
            CREATE INDEX IF NOT EXISTS le_ie ON LAST_EVENT 
            (EVENT_ID);
            """,
            """
            CREATE INDEX IF NOT EXISTS le_stc_ei ON LAST_EVENT 
            (SYSTEM_TYPE_CD, EVENT_ID);
            """,
            """
            CREATE TABLE IF NOT EXISTS EVENT_BY_CORP_FILING (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                PREV_EVENT_ID INTEGER NOT NULL, 
                PREV_EVENT_DATE TIMESTAMP NOT NULL, 
                LAST_EVENT_ID INTEGER NOT NULL, 
                LAST_EVENT_DATE TIMESTAMP NOT NULL, 
                ENTRY_DATE TIMESTAMP NOT NULL,
                PROCESS_DATE TIMESTAMP,
                PROCESS_SUCCESS CHAR,
                PROCESS_MSG VARCHAR(255)
            )
            """,
            """
            -- Hit for counts and queries
            CREATE INDEX IF NOT EXISTS ebcf_pd_null ON EVENT_BY_CORP_FILING 
            (PROCESS_DATE) WHERE PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for query
            CREATE INDEX IF NOT EXISTS ebcf_ri_pd_null_asc ON EVENT_BY_CORP_FILING 
            (RECORD_ID ASC, PROCESS_DATE) WHERE PROCESS_DATE IS NULL;
            """,
            """
            ALTER TABLE EVENT_BY_CORP_FILING
            SET (autovacuum_vacuum_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE EVENT_BY_CORP_FILING
            SET (autovacuum_vacuum_threshold = 5000);
            """,
            """
            ALTER TABLE EVENT_BY_CORP_FILING  
            SET (autovacuum_analyze_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE EVENT_BY_CORP_FILING  
            SET (autovacuum_analyze_threshold = 5000);
            """,
            """ 
            REINDEX TABLE EVENT_BY_CORP_FILING;
            """,
            """
            CREATE TABLE IF NOT EXISTS CORP_HISTORY_LOG (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                CORP_STATE VARCHAR(255) NOT NULL,
                PREV_EVENT JSON NOT NULL, 
                LAST_EVENT JSON NOT NULL, 
                CORP_JSON JSON NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL,
                PROCESS_DATE TIMESTAMP,
                PROCESS_SUCCESS CHAR,
                PROCESS_MSG VARCHAR(255)
            )
            """,
            """
            -- Hit for counts and queries
            CREATE INDEX IF NOT EXISTS chl_pd_null ON CORP_HISTORY_LOG 
            (PROCESS_DATE) WHERE PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for query
            CREATE INDEX IF NOT EXISTS chl_ri_pd_null_asc ON CORP_HISTORY_LOG 
            (RECORD_ID ASC, PROCESS_DATE) WHERE PROCESS_DATE IS NULL;	
            """,
            """
            ALTER TABLE CORP_HISTORY_LOG
            SET (autovacuum_vacuum_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CORP_HISTORY_LOG
            SET (autovacuum_vacuum_threshold = 5000);
            """,
            """
            ALTER TABLE CORP_HISTORY_LOG  
            SET (autovacuum_analyze_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CORP_HISTORY_LOG  
            SET (autovacuum_analyze_threshold = 5000);
            """,
            """ 
            REINDEX TABLE CORP_HISTORY_LOG;
            """,
            """
            CREATE TABLE IF NOT EXISTS CREDENTIAL_TRANSFORM (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CREDENTIAL_TYPE_CD VARCHAR(255) NOT NULL,
                SCHEMA_NAME VARCHAR(255) NOT NULL,
                SCHEMA_VERSION VARCHAR(255) NOT NULL,
                MAPPING_TRANSFORM TEXT NOT NULL
            )
            """,
            """
            -- Hit for query
            CREATE INDEX IF NOT EXISTS ct_stc ON CREDENTIAL_TRANSFORM 
            (SYSTEM_TYPE_CD);
            """,
            """
            CREATE TABLE IF NOT EXISTS CREDENTIAL_LOG (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                CORP_STATE VARCHAR(255) NOT NULL,
                PREV_EVENT JSON NOT NULL, 
                LAST_EVENT JSON NOT NULL, 
                CREDENTIAL_TYPE_CD VARCHAR(255) NOT NULL,
                CREDENTIAL_ID VARCHAR(255) NOT NULL,
                SCHEMA_NAME VARCHAR(255) NOT NULL,
                SCHEMA_VERSION VARCHAR(255) NOT NULL,
                CREDENTIAL_JSON JSON NOT NULL,
                CREDENTIAL_HASH VARCHAR(64) NOT NULL, 
                CREDENTIAL_REASON VARCHAR(255),
                ENTRY_DATE TIMESTAMP NOT NULL,
                END_DATE TIMESTAMP,
                PROCESS_DATE TIMESTAMP,
                PROCESS_SUCCESS CHAR,
                PROCESS_MSG VARCHAR(255)
            )
            """,
            """
            -- Hit duplicate credentials
            CREATE UNIQUE INDEX IF NOT EXISTS cl_hash_index ON CREDENTIAL_LOG 
            (CREDENTIAL_HASH);
            """,
            """
            -- Hit for counts and queries
            CREATE INDEX IF NOT EXISTS cl_pd_null ON CREDENTIAL_LOG 
            (PROCESS_DATE) WHERE PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for counts
            CREATE INDEX IF NOT EXISTS cl_pd_null_cs_act ON CREDENTIAL_LOG 
            (PROCESS_DATE, CORP_STATE) WHERE CORP_STATE = 'ACT' and PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for counts
            CREATE INDEX IF NOT EXISTS cl_cs_act_pd_null_ri_asc ON CREDENTIAL_LOG 
            (CORP_STATE, PROCESS_DATE, RECORD_ID ASC) WHERE CORP_STATE = 'ACT' and PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for queries
            CREATE INDEX IF NOT EXISTS cl_ri_cs_act_pd_null_asc ON CREDENTIAL_LOG 
            (RECORD_ID ASC, CORP_STATE, PROCESS_DATE) WHERE CORP_STATE = 'ACT' and PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for query
            CREATE INDEX IF NOT EXISTS cl_ri_pd_null_asc ON CREDENTIAL_LOG 
            (RECORD_ID ASC, PROCESS_DATE) WHERE PROCESS_DATE IS NULL;
            """,
            #"""
            #-- Hit when checking generated credentials
            #CREATE INDEX IF NOT EXISTS cl_ri_stc_cn_cs_ctc_ci_desc ON CREDENTIAL_LOG 
            #(RECORD_ID DESC,SYSTEM_TYPE_CD, CORP_NUM, CORP_STATE, CREDENTIAL_TYPE_CD, CREDENTIAL_ID)
            #""",
            """
            -- Hit for counts
            CREATE INDEX IF NOT EXISTS cl_ps ON CREDENTIAL_LOG
            (process_success)
            """,
            """
            -- Hit for queries
            CREATE INDEX IF NOT EXISTS cl_ps_pd_desc ON CREDENTIAL_LOG
            (process_success, process_date DESC)
            """,
            """
            ALTER TABLE CREDENTIAL_LOG
            SET (autovacuum_vacuum_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CREDENTIAL_LOG
            SET (autovacuum_vacuum_threshold = 5000);
            """,
            """
            ALTER TABLE CREDENTIAL_LOG  
            SET (autovacuum_analyze_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CREDENTIAL_LOG  
            SET (autovacuum_analyze_threshold = 5000);
            """,
            """ 
            REINDEX TABLE CREDENTIAL_LOG;
            """,
            """
            CREATE TABLE IF NOT EXISTS CORP_AUDIT_LOG (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                LAST_CORP_HISTORY_ID INT NOT NULL,
                LAST_EVENT_DATE TIMESTAMP NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                CORP_STATE VARCHAR(255) NOT NULL,
                CORP_TYPE VARCHAR(255) NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL,
                LAST_CREDENTIAL_ID INT,
                CRED_EFFECTIVE_DATE TIMESTAMP
            )
            """,
            """
            -- Hit for query
            CREATE INDEX IF NOT EXISTS audit_corp_num_asc ON CORP_AUDIT_LOG 
            (CORP_NUM);
            """,
            """
            ALTER TABLE CORP_AUDIT_LOG
            SET (autovacuum_vacuum_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CORP_AUDIT_LOG
            SET (autovacuum_vacuum_threshold = 5000);
            """,
            """
            ALTER TABLE CORP_AUDIT_LOG  
            SET (autovacuum_analyze_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CORP_AUDIT_LOG  
            SET (autovacuum_analyze_threshold = 5000);
            """,
            """ 
            REINDEX TABLE CORP_AUDIT_LOG;
            """,
        )
        self.do_create_tables(commands)

        # tables added subsequent to initial prod release
        self.create_reprocessing_tables()


    def create_reprocessing_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS CORP_CRED_REPROCESS_LOG (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_HISTORY_ID INT NOT NULL,
                CORP_NUM VARCHAR(255) NOT NULL,
                CREDENTIAL_TYPE_CD VARCHAR(255) NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL,
                PROCESS_DATE TIMESTAMP,
                PROCESS_SUCCESS CHAR,
                PROCESS_MSG VARCHAR(255)
            )
            """,
            """
            -- Hit for counts and queries
            CREATE INDEX IF NOT EXISTS crpl_pd_null ON CORP_CRED_REPROCESS_LOG 
            (PROCESS_DATE) WHERE PROCESS_DATE IS NULL;
            """,
            """
            -- Hit for query
            CREATE INDEX IF NOT EXISTS crpl_ri_pd_null_asc ON CORP_CRED_REPROCESS_LOG 
            (RECORD_ID ASC, PROCESS_DATE) WHERE PROCESS_DATE IS NULL;   
            """,
            """
            ALTER TABLE CORP_CRED_REPROCESS_LOG
            SET (autovacuum_vacuum_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CORP_CRED_REPROCESS_LOG
            SET (autovacuum_vacuum_threshold = 5000);
            """,
            """
            ALTER TABLE CORP_CRED_REPROCESS_LOG  
            SET (autovacuum_analyze_scale_factor = 0.0);
            """,
            """ 
            ALTER TABLE CORP_CRED_REPROCESS_LOG  
            SET (autovacuum_analyze_threshold = 5000);
            """,
            """ 
            REINDEX TABLE CORP_CRED_REPROCESS_LOG;
            """,
        )
        self.do_create_tables(commands)


    ###########################################################################
    # utility method to query event processing data
    ###########################################################################

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes sql arguements
    def get_event_proc_sql(self, table, sql, args=None):
        cursor = None
        try:
            cursor = self.conn.cursor()
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            rows = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("Event Processor exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None


    # record the last event processed
    def insert_last_event(self, system_type_cd, event_id, event_date):
        """ insert a new event into the event table """
        sql = """INSERT INTO LAST_EVENT (SYSTEM_TYPE_CD, EVENT_ID, EVENT_DATE, ENTRY_DATE)
                 VALUES (%s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type_cd, event_id, event_date, datetime.datetime.now(),))
            _record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception writing to DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # get the id of the last event processed (at a specific date)
    def get_last_processed_event(self, event_date, system_type_cd):
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute("""SELECT max(event_id) FROM LAST_EVENT where EVENT_DATE = %s and SYSTEM_TYPE_CD = %s""", (event_date, system_type_cd,))
            row = cur.fetchone()
            cur.close()
            cur = None
            prev_event = row[0]
            if prev_event is None:
                prev_event = 0
            return prev_event
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # get the last event processed timestamp
    def get_last_processed_event_date(self, system_type_cd):
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute("""SELECT max(event_date) FROM LAST_EVENT where SYSTEM_TYPE_CD = %s""", (system_type_cd,))
            row = cur.fetchone()
            cur.close()
            cur = None
            prev_event = row[0]
            return prev_event
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # return unprocessed corporations, based on active or historical
    # use for initial data load
    def get_outstanding_audit_corps(self):
        sql = """select corp_num, 0, '0001-01-01 00:00:00', event_id, event_date
            from CORP_AUDIT_LOG, LAST_EVENT
            where CORP_AUDIT_LOG.last_credential_id is null
              and LAST_EVENT.record_id = (select max(record_id) from LAST_EVENT)
              and corp_num not in
              (select corp_num from corp_history_log where process_msg = 'Withdrawn')
              and corp_num not in
              (select corp_num from event_by_corp_filing where process_success is null)
        """

        corps = []
        cur = None
        try:
            LOGGER.info("Executing: " + sql)
            cur = self.conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            while row is not None:
                # LOGGER.info(row)
                corps.append({
                    'corp_num':row[0],
                    'prev_event_id':row[1], 
                    'prev_event_date':row[2],
                    'last_event_id':row[3],
                    'last_event_date':row[4],
                })
                row = cur.fetchone()
            cur.close()
            cur = None
            LOGGER.info("Loaded corps: " + str(len(corps)))
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("Event Processor exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

        return corps

    # update a group of corps into the "unprocessed corp" queue
    def update_corp_audit_event_queue(self, system_type_cd, corps):
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, PREV_EVENT_DATE, LAST_EVENT_ID, LAST_EVENT_DATE, CORP_NUM, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            for i,corp in enumerate(corps): 
                cur = self.conn.cursor()
                cur.execute(sql, (system_type_cd, corp['prev_event_id'], corp['prev_event_date'], corp['last_event_id'], corp['last_event_date'], corp['corp_num'], datetime.datetime.now(),))
                _record_id = cur.fetchone()[0]
                cur.close()
                cur = None
            self.conn.commit()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception updating DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert a record into the "unprocessed corporations" table
    def insert_corporation(self, system_type_cd, prev_event_id, prev_event_dt, last_event_id, last_event_dt, corp_num):
        """ insert a new corps into the corps table """
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, PREV_EVENT_DATE, LAST_EVENT_ID, LAST_EVENT_DATE, CORP_NUM, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type_cd, prev_event_id, prev_event_dt, last_event_id, last_event_dt, 
                                corp_num, datetime.datetime.now(),))
            _record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception updating DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert a list of "unprocessed corporations" into the table
    def insert_corporation_list(self, corporation_list):
        """ insert multiple corps into the corps table  """
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, PREV_EVENT_DATE, LAST_EVENT_ID, LAST_EVENT_DATE, CORP_NUM, ENTRY_DATE) 
                 VALUES(%s, %s, %s, %s, %s)"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.executemany(sql, corporation_list)
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception updating DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # update a group of corps into the "unprocessed corp" queue
    def update_corp_event_queue(self, system_type_cd, corps, max_event_id, max_event_date):
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, PREV_EVENT_DATE, LAST_EVENT_ID, LAST_EVENT_DATE, CORP_NUM, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql2 = """INSERT INTO LAST_EVENT (SYSTEM_TYPE_CD, EVENT_ID, EVENT_DATE, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            for i,corp in enumerate(corps): 
                cur = self.conn.cursor()
                cur.execute(sql, (system_type_cd, corp['PREV_EVENT']['event_id'], corp['PREV_EVENT']['event_date'], corp['LAST_EVENT']['event_id'], corp['LAST_EVENT']['event_date'], corp['CORP_NUM'], datetime.datetime.now(),))
                _record_id = cur.fetchone()[0]
                cur.close()
                cur = None
            cur = self.conn.cursor()
            cur.execute(sql2, (system_type_cd, max_event_id, max_event_date, datetime.datetime.now(),))
            self.conn.commit()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception updating DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert data for one corp into the history table
    def insert_corp_history(self, system_type_cd, prev_event_json, last_event_json, corp_num, corp_state, corp_json):
        """ insert a new corps into the corps table """
        sql = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT, LAST_EVENT, CORP_NUM, CORP_STATE, CORP_JSON, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type_cd, prev_event_json, last_event_json, corp_num, corp_state, corp_json, datetime.datetime.now(),))
            _record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("EventProcessor exception updating DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert a generated JSON credential into our log
    def insert_json_credential(self, cur, system_cd, prev_event, last_event, corp_num, corp_state, cred_type, cred_id, schema_name, schema_version, credential, credential_reason):
        sql = """INSERT INTO CREDENTIAL_LOG (SYSTEM_TYPE_CD, PREV_EVENT, LAST_EVENT, CORP_NUM, CORP_STATE, CREDENTIAL_TYPE_CD, CREDENTIAL_ID, 
                SCHEMA_NAME, SCHEMA_VERSION, CREDENTIAL_JSON, CREDENTIAL_HASH, CREDENTIAL_REASON, ENTRY_DATE)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql_addr = """INSERT INTO CREDENTIAL_LOG (SYSTEM_TYPE_CD, PREV_EVENT, LAST_EVENT, CORP_NUM, CORP_STATE, CREDENTIAL_TYPE_CD, CREDENTIAL_ID, 
                SCHEMA_NAME, SCHEMA_VERSION, CREDENTIAL_JSON, CREDENTIAL_HASH, CREDENTIAL_REASON, ENTRY_DATE, PROCESS_DATE, PROCESS_SUCCESS)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        # create row(s) for corp creds json info
        cred_json = json.dumps(credential, cls=CustomJsonEncoder, sort_keys=True)
        cred_hash = hashlib.sha256(cred_json.encode('utf-8')).hexdigest()
        try:
            cur.execute("savepoint save_" + cred_type)
            # store address creds with a special status, because we don't want to post them yet
            if (cred_type == addr_credential) and (not GENERATE_EXTRA_DEMO_CREDS):
                cur.execute(sql_addr, (system_cd, event_json(prev_event), event_json(last_event), corp_num, corp_state, cred_type, cred_id, 
                            schema_name, schema_version, cred_json, cred_hash, credential_reason, datetime.datetime.now(), datetime.datetime.now(), 'A',))
                # release credentials with no effective date (for now)
                #elif self.is_min_date(credential['effective_date']) or credential['effective_date'] is None or credential['effective_date'] == '':
                #    # create and store credential but don't post it
                #    cur.execute(sql_addr, (system_cd, event_json(prev_event), event_json(last_event), corp_num, corp_state, cred_type, cred_id, 
                #                schema_name, schema_version, cred_json, cred_hash, credential_reason, datetime.datetime.now(), datetime.datetime.now(), 'X',))
            else:
                # release credentials with no effective date (for now)
                if self.is_min_date(credential['effective_date']) or credential['effective_date'] is None or credential['effective_date'] == '':
                    credential['effective_date'] = ''
                cur.execute(sql, (system_cd, event_json(prev_event), event_json(last_event), corp_num, corp_state, cred_type, cred_id, 
                            schema_name, schema_version, cred_json, cred_hash, credential_reason, datetime.datetime.now(),))
            return 1
        except Exception as e:
            # ignore duplicate hash ("duplicate key value violates unique constraint "cl_hash_index"")
            # re-raise all others
            stre = str(e)
            if "duplicate key value violates unique constraint" in stre and "cl_hash_index" in stre:
                #LOGGER.info("Hash exception, skipping duplicate credential for corp: " + corp_num + " " + cred_type + " " + cred_id + " " + str(e))
                cur.execute("rollback to savepoint save_" + cred_type)
                #LOGGER.info(cred_json)
                return 0
            else:
                LOGGER.error(stre)
                LOGGER.error(traceback.print_exc())
                log_error("EventProcessor exception updating DB: " + str(error))
                raise

    # determine jurisdiction for corp
    def get_corp_jurisdiction(self, corp, jurisdiction):
        registered_jurisdiction = ""
        if corp['corp_type']['corp_class'] == 'BC':
            registered_jurisdiction = "BC"
        elif corp['corp_type']['corp_class'] == 'XPRO' or corp['corp_typ_cd'] == 'XP' or corp['corp_typ_cd'] == 'XL' or corp['corp_typ_cd'] == 'XCP' or corp['corp_typ_cd'] == 'XS':
            if jurisdiction is not None and 'can_jur_typ_cd' in jurisdiction:
                if jurisdiction['can_jur_typ_cd'] == 'OT':
                    if 'othr_juris_desc' in jurisdiction and jurisdiction['othr_juris_desc'] is not None:
                        registered_jurisdiction = jurisdiction['othr_juris_desc']
                    else:
                        registered_jurisdiction = jurisdiction['can_jur_typ_cd']
                else:
                    registered_jurisdiction = jurisdiction['can_jur_typ_cd']
        else:
            # default to BC
            registered_jurisdiction = "BC"
        return registered_jurisdiction

    # corp num with prefix
    def corp_num_with_prefix(self, corp_typ_cd, corp_num):
        p_corp_num = corp_num
        if p_corp_num.startswith('BC'):
            return p_corp_num
        if corp_typ_cd == 'BC':
            p_corp_num = 'BC' + corp_num
        elif corp_typ_cd == 'ULC':
            p_corp_num = 'BC' + corp_num
        elif corp_typ_cd == 'CC':
            p_corp_num = 'BC' + corp_num
        elif corp_typ_cd == 'BEN':
            p_corp_num = 'BC' + corp_num
        return p_corp_num

    # determine reason for address credential - returns reason code only
    def build_corp_reason_code(self, loop_start_event):
        corp_reason = ""

        # corp_state reason code
        if 'filing_typ_cd' in loop_start_event['filing']:
            corp_reason = 'Filing:' + loop_start_event['filing']['filing_typ_cd']
        elif 'filing_type' in loop_start_event['filing']:
            corp_reason = 'Filing:' + loop_start_event['filing']['filing_type']
        else:
            corp_reason = 'Event:' + loop_start_event['event_typ_cd'] 

        if (len(corp_reason) > 0 and corp_reason.startswith(", ")):
            corp_reason = corp_reason[2:]
        if (255 < len(corp_reason)):
            endch = corp_reason[len(corp_reason)-1]
            corp_reason = corp_reason[:251] + '...' + endch

        return corp_reason
        
    # determine reason for address credential - returns reason code only
    def build_lear_corp_reason_code(self, event):
        filing = event['transaction']['filing']
        corp_reason = filing['filing_type'] if (filing and 'filing_type' in filing) else ''
        return corp_reason

    def check_required_field(self, corp_num, corp_cred, cred_attr):
        if cred_attr not in corp_cred or corp_cred[cred_attr] is None or corp_cred[cred_attr] == '':
            LOGGER.info(">>>Data Issue:Credential: " + corp_num + " " + cred_attr + " " + corp_cred)

    def compare_dates(self, first_date, op, second_date, msg):
        # check for empty or null strings
        if first_date is None or (isinstance(first_date, str) and 0 == len(first_date)):
            LOGGER.info(msg + " first date is None or empty string")
        if second_date is None or (isinstance(second_date, str) and 0 == len(second_date)):
            LOGGER.info(msg + " second date is None or empty string")
        # make sure the two variables are the same data type
        if isinstance(first_date, str) and not isinstance(second_date, str):
            second_date = str(second_date)
        elif isinstance(second_date, str) and not isinstance(first_date, str):
            first_date = str(first_date)
        # now do the comparison
        if op == "==" or op == '=':
            return first_date == second_date
        elif op == "<=":
            return first_date <= second_date
        elif op == "<":
            return first_date < second_date
        elif op == ">":
            return first_date > second_date
        elif op == ">=":
            return first_date >= second_date
        LOGGER.error(msg + "invalid date op" + op)
        return False

    # generate address credential
    def generate_address_credential(self, corp_num, corp_info, office, address, dba_corp_num, dba_name):
        addr_cred = {}
        addr_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_num)
        if 0 < len(corp_info['org_names']):
            org_name = self.corp_rec_at_effective_date(corp_info['org_names'], office['start_event'])
            if org_name is not None:
                addr_cred['addressee'] = org_name['corp_nme'] if org_name['corp_nme'] else ''
            else:
                addr_cred['addressee'] = ''
        else:
            addr_cred['addressee'] = ''
        addr_cred['address_type'] = office['office_type']['office_typ_cd']
        addr_cred['civic_address'] = address['local_addr'] if address['local_addr'] else ''
        if 'city' in address:
            addr_cred['municipality'] = address['city'] if address['city'] else ''
        else:
            addr_cred['municipality'] = ''
        if 'province' in address:
            addr_cred['province'] = address['province'] if address['province'] else ''
        else:
            addr_cred['province'] = ''
        if 'postal_cd' in address:
            addr_cred['postal_code'] = address['postal_cd'] if address['postal_cd'] else ''
        else:
            addr_cred['postal_code'] = ''
        if 'country_typ_cd' in address:
            addr_cred['country'] = address['country_typ_cd'] if address['country_typ_cd'] else ''
        else:
            addr_cred['country'] = ''
        addr_cred['address_effective_date'] = self.filter_min_date(office['effective_start_date'])
        addr_cred['effective_date'] = addr_cred['address_effective_date']
        if office['end_event_id'] is not None and office['end_event']['effective_date'] <= corp_info['current_date']:
            addr_cred['expiry_date'] = office['effective_end_date']
        else:
            addr_cred['expiry_date'] = ''

        return addr_cred

    # store credentials for the provided corp
    def store_credentials(self, cur, system_type_cd, prev_event, last_event, corp_num, corp_state, corp_info, corp_creds):
        cred_count = 0
        for corp_cred in corp_creds:
            if corp_cred['credential']['effective_date'] is not None and corp_cred['credential']['effective_date'] != '':
                cred_count = cred_count + self.insert_json_credential(cur, system_type_cd, prev_event, last_event, corp_num, corp_state, 
                                                                corp_cred['cred_type'], corp_cred['id'], corp_cred['schema'], corp_cred['version'], 
                                                                corp_cred['credential'], corp_cred['credential_reason'])
            else:
                LOGGER.error("Error can't issue a credential with no effective date! " + corp_num + " " + corp_cred['cred_type'] + " " + str(corp_cred))
        return cred_count

    def build_credential_dict(self, cred_type, schema, version, cred_id, credential, credential_reason, effective_date):
        cred = {}
        cred['cred_type'] = cred_type
        cred['schema'] = schema
        cred['version'] = version
        cred['credential'] = credential
        cred['credential_reason'] = credential_reason
        cred['id'] = cred_id
        cred['effective_date'] = effective_date
        return cred

    # credential effective date is the latest of the individual effective dates in the credential
    def credential_effective_date(self, corp_cred):
        effective_date = None
        if 'entity_status_effective' in corp_cred and str(corp_cred['entity_status_effective']) != '' and corp_cred['entity_status_effective'] is not None:
            effective_date = corp_cred['entity_status_effective']
        if 'entity_name_effective' in corp_cred and str(corp_cred['entity_name_effective']) != '' and corp_cred['entity_name_effective'] is not None:
            if effective_date is None or self.compare_dates(effective_date, "<", corp_cred['entity_name_effective'], 'cred:' + str(corp_cred)):
                effective_date = corp_cred['entity_name_effective']
        if 'entity_name_assumed_effective' in corp_cred and str(corp_cred['entity_name_assumed_effective']) != '' and corp_cred['entity_name_assumed_effective'] is not None:
            if effective_date is None or self.compare_dates(effective_date, "<", corp_cred['entity_name_assumed_effective'], 'cred:' + str(corp_cred)):
                effective_date = corp_cred['entity_name_assumed_effective']
        return effective_date

    def unique_effective_recs(self, rec_type, rec_attr, corp_records, effective_recs):
        for corp_record in corp_records:
            rec_summary = {}
            rec_summary['corp_num'] = corp_record['corp_num']
            rec_summary['rec_type'] = rec_type
            rec_summary['effective_start_date'] = corp_record['effective_start_date']
            rec_summary['effective_end_date']   = corp_record['effective_end_date']
            rec_summary['desc']     = corp_record[rec_attr]
            effective_recs.append(rec_summary)

        # sort to get in date order, and determine ACT/HIS transition dates
        #LOGGER.info('>>>>>>>>>> unique_effective_recs start', rec_type)
        effective_recs = sorted(effective_recs, key=lambda k: k['effective_end_date'])
        effective_recs = sorted(effective_recs, key=lambda k: k['effective_start_date'])
        #LOGGER.info('<<<<<<<<<< unique_effective_recs end', rec_type)

        return effective_recs

    # build a list of unique effective/expiry dates
    def unique_effective_events(self, corp_records, effective_events):
        for corp_record in corp_records:
            effective_events.append(corp_record['start_event'])
            if corp_record['end_event_id'] is not None:
                effective_events.append(corp_record['end_event'])

        # sort to get in date order, and determine ACT/HIS transition dates
        effective_events = sorted(effective_events, key=lambda k: k['event_timestmp'])
        effective_events = sorted(effective_events, key=lambda k: k['effective_date'])
        # eliminate duplicates
        ret_effective_events = []
        prev_effective_event = None
        for effective_event in effective_events:
            if prev_effective_event is None or effective_event['effective_date'] != prev_effective_event['effective_date']:
                ret_effective_events.append(effective_event)
            prev_effective_event = effective_event
        return ret_effective_events

    # org_names etc. active at effective date
    def corp_rec_at_effective_date(self, corp_recs, loop_start_event):
        # pick the lowest effective date where the passed in start date is in range
        loop_start_date = loop_start_event['effective_date']
        loop_start_id = loop_start_event['event_id']
        ret_corp_rec = None

        # find record matching the provided event
        for corp_rec in corp_recs:
            # ignore the record if start_date > end_date
            if self.compare_dates(corp_rec['effective_start_date'], "<=", corp_rec['effective_end_date'], str(corp_rec)):
                #if corp_rec['start_event_id'] == loop_start_id:
                #    # if the start event id matches then we have a match
                #    return corp_rec
                if (self.compare_dates(corp_rec['effective_start_date'], "<=", loop_start_date, str(corp_rec)) and
                    (self.compare_dates(corp_rec['effective_end_date'], ">", loop_start_date, str(corp_rec)))):
                    # if the record date is earlier than the event effective date, it is potential match
                    if 'end_event_id' not in corp_rec or corp_rec['end_event_id'] is None:
                        # if we hit the active record, use it (ignore anything dated after the start date of the currently active record)
                        ret_corp_rec = corp_rec
                        break
                    elif ret_corp_rec is None:
                        ret_corp_rec = corp_rec
                    elif self.compare_dates(corp_rec['effective_start_date'], ">", ret_corp_rec['effective_start_date'], str(corp_rec)):
                        # pick the latest record based on effective date
                        ret_corp_rec = corp_rec
                    elif self.compare_dates(corp_rec['effective_start_date'], "==", ret_corp_rec['effective_start_date'], str(corp_rec)):
                        if self.compare_dates(corp_rec['effective_end_date'], ">", ret_corp_rec['effective_end_date'], str(corp_rec)):
                            # if the start dates are the same, select the latest end date
                            ret_corp_rec = corp_rec

        if ret_corp_rec is None and len(corp_recs) > 0:
            if 'start_event' in corp_recs[0] and is_data_conversion_event(corp_recs[0]['start_event']):
                if corp_recs[0]['effective_start_date'] == corp_recs[0]['start_event']['effective_date']:
                    ret_corp_rec = corp_recs[0]

        return ret_corp_rec

    # currently active state record
    def get_corp_active_state_colin(self, corp_info):
        ret_corp_state = None
        for corp_state in corp_info['corp_state']:
            if corp_state['end_event_id'] is None:
                return corp_state
            elif ret_corp_state is None:
                ret_corp_state = corp_state
            elif corp_state['effective_start_date'] > ret_corp_state['effective_start_date']:
                ret_corp_state = corp_state
        return ret_corp_state

    # currently active state record
    def get_corp_active_state_lear(self, corp_info):
        return {
            "state_typ_cd": corp_info['state_typ_cd'],
            "op_state_typ_cd": corp_info['op_state_typ_cd'],
        }

    # currently active state record
    def get_corp_active_state(self, system_type_cd, corp_info):
        if system_type_cd == system_type:
            return self.get_corp_active_state_colin(corp_info)
        elif system_type_cd == lear_system_type:
            return self.get_corp_active_state_lear(corp_info)
        else:
            raise Exception(f"Unknown system type: {system_type_cd}")

    def corp_unique_record_list(self, corp_num, corp_info):
        # generate a list of (sorted) effective dates for our corp registration credentials
        effective_recs = self.unique_effective_recs('corp_state', 'state_typ_cd', corp_info['corp_state'], [])
        effective_recs = self.unique_effective_recs('jurisdiction', 'can_jur_typ_cd', corp_info['jurisdiction'], effective_recs)
        effective_recs = self.unique_effective_recs('org_names', 'corp_nme', corp_info['org_names'], effective_recs)
        effective_recs = self.unique_effective_recs('org_name_assumed', 'corp_nme', corp_info['org_name_assumed'], effective_recs)
        #effective_recs = self.unique_effective_recs('office', '', corp_info['office'], effective_recs)
        #effective_recs = self.unique_effective_recs('parties', '', corp_info['parties'], effective_recs)

        return effective_recs

    # determine the unique event list for the current corp
    def corp_unique_event_list(self, corp_num, corp_info):
        # generate a list of (sorted) effective dates for our corp registration credentials
        effective_events = self.unique_effective_events(corp_info['corp_state'], [])
        effective_events = self.unique_effective_events(corp_info['jurisdiction'], effective_events)
        effective_events = self.unique_effective_events(corp_info['org_names'], effective_events)
        effective_events = self.unique_effective_events(corp_info['org_name_assumed'], effective_events)
        #effective_events = self.unique_effective_events(corp_info['office'], effective_events)
        #effective_events = self.unique_effective_events(corp_info['parties'], effective_events)

        return effective_events

    def current_and_future_corp_events_colin(self, corp_num, corp_info):
        # get events
        effective_events = self.corp_unique_event_list(corp_num, corp_info)

        # check if the effective date of any event is beyond "now()" (based on when the data was loaded from BC Reg)
        future_events = []
        past_events = []
        for event in effective_events:
            if event['effective_date'] > corp_info['current_date']:
                future_events.append(event)
            else:
                past_events.append(event)

        return (past_events, future_events)

    def current_and_future_corp_events_lear(self, corp_num, corp_info):
        # check if the effective date of any event is beyond "now()" (based on when the data was loaded from BC Reg)
        future_events = []
        past_events = []
        for corp_version in corp_info['versions']:
            effective_date = corp_version['effective_date']
            if effective_date.tzinfo is None or effective_date.tzinfo.utcoffset(effective_date) is None:
                effective_date = effective_date.replace(tzinfo=pytz.utc)
            current_date = corp_info['current_date']
            if current_date.tzinfo is None or current_date.tzinfo.utcoffset(current_date) is None:
                current_date = current_date.replace(tzinfo=pytz.utc)
            if effective_date > current_date:
                future_events.append(corp_version)
            else:
                past_events.append(corp_version)

        return (past_events, future_events)

    def current_and_future_corp_events(self, system_type_cd, corp_num, corp_info):
        if system_type_cd == system_type:
            return self.current_and_future_corp_events_colin(corp_num, corp_info)
        elif system_type_cd == lear_system_type:
            return self.current_and_future_corp_events_lear(corp_num, corp_info)
        else:
            raise Exception(f"Unknown system type: {system_type_cd}")

    def is_min_date(self, cred_date):
        if not cred_date:
            return True
        if isinstance(cred_date, str):
            if cred_date == "":
                return True
            if cred_date < MIN_START_DATE_TZ.astimezone(pytz.utc).isoformat():
                return True
        elif isinstance(cred_date, datetime.date):
            if cred_date.tzinfo is None or cred_date.tzinfo.utcoffset(cred_date) is None:
                if cred_date < MIN_VALID_DATE:
                    return True
            else:
                if cred_date < MIN_VALID_DATE_TZ:
                    return True
        return False

    def filter_min_date(self, cred_date):
        if not cred_date:
            return ""
        if isinstance(cred_date, str):
            if cred_date < MIN_START_DATE_TZ.astimezone(pytz.utc).isoformat():
                return ""
        elif isinstance(cred_date, datetime.date):
            if cred_date.tzinfo is None or cred_date.tzinfo.utcoffset(cred_date) is None:
                if cred_date < MIN_VALID_DATE:
                    return ""
            else:
                if cred_date < MIN_VALID_DATE_TZ:
                    return ""
        return cred_date

    # check if the org name is a notice of alteration
    def is_notice_of_alteration_event(self, org_name):
        if org_name is not None:
            if 'start_event' in org_name and 'event_typ_cd' in org_name['start_event']:
                if org_name['start_event']['event_typ_cd'] == 'FILE':
                    if ('filing' in org_name['start_event'] 
                        and org_name['start_event']['filing']['filing_typ_cd'] == 'NOALB' 
                        or org_name['start_event']['filing']['filing_typ_cd'] == 'NOALC' 
                        or org_name['start_event']['filing']['filing_typ_cd'] == 'NOALD' 
                        or org_name['start_event']['filing']['filing_typ_cd'] == 'NOALE' 
                        or org_name['start_event']['filing']['filing_typ_cd'] == 'NOALR'
                        or org_name['start_event']['filing']['filing_typ_cd'] == 'NOALU'):
                        return True
        return False

    # check for specific relationship type - owned sole prop (DBA)
    def is_owned_sole_prop(self, party, corp_num, corp_info):
        # "parent" is defined as the corp in "bus_company_num" (as opposed to "corp_num")
        # ... assume it may be different for different party records
        if corp_num == party['corp_num']:
            is_parent = False
        else:
            is_parent = True

        # check that self is a sole prop ...
        if ((not is_parent) and (corp_info['corp_typ_cd'] in ('SP', 'MF'))):
            # ... and parent bus_company_num exists
            if (party['bus_company_num'] is not None and 'corp_info' in party and 0 < len(party['corp_info']['corp_num'])):
                return True

        return False

    # check for specific relationship type - owner of sole prop (Owns)
    def is_owner_of_sole_prop(self, party, corp_num, corp_info):
        if not 'corp_info' in party:
            return False;

        # "parent" is defined as the corp in "bus_company_num" (as opposed to "corp_num")
        # ... assume it may be different for different party records
        if corp_num == party['corp_num']:
            is_parent = False
        else:
            is_parent = True

        # check that child is a sole prop
        if (is_parent and 'corp_info' in party and (party['corp_info']['corp_typ_cd'] in ('SP', 'MF'))):
            return True

        return False

    # check if we should build a relationship credential for the given party record
    def should_generate_relationship_credential(self, party, prev_event, last_event, corp_num, corp_info):
        #LOGGER.info("should_generate_relationship_credential", party['corp_num'], party['bus_company_num'], party['party_typ_cd'])
        if not 'corp_info' in party:
            #LOGGER.info("  --> no corp_info, return False")
            return False;

        # only look at FBO's (for now)
        if party['party_typ_cd'] != 'FBO' and party['party_typ_cd'] != 'organization':
            #LOGGER.info("  --> party['party_typ_cd'] != 'FBO'/'organization', return False")
            return False

        # special case where the corp_num and bus_company_num are the same
        #if 'bus_company_num' in party and party['bus_company_num'] == corp_num:
        #    LOGGER.info("  --> party['bus_company_num'] == corp_num, return False")
        #    return False

        """
        # include if this record is within the desired event range ...
        if ((prev_event['event_date'] <= party['start_event']['event_timestmp'] and party['start_event']['event_timestmp'] <= last_event['event_date']) or
            (party['end_event_id'] is not None and prev_event['event_date'] <= party['end_event']['event_timestmp'] and party['end_event']['event_timestmp'] <= last_event['event_date'])):
            #LOGGER.info("  ---> party record is in our window, check for ownership")

            # ... AND it belongs to the correct company type/party type logic
            if self.is_owned_sole_prop(party, corp_num, corp_info) or self.is_owner_of_sole_prop(party, corp_num, corp_info):
                #LOGGER.info("  --->", self.is_owned_sole_prop(party, corp_num, corp_info), self.is_owner_of_sole_prop(party, corp_num, corp_info))
                return True

            # TBD check for partnerships and amalgamations
            #if self.is_partnership() or self.is_amalgamation():
            #   return True
        """

        # ... AND it belongs to the correct company type/party type logic
        if self.is_owned_sole_prop(party, corp_num, corp_info) or self.is_owner_of_sole_prop(party, corp_num, corp_info):
            #LOGGER.info("  --->", self.is_owned_sole_prop(party, corp_num, corp_info), self.is_owner_of_sole_prop(party, corp_num, corp_info))
            return True

        #LOGGER.info("  ---> fall-through, return False")

        return False


    # randomize name and phone #
    def random_seed(self, name):
        seed = 0
        for ch in name:
            seed = seed + ord(ch)
        return seed

    def random_name(self, name):
        # need to have a deterministic random function for each name
        name = name.split()[0].upper() if name else "RANDOM"
        my_random = random.Random(self.random_seed(name))
        if names_list and 0 < len(names_list):
            ret_name = names_list[my_random.randint(0, len(names_list)-1)][0].upper()
        else:
            ret_name = ""
            for ch in name:
                ret_ch = chr(ord('A') + my_random.randint(0, 25))
                ret_name = ret_name + ret_ch
        return ret_name

    def random_phone(self, fn, ln):
        name = fn + ln
        phone_no = "250"
        while True:
            for ch in name:
                phone_no = phone_no + chr(ord('0') + ord(ch) % 10)
                if len(phone_no) == 10:
                    return phone_no

    # generate verified person info
    def get_vp_info(self, party):
        vp_fn = self.random_name(party["first_nme"])
        vp_ln = self.random_name(party["last_nme"])

        vp_reg_id = "VP" + vp_fn + vp_ln
        vp_email = vp_fn + "." + vp_ln + "@MAIL.COM"
        vp_phone = self.random_phone(vp_fn, vp_ln)

        return (vp_reg_id, vp_fn, vp_ln, vp_email, vp_phone)

    def generate_bn_credential(self, system_type_cd, corp_num, corp_info, effective_event=None):
        """Generate a BN credential."""
        # generate a BN credential if the corp has a BN
        if "bn_9" in corp_info and corp_info["bn_9"] and 0 < len(corp_info["bn_9"]):
            # print(">>> generate a bn credential for", corp_num, corp_info)
            effective_date = corp_info["recognition_dts"] if corp_info["recognition_dts"] else effective_event['effective_date'] if effective_event else None
            bn_cred = {}
            bn_cred["registration_id"] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
            bn_cred["business_number"] = corp_info["bn_9"].strip()
            bn_cred["effective_date"] = effective_date
            bn_cred["expiry_date"] = ""
            bn_cred_dict = self.build_credential_dict(bn_credential, bn_schema, bn_version, bn_cred['registration_id'], bn_cred, '', bn_cred['effective_date'])
            return bn_cred_dict

        return None

    def generate_credentials_of_type(self, system_type_cd, credential_type_cd, corp_num, corp_info):
        """Generate credentials only of the specified type."""
        corp_creds = []
        if credential_type_cd == bn_credential:
            bn_cred = self.generate_bn_credential(system_type_cd, corp_num, corp_info)
            if bn_cred:
                corp_creds.append(bn_cred)
        else:
            raise Exception("Error credential type not supported: " + credential_type_cd)

        return corp_creds

    # generate credentials for the provided corp
    def generate_credentials_colin(self, system_type_cd, prev_event, last_event, corp_num, corp_info):
        """
        Generate credentials for the given corporation based on the supplied event range.
        prev_event and last_event represent the start and end event range we are processing.
        (for the initial load, prev_event is the genesis date of Jan 1, 0000)
        The event "date" is based on some complicated logic and can come from the event or the related filing.
        """
        # LOGGER.info("Generate credentials for", corp_num, prev_event, last_event)
        corp_creds = []

        # get events - only generate credentials for events in the past
        (effective_events, future_events) = self.current_and_future_corp_events(system_type_cd, corp_num, corp_info)
        # print(corp_num, len(effective_events), len(future_events))

        if 0 < len(effective_events):
            #LOGGER.info('effective_events', effective_events)
            # build a standard dict for the first and last events in the effective range
            prev_effective_event = event_dict(effective_events[0]['event_id'], effective_events[0]['event_timestmp'])
            last_effective_event = event_dict(effective_events[len(effective_events)-1]['event_id'], effective_events[len(effective_events)-1]['event_timestmp'])

            # get the "overlap" with the supplied event range (this check is based on the event date, the date the event was registered)
            #if self.compare_dates(prev_effective_event['event_date'], ">=", prev_event['event_date'], 'Events'):
            #    use_prev_event = prev_effective_event
            #else:
            #    use_prev_event = prev_event
            #if self.compare_dates(last_effective_event['event_date'], "<=", last_event['event_date'], 'Events'):
            #    use_last_event = last_effective_event
            #else:
            #    use_last_event = last_event

            use_prev_event = prev_event
            use_last_event = last_event

            # loop based on start/end events
            for i in range(len(effective_events)):
                loop_start_event = effective_events[i]

                #print(use_prev_event['event_date'], loop_start_event['event_timestmp'], use_last_event['event_date'])
                # for the registration credential, we need to check if this event is in the "overlap range"
                # note the special case logic for data conversion events:
                #   - if it is a data conversion event and we don't have any other dates we can apply, skip it
                #   - unless it is the most recent event, in which case include it anyways
                if (i < (len(effective_events)-1) and
                    is_data_conversion_event(loop_start_event) and
                    loop_start_event['event_timestmp'] == loop_start_event['effective_date']):
                    # skip data conversion event
                    pass
                elif use_prev_event['event_date'] <= loop_start_event['event_timestmp']: # and loop_start_event['event_timestmp'] <= use_last_event['event_date']:
                    # event is in the "overlap" range
                    # generate corp credential
                    corp_cred = {}
                    corp_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                    corp_cred['registration_date'] = self.filter_min_date(corp_info['recognition_dts'])
                    corp_cred['registration_expiry_date'] = ''
                    corp_cred['entity_type'] = corp_info['corp_type']['corp_typ_cd']

                    # org_names active at effective date
                    org_name = self.corp_rec_at_effective_date(corp_info['org_names'], loop_start_event)
                    if org_name is not None:
                        #LOGGER.info('org_name', org_name)
                        corp_cred['entity_name'] = org_name['corp_nme']
                        if (is_data_conversion_event(org_name['start_event']) and 
                            org_name['effective_start_date'] == org_name['start_event']['event_timestmp'] and
                            i < (len(effective_events)-1)
                            ):
                            corp_cred['entity_name_effective'] = ''
                        else:
                            corp_cred['entity_name_effective'] = self.filter_min_date(org_name['effective_start_date'])
                    else:
                        corp_cred['entity_name'] = ''
                        corp_cred['entity_name_effective'] = ''

                    # org_name_assumed active at effective date
                    org_name_assumed = self.corp_rec_at_effective_date(corp_info['org_name_assumed'], loop_start_event)
                    #LOGGER.info("org_name_assumed", org_name_assumed)
                    if org_name_assumed is not None:
                        #LOGGER.info('org_name_assumed', org_name_assumed)
                        corp_cred['entity_name_assumed'] = org_name_assumed['corp_nme'] 
                        if is_data_conversion_event(org_name_assumed['start_event']) and org_name_assumed['effective_start_date'] == org_name_assumed['start_event']['event_timestmp']:
                            corp_cred['entity_name_assumed_effective'] = ''
                        else:
                            corp_cred['entity_name_assumed_effective'] = self.filter_min_date(org_name_assumed['effective_start_date'])
                    else:
                        corp_cred['entity_name_assumed'] = ''
                        corp_cred['entity_name_assumed_effective'] = ''

                    # corp_state active at effective date
                    corp_state = self.corp_rec_at_effective_date(corp_info['corp_state'], loop_start_event)
                    if corp_state is not None:
                        #LOGGER.info('corp_state', corp_state)
                        corp_cred['entity_status'] = corp_state['op_state_typ_cd']
                        if is_data_conversion_event(corp_state['start_event']) and corp_state['effective_start_date'] == corp_state['start_event']['event_timestmp']:
                            corp_cred['entity_status_effective'] = ''
                        else:
                            corp_cred['entity_status_effective'] = self.filter_min_date(corp_state['effective_start_date'])
                    else:
                        corp_cred['entity_status'] = ''
                        corp_cred['entity_status_effective'] = ''

                    # jurisdiction active at effective date
                    jurisdiction = self.corp_rec_at_effective_date(corp_info['jurisdiction'], loop_start_event)
                    corp_cred['home_jurisdiction'] = self.get_corp_jurisdiction(corp_info, jurisdiction)
                    if corp_cred['home_jurisdiction'] and 0 < len(corp_cred['home_jurisdiction']) and corp_cred['home_jurisdiction'] != 'BC':
                        corp_cred['registered_jurisdiction'] = 'BC' 
                    else:
                        corp_cred['registered_jurisdiction'] = '' 
                    corp_cred['extra_jurisdictional_registration'] = ''
                    # determine the date to use for jurisdiction effective
                    if jurisdiction is not None:
                        if is_data_conversion_event(jurisdiction['start_event']) and jurisdiction['effective_start_date'] == jurisdiction['start_event']['event_timestmp']:
                            jurisdiction_effective_date = None
                        else:
                            jurisdiction_effective_date = self.filter_min_date(jurisdiction['effective_start_date'])
                    else:
                        jurisdiction_effective_date = None

                    # make sure we set an effective date for the credential!
                    #corp_cred['effective_date'] = self.credential_effective_date(corp_cred)
                    corp_cred['effective_date'] = loop_start_event['effective_date']
                    #if corp_cred['effective_date'] is None or corp_cred['effective_date'] == '':
                    #    corp_cred['effective_date'] = loop_start_event['effective_date']
                    if corp_cred['effective_date'] is None or corp_cred['effective_date'] == '':
                        corp_cred['effective_date'] = corp_cred['registration_date']
                    #if corp_cred['effective_date'] is None or (jurisdiction_effective_date is not None and self.compare_dates(jurisdiction_effective_date, ">", corp_cred['effective_date'], "jurisdiction_effective")):
                    if corp_cred['effective_date'] is None or corp_cred['effective_date'] == '':
                        if jurisdiction_effective_date is not None:
                            corp_cred['effective_date'] = jurisdiction_effective_date

                    # check for NOALU/NOALB/NOALC filing type on the org_name end event
                    if self.is_notice_of_alteration_event(org_name):
                        # erase the corp_type in previously created/expired credentials
                        #print("Cleaning corp type history for 'notice of alteration'", corp_num)
                        for cred in corp_creds:
                            if cred['credential']['effective_date'] < corp_cred['effective_date']:
                                cred['credential']['entity_type'] = ''

                    corp_cred['expiry_date'] = ''
                    corp_cred['registration_renewal_effective'] = ''
                    corp_cred['entity_name_trans'] = ''
                    corp_cred['entity_name_trans_effective'] = ''

                    reason_description = self.build_corp_reason_code(loop_start_event)

                    #self.check_required_field(corp_num, corp_cred, 'registration_date')
                    #self.check_required_field(corp_num, corp_cred, 'entity_name')
                    #self.check_required_field(corp_num, corp_cred, 'entity_status')

                    corp_cred = self.build_credential_dict(corp_credential, corp_schema, corp_version, corp_num, corp_cred, reason_description, corp_cred['effective_date'])

                    # these will be sorted by date, but we need to make sure we are not submitting duplicates
                    # checking against the previously generated credential is sufficient
                    #LOGGER.info('credential', corp_cred['credential'])
                    if (len(corp_creds) == 0) or (len(corp_creds) > 0 and corp_cred['credential'] != corp_creds[len(corp_creds)-1]['credential']):
                        corp_creds.append(corp_cred)
                    else:
                        #LOGGER.info(" >>> Skip credential for reason Duplicate")
                        pass
                else:
                    # skipping event because out of range of start/end period
                    #LOGGER.info(use_prev_event['event_date'], loop_start_event['event_timestmp'], use_last_event['event_date'])
                    pass

        else:
            # skip due to no effective dates in range
            #LOGGER.info(" >>> Skip no effective events in range")
            pass

        # generate addr credential(s)
        corp_offices = sorted(corp_info['office'], key=lambda k: int(k['start_event_id']))
        corp_offices = sorted(corp_info['office'], key=lambda k: k['effective_start_date'])
        for office in corp_offices:
            if ((prev_event['event_date'] <= office['start_event']['event_timestmp'] and office['start_event']['event_timestmp'] <= last_event['event_date']) or
                (office['end_event_id'] is not None and prev_event['event_date'] <= office['end_event']['event_timestmp'] and office['end_event']['event_timestmp'] <= last_event['event_date'])):
                # ensure address history is generated correctly
                if 'office_typ_cd' in office:
                    if 'delivery_addr' in office and 'local_addr' in office['delivery_addr']:
                        addr_cred = self.generate_address_credential(corp_num, corp_info, office, office['delivery_addr'], "", "")
                        reason_description = self.build_corp_reason_code(office['start_event'])
                        corp_creds.append(self.build_credential_dict(addr_credential, addr_schema, addr_version, 
                                                                    corp_num + ',' + office['office_typ_cd'], 
                                                                    addr_cred, reason_description, addr_cred['effective_date']))

        corp_type = corp_info['corp_typ_cd']

        # generate relationship credential(s) 
        if 'parties' in corp_info and 0 < len(corp_info['parties']):
            # ensure relationship history is generated correctly
            # corp_parties = sorted(corp_info['parties'], key=lambda k: int(k['start_event_id']))
            corp_parties = sorted(corp_info['parties'], key=lambda k: k['effective_start_date'])
            # first check if party records are for unique firms
            party_count = {}
            for party in corp_parties:
                if self.should_generate_relationship_credential(party, prev_event, last_event, corp_num, corp_info):
                    if corp_num == party['corp_num']:
                        count_corp_num = party['bus_company_num']
                    else:
                        count_corp_num = party['corp_num']
                    if count_corp_num in party_count:
                        party_count[count_corp_num] = party_count[count_corp_num] + 1
                    else:
                        party_count[count_corp_num] = 1

            # now generate credentials
            for party in corp_parties:
                if self.should_generate_relationship_credential(party, prev_event, last_event, corp_num, corp_info):
                    dba_cred = {}
                    dba_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                    dba_cred['associated_registration_id'] = self.corp_num_with_prefix(party['corp_info']['corp_typ_cd'], party['corp_info']['corp_num'])
                    if self.is_owner_of_sole_prop(party, corp_num, corp_info):
                        dba_cred['relationship'] = 'Owns'
                        dba_cred['relationship_description'] = 'Does Business As'
                        dba_cred['associated_registration_name'] = ''
                    elif self.is_owned_sole_prop(party, corp_num, corp_info):
                        dba_cred['relationship'] = 'IsOwned'
                        dba_cred['relationship_description'] = 'Is Owned By'
                        if 'business_nme' in party and 0 < len(party['business_nme']):
                            dba_cred['associated_registration_name'] = party['business_nme']
                        else:
                            dba_cred['associated_registration_name'] = ''
                    else:
                        dba_cred['relationship'] = 'TBD' # party['']
                        dba_cred['relationship_description'] = 'TBD' # party['']
                        dba_cred['associated_registration_name'] = ''
                    dba_cred['relationship_status'] = 'ACT'
                    dba_cred['effective_date'] = party['effective_start_date']

                    # if the start event is 'ADMIN' type and there is only one party record, use the firm effective date
                    if 'start_event' in party and party['start_event']['event_typ_cd'] == 'ADMIN' and party_count[party['corp_info']['corp_num']] == 1 and party['corp_info']['recognition_dts']:
                        dba_cred['effective_date'] = party['corp_info']['recognition_dts']

                    dba_cred['relationship_status_effective'] = self.filter_min_date(dba_cred['effective_date'])
                    if 'end_event_id' in party and party['end_event_id'] is not None and party['end_event']['effective_date'] <= corp_info['current_date']:
                        dba_cred['expiry_date'] = party['effective_end_date']
                    else:
                        dba_cred['expiry_date'] = ''
                    if 'start_event' in party:
                        reason_description = self.build_corp_reason_code(party['start_event'])
                    else:
                        reason_description = ""
                    corp_creds.append(self.build_credential_dict(dba_credential, dba_schema, dba_version, dba_cred['registration_id'], dba_cred, reason_description, dba_cred['effective_date']))

        # generate a BN credential if the corp has a BN
        effective_event = effective_events[0] if 0 < len(effective_events) else None
        bn_cred = self.generate_bn_credential(system_type_cd, corp_num, corp_info, effective_event=effective_event)
        if bn_cred:
            corp_creds.append(bn_cred)

        if GENERATE_EXTRA_DEMO_CREDS:
            # DEMO generate Verified Individual credentials and relationships (2 way)
            vi_party_types = {"DIR":"Director", "OFF":"Officer", "FIO":"Firm Owner",}
            if 'parties' in corp_info and 0 < len(corp_info['parties']):
                # ensure relationship history is generated correctly
                corp_parties = sorted(corp_info['parties'], key=lambda k: int(k['start_event_id']))
                corp_parties = sorted(corp_parties, key=lambda k: k['effective_start_date'])
                for party in corp_parties:
                    if party["party_typ_cd"] in vi_party_types and party["corp_num"] == corp_num and ("end_event" not in party or party["end_event"] is None):
                        (vp_reg_id, vp_fn, vp_ln, vp_email, vp_phone) = self.get_vp_info(party)

                        # generate a verified person credential
                        #print(">>> generate a verified person credential for", vp_reg_id, vp_fn, vp_ln, vp_email, vp_phone)
                        vp_cred = {}
                        vp_cred["registration_id"] = vp_reg_id
                        vp_cred["full_name"] = vp_fn + " " + vp_ln
                        vp_cred["entity_status"] = 'ACT'
                        vp_cred["first_name"] = vp_fn
                        vp_cred["last_name"] = vp_ln
                        vp_cred["email_address"] = vp_email
                        vp_cred["phone_number"] = vp_phone
                        # TODO hard code the effective date for now
                        vp_cred["effective_date"] = "2000-01-01"
                        vp_cred["expiry_date"] = ""
                        corp_creds.append(self.build_credential_dict(vp_credential, vp_schema, vp_version, vp_cred['registration_id'], vp_cred, '', vp_cred['effective_date']))

                        # generate relationship credentials
                        #print(">>> generate relationship credentials between", corp_num, party["party_typ_cd"], vp_reg_id, vp_email, vp_phone)
                        corp_vp_rel_cred = {}
                        vp_corp_rel_cred = {}
                        corp_vp_rel_cred["registration_id"] = vp_reg_id
                        corp_vp_rel_cred["associated_registration_id"] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                        corp_vp_rel_cred["associated_registration_name"] = ""
                        corp_vp_rel_cred["relationship"] = party["party_typ_cd"]
                        corp_vp_rel_cred["relationship_description"] = vi_party_types[party["party_typ_cd"]]
                        corp_vp_rel_cred["relationship_status"] = 'ACT'
                        corp_vp_rel_cred["relationship_status_effective"] = party['effective_start_date']
                        corp_vp_rel_cred["effective_date"] = party['effective_start_date']
                        corp_vp_rel_cred["expiry_date"] = ""
                        corp_creds.append(self.build_credential_dict(vp_rel_credential, vp_rel_schema, vp_rel_version, corp_vp_rel_cred['registration_id'], corp_vp_rel_cred, '', corp_vp_rel_cred['effective_date']))

                        vp_corp_rel_cred["registration_id"] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                        vp_corp_rel_cred["associated_registration_id"] = vp_reg_id
                        vp_corp_rel_cred["associated_registration_name"] = vp_fn + " " + vp_ln
                        vp_corp_rel_cred["relationship"] = party["party_typ_cd"]
                        vp_corp_rel_cred["relationship_description"] = vi_party_types[party["party_typ_cd"]]
                        vp_corp_rel_cred["relationship_status"] = 'ACT'
                        vp_corp_rel_cred["relationship_status_effective"] = party['effective_start_date']
                        vp_corp_rel_cred["effective_date"] = party['effective_start_date']
                        vp_corp_rel_cred["expiry_date"] = ""
                        corp_creds.append(self.build_credential_dict(org_rel_credential, org_rel_schema, org_rel_version, vp_corp_rel_cred['registration_id'], vp_corp_rel_cred, '', vp_corp_rel_cred['effective_date']))

        return corp_creds

    # generate credentials for the provided corp
    def generate_credentials_lear(self, system_type_cd, prev_event, last_event, corp_num, corp_info):
        """
        Generate credentials for the given corporation based on the supplied event range.
        prev_event and last_event represent the start and end event range we are processing.
        (for the initial load, prev_event is the genesis date of Jan 1, 0000)
        The event "date" is based on some complicated logic and can come from the event or the related filing.
        """
        """
        Generate credentials for the given corporation based on the supplied event range.
        prev_event and last_event represent the start and end event range we are processing.
        (for the initial load, prev_event is the genesis date of Jan 1, 0000)
        The event "date" is based on some complicated logic and can come from the event or the related filing.
        """
        # print("Generate credentials for", corp_num, prev_event, last_event)
        corp_creds = []

        # get events - only generate credentials for events in the past
        (effective_events, future_events) = self.current_and_future_corp_events(system_type_cd, corp_num, corp_info)
        effective_events = sorted(effective_events, key=lambda k: k['effective_date'])
        # print(">>> lengths   :", corp_num, len(effective_events), len(future_events))
        # print(">>> effective :", corp_num, json.dumps(effective_events, cls=CustomJsonEncoder, sort_keys=True))
        # print(">>> future    :", corp_num, json.dumps(future_events, cls=CustomJsonEncoder, sort_keys=True))

        # print(">>> corp_info:", json.dumps(corp_info, cls=CustomJsonEncoder, sort_keys=True))

        for event in effective_events:
            corp_version_info = event
            # print(">>> corp_version_info:", json.dumps(corp_version_info, cls=CustomJsonEncoder, sort_keys=True))

            corp_cred = {}
            corp_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
            corp_cred['registration_date'] = self.filter_min_date(corp_version_info['recognition_dts'])
            corp_cred['registration_expiry_date'] = ''
            corp_cred['entity_type'] = corp_version_info['corp_typ_cd']
            corp_cred['entity_name'] = corp_version_info['corp_nme']
            corp_cred['entity_name_effective'] = corp_version_info['corp_nme_effective_date']
            corp_cred['entity_name_assumed'] = corp_version_info['corp_nme_as'] 
            corp_cred['entity_name_assumed_effective'] = ''
            corp_cred['entity_status'] = corp_version_info['state_typ_cd']
            corp_cred['entity_status_effective'] = corp_version_info['state_typ_effective_date']
            corp_cred['home_jurisdiction'] = 'BC'
            corp_cred['registered_jurisdiction'] = 'BC' 
            corp_cred['extra_jurisdictional_registration'] = ''
            corp_cred['effective_date'] = corp_version_info['effective_date']

            """
            TODO
            # check for NOALU/NOALB/NOALC filing type on the org_name end event
            if self.is_notice_of_alteration_event(org_name):
                # erase the corp_type in previously created/expired credentials
                #print("Cleaning corp type history for 'notice of alteration'", corp_num)
                for cred in corp_creds:
                    if cred['credential']['effective_date'] < corp_cred['effective_date']:
                        cred['credential']['entity_type'] = ''
            """

            corp_cred['expiry_date'] = ''
            corp_cred['registration_renewal_effective'] = ''
            corp_cred['entity_name_trans'] = ''
            corp_cred['entity_name_trans_effective'] = ''

            reason_description = self.build_lear_corp_reason_code(event)

            corp_cred = self.build_credential_dict(corp_credential, corp_schema, corp_version, corp_num, corp_cred, reason_description, corp_cred['effective_date'])

            # these will be sorted by date, but we need to make sure we are not submitting duplicates
            # checking against the previously generated credential is sufficient
            #LOGGER.info('credential', corp_cred['credential'])
            if (len(corp_creds) == 0) or (len(corp_creds) > 0 and corp_cred['credential'] != corp_creds[len(corp_creds)-1]['credential']):
                corp_creds.append(corp_cred)
            else:
                #LOGGER.info(" >>> Skip credential for reason Duplicate")
                pass

        corp_type = corp_info['corp_typ_cd']

        # generate relationship credential(s)
        if 'parties' in corp_info and 0 < len(corp_info['parties']):
            # ensure relationship history is generated correctly
            corp_parties = sorted(corp_info['parties'], key=lambda k: int(k['transaction_id']))
            corp_parties = sorted(corp_parties, key=lambda k: k['effective_start_date'])
            # first check if party records are for unique firms
            party_count = {}
            for party in corp_parties:
                if self.should_generate_relationship_credential(party, prev_event, last_event, corp_num, corp_info):
                    if corp_num == party['corp_num']:
                        count_corp_num = party['bus_company_num']
                    else:
                        count_corp_num = party['corp_num']
                    if count_corp_num in party_count:
                        party_count[count_corp_num] = party_count[count_corp_num] + 1
                    else:
                        party_count[count_corp_num] = 1

            # now generate credentials
            for party in corp_parties:
                if self.should_generate_relationship_credential(party, prev_event, last_event, corp_num, corp_info):
                    dba_cred = {}
                    dba_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                    dba_cred['associated_registration_id'] = self.corp_num_with_prefix(party['corp_info']['corp_typ_cd'], party['corp_info']['corp_num'])
                    if self.is_owner_of_sole_prop(party, corp_num, corp_info):
                        dba_cred['relationship'] = 'Owns'
                        dba_cred['relationship_description'] = 'Does Business As'
                        dba_cred['associated_registration_name'] = ''
                    elif self.is_owned_sole_prop(party, corp_num, corp_info):
                        dba_cred['relationship'] = 'IsOwned'
                        dba_cred['relationship_description'] = 'Is Owned By'
                        if 'business_nme' in party and 0 < len(party['business_nme']):
                            dba_cred['associated_registration_name'] = party['business_nme']
                        else:
                            dba_cred['associated_registration_name'] = ''
                    else:
                        dba_cred['relationship'] = 'TBD' # party['']
                        dba_cred['relationship_description'] = 'TBD' # party['']
                        dba_cred['associated_registration_name'] = ''
                    dba_cred['relationship_status'] = 'ACT'
                    dba_cred['effective_date'] = party['effective_start_date']

                    # if the start event is 'ADMIN' type and there is only one party record, use the firm effective date
                    # if party['start_event']['event_typ_cd'] == 'ADMIN' and party_count[party['corp_info']['corp_num']] == 1 and party['corp_info']['recognition_dts']:
                    #     dba_cred['effective_date'] = party['corp_info']['recognition_dts']

                    dba_cred['relationship_status_effective'] = self.filter_min_date(dba_cred['effective_date'])
                    if party['end_transaction_id'] is not None and party['end_transaction']['effective_date'] <= corp_info['current_date']:
                        dba_cred['expiry_date'] = party['effective_end_date']
                    else:
                        dba_cred['expiry_date'] = ''
                    reason_description = self.build_corp_reason_code(party['transaction'])
                    corp_creds.append(self.build_credential_dict(dba_credential, dba_schema, dba_version, dba_cred['registration_id'], dba_cred, reason_description, dba_cred['effective_date']))

        # generate a BN credential if the corp has a BN
        effective_event = effective_events[0] if 0 < len(effective_events) else None
        bn_cred = self.generate_bn_credential(system_type_cd, corp_num, corp_info, effective_event=None)
        if bn_cred:
            corp_creds.append(bn_cred)

        return corp_creds


    # generate credentials for the provided corp
    def generate_credentials(self, system_type_cd, prev_event, last_event, corp_num, corp_info):
        """
        Generate credentials for the given corporation based on the supplied event range.
        prev_event and last_event represent the start and end event range we are processing.
        (for the initial load, prev_event is the genesis date of Jan 1, 0000)
        The event "date" is based on some complicated logic and can come from the event or the related filing.
        """
        if system_type_cd == system_type:
            return self.generate_credentials_colin(system_type_cd, prev_event, last_event, corp_num, corp_info)
        elif system_type_cd == lear_system_type:
            return self.generate_credentials_lear(system_type_cd, prev_event, last_event, corp_num, corp_info)
        else:
            raise Exception(f"Unknown system type: {system_type_cd}")

    def bc_reg_processor(self, system_type_cd, use_cache=False):
        if system_type_cd == system_type:
            return BCRegistries(use_cache)
        elif system_type_cd == lear_system_type:
            return BCReg_Lear(use_cache)
        else:
            raise Exception(f"Unknown system type: {system_type_cd}")

    def get_max_event_for_other_system_type(self, system_type_cd, use_cache=False):
        use_system_type_cd = lear_system_type if system_type_cd == system_type else system_type
        if system_type_cd == system_type:
            reg_system = BCRegistries(use_cache)
        elif system_type_cd == lear_system_type:
            reg_system = BCReg_Lear(use_cache)
        else:
            raise Exception(f"Unknown system type: {system_type_cd}")
        max_event_date = reg_system.get_max_event_date()
        max_event_id = reg_system.get_max_event(max_event_date)
        return (max_event_date, max_event_id)

    def get_in_scope_corps_for_other_system_type(self, system_type_cd):
        use_system_type_cd = lear_system_type if system_type_cd == system_type else system_type
        if system_type_cd == system_type:
            return LEAR_CORP_TYPES_IN_SCOPE
        elif system_type_cd == lear_system_type:
            return CORP_TYPES_IN_SCOPE
        else:
            raise Exception(f"Unknown system type: {system_type_cd}")

    # process corps that have been queued - update data from bc_registries
    def process_corp_event_queue_internal(self, system_type_cd, load_regs=True, generate_creds=False, use_cache=False, corp_types=CORP_TYPES_IN_SCOPE):
        """
        The main process for loading BC Reg data and producing credentials.
        This process takes unprocessed events from the EVENT_BY_CORP_FILING table, and for each corp_num:
           - if load_regs: loads data from BC Reg for that corp (stores in CORP_HISTORY_LOG)
           - if generate_creds: produces credentials (stores in CREDENTIAL_LOG)
        Credentials are submitted to TOB via the agent using a separate process.
        If use_cache is True, BC Reg data is cached into a local in-memory sqlite database prior to generating credentials.
        """

        print(">>> in scope corp types:", corp_types)

        sql1 = """SELECT RECORD_ID, 
                         SYSTEM_TYPE_CD, 
                         PREV_EVENT_ID, 
                         PREV_EVENT_DATE, 
                         LAST_EVENT_ID, 
                         LAST_EVENT_DATE, 
                         CORP_NUM, 
                         ENTRY_DATE
                  FROM EVENT_BY_CORP_FILING
                  WHERE SYSTEM_TYPE_CD = %s
                  AND RECORD_ID IN
                  (
                    SELECT RECORD_ID
                    FROM EVENT_BY_CORP_FILING 
                    WHERE SYSTEM_TYPE_CD = %s
                    AND PROCESS_DATE is null
                    ORDER BY RECORD_ID
                    LIMIT !BS!
                  )
                  ORDER BY RECORD_ID;"""

        sql1a = """SELECT RECORD_ID, 
                          SYSTEM_TYPE_CD, 
                          PREV_EVENT, 
                          LAST_EVENT, 
                          CORP_NUM, 
                          CORP_JSON, 
                          ENTRY_DATE
                  FROM CORP_HISTORY_LOG
                  WHERE SYSTEM_TYPE_CD = %s
                  AND RECORD_ID IN
                   (
                     SELECT RECORD_ID
                     FROM CORP_HISTORY_LOG 
                     WHERE SYSTEM_TYPE_CD = %s
                     AND PROCESS_DATE is null
                     ORDER BY RECORD_ID
                     LIMIT !BS!
                   )
                   ORDER BY RECORD_ID;"""

        sql2 = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT, LAST_EVENT, CORP_NUM, CORP_STATE, CORP_JSON, ENTRY_DATE)
                  VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql2a = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT, LAST_EVENT, CORP_NUM, CORP_STATE, CORP_JSON, ENTRY_DATE, PROCESS_DATE, PROCESS_SUCCESS, PROCESS_MSG)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql2b = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, PREV_EVENT_DATE, LAST_EVENT_ID, LAST_EVENT_DATE, CORP_NUM, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""

        sql3 = """UPDATE EVENT_BY_CORP_FILING
                  SET PROCESS_DATE = %s, PROCESS_SUCCESS = %s, PROCESS_MSG = %s
                  WHERE RECORD_ID = %s"""
        sql3a = """UPDATE CORP_HISTORY_LOG
                  SET PROCESS_DATE = %s, PROCESS_SUCCESS = %s, PROCESS_MSG = %s
                  WHERE RECORD_ID = %s"""

        # get max event for "other" system in case we need to re-direct an company for processing
        (other_max_event_date, other_max_event_id) = self.get_max_event_for_other_system_type(system_type_cd)
        other_in_scope_corps = self.get_in_scope_corps_for_other_system_type(system_type_cd)

        cur = None
        start_time = time.perf_counter()
        processing_time = 0
        max_processing_time = 10 * 60
        continue_loop = True
        max_batch_size = CORP_BATCH_SIZE
        use_cache_param = use_cache
        while continue_loop and processing_time < max_processing_time:
            corps = []
            specific_corps = []

            # load data from BC Registries for the corporations we need to process (max of 3000 per chunk)
            # this data may be pulled directly, or pulled from a "cache" in the event processor database
            if load_regs:
                try:
                    # we are loading data from BC Registries based on the corp event queue
                    # sql1 = find unprocessed events from our local table EVENT_BY_CORP_FILING
                    cur = self.conn.cursor()
                    sql1e = sql1.replace("!BS!", str(max_batch_size))
                    cur.execute(sql1e, (system_type_cd,system_type_cd,))
                    row = cur.fetchone()
                    while row is not None:
                        # include the date(s) for the start and end events
                        corps.append({'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'PREV_EVENT': event_dict(row[2], row[3]), 'LAST_EVENT': event_dict(row[4], row[5]), 
                                        'CORP_NUM':row[6], 'ENTRY_DATE':row[7]})
                        specific_corps.append(row[6])
                        row = cur.fetchone()
                    cur.close()
                    cur = None
                except (Exception, psycopg2.DatabaseError) as error:
                    LOGGER.error(error)
                    LOGGER.error(traceback.print_exc())
                    log_error("EventProcessor exception updating DB: " + str(error))
                    raise
                finally:
                    if cur is not None:
                        cur.close()
            else:
                try:
                    # not loading from BC Reg, just processing data already loaded in corp_history
                    # sql1a = load staged corp data from local table CORP_HISTORY_LOG
                    cur = self.conn.cursor()
                    sql1ae = sql1a.replace("!BS!", str(max_batch_size))
                    # print(">>> executing with:", system_type_cd, sql1ae)
                    cur.execute(sql1ae, (system_type_cd,system_type_cd,))
                    row = cur.fetchone()
                    while row is not None:
                        # includes the date(s) for the start and end events
                        corps.append({'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'PREV_EVENT':row[2], 'LAST_EVENT':row[3], 
                                    'CORP_NUM':row[4], 'CORP_JSON':row[5], 'ENTRY_DATE':row[6]})
                        specific_corps.append(row[4])
                        row = cur.fetchone()
                    cur.close()
                    cur = None
                except (Exception, psycopg2.DatabaseError) as error:
                    LOGGER.error(error)
                    LOGGER.error(traceback.print_exc())
                    log_error("EventProcessor exception updating DB: " + str(error))
                    raise
                finally:
                    if cur is not None:
                        cur.close()

            # at this point specific corps will be either:
            #   - a list of corps from the event table EVENT_BY_CORP_FILING
            #   - a list of corp data from the corp history table CORP_HISTORY_LOG
            if len(specific_corps) == 0:
                continue_loop = False
            else:
                saved_creds = 0
                force_continue = False
                # now generate credentials from the corporate data
                # with BCRegistries(use_cache) as bc_registries:
                with self.bc_reg_processor(system_type_cd, use_cache=use_cache) as bc_registries:
                    if use_cache:
                        try:
                            # cache BC Reg data into local in-memory sqlite database (for performance)
                            bc_registries.cache_bcreg_corps(specific_corps)
                        except (Exception, psycopg2.DatabaseError, psycopg2.DataError) as error:
                            # raises a SQL error if error during caching
                            LOGGER.error(error)
                            LOGGER.error(traceback.print_exc())
                            force_continue = True
                            if max_batch_size == CORP_BATCH_SIZE:
                                LOGGER.error("Error during caching operation, switching to smaller cache size")
                                corps = []
                                max_batch_size = FALLBACK_CORP_BATCH_SIZE
                            else:
                                LOGGER.error("Error during caching operation, switching to non-cached mode")
                                corps = []
                                use_cache = False

                    # process each corp in our list
                    for i,corp in enumerate(corps): 
                        process_success = True
                        process_msg = None
                        corp_in_scope = False
                        corp_in_scope_other = False
                        if (i % 100 == 0) or (i+1 == len(corps)):
                            processing_time = time.perf_counter() - start_time
                            print('Processing: ' + str(processing_time))
                            print('>>> Processing ' + str(i+1) + ' of ' + str(len(corps)) + ' corporations. ')

                        # check if we need to load BC Reg data (we need to do this if we are running from the event list)
                        if load_regs:
                            try:
                                # fetch corp info from bc_registries
                                corp_info = bc_registries.get_bc_reg_corp_info(corp['CORP_NUM'])

                                if corp_info['corp_typ_cd'] in corp_types:
                                    # the following is COLIN-specific processing
                                    if system_type_cd == system_type:
                                        # get event summary
                                        effective_recs = self.corp_unique_record_list(corp['CORP_NUM'], corp_info)
                                        corp_info['reg_summary'] = effective_recs

                                    corp_info_json = bc_registries.to_json(corp_info)
                                    corp_in_scope = True
                                elif corp_info['corp_typ_cd'] in other_in_scope_corps:
                                    corp_in_scope_other = True

                                prev_event_json = event_json(corp['PREV_EVENT'])
                                last_event_json = event_json(corp['LAST_EVENT'])
                            except (Exception, psycopg2.DatabaseError) as error:
                                LOGGER.error(error)
                                LOGGER.error(traceback.print_exc())
                                process_success = False
                                process_msg = str(error)
                                #raise
                        else:
                            # json blob is cached in event processor database
                            corp_info = corp['CORP_JSON']
                            corp_info_json = bc_registries.to_json(corp_info)
                            prev_event_json = corp['PREV_EVENT']
                            last_event_json = corp['LAST_EVENT']
                            if corp_info['corp_typ_cd'] in corp_types:
                                corp_in_scope = True
                            elif corp_info['corp_typ_cd'] in other_in_scope_corps:
                                corp_in_scope_other = True

                        # at this point we have all the corp data, now generate credentials
                        if corp_in_scope and process_success:
                            # get events - only generate credentials for events in the past
                            # for future-effective events (if any) we defer to the next processing cycle
                            (effective_events, future_events) = self.current_and_future_corp_events(corp['SYSTEM_TYPE_CD'], corp['CORP_NUM'], corp_info)

                            corp_active_state = self.get_corp_active_state(corp['SYSTEM_TYPE_CD'], corp_info)

                            # if corporation is "withdrawn" then don't create any events
                            withdrawn_corp = (corp_active_state is not None) and ('state_typ_cd' in corp_active_state) and (corp_active_state['state_typ_cd'] == CORP_WITHDRAWN_STATE)
                            if withdrawn_corp:
                                # setting these to empty arrays will force a status update with no creds generated
                                effective_events = []
                                future_events = []

                            # check if we are generating credentials (vs just pre-loading BC Reg data)
                            if generate_creds:
                                corp_creds = []
                                if 0 < len(effective_events):
                                    try:
                                        # generate and store credentials
                                        #LOGGER.info(" >>> Generate credentials for corp", corp['CORP_NUM'])
                                        corp_creds = self.generate_credentials(corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT'], corp['LAST_EVENT'], corp['CORP_NUM'], corp_info)
                                        if len(corp_creds) > 0:
                                            cur = self.conn.cursor()
                                            if corp_active_state and 'op_state_typ_cd' in corp_active_state:
                                                op_state_typ_cd = corp_active_state['op_state_typ_cd']
                                            else:
                                                op_state_typ_cd = 'N/A'
                                            saved_creds = saved_creds + self.store_credentials(cur, corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT'], corp['LAST_EVENT'], 
                                                                    corp['CORP_NUM'], op_state_typ_cd, corp_info, corp_creds)
                                            cur.close()
                                            cur = None
                                    except (Exception, psycopg2.DatabaseError) as error:
                                        LOGGER.error(error)
                                        LOGGER.error(traceback.print_exc())
                                        process_success = False
                                        process_msg = str(error)
                                        #raise
                                    finally:
                                        if cur is not None:
                                            cur.close()

                                # store corporate info 
                                if process_success:
                                    flag = 'Y'
                                    if withdrawn_corp:
                                        res = 'Withdrawn'
                                    else:
                                        res = None
                                else:
                                    flag = 'N'
                                    if 255 < len(process_msg):
                                        res = process_msg[:250] + '...'
                                    else:
                                        res = process_msg
                                if load_regs:
                                    cur = self.conn.cursor()
                                    if 0 < len(corp_creds) or 0 == len(future_events):
                                        if corp_active_state and 'op_state_typ_cd' in corp_active_state:
                                            op_state_typ_cd = corp_active_state['op_state_typ_cd']
                                        else:
                                            op_state_typ_cd = 'N/A'
                                        cur.execute(sql2a, (corp['SYSTEM_TYPE_CD'], prev_event_json, last_event_json, corp['CORP_NUM'], 
                                                            op_state_typ_cd, corp_info_json, datetime.datetime.now(), datetime.datetime.now(), 
                                                            flag, res,))
                                        if flag == 'N':
                                            log_warning('Event processing error:' + res)
                                    cur.close()
                                    cur = None
                                else:
                                    # update process date
                                    cur = self.conn.cursor()
                                    if 0 < len(corp_creds) or 0 == len(future_events):
                                        cur.execute(sql3a, (datetime.datetime.now(), flag, res, corp['RECORD_ID'], ))
                                        if flag == 'N':
                                            log_warning('Event processing error:' + res)
                                    cur.close()
                                    cur = None
                                if (0 < len(future_events)) and (0 < len(corp_creds) or load_regs):
                                    # create another record to handle future events (will do a re-load)
                                    future_events = sorted(future_events, key=lambda k: int(k['event_id']))
                                    future_events = sorted(future_events, key=lambda k: k['effective_date'])
                                    cur = self.conn.cursor()
                                    cur.execute(sql2b, (corp['SYSTEM_TYPE_CD'], future_events[0]['event_id'], future_events[0]['event_timestmp'], 
                                                        future_events[len(future_events)-1]['event_id'], future_events[len(future_events)-1]['effective_date'],  
                                                        corp['CORP_NUM'], datetime.datetime.now(),))
                                    cur.close()
                                    cur = None
                            elif load_regs:
                                try:
                                    # store corporate info for future generation of credentials
                                    cur = self.conn.cursor()
                                    cur.execute(sql2, (corp['SYSTEM_TYPE_CD'], prev_event_json, last_event_json, corp['CORP_NUM'], 
                                                        corp_active_state['op_state_typ_cd'], corp_info_json, datetime.datetime.now(),))
                                    cur.close()
                                    cur = None
                                except (Exception, psycopg2.DatabaseError) as error:
                                    LOGGER.error(error)
                                    LOGGER.error(traceback.print_exc())
                                    process_success = False
                                    process_msg = str(error)
                                    log_error("EventProcessor exception updating DB: " + str(error))
                                    raise
                                finally:
                                    if cur is not None:
                                        cur.close()

                        # update process date
                        cur = self.conn.cursor()
                        if process_success:
                            if corp_in_scope:
                                cur.execute(sql3, (datetime.datetime.now(), 'Y', corp_info['corp_typ_cd'], corp['RECORD_ID'], ))
                            else:
                                if not corp_in_scope_other:
                                    cur.execute(sql3, (datetime.datetime.now(), 'S', corp_info['corp_typ_cd'] + ": Skipped, not in scope", corp['RECORD_ID'], ))
                                else:
                                    # add a record to trigger this company to process from the "in scope" source DB
                                    use_system_type_cd = lear_system_type if corp['SYSTEM_TYPE_CD'] == system_type else system_type
                                    if use_system_type_cd == system_type:
                                        # for now just drop a "BC" prefx if we are processing from COLIN
                                        use_corp_num = corp['CORP_NUM'][2:] if corp['CORP_NUM'].startswith("BC") else corp['CORP_NUM']
                                    else:
                                        use_corp_num = corp['CORP_NUM']
                                    cur.execute(sql2b, (use_system_type_cd, 0, "0001-01-01",
                                                        other_max_event_id, other_max_event_date,
                                                        use_corp_num, datetime.datetime.now(),))
                                    cur.execute(sql3, (datetime.datetime.now(), 'S', corp_info['corp_typ_cd'] + ": Skipped, requeue in " + use_system_type_cd, corp['RECORD_ID'], ))
                        else:
                            if 255 < len(process_msg):
                                res = process_msg[:250] + '...'
                            else:
                                res = process_msg
                            cur.execute(sql3, (datetime.datetime.now(), 'N', res, corp['RECORD_ID'], ))
                        self.conn.commit()
                        cur.close()
                        cur = None

                processing_time = time.perf_counter() - start_time
                print('Processing: ' + str(processing_time))

                # if we are generating creds but didn't on the last loop, bail
                if generate_creds and 0 == saved_creds and not force_continue:
                    LOGGER.info("Didn't complete any activity this loop, so bail")
                    continue_loop = False

                # if we processed a set of corps in non-cached mode, try to switch back
                if len(corps) > 0 and not use_cache:
                    LOGGER.info("Restoring cache mode")
                    use_cache = use_cache_param


    # process corps that have been queued - update data from bc_registries
    def process_corp_event_queue(self, system_type_cd, use_cache=False, corp_types=CORP_TYPES_IN_SCOPE):
        """
        Reads data from BC Reg and loads into local database (CORP_HISTORY_LOG).
        """
        self.process_corp_event_queue_internal(system_type_cd, load_regs=True, generate_creds=False, use_cache=use_cache, corp_types=corp_types)

    # generate creds based on pre-processed data (no connect to bc reg)
    def process_corp_generate_creds(self, system_type_cd):
        """
        Reads staged data (CORP_HISTORY_LOG) and produces credentials (CREDENTIAL_LOG).
        """
        self.process_corp_event_queue_internal(system_type_cd, load_regs=False, generate_creds=True)

    # process corps that have been queued - update data from bc_registries - and generate credentials
    def process_corp_event_queue_and_generate_creds(self, system_type_cd, use_cache=False, corp_types=CORP_TYPES_IN_SCOPE):
        """
        The main process for loading BC Reg data and producing credentials.
        This process takes unprocessed events from the EVENT_BY_CORP_FILING table, and for each corp_num:
           - loads data from BC Reg for that corp (stores in CORP_HISTORY_LOG)
           - produces credentials (stores in CREDENTIAL_LOG)
        Credentials are submitted to TOB via the agent using a separate process.
        """
        self.process_corp_event_queue_internal(system_type_cd, load_regs=True, generate_creds=True, use_cache=use_cache, corp_types=corp_types)

    def generate_credential_type(self, system_type_cd, credential_typ_cd):
        """Generate credentials of the requested type for all queued orgs."""
        sql1 = """SELECT repo.record_id, repo.system_type_cd, repo.corp_history_id, repo.credential_type_cd,
                         repo.corp_num, hist.corp_state, hist.corp_json, hist.prev_event, hist.last_event
                  FROM corp_cred_reprocess_log repo, corp_history_log hist
                  WHERE repo.process_success is null
                    AND hist.record_id = repo.corp_history_id
                  LIMIT !BS!;"""

        sql3a = """UPDATE corp_cred_reprocess_log
                  SET PROCESS_DATE = %s, PROCESS_SUCCESS = %s, PROCESS_MSG = %s
                  WHERE RECORD_ID = %s"""

        # print(datetime.datetime.now(), "Generating credentials for", system_type_cd, credential_typ_cd, "...")
        cur = None
        i = 0
        while True:
            try:
                # we are loading data from BC Registries based on the corp event queue
                # sql1 = find unprocessed events from our local table EVENT_BY_CORP_FILING
                corps = []
                cur = self.conn.cursor()
                cur.execute(sql1.replace("!BS!", str(CORP_BATCH_SIZE)))
                row = cur.fetchone()
                while row is not None:
                    # include the date(s) for the start and end events
                    corp = {'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'CORP_HISTORY_ID':row[2], 'CREDENTIAL_TYPE_CD':row[3],
                                    'CORP_NUM':row[4], 'CORP_STATE':row[5], 'CORP_JSON':row[6], 'PREV_EVENT':row[7], 'LAST_EVENT':row[8]}
                    corps.append(corp)
                    row = cur.fetchone()
                cur.close()
                cur = None

                if len(corps) == 0:
                    return

                # print(datetime.datetime.now(), "Processing " + str(len(corps)) + " orgs for credential " + system_type_cd + " " + credential_typ_cd)
                saved_creds = 0
                for corp in corps:
                    corp_creds = []
                    process_success = True
                    try:
                        # generate and store credentials
                        corp_creds = self.generate_credentials_of_type(corp['SYSTEM_TYPE_CD'], corp['CREDENTIAL_TYPE_CD'], corp['CORP_NUM'], corp['CORP_JSON'])
                        if len(corp_creds) > 0:
                            cur = self.conn.cursor()
                            saved_creds = saved_creds + self.store_credentials(cur, corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT'], corp['LAST_EVENT'], 
                                                    corp['CORP_NUM'], corp['CORP_STATE'], corp['CORP_JSON'], corp_creds)
                            cur.close()
                            cur = None
                    except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        LOGGER.error(error)
                        LOGGER.error(traceback.print_exc())
                        process_success = False
                        process_msg = str(error)
                        #raise
                    finally:
                        if cur is not None:
                            cur.close()

                    # store corporate info 
                    if process_success:
                        flag = 'Y'
                        if 0 < len(corp_creds):
                            res = "Credential generated"
                        else:
                            res = "No credential generated"
                    else:
                        flag = 'N'
                        if 255 < len(process_msg):
                            res = process_msg[:250] + '...'
                        else:
                            res = process_msg

                    # update process date
                    cur = self.conn.cursor()
                    cur.execute(sql3a, (datetime.datetime.now(), flag, res, corp['RECORD_ID'], ))
                    if flag == 'N':
                        log_warning('Event processing error:' + res)
                    self.conn.commit()
                    cur.close()
                    cur = None

                    i = i + 1
                    if 0 == (i % 10000):
                        print(datetime.datetime.now(), i)

            except (Exception, psycopg2.DatabaseError) as error:
                LOGGER.error(error)
                LOGGER.error(traceback.print_exc())
                log_error("EventProcessor exception updating DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()

    def queue_reprocess_credential_type(self, system_type_cd, credential_typ_cd):
        """Queue up all existing orgs to process a credential of a specific type."""
        sql1 = """SELECT RECORD_ID, 
                         SYSTEM_TYPE_CD, 
                         CORP_NUM, 
                         PROCESS_SUCCESS,
                         PROCESS_DATE
                  FROM CORP_HISTORY_LOG
                  WHERE PROCESS_SUCCESS = 'Y'
                    AND SYSTEM_TYPE_CD = %s
                  order by PROCESS_DATE desc;"""

        sql1a = """SELECT RECORD_ID, SYSTEM_TYPE_CD, CORP_NUM, CORP_HISTORY_ID FROM CORP_CRED_REPROCESS_LOG 
                   WHERE SYSTEM_TYPE_CD = %s
                     AND CREDENTIAL_TYPE_CD = %s"""

        sql1b = """SELECT RECORD_ID, SYSTEM_TYPE_CD, CORP_NUM, CREDENTIAL_TYPE_CD FROM CREDENTIAL_LOG
                   WHERE SYSTEM_TYPE_CD = %s
                     AND CREDENTIAL_TYPE_CD = %s"""

        sql2 = """INSERT INTO CORP_CRED_REPROCESS_LOG (SYSTEM_TYPE_CD, CORP_HISTORY_ID, CORP_NUM, CREDENTIAL_TYPE_CD, ENTRY_DATE)
                  VALUES (%s, %s, %s, %s, %s)  RETURNING RECORD_ID;"""

        #sql2a = """SELECT RECORD_ID FROM CORP_CRED_REPROCESS_LOG 
        #           WHERE CORP_NUM = %s
        #             AND SYSTEM_TYPE_CD = %s
        #             AND CREDENTIAL_TYPE_CD = %s"""

        # build the new table, just in case
        self.create_reprocessing_tables()

        cur = None
        try:
            print(datetime.datetime.now(), "Checking for existing credentials ...")
            existing_corps = {}
            cur = self.conn.cursor()
            cur.execute(sql1b, (system_type_cd, credential_typ_cd,))
            for row in cur:
                corp = {}
                corp['record_id'] = row[0]
                corp['system_type'] = row[1]
                corp['corp_num'] = row[2]
                corp['credential_type_cd'] = row[3]
                existing_corps[corp['corp_num']] = corp
            cur.close()
            cur = None

            print(datetime.datetime.now(), "Checking for orgs requiring re-processing ...")
            corps = []
            cur = self.conn.cursor()
            cur.execute(sql1, (system_type_cd,))
            for row in cur:
                corp = {}
                corp['record_id'] = row[0]
                corp['system_type'] = row[1]
                corp['corp_num'] = row[2]
                corp['process_success'] = row[3]
                corp['process_date'] = row[4]
                if corp['corp_num'] not in existing_corps:
                    corps.append(corp)
            cur.close()
            cur = None

            print(datetime.datetime.now(), "Checking for previously re-processed orgs ...")
            repro_corps = {}
            cur = self.conn.cursor()
            cur.execute(sql1a, (system_type_cd, credential_typ_cd,))
            for row in cur:
                corp = {}
                corp['record_id'] = row[0]
                corp['system_type'] = row[1]
                corp['corp_num'] = row[2]
                corp['corp_history_id'] = row[3]
                repro_corps[corp['corp_history_id']] = corp
            cur.close()
            cur = None

            print(datetime.datetime.now(), "Queuing " + str(len(corps)) + " orgs for re-processing ...")
            i = 0
            cur = self.conn.cursor()
            for corp in corps:
                # check if we have already queued this company
                #cur.execute(sql2a, (corp['corp_num'], corp['system_type'], credential_typ_cd,))
                #row = cur.fetchone()
                #if row is None:
                if not (corp['record_id'] in repro_corps):
                    cur.execute(sql2, (corp['system_type'], corp['record_id'], corp['corp_num'], credential_typ_cd, datetime.datetime.now(),))
                    self.conn.commit()
                    repro_corps[corp['corp_num']] = corp
                    i = i + 1
                    if 0 == (i % 10000):
                        print(datetime.datetime.now(), i)
            cur = None
            print(datetime.datetime.now(), "Done, queued " + str(i) + " orgs for re-processing.")
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            raise
        finally:
            if cur is not None:
                cur.close()
            cur = None

    # insert a transform into the transform table
    def insert_credential_transform(self, system_type_cd, credential_typ_cd, mapping_transform, schema_name, schema_version):
        """ insert a new event into the event table """
        sql = """INSERT INTO CREDENTIAL_TRANSFORM (SYSTEM_TYPE_CD, CREDENTIAL_TYPE_CD, MAPPING_TRANSFORM, SCHEMA_NAME, SCHEMA_VERSION)
                 VALUES(%s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type_cd, credential_typ_cd, mapping_transform, schema_name, schema_version,))
            _record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            raise
        finally:
            if cur is not None:
                cur.close()
            cur = None

    def display_event_processing_status(self, system_type_cd=system_type):
        tables = ['event_by_corp_filing', 'corp_history_log', 'credential_log']

        for table in tables:
            process_ct     = self.get_record_count(table, False, system_type_cd=system_type_cd)
            outstanding_ct = self.get_record_count(table, True, system_type_cd=system_type_cd)
            print(system_type_cd, ': Table:', table, 'Processed:', process_ct, 'Outstanding:', outstanding_ct)

            sql = "select count(*) from " + table + " where process_success = 'N'"
            error_ct = self.get_sql_record_count(sql)
            print(system_type_cd, ':       ', table, 'Process Errors:', error_ct)
            if 0 < error_ct:
                self.print_processing_errors(table)

    def get_outstanding_corps_record_count(self, system_type_cd=system_type):
        return self.get_record_count('event_by_corp_filing', system_type_cd=system_type_cd)
        
    def get_outstanding_creds_record_count(self, system_type_cd=system_type):
        return self.get_record_count('credential_log', system_type_cd=system_type_cd)
        
    def get_record_count(self, table, unprocessed=True, system_type_cd=system_type):
        sql_ct_select = 'select count(*) from'
        where_clause = "where system_type_cd = '" + system_type_cd + "'"
        sql_corp_ct_processed   = where_clause + ' and process_date is not null'
        sql_corp_ct_outstanding = where_clause + ' and process_date is null'

        if table == 'credential_log':
            cutoff_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            cutoff_time_str = cutoff_time.strftime("%Y-%m-%dT%H:%M:%S")
            sql_corp_ct_processed = sql_corp_ct_processed + " and process_success != 'A'"
            sql_corp_ct_processed = sql_corp_ct_processed + """ and (CREDENTIAL_JSON->>'expiry_date' = ''
                or CREDENTIAL_JSON->>'expiry_date' is null
                or CREDENTIAL_JSON->>'expiry_date' <= '""" + cutoff_time_str + """')"""

        sql = sql_ct_select + ' ' + table + ' ' + (sql_corp_ct_outstanding if unprocessed else sql_corp_ct_processed)

        return self.get_sql_record_count(sql)

    def get_sql_record_count(self, sql):
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            ct = cur.fetchone()[0]
            cur.close()
            cur = None
            return ct
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            raise
        finally:
            if cur is not None:
                cur.close()
            cur = None

    def print_processing_errors(self, table):
        sql = """select * from """ + table + """
                 where process_success = 'N'
                 order by process_date DESC
                 limit 20"""
        rows = self.get_sql_rows(sql)
        print("       Recent errors:")
        print(rows)

    def get_sql_rows(self, sql):
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            rows = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            raise
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None


