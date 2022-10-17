#!/usr/bin/python
import psycopg2
import sqlite3
import datetime
import pytz
import json
import string
import decimal
import random
import types
import traceback
import logging

from bcreg.bcreg_core import BCReg_Core, MAX_WHERE_IN
from bcreg.config import config
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


lear_system_type = 'BCREG_LEAR'

BC_REGISTRIES_DATABASE_NAME = 'bc_reg_lear'
BC_REGISTRIES_TIMEZONE = 'PST8PDT'

# for now, we are in PST time
timezone = pytz.timezone("PST8PDT")

LOGGER = logging.getLogger(__name__)

STATE_CODES = {
    "ACTIVE": "ACT",
    "HISTORICAL": "HIS",
}

FILING_TYPE_CODES = {
    "filing_type": "filing_type",
    "alteration": "alteration",
    "amalgamation": "amalgamation",
    "amalgamationApplication": "amalgamationApplication",
    "amendedAGM": "amendedAGM",
    "amendedAnnualReport": "amendedAnnualReport",
    "amendedChangeOfDirectors": "amendedChangeOfDirectors",
    "annualReport": "annualReport",
    "changeOfAddress": "changeOfAddress",
    "changeOfDirectors": "changeOfDirectors",
    "changeOfName": "changeOfName",
    "changeOfRegistration": "changeOfRegistration",
    "conversion": "conversion",
    "correction": "correction",
    "courtOrder": "courtOrder",
    "dissolution": "dissolution",
    "dissolved": "dissolved",
    "F.18": "F.18",
    "incorporationApplication": "incorporationApplication",
    "Involuntary Dissolution": "Involuntary Dissolution",
    "lear_epoch": "lear_epoch",
    "putBackOn": "putBackOn",
    "registrarsNotation": "registrarsNotation",
    "registrarsOrder": "registrarsOrder",
    "registration": "registration",
    "restorationApplication": "restorationApplication",
    "specialResolution": "specialResolution",
    "transition": "transition",
    "voluntaryDissolution": "voluntaryDissolution",
    "voluntaryLiquidation": "voluntaryLiquidation",
}

def event_dict(event_id, event_date):
    event = {'event_id': event_id, 'event_date': event_date}
    return event


# custom encoder to convert wierd data types to strings
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            try:
                # tz_aware = timezone.localize(o)
                # ret = tz_aware.astimezone(pytz.utc).isoformat()
                ret = o.astimezone(pytz.utc).isoformat()
                return ret
            except (Exception) as error:
                LOGGER.error(error)
                LOGGER.error(traceback.print_exc())
                raise error
        elif isinstance(o, (list, dict, str, int, float, bool, type(None))):
            return JSONEncoder.default(self, o)        
        elif isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        elif isinstance(o, set):
            return list(o)
        elif isinstance(o, map):
            return list(o)
        elif isinstance(o, types.GeneratorType):
            ret = ""
            for s in next(o):
                ret = ret + str(s)
            return ret
        return json.JSONEncoder.default(self, o)


# interface to BC Registries database
# data is returned as dictionaries, using the sql column name as identifier
class BCReg_Lear(BCReg_Core):

    def __init__(self, cache=False):
        self.sql_local_cache = cache
        self.PG_DATABASE_NAME = BC_REGISTRIES_DATABASE_NAME
        super().__init__(cache)


    ###########################################################################
    # load all bc registries data for the specified corps into our in-mem cache
    ###########################################################################

    # load everything:
    code_tables =  ['corp_types']
    # load by identifier (was corp_num)
    corp_tables =  ['businesses',
                    'businesses_version']
    # load by business_id (id on businesses_version table)
    other_tables = ['filings',
                    'aliases',
                    'aliases_version',
                    'party_roles',
                    'party_roles_version']
    # custom load
    other_other_tables = ['parties',
                          'parties_version',]
    other_other_other_tables = ['transaction',]

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corps(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            self.cache_bcreg_corp_tables(specific_corps, generate_individual_sql)
            self.cache_bcreg_code_tables(generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corp_tables(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            # ensure we have a unique list
            specific_corps = list({s_corp for s_corp in specific_corps})
            specific_corps_lists = self.split_list(specific_corps, MAX_WHERE_IN)

            LOGGER.info('Caching data for parties and events ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            LOGGER.info('Caching data for corporations ...')
            for corp_nums_list in specific_corps_lists:
                bus_ids_list = []
                txn_ids_list = []
                corp_nums_list = self.id_where_in(corp_nums_list, True)
                corp_num_where = 'identifier in (' + corp_nums_list + ')'
                for corp_table in self.corp_tables:
                    _rows = self.get_bcreg_table(corp_table, corp_num_where, '', True, generate_individual_sql)
                    if corp_table == 'businesses':
                        for _row in _rows:
                            bus_ids_list.append(_row['id'])
                    elif corp_table == 'businesses_version':
                        for _row in _rows:
                            if _row['transaction_id'] is not None:
                                txn_ids_list.append(_row['transaction_id'])

                party_ids_list = []
                bus_id_where = 'business_id in (' + self.id_where_in(bus_ids_list, True) + ')'
                for other_table in self.other_tables:
                    _rows = self.get_bcreg_table(other_table, bus_id_where, '', True, generate_individual_sql)
                    if other_table == 'party_roles':
                        for _row in _rows:
                            if _row['party_id'] is not None:
                                party_ids_list.append(_row['party_id'])
                    elif other_table == 'filings':
                        for _row in _rows:
                            if _row['transaction_id'] is not None:
                                txn_ids_list.append(_row['transaction_id'])

                party_id_where = 'id in (' + self.id_where_in(party_ids_list, True) + ')'
                for other_table in self.other_other_tables:
                    _rows = self.get_bcreg_table(other_table, party_id_where, '', True, generate_individual_sql)

                txn_id_where = 'id in (' + self.id_where_in(txn_ids_list, True) + ')'
                for other_table in self.other_other_other_tables:
                    _rows = self.get_bcreg_table(other_table, txn_id_where, '', True, generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_code_tables(self, generate_individual_sql=False):
        if self.use_local_cache():
            LOGGER.info('Caching data for code tables ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            for code_table in self.code_tables:
                _rows = self.get_bcreg_table(code_table, '', '', True, generate_individual_sql)

    # clear in-mem cache - delete all existing data
    def cache_cleanup(self):
        for table in self.corp_tables:
            self.cache_cleanup_data(table)
        for table in self.other_tables:
            self.cache_cleanup_data(table)
        for table in self.code_tables:
            self.cache_cleanup_data(table)


    ###########################################################################
    # methods to determine un-processed corporations/events
    ###########################################################################

    # get max event number from bc registries event log
    def get_max_event(self, event_date):
        cur = None
        try:
            # create a cursor
            cur = self.conn.cursor()
            cur.execute("""SELECT max(id) FROM """ + self.DB_TABLE_PREFIX + """transaction where issued_at = %s""", (event_date,))
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # get max event number from bc registries event log
    def get_max_event_date(self):
        cur = None
        try:
            # create a cursor
            cur = self.conn.cursor()
            cur.execute("""SELECT max(issued_at) FROM """ + self.DB_TABLE_PREFIX + """transaction""")
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # get the last event date on or before now
    def get_max_date_before_now(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SET TIME ZONE """ + BC_REGISTRIES_TIMEZONE)
                cur.execute("""SELECT max(issued_at) FROM """ + self.DB_TABLE_PREFIX + """transaction where issued_at <= NOW()::timestamp without time zone""")
                row = cur.fetchone()
                return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # get max event number from bc registries event log
    def get_event_id_date(self, event_id):
        cur = None
        try:
            # create a cursor
            cur = self.conn.cursor()
            cur.execute("""SELECT issued_at FROM """ + self.DB_TABLE_PREFIX + """transaction where id = %s""", (event_id,))
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # return a specific set of corporations, based on an event range
    def get_specific_corps(self, corp_filter):
        # TODO add logic to include related companies (DBA's or "owned by")
        # for now just return the same corps
        corps = []
        for corp in corp_filter:
            corps.append({'CORP_NUM':corp,})
        return corps

    # return unprocessed corporations, based on active or historical
    # use for initial data load
    def get_unprocessed_corps_data_load(self, last_event_id, last_event_dt, max_event_id, max_event_dt):
        sqls = []
        
        # select *all* corps - we will filter in the next stage
        sqls.append("""SELECT distinct(identifier) from """ + self.DB_TABLE_PREFIX + """businesses""")

        corps = []
        for sql in sqls:
            cur = None
            try:
                LOGGER.info("Executing: " + sql)
                cur = self.conn.cursor()
                cur.execute(sql)
                row = cur.fetchone()
                while row is not None:
                    # LOGGER.info(row)
                    corps.append({
                        'CORP_NUM':row[0],
                        'PREV_EVENT': event_dict(last_event_id, last_event_dt),
                        'LAST_EVENT': event_dict(max_event_id, max_event_dt),
                    })
                    row = cur.fetchone()
                cur.close()
                cur = None
                LOGGER.info("Loaded corps: " + str(len(corps)))
            except (Exception, psycopg2.DatabaseError) as error:
                LOGGER.error(error)
                LOGGER.error(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()
        return corps

    # return unprocessed corporations, based on an event range
    def get_unprocessed_corps(self, last_event_id, last_event_dt):
        sqlt = """SELECT id, issued_at from transaction
                  WHERE issued_at >= %s"""
        sqlb = """SELECT identifier from businesses_version
                  WHERE transaction_id = %s"""

        corps = []
        event_ids = []
        corp_set = {}
        cur = None
        try:
            LOGGER.info("Executing: " + sqlt + " with " + str(last_event_dt))
            cur = self.conn.cursor()
            cur.execute(sqlt, (last_event_dt,))
            row = cur.fetchone()
            while row is not None:
                event_ids.append(row[0])
                row = cur.fetchone()
            cur.close()
            cur = None
            for event_id in event_ids:
                LOGGER.info("Executing: " + sqlb + " with " + str(event_id))
                cur = self.conn.cursor()
                cur.execute(sqlb, (event_id,))
                row = cur.fetchone()
                while row is not None:
                    if not row[0] in corp_set:
                        corp_set[row[0]] = row[0]
                        corps.append({'CORP_NUM':row[0],})
                    row = cur.fetchone()
                cur.close()
                cur = None
            LOGGER.info("Loaded corps: " + str(len(corps)))
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

        # since the event may affect more than one corp, check corp_state to see if there are any other corps to bring into scope
        """
        # TODO need to see how this applies in the new LEAR database
        sql = " " "SELECT corp_num from " " " + self.DB_TABLE_PREFIX + " " "corp_state
                where start_event_id = %s or end_event_id = %s" " "
        i = 0
        for event_id in event_ids:
            i = i + 1
            if (i % 1000 == 0):
                LOGGER.info("Processing %s of %s", i, len(event_ids))
            cur = None
            try:
                cur = self.conn.cursor()
                cur.execute(sql, (event_id, event_id,))
                row = cur.fetchone()
                while row is not None:
                    if not row[0] in corp_set:
                        corp_set[row[0]] = row[0]
                        corps.append({'CORP_NUM':row[0],})
                    row = cur.fetchone()
                cur.close()
                cur = None
            except (Exception, psycopg2.DatabaseError) as error:
                LOGGER.error(error)
                LOGGER.error(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()
        LOGGER.info("Loaded corps: " + str(len(corps)))
        """

        # since a related corp may be impacted by a corp change, check for related corps via corp_party table
        """
        # TODO need to see how this applies in the new LEAR database
        sql1 = " " "select corp_num from " " " + self.DB_TABLE_PREFIX + " " "corp_party
                    where bus_company_num = %s
                    and party_typ_cd = 'FBO'
                    union
                    select bus_company_num from bc_registries.corp_party
                    where corp_num = %s
                    and party_typ_cd = 'FBO'" " "
        new_corps = []
        for corp in corps:
            cur = None
            try:
                #LOGGER.info("Executing: " + sql1 + " with" + str(corp['CORP_NUM']))
                cur = self.conn.cursor()
                cur.execute(sql1, (corp['CORP_NUM'],corp['CORP_NUM'],))
                row = cur.fetchone()
                while row is not None and row[0] is not None:
                    if not row[0] in corp_set:
                        corp_set[row[0]] = row[0]
                        new_corps.append({'CORP_NUM':row[0],})
                    row = cur.fetchone()
                cur.close()
                cur = None
            except (Exception, psycopg2.DatabaseError) as error:
                LOGGER.error(error)
                LOGGER.error(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()
        LOGGER.info("Loaded corps: " + str(len(new_corps)))
        corps.extend(new_corps)
        """

        return corps

    #return the (unprocessed) event range for each provided corporation
    def get_unprocessed_corp_events(self, last_event_id, last_event_dt, max_event_id, max_event_dt, corps, max=None):
        for i,corp in enumerate(corps): 
            if (i % 100 == 0) or (i+1 == len(corps)):
                print('>>> Processing ' + str(i+1) + ' of ' + str(len(corps)) + ' corporations. ')
            corp['PREV_EVENT'] = event_dict(last_event_id, last_event_dt)
            corp['LAST_EVENT'] = event_dict(max_event_id, max_event_dt)
            if max and i >= max:
                break
        return corps


    ###########################################################################
    # methods to run corporation-specific queries 
    # (can run against the in-memory cache 
    #  or against bc registries database directly)
    ###########################################################################

    # return the "effective date" given an event and filing
    def get_event_filing_effective_date(self, event, corp_type_cd=None):
        ret_date = None

        """
        # TODO for now just return the filing completion_date
        # if corp type is Firm and it is a dissolusion event the effective date will be in event.trigger_dts
        if corp_type_cd and corp_type_cd in ('SP','GP','LP','XP','LL','XL','MF'):
            if 'trigger_dts' in event and event['trigger_dts'] is not None:
                ret_date = event['trigger_dts']

        if ret_date is None:
            # use the filing effective date if it is present
            if 'filing' in event and 'effective_dt' in event['filing']:
                ret_date = event['filing']['effective_dt']

        # else use the conversion event if present
        if ret_date is None and 'conv_event' in event and 'effective_dt' in event['conv_event']:
            if event['conv_event']['effective_dt'] is not None:
                ret_date = event['conv_event']['effective_dt']
        
        # finally use the event timestamp if we have no other option
        if ret_date is None:
            if event['event_timestmp'] is None or event['event_timestmp'] == '':
                ret_date = None
            else:
                ret_date = event['event_timestmp']

        if ret_date is None:
            LOGGER.error('Error ret_date is None: ' + str(event))
        """
        ret_date = event['issued_at']
        if 'filing' in event:
            if 'completion_date' in event['filing'] and event['filing']['completion_date']:
                ret_date = event['filing']['completion_date']
            elif 'effective_date' in event['filing'] and event['filing']['effective_date']:
                ret_date = event['filing']['effective_date']
        elif 'transaction' in event:
            if 'issued_at' in event['transaction']:
                ret_date = event['transaction']['issued_at']

        if ret_date is None:
            LOGGER.error('Error ret_date is None: ' + str(event))

        return ret_date

    # return the "effective date" given an event id
    def get_event_effective_date(self, event_id):
        # note that corp_num is ignored in the following queries
        if event_id == 0:
            return datetime.datetime(datetime.MINYEAR, 1, 1) # MIN_START_DATE
        event = self.get_event('0', event_id)
        event_date = self.get_event_filing_effective_date(event)
        return event_date

    # find a specific event, 
    # return None if not found
    def get_event(self, corp_num, event_id, corp_type_cd=None, force_query_remote=False):
        sql = """SELECT id, issued_at
                    FROM """ + self.get_table_prefix(force_query_remote) + """transaction 
                    WHERE id = """ + self.get_db_sql_param(force_query_remote)
        ret_event = None
        cursor = None
        try:
            cursor = self.get_db_connection(force_query_remote).cursor()
            cursor.execute(sql, (event_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(event) > 0:
                ret_event = event[0]
            else:
                # check for a cache miss
                if self.use_local_cache() and (not force_query_remote):
                    event = self.get_event(corp_num, event_id, corp_type_cd=corp_type_cd, force_query_remote=True)
                    self.add_cache_miss('event', corp_num, event_id, event)
                    ret_event = event
            if ret_event is None:
                return {}

            # fill in filing
            if 'filing' not in ret_event:
                ret_event['filing'] = self.get_filing_event(corp_num, event_id, None, force_query_remote=force_query_remote)
            ret_event['effective_date'] = self.get_event_filing_effective_date(ret_event, corp_type_cd)
            return ret_event
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_filing_event(self, corp_num, event_id, event_type, force_query_remote=False):
        sql_filing = """SELECT filing.id, filing_type, filing_date, filing_json, filing.transaction_id, effective_date, completion_date, 
                        status, business_id, corp.identifier as corp_num 
                        from """ + self.get_table_prefix(force_query_remote) + """filings filing, """ + self.get_table_prefix(force_query_remote) + """businesses corp
                        WHERE filing.transaction_id = """ + self.get_db_sql_param(force_query_remote) + """ and corp.id = filing.business_id"""
        cursor = None
        try:
            cursor = self.get_db_connection(force_query_remote).cursor()
            cursor.execute(sql_filing, (event_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            filing_event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(filing_event) > 0:
                return filing_event[0]
            # check for a cache miss
            if self.use_local_cache() and (not force_query_remote):
                filing_event = self.get_filing_event(corp_num, event_id, event_type, True)
                self.add_cache_miss('filing', corp_num, event_id, filing_event)
                return filing_event
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_corp_filings(self, filing_id: int = None, business_id: str = None):
        sql = """SELECT id, filing_type, filing_date, filing_json, transaction_id,
                        business_id, status, completion_date, effective_date
                FROM """ + self.get_table_prefix() + """filings"""
        if filing_id:
            sql2 = sql + " WHERE id = " + str(filing_id)
        elif business_id:
            sql2 = sql + " WHERE business_id = " + str(business_id)
        else:
            sql2 = sql

        cur = None
        try:
            filings = []
            cur = self.get_db_connection().cursor()
            cur.execute(sql2)
            row = cur.fetchone()
            while row is not None:
                filing = {
                    "id": row[0],
                    "filing_type": FILING_TYPE_CODES[row[1]] if row[1] in FILING_TYPE_CODES else row[1],
                    "filing_date": row[2],
                    "filing_json": row[3],
                    "transaction_id": row[4],
                    "business_id": row[5],
                    "status": row[6],
                    "completion_date": row[7],
                    "effective_date": row[8],
                }
                filings.append(filing)
                row = cur.fetchone()

            return filings
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading corp info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()

    def get_basic_corp_info(self, corp_num, deep_copy=True, versions=False):
        bus_table = 'businesses'
        bus_ver_columns = ''
        if versions:
            bus_table = 'businesses_version'
            bus_ver_columns = ', state_filing_id as state_filing_id, transaction_id as transaction_id'
        sql_corp = """SELECT identifier as corp_num,
                             legal_type as corp_typ_cd,
                             founding_date as recognition_dts,
                             '' as last_ar_filed_dt,
                             tax_id as bn_9,
                             tax_id as bn_15,
                             '' as admin_email,
                             '' as last_ledger_dt,
                             last_modified as last_event_dt,
                             legal_name as corp_nme,
                             '' as corp_nme_as,
                             'BC' as can_jur_typ_cd,
                             '' as xpro_typ_cd,
                             '' as othr_juris_desc,
                             state as state_typ_cd,
                             state as op_state_typ_cd,
                             '' as corp_class""" + bus_ver_columns + """
                 FROM """ + self.get_table_prefix() + bus_table + """
                 WHERE identifier = """ + self.get_db_sql_param()

        cur = None
        try:
            corps = []
            corp = None

            cur = self.get_db_connection().cursor()
            cur.execute(sql_corp, (corp_num,))
            row = cur.fetchone()
            while row is not None:
                corp = {}
                corp['current_date'] = timezone.localize(datetime.datetime.now())
                corp['corp_num'] = row[0]
                if deep_copy:
                    # TODO
                    # corp['jurisdiction'] = self.get_jurisdictions(row[0])
                    pass
                corp['corp_typ_cd'] = row[1]
                # corp['corp_type'] = self.get_corp_type(row[1])
                corp['recognition_dts'] = row[2]
                corp['last_ar_filed_dt'] = row[3]
                bn_9 = ''
                if row[4] and 9 <= len(row[4]):
                    bn_9 = row[4][:9]
                corp['bn_9'] = bn_9
                corp['bn_15'] = row[5]
                corp['admin_email'] = row[6]
                corp['last_ledger_dt'] = row[7]
                corp['last_event_dt'] = row[8]
                corp['corp_nme'] = row[9]
                corp['corp_nme_as'] = row[10]
                corp['can_jur_typ_cd'] = row[11]
                corp['xpro_typ_cd'] = row[12]
                corp['othr_juris_desc'] = row[13]
                corp['state_typ_cd'] = STATE_CODES[row[14]] if row[14] in STATE_CODES else row[14]
                corp['op_state_typ_cd'] = STATE_CODES[row[15]] if row[15] in STATE_CODES else row[15]
                corp['corp_class'] = row[16]
                if versions:
                    state_filing_id = row[17]
                    corp['state_filing_id'] = state_filing_id
                    if state_filing_id and 0 < state_filing_id:
                        filings = self.get_corp_filings(filing_id=corp['state_filing_id'])
                        corp['filing'] = filings[0] if 0 < len(filings) else {}
                    else:
                        corp['filing'] = {}
                    transaction_id = row[18]
                    if transaction_id and 0 < transaction_id:
                        transaction = self.get_event(corp['corp_num'], transaction_id)
                        corp['transaction'] = transaction
                    else:
                        corp['transaction'] = {}

                if versions:
                    corps.append(corp)
                    row = cur.fetchone()
                else:
                    row = None

                if deep_copy:
                    """
                    # get corp names
                    # TODO
                    corp['org_names'] = self.get_names(corp_num, ['CO','NB'], corp['recognition_dts'])
                    self.flag_start_events_which_are_not_also_end_events(corp_num, corp['org_names'])
                    for corp_name in corp['org_names']:
                        if is_data_conversion_event(corp_name['start_event']) and not corp_name['start_event']['appears_as_end_event'] and corp['recognition_dts'] is not None:
                            corp_name['start_event']['effective_date'] = corp['recognition_dts']
                            corp_name['effective_start_date'] = corp['recognition_dts']
                    corp['org_name_assumed'] = self.get_names(corp_num, ['AS'], corp['recognition_dts'])
                    self.flag_start_events_which_are_not_also_end_events(corp_num, corp['org_name_assumed'])
                    for corp_name in corp['org_name_assumed']:
                        if is_data_conversion_event(corp_name['start_event']) and not corp_name['start_event']['appears_as_end_event'] and corp['recognition_dts'] is not None:
                            corp_name['start_event']['effective_date'] = corp['recognition_dts']
                            corp_name['effective_start_date'] = corp['recognition_dts']
                    #corp['org_name_trans'] = self.get_names(corp_num, ['TR', 'NO'], corp['recognition_dts'])
                    corp['office'] = self.get_offices(corp_num)

                    # get corp state (active, historical), and get the start/end date of each state change
                    corp_states = self.get_corp_states(corp_num)
                    for corp_state in corp_states:
                        corp_state['start_event'] = self.get_event(corp['corp_num'], corp_state['start_event_id'], corp_type_cd=corp['corp_typ_cd'])
                        corp_state['event_date'] = corp_state['start_event']['effective_date']
                        if corp_state['end_event_id'] is not None:
                            corp_state['end_event'] = self.get_event(corp['corp_num'], corp_state['end_event_id'], corp_type_cd=corp['corp_typ_cd'])
                            corp_state['effective_end_date'] = corp_state['end_event']['effective_date']
                        else:
                            corp_state['effective_end_date'] = MAX_END_DATE

                        #if corp_state['event_date'] > corp_state['effective_end_date']:
                        #    LOGGER.info(">>>Data Issue:Date:" + corp_num + ":Corp_State:", corp_state)
                    self.flag_start_events_which_are_not_also_end_events(corp_num, corp_states)

                    #self.check_same_start_date(corp_num, 'corp_state', corp_states, 'event_date')

                    # sort to get in date order, and determine ACT/HIS transition dates
                    corp_states = sorted(corp_states, key=lambda k: k['effective_end_date'])
                    corp_states = sorted(corp_states, key=lambda k: int(k['start_event_id']))
                    corp['corp_state'] = sorted(corp_states, key=lambda k: k['event_date'])
                    prev_state = None
                    for corp_state in corp['corp_state']:
                        # check if state has changed
                        use_registration_dt = False
                        if prev_state is None and corp_state['op_state_typ_cd'] == 'ACT':
                            use_registration_dt = True
                        elif prev_state is None and is_data_conversion_event(corp_state['start_event']) and not corp_state['start_event']['appears_as_end_event']:
                            use_registration_dt = True
                        if prev_state is None or prev_state['op_state_typ_cd'] != corp_state['op_state_typ_cd']:
                            # state has changed
                            prev_state = corp_state
                            prev_state['corp_state_effective_event'] = prev_state['start_event']
                            if use_registration_dt and corp['recognition_dts'] is not None:
                                prev_state['start_event']['effective_date'] = corp['recognition_dts']
                                prev_state['effective_start_date'] = corp['recognition_dts']
                            else:
                                prev_state['effective_start_date'] = prev_state['event_date']
                        corp_state['corp_state_effective_event'] = prev_state['corp_state_effective_event']
                        corp_state['effective_start_date'] = prev_state['effective_start_date']
                    """
                    pass

            cur.close()
            cur = None

            if (not versions) and corp is None:
                # TODO maybe check BC Reg database if the corp is not in the cache?
                LOGGER.info("No corp rec found for " + str(corp_num))
                corp = {}
                corp['corp_num'] = ''
                corp['corp_typ_cd'] = ''
                corp['recognition_dts'] = ''
                corp['filing'] = {}
                corp['transaction'] = {}

            if versions:
                return corps
            else:
                return corp

        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading corp info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()


    ###########################################################################
    # primary method to load all bc registries data for the specified corporation
    ###########################################################################

    def get_bc_reg_corp_info(self, corp_num):
        """
        sql_party = " " "SELECT corp_num, corp_party_id, mailing_addr_id, delivery_addr_id, party_typ_cd, start_event_id, end_event_id, cessation_dt,
                         last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt,
                         phone, reason_typ_cd
                      FROM " " " + self.get_table_prefix() + " " "corp_party
                      WHERE (corp_num = " " " + self.get_db_sql_param() + " " " OR bus_company_num = " " " + self.get_db_sql_param() + " " ")
                        " " "
                        #AND party_typ_cd = 'FBO'" " "
        """

        cur = None
        try:
            corp = self.get_basic_corp_info(corp_num, versions=False)
            corp_type = corp['corp_typ_cd']
            corp['versions'] = self.get_basic_corp_info(corp_num, versions=True)

            """
            # get parties
            # TODO
            corp['parties'] = []
            cur = self.get_db_connection().cursor()
            cur.execute(sql_party, (corp_num, corp_num,))
            row = cur.fetchone()
            while row is not None:
                corp_party = {}
                corp_party['corp_num'] = row[0]
                corp_party['corp_party_id'] = row[1]
                corp_party['mailing_addr_id'] = row[2]
                #corp_party['mailing_addr'] = self.get_address(corp_num, row[2])
                corp_party['delivery_addr_id'] = row[3]
                #corp_party['delivery_addr'] = self.get_address(corp_num, row[3])
                corp_party['party_typ_cd'] = row[4]
                corp_party['start_event_id'] = row[5]
                corp_party['start_event'] = self.get_event(row[0], row[5], corp_type_cd=corp['corp_typ_cd'])
                corp_party['effective_start_date'] = corp_party['start_event']['effective_date']
                corp_party['end_event_id'] = row[6]
                if corp_party['end_event_id'] is not None:
                    corp_party['end_event'] = self.get_event(corp['corp_num'], corp_party['end_event_id'], corp_type_cd=corp['corp_typ_cd'])
                    corp_party['effective_end_date'] = corp_party['end_event']['effective_date']
                else:
                    corp_party['effective_end_date'] = MAX_END_DATE
                corp_party['cessation_dt'] = row[7]
                corp_party['last_nme'] = row[8]
                corp_party['middle_nme'] = row[9]
                corp_party['first_nme'] = row[10]
                corp_party['business_nme'] = row[11]
                corp_party['bus_company_num'] = row[12]
                corp_party['email_address'] = row[13]
                corp_party['corp_party_seq_num'] = row[14]
                corp_party['office_notification_dt'] = row[15]
                corp_party['phone'] = row[16]
                corp_party['reason_typ_cd'] = row[17]

                # note we are only issuing a relationship credential (with the two corp_nums) 
                # ... so just get basic info for the "other" corp in the relationship
                if corp_num == corp_party['corp_num']:
                    if corp['corp_typ_cd'] == 'FBO' and corp_party['bus_company_num'] is not None:
                        corp_party['corp_info'] = self.get_basic_corp_info(corp_party['bus_company_num'], False)
                else:
                    corp_party['corp_info'] = self.get_basic_corp_info(corp_party['corp_num'], False)

                corp['parties'].append(corp_party)
                row = cur.fetchone()
            cur.close()
            cur = None
            """

            return corp
        except (Exception, psycopg2.DatabaseError) as error:
            # TODO right now we are not reading party info
            #LOGGER.error(error)
            #LOGGER.error(traceback.print_exc())
            #log_error("BCRegistries exception reading corp party info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()

    # convert object to JSON, converting data types (decimal, date) to string
    def to_json(self, data):
        ret = json.dumps(data, cls=CustomJsonEncoder)
        return ret

