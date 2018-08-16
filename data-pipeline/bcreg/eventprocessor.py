#!/usr/bin/python
 
import psycopg2
import datetime
import json
from bcreg.config import config
from bcreg.bcregistries import BCRegistries


corp_credential = 'CORP'
corp_schema = 'incorporation.bc_registries'
corp_version = '1.0.31'

addr_credential = 'ADDR'
addr_schema = 'address.bc_registries'
addr_version = '1.0.31'

dba_credential = 'DBA'
dba_schema = 'doing_business_as.bc_registries'
dba_version = '1.0.31'

CORP_BATCH_SIZE = 3000


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
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
            CREATE INDEX IF NOT EXISTS le_i1 ON LAST_EVENT 
            (SYSTEM_TYPE_CD)
            """,
            """
            CREATE INDEX IF NOT EXISTS le_i2 ON LAST_EVENT 
            (EVENT_ID)
            """,
            """
            CREATE TABLE IF NOT EXISTS EVENT_BY_CORP_FILING (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                PREV_EVENT_ID INTEGER NOT NULL, 
                LAST_EVENT_ID INTEGER NOT NULL, 
                ENTRY_DATE TIMESTAMP NOT NULL,
                PROCESS_DATE TIMESTAMP
            )
            """,
            """
            CREATE INDEX IF NOT EXISTS ebc_i1 ON EVENT_BY_CORP_FILING 
            (SYSTEM_TYPE_CD)
            """,
            """
            CREATE INDEX IF NOT EXISTS ebc_i2 ON EVENT_BY_CORP_FILING 
            (PROCESS_DATE)
            """,
            """
            CREATE TABLE IF NOT EXISTS CORP_HISTORY_LOG (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                PREV_EVENT_ID INTEGER NOT NULL, 
                LAST_EVENT_ID INTEGER NOT NULL, 
                CORP_JSON JSON NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL,
                PROCESS_DATE TIMESTAMP
            )
            """,
            """
            CREATE INDEX IF NOT EXISTS chl_i1 ON CORP_HISTORY_LOG 
            (SYSTEM_TYPE_CD)
            """,
            """
            CREATE INDEX IF NOT EXISTS chl_i2 ON CORP_HISTORY_LOG 
            (PROCESS_DATE)
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
            CREATE INDEX IF NOT EXISTS ct_i1 ON CREDENTIAL_TRANSFORM 
            (SYSTEM_TYPE_CD)
            """,
            """
            CREATE INDEX IF NOT EXISTS cy_i2 ON CREDENTIAL_TRANSFORM 
            (CREDENTIAL_TYPE_CD)
            """,
            """
            CREATE TABLE IF NOT EXISTS CREDENTIAL_LOG (
                RECORD_ID SERIAL PRIMARY KEY,
                SYSTEM_TYPE_CD VARCHAR(255) NOT NULL, 
                CORP_NUM VARCHAR(255) NOT NULL,
                PREV_EVENT_ID INTEGER NOT NULL, 
                LAST_EVENT_ID INTEGER NOT NULL, 
                CREDENTIAL_TYPE_CD VARCHAR(255) NOT NULL,
                SCHEMA_NAME VARCHAR(255) NOT NULL,
                SCHEMA_VERSION VARCHAR(255) NOT NULL,
                CREDENTIAL_JSON JSON NOT NULL,
                ENTRY_DATE TIMESTAMP NOT NULL,
                PROCESS_DATE TIMESTAMP,
                PROCESS_SUCCESS CHAR,
                PROCESS_MSG VARCHAR(255)
            )
            """,
            """
            CREATE INDEX IF NOT EXISTS cl_i1 ON CREDENTIAL_LOG 
            (SYSTEM_TYPE_CD)
            """,
            """
            CREATE INDEX IF NOT EXISTS cl_i2 ON CREDENTIAL_LOG 
            (PROCESS_DATE)
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
    def insert_corp_history(self, system_type, prev_event_id, last_event_id, corp_num, corp_json):
        """ insert a new corps into the corps table """
        sql = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_JSON, ENTRY_DATE)
                 VALUES(%s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (system_type, prev_event_id, last_event_id, corp_num, corp_json, datetime.datetime.now(),))
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
    def insert_json_credential(self, cur, system_cd, prev_event_id, last_event_id, corp_num, cred_type, schema_name, schema_version, credential):
        sql = """INSERT INTO CREDENTIAL_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CREDENTIAL_TYPE_CD, 
                SCHEMA_NAME, SCHEMA_VERSION, CREDENTIAL_JSON, ENTRY_DATE)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        # create row(s) for corp creds json info
        cur.execute(sql, (system_cd, prev_event_id, last_event_id, corp_num, cred_type, 
                    schema_name, schema_version, json.dumps(credential, cls=DateTimeEncoder), datetime.datetime.now(),))

    # determine jurisdiction for corp
    def get_corp_jurisdiction(self, corp):
        registered_jurisdiction = ""
        if corp['corp_type']['corp_class'] == 'BC':
            registered_jurisdiction = "BC"
        elif corp['corp_type']['corp_class'] == 'XPRO':
            if 'jurisdiction' in corp and 'can_jur_typ_cd' in corp['jurisdiction']:
                if corp['jurisdiction']['can_jur_typ_cd'] == 'OT':
                    if 'othr_juris_desc' in corp['jurisdiction']:
                        registered_jurisdiction = corp['jurisdiction']['othr_juris_desc']
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
        addr_cred['legal_entity_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_num)
        addr_cred['org_registry_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_num)
        if 0 < len(corp_info['org_names']):
            addr_cred['addressee'] = corp_info['org_names'][0]['corp_nme']
        addr_cred['registered_jurisdiction'] = self.get_corp_jurisdiction(corp_info)
        addr_cred['addr_type'] = office['office_typ_cd']
        addr_cred['local_address'] = address['local_addr']
        if 'city' in address:
            addr_cred['municipality'] = address['city']
        if 'province' in address:
            addr_cred['province'] = address['province']
        if 'postal_cd' in address:
            addr_cred['postal_code'] = address['postal_cd']
        if 'country_typ_cd' in address:
            addr_cred['country'] = address['country_typ_cd']
        if 'effective_dt' in office['start_filing_event']:
            addr_cred['effective_date'] = office['start_filing_event']['effective_dt']
        else:
            addr_cred['effective_date'] = office['start_event']['event_timestmp']
        addr_cred['dba_corp_num'] = dba_corp_num
        addr_cred['dba_name'] = dba_name
        addr_cred['end_date'] = ""

        return addr_cred

    # store credentials for the provided corp
    def store_credentials(self, cur, system_typ_cd, prev_event_id, last_event_id, corp_num, corp_info, corp_creds):
        for corp_cred in corp_creds:
            self.insert_json_credential(cur, system_typ_cd, prev_event_id, last_event_id, corp_num, 
                                    corp_cred['cred_type'], corp_cred['schema'], corp_cred['version'], corp_cred['credential'])

    def build_credential_dict(self, cred_type, schema, version, credential):
        cred = {}
        cred['cred_type'] = cred_type
        cred['schema'] = schema
        cred['version'] = version
        cred['credential'] = credential
        return cred

    # generate credentials for the provided corp
    def generate_credentials(self, system_typ_cd, prev_event_id, last_event_id, corp_num, corp_info):
        corp_creds = []

        # generate corp credential
        corp_cred = {}
        corp_cred['legal_entity_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
        corp_cred['corp_num']        = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
        corp_cred['effective_date'] = corp_info['recognition_dts']
        if 0 < len(corp_info['org_names']):
            corp_cred['legal_name'] = corp_info['org_names'][0]['corp_nme'] 
            if 'effectiv_dt' in corp_info['org_names'][0]['start_filing_event']:
                corp_cred['org_name_effective'] = corp_info['org_names'][0]['start_filing_event']['effective_dt']
            else:
                corp_cred['org_name_effective'] = corp_info['org_names'][0]['start_event']['event_timestmp']
        if 0 < len(corp_info['org_name_assumed']):
            corp_cred['org_name_assumed'] = corp_info['org_name_assumed'][0]['corp_nme'] 
            if 'effectiv_dt' in corp_info['org_name_assumed'][0]['start_filing_event']:
                corp_cred['org_name_assumed_effective'] = corp_info['org_name_assumed'][0]['start_filing_event']['effective_dt']
            else:
                corp_cred['org_name_assumed_effective'] = corp_info['org_name_assumed'][0]['start_event']['event_timestmp']
        if 0 < len(corp_info['org_name_trans']):
            corp_cred['org_name_trans'] = corp_info['org_name_trans'][0]['corp_nme'] 
            if 'effectiv_dt' in corp_info['org_name_trans'][0]['start_filing_event']:
                corp_cred['org_name_trans_effective'] = corp_info['org_name_trans'][0]['start_filing_event']['effective_dt']
            else:
                corp_cred['org_name_trans_effective'] = corp_info['org_name_trans'][0]['start_event']['event_timestmp']
        corp_cred['org_reg_status'] = corp_info['corp_state']['op_state_typ_cd']
        corp_cred['org_status_effective'] = corp_info['corp_state_dt']
        corp_cred['org_type'] = corp_info['corp_typ_cd']
        corp_cred['registered_jurisdiction'] = self.get_corp_jurisdiction(corp_info)
        if 'tilma_involved' in corp_info and 'tilma_jurisdiction' in corp_info['tilma_involved']:
            corp_cred['registration_type'] = corp_info['tilma_involved']['tilma_jurisdiction'] 
        corp_cred['home_jurisdiction'] = self.get_corp_jurisdiction(corp_info)
        corp_cred['end_date'] = ""

        corp_creds.append(self.build_credential_dict(corp_credential, corp_schema, corp_version, corp_cred))

        # generate addr credential(s)
        for office in corp_info['office']:
            if 'office_typ_cd' in office:
                if 'delivery_addr' in office and 'local_addr' in office['delivery_addr']:
                    addr_cred = self.generate_address_credential(corp_num, corp_info, office, office['delivery_addr'], "", "")
                    corp_creds.append(self.build_credential_dict(addr_credential, addr_schema, addr_version, addr_cred))

        # generate dba credential(s)
        if 'parties' in corp_info:
            for party in corp_info['parties']:
                for dba_name in party['corp_info']['org_names']:
                    dba_cred = {}
                    dba_cred['legal_entity_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                    dba_cred['org_registry_id'] = self.corp_num_with_prefix(corp_info['corp_typ_cd'], corp_info['corp_num'])
                    if 0 < len(corp_info['org_names']):
                        dba_cred['org_name'] = corp_info['org_names'][0]['corp_nme'] 
                    dba_cred['registered_jurisdiction'] = self.get_corp_jurisdiction(party['corp_info'])
                    dba_cred['dba_name'] = dba_name['corp_nme']
                    dba_cred['dba_corp_num'] = self.corp_num_with_prefix(party['corp_info']['corp_typ_cd'], party['corp_info']['corp_num'])
                    if 'effective_dt' in dba_name['start_filing_event']:
                        dba_cred['effective_date'] = dba_name['start_filing_event']['effective_dt']
                    else:
                        dba_cred['effective_date'] = dba_name['start_event']['event_timestmp']
                    dba_cred['end_date'] = ""
                    corp_creds.append(self.build_credential_dict(dba_credential, dba_schema, dba_version, dba_cred))

                # generate addr credential(s)
                for office in party['corp_info']['office']:
                    if 'office_typ_cd' in office and 'local_addr' in office:
                        # generate address for each party
                        if 0 < len(party['corp_info']['org_names']):
                            party_dba_name = party['corp_info']['org_names'][0]['corp_nme']
                        else:
                            party_dba_name = party['business_nme']
                        if 'delivery_addr' in office and 'local_addr' in office['delivery_addr']:
                            addr_cred = self.generate_address_credential(corp_num, corp_info, office, office['delivery_addr'], 
                                            self.corp_num_with_prefix(party['corp_info']['corp_typ_cd'], party['corp_info']['corp_num']), 
                                            party_dba_name)
                            corp_creds.append(self.build_credential_dict(addr_credential, addr_schema, addr_version, addr_cred))

        return corp_creds

    # process corps that have been queued - update data from bc_registries
    def process_corp_event_queue_internal(self, load_regs=True, generate_creds=False, use_cache=False):
        sql1 = """SELECT RECORD_ID, SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, ENTRY_DATE
                 FROM EVENT_BY_CORP_FILING
                 WHERE PROCESS_DATE is null
                 LIMIT """ + str(CORP_BATCH_SIZE)
        sql1a = """SELECT RECORD_ID, SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_JSON, ENTRY_DATE
                 FROM CORP_HISTORY_LOG
                 WHERE PROCESS_DATE is null
                 LIMIT """ + str(CORP_BATCH_SIZE)

        sql2 = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_JSON, ENTRY_DATE)
                  VALUES(%s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""
        sql2a = """INSERT INTO CORP_HISTORY_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_JSON, ENTRY_DATE, PROCESS_DATE)
                  VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""

        sql3 = """UPDATE EVENT_BY_CORP_FILING
                  SET PROCESS_DATE = %s
                  WHERE RECORD_ID = %s"""
        sql3a = """UPDATE CORP_HISTORY_LOG
                  SET PROCESS_DATE = %s
                  WHERE RECORD_ID = %s"""

        cur = None
        try:
            continue_loop = True
            while continue_loop:
                corps = []
                specific_corps = []
                if load_regs:
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
                else:
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

                if len(specific_corps) == 0:
                    continue_loop = False
                else:
                    with BCRegistries(use_cache) as bc_registries:
                        if use_cache:
                            bc_registries.cache_bcreg_corps(specific_corps)
                        for i,corp in enumerate(corps): 
                            print('>>> Processing {} of {} corporations.'.format(i+1, len(corps)))
                            if load_regs:
                                # fetch corp info from bc_registries
                                corp_info = bc_registries.get_bc_reg_corp_info(corp['CORP_NUM'], corp['LAST_EVENT_ID'])
                            else:
                                corp_info = corp['CORP_JSON']

                            if generate_creds:
                                # generate and store credentials
                                cur = self.conn.cursor()
                                corp_creds = self.generate_credentials(corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'],
                                                        corp_info)
                                self.store_credentials(cur, corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'],
                                                        corp_info, corp_creds)
                                cur.close()
                                cur = None

                                # store corporate info 
                                if load_regs:
                                    cur = self.conn.cursor()
                                    cur.execute(sql2a, (corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'], 
                                                        bc_registries.to_json(corp_info), datetime.datetime.now(), datetime.datetime.now(),))
                                    cur.close()
                                    cur = None
                                else:
                                    # update process date
                                    cur = self.conn.cursor()
                                    cur.execute(sql3a, (datetime.datetime.now(), corp['RECORD_ID'], ))
                                    cur.close()
                                    cur = None

                            elif load_regs:
                                # store corporate info for future generation of credentials
                                cur = self.conn.cursor()
                                cur.execute(sql2, (corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'], 
                                                    bc_registries.to_json(corp_info), datetime.datetime.now(),))
                                cur.close()
                                cur = None

                            # update process date
                            cur = self.conn.cursor()
                            cur.execute(sql3, (datetime.datetime.now(), corp['RECORD_ID'], ))
                            self.conn.commit()
                            cur.close()
                            cur = None

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()
                print('Cursor closed.')

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
        sql_ct_select = 'select count(*) from'
        sql_corp_ct_processed   = 'where process_date is not null'
        sql_corp_ct_outstanding = 'where process_date is null'

        cur = None
        try:
            cur = self.conn.cursor()
            for table in tables:
                sql = sql_ct_select + ' ' + table + ' ' + sql_corp_ct_processed
                cur.execute(sql)
                process_ct = cur.fetchone()[0]
                sql = sql_ct_select + ' ' + table + ' ' + sql_corp_ct_outstanding
                cur.execute(sql)
                outstanding_ct = cur.fetchone()[0]
                print('Table:', table, 'Processed:', process_ct, 'Outstanding:', outstanding_ct)
            cur.close()
            cur = None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()
            cur = None


