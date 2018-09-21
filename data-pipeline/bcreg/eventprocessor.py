#!/usr/bin/python
 
import psycopg2
import datetime
import pytz
import json
import time
from bcreg.config import config
from bcreg.bcregistries import BCRegistries


corp_credential = 'REG'
corp_schema = 'registration.bc_registries'
corp_version = '1.0.32'

addr_credential = 'ADDR'
addr_schema = 'address.bc_registries'
addr_version = '1.0.32'

dba_credential = 'REL'
dba_schema = 'relationship.bc_registries'
dba_version = '1.0.32'

CORP_BATCH_SIZE = 3000

# for now, we are in PST time
timezone = pytz.timezone("America/Los_Angeles")
epochstart = timezone.localize(datetime.datetime(1970, 1, 1))


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            try:
                tz_aware = timezone.localize(o)
            except (Exception) as error:
                print("date conversion error", o, error)
                return o.isoformat()
            if tz_aware >= epochstart:
                return str(int((tz_aware - epochstart).total_seconds()))
            else:
                return tz_aware.astimezone(pytz.utc).isoformat()
        return json.JSONEncoder.default(self, o)


# interface to Event Processor database
class EventProcessor:
    def __init__(self):
        try:
            params = config(section='event_processor')
            self.conn = psycopg2.connect(**params)
        except (Exception) as error:
            print(error)
            self.conn = None
            raise

    def __del__(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        # todo
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # todo
        pass
 
    # create our base processing tables
    def create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS LAST_EVENT (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                EVENT_ID INTEGER NOT NULL,
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
                LAST_EVENT_ID INTEGER NOT NULL, 
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
                PREV_EVENT_ID INTEGER NOT NULL, 
                LAST_EVENT_ID INTEGER NOT NULL, 
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
                PREV_EVENT_ID INTEGER NOT NULL, 
                LAST_EVENT_ID INTEGER NOT NULL, 
                CREDENTIAL_TYPE_CD VARCHAR(255) NOT NULL,
                CREDENTIAL_ID VARCHAR(255) NOT NULL,
                SCHEMA_NAME VARCHAR(255) NOT NULL,
                SCHEMA_VERSION VARCHAR(255) NOT NULL,
                CREDENTIAL_JSON JSON NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL,
                END_DATE TIMESTAMP,
                PROCESS_DATE TIMESTAMP,
                PROCESS_SUCCESS CHAR,
                PROCESS_MSG VARCHAR(255)
            )
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
            """
            -- Hit when checking generated credentials
            CREATE INDEX IF NOT EXISTS cl_ri_stc_cn_cs_ctc_ci_desc ON CREDENTIAL_LOG 
            (RECORD_ID DESC,SYSTEM_TYPE_CD, CORP_NUM, CORP_STATE, CREDENTIAL_TYPE_CD, CREDENTIAL_ID)
            """,
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
            """
            )
        cur = None
        try:
            cur = self.conn.cursor()
            for command in commands:
                cur.execute(command)
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # record the last event processed
    def insert_last_event(self, system_type, event_id):
        """ insert a new event into the event table """
        sql = """INSERT INTO LAST_EVENT (SYSTEM_TYPE_CD, EVENT_ID, ENTRY_DATE)
                 VALUES(%s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type, event_id, datetime.datetime.now(),))
            record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # get the last event processed
    def get_last_processed_event(self, system_type):
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute("""SELECT max(event_id) FROM LAST_EVENT where SYSTEM_TYPE_CD = %s""", (system_type,))
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert a record into the "unprocessed corporations" table
    def insert_corporation(self, system_type, prev_event_id, last_event_id, corp_num):
        """ insert a new corps into the corps table """
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type, prev_event_id, last_event_id, corp_num, datetime.datetime.now(),))
            record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert a list of "unprocessed corporations" into the table
    def insert_corporation_list(self, corporation_list):
        """ insert multiple corps into the corps table  """
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, ENTRY_DATE) 
                 VALUES(%s, %s, %s, %s, %s)"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.executemany(sql, corporation_list)
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # update a group of corps into the "unprocessed corp" queue
    def update_corp_event_queue(self, system_type, corps, max_event_id):
        sql = """INSERT INTO EVENT_BY_CORP_FILING (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql2 = """INSERT INTO LAST_EVENT (SYSTEM_TYPE_CD, EVENT_ID, ENTRY_DATE)
                 VALUES(%s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            for i,corp in enumerate(corps): 
                cur = self.conn.cursor()
                cur.execute(sql, (system_type, corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'], datetime.datetime.now(),))
                record_id = cur.fetchone()[0]
                cur.close()
                cur = None
            cur = self.conn.cursor()
            cur.execute(sql2, (system_type, max_event_id, datetime.datetime.now(),))
            self.conn.commit()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert data for one corp into the history table
    def insert_corp_history(self, system_type, prev_event_id, last_event_id, corp_num, corp_state, corp_json):
        """ insert a new corps into the corps table """
        sql = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_STATE, CORP_JSON, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type, prev_event_id, last_event_id, corp_num, corp_state, corp_json, datetime.datetime.now(),))
            record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # insert a generated JSON credential into our log
    def insert_json_credential(self, cur, system_cd, prev_event_id, last_event_id, corp_num, corp_state, cred_type, cred_id, schema_name, schema_version, credential):
        sql = """INSERT INTO CREDENTIAL_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_STATE, CREDENTIAL_TYPE_CD, CREDENTIAL_ID, 
                SCHEMA_NAME, SCHEMA_VERSION, CREDENTIAL_JSON, ENTRY_DATE)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        # create row(s) for corp creds json info
        cur.execute(sql, (system_cd, prev_event_id, last_event_id, corp_num, corp_state, cred_type, cred_id, 
                    schema_name, schema_version, json.dumps(credential, cls=DateTimeEncoder), datetime.datetime.now(),))

    # determine jurisdiction for corp
    def get_corp_jurisdiction(self, corp):
        registered_jurisdiction = ""
        if corp['corp_type']['corp_class'] == 'BC':
            registered_jurisdiction = "BC"
        elif corp['corp_type']['corp_class'] == 'XPRO':
            if 'jurisdiction' in corp and 'can_jur_typ_cd' in corp['jurisdiction']:
                if corp['jurisdiction']['can_jur_typ_cd'] == 'OT':
                    if 'othr_juris_desc' in corp['jurisdiction'] and corp['jurisdiction']['othr_juris_desc'] is not None:
                        registered_jurisdiction = corp['jurisdiction']['othr_juris_desc']
                    else:
                        registered_jurisdiction = corp['jurisdiction']['can_jur_typ_cd']
                else:
                    registered_jurisdiction = corp['jurisdiction']['can_jur_typ_cd']
        else:
            # default to BC
            registered_jurisdiction = "BC"
        return registered_jurisdiction

    # corp num with prefix
    def corp_num_with_prefix(self, corp_typ_cd, corp_num):
        p_corp_num = corp_num
        if corp_typ_cd == 'BC':
            p_corp_num = 'BC' + corp_num
        elif corp_typ_cd == 'ULC':
            p_corp_num = 'BC' + corp_num
        elif corp_typ_cd == 'CC':
            p_corp_num = 'BC' + corp_num
        return p_corp_num

    # generate address credential
    def generate_address_credential(self, corp_num, corp_info, office, address, dba_corp_num, dba_name):
        addr_cred = {}
        addr_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_num)
        if 0 < len(corp_info['org_names']):
            addr_cred['addressee'] = corp_info['org_names'][0]['corp_nme']
        addr_cred['address_type'] = office['office_type']['full_desc']
        addr_cred['civic_address'] = address['local_addr']
        if 'city' in address:
            addr_cred['municipality'] = address['city']
        if 'province' in address:
            addr_cred['province'] = address['province']
        if 'postal_cd' in address:
            addr_cred['postal_code'] = address['postal_cd']
        if 'country_typ_cd' in address:
            addr_cred['country'] = address['country_typ_cd']
        if 'effective_dt' in office['start_filing_event']:
            addr_cred['address_effective_date'] = office['start_filing_event']['effective_dt']
        else:
            addr_cred['address_effective_date'] = office['start_event']['event_timestmp']
        addr_cred['effective_date'] = addr_cred['address_effective_date']

        return addr_cred

    # check if the newly generated credential is the same as the previously issued credential (if applicable)
    def same_as_existing_cred(self, system_typ_cd, corp_num, corp_state, cred_type, cred_id, credential):
        sql = """SELECT CREDENTIAL_JSON FROM CREDENTIAL_LOG 
                 WHERE SYSTEM_TYPE_CD = %s
                   AND CORP_NUM = %s
                   AND CORP_STATE = %s
                   AND CREDENTIAL_TYPE_CD = %s
                   AND CREDENTIAL_ID = %s
                 ORDER BY RECORD_ID DESC"""
        cur = None
        try:
            # check whatever is the most recent "version" of this credential
            cur = self.conn.cursor()
            cur.execute(sql, (system_typ_cd, corp_num, corp_state, cred_type, cred_id,))
            row = cur.fetchone()
            existing_cred = ''
            if row is not None:
                existing_cred = row[0]
            cur.close()
            cur = None
            return (existing_cred == credential)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()
        return False

    # store credentials for the provided corp
    def store_credentials(self, cur, system_typ_cd, prev_event_id, last_event_id, corp_num, corp_state, corp_info, corp_creds):
        for corp_cred in corp_creds:
            # check if the credential already exists, and (if so) if our new credential has changed
            if (not self.same_as_existing_cred(system_typ_cd, corp_num, corp_state, corp_cred['cred_type'], corp_cred['id'], corp_cred['credential'])):
                self.insert_json_credential(cur, system_typ_cd, prev_event_id, last_event_id, corp_num, corp_state, 
                                        corp_cred['cred_type'], corp_cred['id'], corp_cred['schema'], corp_cred['version'], corp_cred['credential'])

    def build_credential_dict(self, cred_type, schema, version, cred_id, credential):
        cred = {}
        cred['cred_type'] = cred_type
        cred['schema'] = schema
        cred['version'] = version
        cred['credential'] = credential
        cred['id'] = cred_id
        return cred

    # generate credentials for the provided corp
    def generate_credentials(self, system_typ_cd, prev_event_id, last_event_id, corp_num, corp_info):
        corp_creds = []

        # generate corp credential
        corp_cred = {}
        corp_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
        corp_cred['registration_date'] = corp_info['recognition_dts']
        if 0 < len(corp_info['org_names']):
            corp_cred['entity_name'] = corp_info['org_names'][0]['corp_nme'] 
            if 'effectiv_dt' in corp_info['org_names'][0]['start_filing_event']:
                corp_cred['entity_name_effective'] = corp_info['org_names'][0]['start_filing_event']['effective_dt']
            else:
                corp_cred['entity_name_effective'] = corp_info['org_names'][0]['start_event']['event_timestmp']
        if 0 < len(corp_info['org_name_assumed']):
            corp_cred['entity_name_assumed'] = corp_info['org_name_assumed'][0]['corp_nme'] 
            if 'effectiv_dt' in corp_info['org_name_assumed'][0]['start_filing_event']:
                corp_cred['entity_name_assumed_effective'] = corp_info['org_name_assumed'][0]['start_filing_event']['effective_dt']
            else:
                corp_cred['entity_name_assumed_effective'] = corp_info['org_name_assumed'][0]['start_event']['event_timestmp']
        if 0 < len(corp_info['org_name_trans']):
            corp_cred['entity_name_trans'] = corp_info['org_name_trans'][0]['corp_nme'] 
            if 'effectiv_dt' in corp_info['org_name_trans'][0]['start_filing_event']:
                corp_cred['entity_name_trans_effective'] = corp_info['org_name_trans'][0]['start_filing_event']['effective_dt']
            else:
                corp_cred['entity_name_trans_effective'] = corp_info['org_name_trans'][0]['start_event']['event_timestmp']
        corp_cred['entity_status'] = corp_info['corp_state']['op_state_typ_cd']
        corp_cred['entity_status_effective'] = corp_info['corp_state_dt']
        corp_cred['effective_date'] = corp_info['corp_state_dt']
        corp_cred['entity_type'] = corp_info['corp_type']['full_desc']

        # TODO seems like every corporation has a registered jurisdiction of 'BC'
        corp_cred['registered_jurisdiction'] = 'BC' # self.get_corp_jurisdiction(corp_info)

        if 'tilma_involved' in corp_info and 'tilma_jurisdiction' in corp_info['tilma_involved']:
            corp_cred['registration_type'] = corp_info['tilma_involved']['tilma_jurisdiction'] 
        else:
            corp_cred['registration_type'] = ''
        corp_cred['home_jurisdiction'] = self.get_corp_jurisdiction(corp_info)

        corp_creds.append(self.build_credential_dict(corp_credential, corp_schema, corp_version, corp_num, corp_cred))

        # generate addr credential(s)
        for office in corp_info['office']:
            if 'office_typ_cd' in office:
                if 'delivery_addr' in office and 'local_addr' in office['delivery_addr']:
                    addr_cred = self.generate_address_credential(corp_num, corp_info, office, office['delivery_addr'], "", "")
                    corp_creds.append(self.build_credential_dict(addr_credential, addr_schema, addr_version, 
                                                                corp_num + ',' + office['office_typ_cd'], addr_cred))
        
        corp_type = corp_info['corp_typ_cd']
        if corp_type == 'SP' or corp_type == 'MF':
            is_parent = False
        else:
            is_parent = True

        # generate relationship credential(s) (only for parent right now):
        if is_parent:
            if 'parties' in corp_info:
                for party in corp_info['parties']:
                    if party['corp_info']['corp_typ_cd'] == 'SP' or party['corp_info']['corp_typ_cd'] == 'MF':
                        dba_cred = {}
                        dba_cred['registration_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                        dba_cred['associated_registration_id'] = self.corp_num_with_prefix(party['corp_info']['corp_typ_cd'], party['corp_info']['corp_num'])
                        dba_cred['relationship'] = 'Owns'
                        dba_cred['relationship_description'] = 'Does Business As'
                        dba_cred['relationship_status'] = 'ACT'
                        if 'effective_dt' in party['start_filing_event']:
                            dba_cred['effective_date'] = party['start_filing_event']['effective_dt']
                        else:
                            dba_cred['effective_date'] = party['start_event']['event_timestmp']
                        dba_cred['relationship_status_effective'] = dba_cred['effective_date']
                        corp_creds.append(self.build_credential_dict(dba_credential, dba_schema, dba_version, 
                                                                    dba_cred['registration_id'], dba_cred))

        return corp_creds

    # process corps that have been queued - update data from bc_registries
    def process_corp_event_queue_internal(self, load_regs=True, generate_creds=False, use_cache=False):
        sql1 = """SELECT RECORD_ID, 
                         SYSTEM_TYPE_CD, 
                         PREV_EVENT_ID, 
                         LAST_EVENT_ID, 
                         CORP_NUM, 
                         ENTRY_DATE
                  FROM EVENT_BY_CORP_FILING
                  WHERE RECORD_ID IN
                  (
                    SELECT RECORD_ID
                    FROM EVENT_BY_CORP_FILING 
                    WHERE PROCESS_DATE is null
                  )
                  ORDER BY RECORD_ID
                  LIMIT """ + str(CORP_BATCH_SIZE)

        sql1a = """SELECT RECORD_ID, 
                          SYSTEM_TYPE_CD, 
                          PREV_EVENT_ID, 
                          LAST_EVENT_ID, 
                          CORP_NUM, 
                          CORP_JSON, 
                          ENTRY_DATE
                   FROM CORP_HISTORY_LOG
                   WHERE RECORD_ID IN
                   (
                     SELECT RECORD_ID
                     FROM CORP_HISTORY_LOG 
                     WHERE PROCESS_DATE is null
                   )
                   ORDER BY RECORD_ID
                   LIMIT """ + str(CORP_BATCH_SIZE)

        sql2 = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_STATE, CORP_JSON, ENTRY_DATE)
                  VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql2a = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_STATE, CORP_JSON, ENTRY_DATE, PROCESS_DATE, PROCESS_SUCCESS, PROCESS_MSG)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""

        sql3 = """UPDATE EVENT_BY_CORP_FILING
                  SET PROCESS_DATE = %s, PROCESS_SUCCESS = %s, PROCESS_MSG = %s
                  WHERE RECORD_ID = %s"""
        sql3a = """UPDATE CORP_HISTORY_LOG
                  SET PROCESS_DATE = %s, PROCESS_SUCCESS = %s, PROCESS_MSG = %s
                  WHERE RECORD_ID = %s"""

        cur = None
        start_time = time.perf_counter()
        processing_time = 0
        max_processing_time = 10 * 60
        continue_loop = True
        while continue_loop and processing_time < max_processing_time:
            corps = []
            specific_corps = []

            # load data from BC Registries for the corporations we need to process (max of 3000 per chunk)
            # this data may be pulled directly, or pulled from a "cache" in the event processor database
            if load_regs:
                try:
                    # we are loading data from BC Registries based on the corp event queue
                    cur = self.conn.cursor()
                    cur.execute(sql1)
                    row = cur.fetchone()
                    while row is not None:
                        corps.append({'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'PREV_EVENT_ID':row[2], 'LAST_EVENT_ID':row[3], 
                                        'CORP_NUM':row[4], 'ENTRY_DATE':row[5]})
                        specific_corps.append(row[4])
                        row = cur.fetchone()
                    cur.close()
                    cur = None
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                    raise
                finally:
                    if cur is not None:
                        cur.close()
            else:
                try:
                    # not loading from BC Reg, just processing data already loaded in corp_history
                    cur = self.conn.cursor()
                    cur.execute(sql1a)
                    row = cur.fetchone()
                    while row is not None:
                        # print(row)
                        corps.append({'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'PREV_EVENT_ID':row[2], 'LAST_EVENT_ID':row[3], 
                                    'CORP_NUM':row[4], 'CORP_JSON':row[5], 'ENTRY_DATE':row[6]})
                        specific_corps.append(row[4])
                        row = cur.fetchone()
                    cur.close()
                    cur = None
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                    raise
                finally:
                    if cur is not None:
                        cur.close()

            if len(specific_corps) == 0:
                continue_loop = False
            else:
                # now generate credentials from the corporate data
                with BCRegistries(use_cache) as bc_registries:
                    if use_cache:
                        try:
                            bc_registries.cache_bcreg_corps(specific_corps)
                        except (Exception, psycopg2.DatabaseError) as error:
                            # raises a SQL error if error during caching
                            print(error)
                            raise

                    for i,corp in enumerate(corps): 
                        process_success = True
                        process_msg = None
                        if (i % 100 == 0) or (i+1 == len(corps)):
                            print('>>> Processing {} of {} corporations.'.format(i+1, len(corps)))

                        if load_regs:
                            try:
                                # fetch corp info from bc_registries
                                corp_info = bc_registries.get_bc_reg_corp_info(corp['CORP_NUM'], corp['LAST_EVENT_ID'])
                                corp_info_json = bc_registries.to_json(corp_info)
                            except (Exception, psycopg2.DatabaseError) as error:
                                print(error)
                                process_success = False
                                process_msg = str(error)
                                #raise
                        else:
                            # json blob is cached in event processor database
                            corp_info = corp['CORP_JSON']
                            corp_info_json = corp_info

                        if process_success:
                            if generate_creds:
                                try:
                                    # generate and store credentials
                                    cur = self.conn.cursor()
                                    corp_creds = self.generate_credentials(corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'],
                                                            corp_info)
                                    self.store_credentials(cur, corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'],
                                                            corp_info['corp_state']['op_state_typ_cd'], corp_info, corp_creds)
                                    cur.close()
                                    cur = None
                                except (Exception, psycopg2.DatabaseError) as error:
                                    print(error)
                                    process_success = False
                                    process_msg = str(error)
                                    #raise
                                finally:
                                    if cur is not None:
                                        cur.close()

                                # store corporate info 
                                if process_success:
                                    flag = 'Y'
                                    res = None
                                else:
                                    flag = 'N'
                                    if 255 < len(process_msg):
                                        res = process_msg[:250] + '...'
                                    else:
                                        res = process_msg
                                if load_regs:
                                    cur = self.conn.cursor()
                                    cur.execute(sql2a, (corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'], corp_info['corp_state']['op_state_typ_cd'], 
                                                        corp_info_json, datetime.datetime.now(), datetime.datetime.now(), flag, res,))
                                    cur.close()
                                    cur = None
                                else:
                                    # update process date
                                    cur = self.conn.cursor()
                                    cur.execute(sql3a, (datetime.datetime.now(), flag, res, corp['RECORD_ID'], ))
                                    cur.close()
                                    cur = None

                            elif load_regs:
                                try:
                                    # store corporate info for future generation of credentials
                                    cur = self.conn.cursor()
                                    cur.execute(sql2, (corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'], corp_info['corp_state']['op_state_typ_cd'], 
                                                        corp_info_json, datetime.datetime.now(),))
                                    cur.close()
                                    cur = None
                                except (Exception, psycopg2.DatabaseError) as error:
                                    print(error)
                                    process_success = False
                                    process_msg = str(error)
                                    raise
                                finally:
                                    if cur is not None:
                                        cur.close()

                        # update process date
                        cur = self.conn.cursor()
                        if process_success:
                            cur.execute(sql3, (datetime.datetime.now(), 'Y', None, corp['RECORD_ID'], ))
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


    # process corps that have been queued - update data from bc_registries
    def process_corp_event_queue(self, use_cache=False):
        self.process_corp_event_queue_internal(True, False, use_cache)

    # generate creds based on pre-processed data (no connect to bc reg)
    def process_corp_generate_creds(self):
        self.process_corp_event_queue_internal(False, True)

    # process corps that have been queued - update data from bc_registries - and generate credentials
    def process_corp_event_queue_and_generate_creds(self, use_cache=False):
        self.process_corp_event_queue_internal(True, True, use_cache)

    # insert a transform into the transform table
    def insert_credential_transform(self, system_type, credential_typ_cd, mapping_transform, schema_name, schema_version):
        """ insert a new event into the event table """
        sql = """INSERT INTO CREDENTIAL_TRANSFORM (SYSTEM_TYPE_CD, CREDENTIAL_TYPE_CD, MAPPING_TRANSFORM, SCHEMA_NAME, SCHEMA_VERSION)
                 VALUES(%s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type, credential_typ_cd, mapping_transform, schema_name, schema_version,))
            record_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()
            cur = None

    def display_event_processing_status(self):
        tables = ['event_by_corp_filing', 'corp_history_log', 'credential_log']

        for table in tables:
            process_ct     = self.get_record_count(table, False)
            outstanding_ct = self.get_record_count(table, True)
            print('Table:', table, 'Processed:', process_ct, 'Outstanding:', outstanding_ct)

            sql = "select count(*) from " + table + " where process_success = 'N'"
            error_ct = self.get_sql_record_count(sql)
            print('      ', table, 'Process Errors:', error_ct)
            if 0 < error_ct:
                self.print_processing_errors(table)

    def get_outstanding_corps_record_count(self):
        return self.get_record_count('event_by_corp_filing')
        
    def get_outstanding_creds_record_count(self):
        return self.get_record_count('credential_log')
        
    def get_record_count(self, table, unprocessed=True):
        tables = ['event_by_corp_filing', 'corp_history_log', 'credential_log']
        sql_ct_select = 'select count(*) from'
        sql_corp_ct_processed   = 'where process_date is not null'
        sql_corp_ct_outstanding = 'where process_date is null'

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
            print(error)
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
            print(error)
            raise
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None


