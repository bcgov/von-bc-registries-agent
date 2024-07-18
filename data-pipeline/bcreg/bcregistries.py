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
from bcreg.bcreg_lear import STATE_CODES, FILING_TYPE_CODES
from bcreg.config import config
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


system_type = 'BC_REG'

BC_REGISTRIES_TABLE_PREFIX = 'bc_registries.'
BC_REGISTRIES_DATABASE_NAME = 'bc_registries'
BC_REG_LEAR_DATABASE_NAME = 'bc_reg_lear'
BC_REGISTRIES_TIMEZONE = 'PST8PDT'
INMEM_CACHE_TABLE_PREFIX   = ''

MIN_START_DATE = datetime.datetime(datetime.MINYEAR+1, 1, 1)
MAX_END_DATE   = datetime.datetime(datetime.MAXYEAR-1, 12, 31)
DATA_CONVERSION_DATE = datetime.datetime(2004, 3, 26)
DATA_CONVERSION_DATE_STR = "2004-03-26"

# for now, we are in PST time
timezone = pytz.timezone("PST8PDT")

MIN_START_DATE_TZ = timezone.localize(MIN_START_DATE)
MAX_END_DATE_TZ   = timezone.localize(MAX_END_DATE)
DATA_CONVERSION_DATE_TZ = timezone.localize(DATA_CONVERSION_DATE)

CORP_TYPES_IN_SCOPE = {
    "A":   "EXTRA PRO",
    "B":   "EXTRA PRO",
    "BC":  "BC COMPANY",
    "BEN": "BENEFIT COMPANY",
    "C":   "CONTINUE IN",
    "CC":  "BC CCC",
    "CP":  "COOP",
    "CS":  "CONT IN SOCIETY",
    "CUL": "ULC CONTINUE IN",
    "EPR": "EXTRA PRO REG",
    "FOR": "FOREIGN",
    "FI":  "FINANCIAL",
    #"GP":  "PARTNERSHIP",
    "LIB": "LIBRARY",
    "LIC": "LICENSED",
    "LL":  "LL PARTNERSHIP",
    "LLC": "LIMITED CO",
    "LP":  "LIM PARTNERSHIP",
    "MF":  "MISC FIRM",
    "PA":  "PRIVATE ACT",
    "PAR": "PARISHES",
    "QA":  "CO 1860",
    "QB":  "CO 1862",
    "QC":  "CO 1878",
    "QD":  "CO 1890",
    "QE":  "CO 1897",
    "REG": "REGISTRATION",
    "S":   "SOCIETY",
    #"SP":  "SOLE PROP",
    "ULC": "BC ULC COMPANY",
    "XCP": "XPRO COOP",
    "XL":  "XPRO LL PARTNR",
    "XP":  "XPRO LIM PARTNR",
    "XS":  "XPRO SOCIETY",
}

LOGGER = logging.getLogger(__name__)


def event_dict(event_id, event_date):
    event = {'event_id': event_id, 'event_date': event_date}
    return event


# custom encoder to convert wierd data types to strings
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            try:
                tz_aware = timezone.localize(o)
                ret = tz_aware.astimezone(pytz.utc).isoformat()
                return ret
            except (Exception) as error:
                if o.year <= datetime.MINYEAR+1:
                    return MIN_START_DATE_TZ.astimezone(pytz.utc).isoformat()
                elif o.year >= datetime.MAXYEAR-1:
                    return MAX_END_DATE_TZ.astimezone(pytz.utc).isoformat()
                return o.isoformat()
        if isinstance(o, (list, dict, str, int, float, bool, type(None))):
            return JSONEncoder.default(self, o)        
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        if isinstance(o, set):
            return list(o)
        if isinstance(o, map):
            return list(o)
        if isinstance(o, types.GeneratorType):
            ret = ""
            for s in next(o):
                ret = ret + str(s)
            return ret
        return json.JSONEncoder.default(self, o)


def is_data_conversion_event(event):
    if isinstance(event['event_timestmp'], datetime.datetime):
        if event['event_timestmp'].year == DATA_CONVERSION_DATE.year and event['event_timestmp'].month == DATA_CONVERSION_DATE.month and event['event_timestmp'].day == DATA_CONVERSION_DATE.day:
            return True
    else:
        # assume string
        if event['event_timestmp'].startswith(DATA_CONVERSION_DATE_STR):
            return True
    return False


# interface to BC Registries database
# data is returned as dictionaries, using the sql column name as identifier
class BCRegistries(BCReg_Core):

    def __init__(self, cache=False):
        self.sql_local_cache = cache
        self.DB_TABLE_PREFIX = BC_REGISTRIES_TABLE_PREFIX
        self.PG_DATABASE_NAME = BC_REGISTRIES_DATABASE_NAME
        self.source_system_type = system_type
        self.SEC_DB_TABLE_PREFIX = ""
        self.SEC_PG_DATABASE_NAME = BC_REG_LEAR_DATABASE_NAME
        super().__init__(cache)


    ###########################################################################
    # load all bc registries data for the specified corps into our in-mem cache
    ###########################################################################

    colin_code_tables =  ['corp_type', 
                    'corp_op_state', 
                    'party_type', 
                    'office_type', 
                    'event_type', 
                    'filing_type', 
                    'corp_name_type', 
                    'jurisdiction_type',
                    'xpro_type']
    colin_corp_tables =  ['corporation', 
                    'corp_state', 
                    'jurisdiction', 
                    'corp_name']
    colin_other_tables = ['corp_party', 
                    'event', 
                    'filing',
                    'conv_event',
                    'office',
                    'address']

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corps(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            lear_specific_corps = specific_corps.copy()
            self.cache_bcreg_corp_tables(specific_corps, generate_individual_sql=generate_individual_sql)
            self.cache_bcreg_code_tables(generate_individual_sql=generate_individual_sql)

            # also cache LEAR data
            self.cache_lear_bcreg_corp_tables(lear_specific_corps, generate_individual_sql=generate_individual_sql, use_sec=True)
            self.cache_lear_bcreg_code_tables(generate_individual_sql=generate_individual_sql, use_sec=True)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corp_tables(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            LOGGER.info('Caching data for parties and events ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            # ensure we have a unique list
            specific_corps = list({s_corp for s_corp in specific_corps})
            specific_corps_lists = self.split_list(specific_corps, MAX_WHERE_IN)

            addr_id_list = []
            for corp_nums_list in specific_corps_lists:
                corp_list = self.id_where_in(corp_nums_list, True)
                corp_party_where = 'bus_company_num in (' + corp_list + ') or corp_num in (' + corp_list + ')'
                party_rows = self.get_bcreg_table(self.colin_other_tables[0], corp_party_where, '', True, generate_individual_sql)

                # include all corp_num from the parties just returned (dba related companies)
                for party in party_rows:
                    specific_corps.append(party['corp_num'])
                    if 'bus_company_num' in party and party['bus_company_num'] is not None and 0 < len(party['bus_company_num']):
                        specific_corps.append(party['bus_company_num'])

            # ensure we have a unique list
            specific_corps = list({s_corp for s_corp in specific_corps})
            specific_corps_lists = self.split_list(specific_corps, MAX_WHERE_IN)

            event_ids = []
            for corp_nums_list in specific_corps_lists:
                corp_nums_list = self.id_where_in(corp_nums_list, True)
                event_where = 'corp_num in (' + corp_nums_list + ')'
                event_rows = self.get_bcreg_table(self.colin_other_tables[1], event_where, '', True, generate_individual_sql)

                for event in event_rows:
                    event_ids.append(str(event['event_id']))

            # ensure we have a unique list
            event_ids = list({event_id for event_id in event_ids})
            event_ids_lists = self.split_list(event_ids, MAX_WHERE_IN)

            for ids_list in event_ids_lists:
                event_list = self.id_where_in(ids_list)
                filing_where = 'event_id in (' + event_list + ')'
                _rows = self.get_bcreg_table(self.colin_other_tables[2], filing_where, '', True, generate_individual_sql)
                _rows = self.get_bcreg_table(self.colin_other_tables[3], filing_where, '', True, generate_individual_sql)

            LOGGER.info('Caching data for corporations ...')
            for corp_nums_list in specific_corps_lists:
                corp_nums_list = self.id_where_in(corp_nums_list, True)
                corp_num_where = 'corp_num in (' + corp_nums_list + ')'
                for corp_table in self.colin_corp_tables:
                    _rows = self.get_bcreg_table(corp_table, corp_num_where, '', True, generate_individual_sql)

                office_where = 'corp_num in (' + corp_nums_list + ')'
                office_rows = self.get_bcreg_table(self.colin_other_tables[4], office_where, '', True, generate_individual_sql)

                for office in office_rows:
                    if office['mailing_addr_id'] is not None:
                        addr_id_list.append(str(office['mailing_addr_id']))
                    if office['delivery_addr_id'] is not None:
                        addr_id_list.append(str(office['delivery_addr_id']))

            # ensure we have a unique list
            addr_id_list = list({addr_id for addr_id in addr_id_list})
            addr_ids_lists = self.split_list(addr_id_list, MAX_WHERE_IN)
            for ids_list in addr_ids_lists:
                addr_list = self.id_where_in(ids_list)
                address_where = 'addr_id in (' + addr_list + ')'
                _rows = self.get_bcreg_table(self.colin_other_tables[5], address_where, '', True, generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_code_tables(self, generate_individual_sql=False):
        if self.use_local_cache():
            LOGGER.info('Caching data for code tables ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            for code_table in self.colin_code_tables:
                _rows = self.get_bcreg_table(code_table, '', '', True, generate_individual_sql)

    # clear in-mem cache - delete all existing data
    def cache_cleanup(self):
        for table in self.colin_corp_tables:
            self.cache_cleanup_data(table)
        for table in self.colin_other_tables:
            self.cache_cleanup_data(table)
        for table in self.colin_code_tables:
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
            cur.execute("""SELECT max(event_id) FROM """ + self.DB_TABLE_PREFIX + """event where event_timestmp = %s""", (event_date,))
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
            cur.execute("""SELECT max(event_timestmp) FROM """ + self.DB_TABLE_PREFIX + """event""")
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
                cur.execute("""SELECT max(event_timestmp) FROM """ + self.DB_TABLE_PREFIX + """event where event_timestmp <= NOW()::timestamp without time zone""")
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
            cur.execute("""SELECT event_timestmp FROM """ + self.DB_TABLE_PREFIX + """event where event_id = %s""", (event_id,))
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
        sql = """SELECT distinct(corp_num) from """ + self.DB_TABLE_PREFIX + """event
                where corp_num in ({})
                order by corp_num;"""
        sql2 = """SELECT distinct(corp.corp_num) from """ + self.DB_TABLE_PREFIX + """corporation corp,
                            """ + self.DB_TABLE_PREFIX + """corp_party party
                         where corp.corp_typ_cd in ('SP','MF')
                          and corp.corp_num = party.corp_num
                          and party.party_typ_cd in ('FBO')
                          and party.bus_company_num is not null
                          and party.bus_company_num in ({})"""
        cur = None
        try:
            cur = self.conn.cursor()
            placeholders= ', '.join(['%s']*len(corp_filter))  # "%s, %s, %s, ... %s"
            sql = sql.format(placeholders)
            cur.execute(sql, tuple(corp_filter))
            row = cur.fetchone()
            corps = []
            while row is not None:
                # LOGGER.info(row)
                corps.append({'CORP_NUM':row[0],})
                row = cur.fetchone()

            sql2 = sql2.format(placeholders)
            cur.execute(sql2, tuple(corp_filter))
            row = cur.fetchone()
            while row is not None:
                # LOGGER.info(row)
                corps.append({'CORP_NUM':row[0],})
                row = cur.fetchone()

            cur.close()
            cur = None
            return corps
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # return unprocessed corporations, based on active or historical
    # use for initial data load
    def get_unprocessed_corps_data_load(self, last_event_id, last_event_dt, max_event_id, max_event_dt):
        sqls = []
        
        # select *all* corps - we will filter in the next stage
        sqls.append("""SELECT distinct(corp.corp_num) from """ + self.DB_TABLE_PREFIX + """corporation corp """)

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
                    corps.append({'CORP_NUM':row[0], 'PREV_EVENT': event_dict(last_event_id, last_event_dt), 
                                                     'LAST_EVENT': event_dict(max_event_id, max_event_dt), })
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
        sqls = []

        # select *all* corps - we will filter in the next stage
        sqls.append("""SELECT corp_num, event_id from """ + self.DB_TABLE_PREFIX + """event
                        where event_timestmp >= %s""")

        corps = []
        event_ids = []
        corp_set = {}
        for sql in sqls:
            cur = None
            try:
                LOGGER.info("Executing: " + sql + " with " + str(last_event_dt))
                cur = self.conn.cursor()
                cur.execute(sql, (last_event_dt,))
                row = cur.fetchone()
                while row is not None:
                    if not row[0] in corp_set:
                        corp_set[row[0]] = row[0]
                        corps.append({'CORP_NUM':row[0],})
                    event_ids.append(row[1])
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
        sql = """SELECT corp_num from """ + self.DB_TABLE_PREFIX + """corp_state
                where start_event_id = %s or end_event_id = %s"""
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

        # since a related corp may be impacted by a corp change, check for related corps via corp_party table
        sql1 = """select corp_num from """ + self.DB_TABLE_PREFIX + """corp_party
                    where bus_company_num = %s
                    and party_typ_cd = 'FBO'
                    union
                    select bus_company_num from bc_registries.corp_party
                    where corp_num = %s
                    and party_typ_cd = 'FBO'"""
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
            LOGGER.error('Error ret_date is None' + str(event))

        return ret_date

    # return the "effective date" given an event id
    def get_event_effective_date(self, event_id):
        # note that corp_num is ignored in the following queries
        if event_id == 0:
            return datetime.datetime(datetime.MINYEAR, 1, 1) # MIN_START_DATE
        event = self.get_event('0', event_id)
        #filing = self.get_filing_event('0', event_id, event['event_typ_cd'])
        return self.get_event_filing_effective_date(event)

    # find a specific event, 
    # return None if not found
    def get_event(self, corp_num, event_id, corp_type_cd=None, force_query_remote=False):
        sql = """SELECT event_id, corp_num, event.event_typ_cd, event_timestmp, trigger_dts, event_class, short_desc, full_desc
                    FROM """ + self.get_table_prefix(force_query_remote) + """event event, """ + self.get_table_prefix(force_query_remote) + """event_type event_type
                    WHERE event_id = """ + self.get_db_sql_param(force_query_remote) + """ and event.event_typ_cd = event_type.event_typ_cd"""
                    # WHERE corp_num = """ + self.get_db_sql_param(force_query_remote) + """ and event_id = """ + self.get_db_sql_param(force_query_remote)
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

            # don't use data conversion date as a timestamp
            #if is_data_conversion_event(ret_event):
            #    ret_event['event_timestmp'] = ''

            # fill in filing and conv_event
            if 'filing' not in ret_event:
                ret_event['filing'] = self.get_filing_event(corp_num, event_id, ret_event['event_typ_cd'], force_query_remote)
            if 'conv_event' not in ret_event:
                ret_event['conv_event'] = self.get_conv_event(corp_num, event_id, ret_event['event_typ_cd'], force_query_remote)
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

    def get_conv_event(self, corp_num, event_id, event_type, force_query_remote=False):
        if not event_type.startswith('CONV'):
            return {}
        sql_conv = """SELECT * from """ + self.get_table_prefix(force_query_remote) + """conv_event 
                        WHERE event_id = """ + self.get_db_sql_param(force_query_remote)
        cursor = None
        try:
            cursor = self.get_db_connection(force_query_remote).cursor()
            cursor.execute(sql_conv, (event_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            conv_event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(conv_event) > 0:
                return conv_event[0]
            # don't check for a cache miss - assume conv_event are all there (most CONV data in dev is missing)
            #if self.use_local_cache() and (not force_query_remote):
            #   LOGGER.error('Cache miss for conv_event ', event_type)
            #    conv_event = self.get_conv_event(corp_num, event_id, event_type, True)
            #    self.add_cache_miss('conv_event', corp_num, event_id, conv_event)
            #    return conv_event
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_filing_event(self, corp_num, event_id, event_type, force_query_remote=False):
        if event_type != 'FILE':
            return {}
        sql_filing = """SELECT event_id, filing.filing_typ_cd, effective_dt, new_corp_num, filing_typ_class, short_desc, full_desc 
                        from """ + self.get_table_prefix(force_query_remote) + """filing filing, """ + self.get_table_prefix(force_query_remote) + """filing_type filing_type 
                        WHERE event_id = """ + self.get_db_sql_param(force_query_remote) + """ and filing.filing_typ_cd = filing_type.filing_typ_cd """
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

    def check_same_start_date(self, corp_num, record_type, records, date_key):
        sorted_records = sorted(records, key=lambda k: k[date_key])
        prev_date = None
        flag = False
        i = 0
        active_id = None
        for record in sorted_records:
            if prev_date is not None and record[date_key] == prev_date:
                flag = True
            prev_date = record[date_key]
            i = i + 1
            if 'end_event_id' not in record or record['end_event_id'] is None:
                active_id = i
        if flag:
            LOGGER.info(">>>Data Issue:Same Start Date:" + corp_num + ":" + record_type + ":" + str(records))
        if active_id is not None and active_id != len(sorted_records):
            LOGGER.info(">>>Data Issue:Active Record:" + corp_num + ":" + record_type + ":" + str(records))

    def flag_start_events_which_are_not_also_end_events(self, corp_num, corp_recs):
        if corp_recs is not None:
            end_events = []
            for rec in corp_recs:
                if 'end_event_id' in rec and rec['end_event_id'] is not None:
                    end_events.append(rec['end_event_id'])
            for rec in corp_recs:
                flag = False
                for i in end_events:
                    if rec['start_event_id'] == i:
                        flag = True
                rec['start_event']['appears_as_end_event'] = flag

    def get_offices(self, corp_num):
        sql_office = """SELECT * from """ + self.get_table_prefix() + """office
                        WHERE corp_num = """ + self.get_db_sql_param() + """ and office_typ_cd in ('RG','HD','FO')"""
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql_office, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            offices = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None

            for office in offices:
                office['office_type'] = self.get_office_type(office['office_typ_cd'])
                office['delivery_addr'] = self.get_address(corp_num, office['delivery_addr_id'])
                if 'mailing_addr_id' in office and office['mailing_addr_id'] != office['delivery_addr_id']:
                    office['mailing_addr'] = self.get_address(corp_num, office['mailing_addr_id'])
                office['start_event'] = self.get_event(corp_num, office['start_event_id'])
                office['effective_start_date'] = office['start_event']['effective_date']
                if office['end_event_id'] is not None:
                    office['end_event'] = self.get_event(corp_num, office['end_event_id'])
                    office['effective_end_date'] = office['end_event']['effective_date']
                else:
                    office['effective_end_date'] = MAX_END_DATE

                #if office['effective_start_date'] > office['effective_end_date']:
                #    LOGGER.info(">>>Data Issue:Date:" + corp_num + ":Office:", office)

            #self.check_same_start_date(corp_num, 'office', offices, 'effective_start_date')
            return offices
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_address(self, corp_num, address_id, force_query_remote=False):
        if address_id is None:
            return {}

        sql_addr = """SELECT addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type,
                         address_desc, address_desc_short, unit_no, unit_type, province_state_name
                  FROM """ + self.get_table_prefix(force_query_remote) + """address
                  WHERE addr_id = """ + self.get_db_sql_param(force_query_remote)
        cursor = None
        try:
            cursor = self.get_db_connection(force_query_remote).cursor()
            cursor.execute(sql_addr, (address_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            addresses = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(addresses) >  0:
                address = addresses[0]
                if 'addr_line_1' in address and address['addr_line_1'] is not None:
                    address['local_addr'] = self.addr_line(address['addr_line_1'], ', ') + \
                                                self.addr_line(address['addr_line_2'], ', ') + \
                                                self.addr_line(address['addr_line_3'], ', ') + \
                                                self.addr_line(address['city'], ', ') + \
                                                self.addr_line(address['province'], ', ') + \
                                                self.addr_line(address['postal_cd'], ', ') + \
                                                self.addr_line(address['country_typ_cd'], '')
                elif 'address_desc' in address and address['address_desc'] is not None:
                    address['local_addr'] = address['address_desc']
                else:
                    address['local_addr'] = ""
                return address
            # check for a cache miss
            if self.use_local_cache() and (not force_query_remote):
                address = self.get_address(corp_num, address_id, True)
                self.add_cache_miss('address', corp_num, address_id, address)
                return address
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_names(self, corp_num, name_typ_cds, registration_date):
        sql_name = """SELECT corp_num, corp_name_typ_cd, start_event_id, end_event_id, corp_name_seq_num, srch_nme, corp_nme, dd_corp_num
                  FROM """ + self.get_table_prefix() + """corp_name
                  WHERE corp_num = """ + self.get_db_sql_param() + """ AND corp_name_typ_cd in ({}) """

        cur = None
        try:
            names = []
            cur = self.get_db_connection().cursor()
            placeholders= ', '.join([self.get_db_sql_param()]*len(name_typ_cds))  # "%s, %s, %s, ... %s"
            sql_name = sql_name.format(placeholders)
            cur.execute(sql_name, (corp_num,) + tuple(name_typ_cds))
            row = cur.fetchone()
            while row is not None:
                corp_name = {}
                corp_name['corp_num'] = row[0]
                corp_name['corp_name_typ_cd'] = row[1]
                corp_name['start_event_id'] = row[2]
                corp_name['start_event'] = self.get_event(row[0], row[2])
                corp_name['effective_start_date'] = corp_name['start_event']['effective_date']
                corp_name['end_event_id'] = row[3]
                if corp_name['end_event_id'] is not None:
                    corp_name['end_event'] = self.get_event(corp_num, corp_name['end_event_id'])
                    corp_name['effective_end_date'] = corp_name['end_event']['effective_date']
                else:
                    corp_name['effective_end_date'] = MAX_END_DATE
                corp_name['corp_name_seq_num'] = row[4]
                corp_name['srch_nme'] = row[5]
                corp_name['corp_nme'] = row[6]
                corp_name['dd_corp_num'] = row[7]

                if corp_name['effective_start_date'] > corp_name['effective_end_date']:
                    #LOGGER.info(">>>Data Issue:Date:" + corp_num + ":Corp_Name:", corp_name)
                    if is_data_conversion_event(corp_name['start_event']) and registration_date is not None:
                        corp_name['start_event']['effective_date'] = registration_date
                        corp_name['effective_start_date'] = registration_date

                names.append(corp_name)
                row = cur.fetchone()

            cur.close()
            cur = None

            if len(names) == 1 and registration_date is not None and (names[0]['effective_start_date'] is None or names[0]['effective_start_date'] == '' or is_data_conversion_event(corp_name['start_event'])):
                names[0]['start_event']['effective_date'] = registration_date
                names[0]['effective_start_date'] = registration_date

            #self.check_same_start_date(corp_num, 'corp_name', names, 'effective_start_date')

            return names
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()

    # get the corporation's current state
    def get_corp_states(self, corp_num):
        sql_state = """SELECT state.corp_num corp_num, state.start_event_id start_event_id, state.end_event_id end_event_id, 
                        state.state_typ_cd state_typ_cd, state.dd_corp_num dd_corp_num, 
                        op_state.op_state_typ_cd op_state_typ_cd, op_state.short_desc short_desc, op_state.full_desc full_desc
                        FROM """ + self.get_table_prefix() + """corp_state state, """ + self.get_table_prefix() + """corp_op_state op_state
                        WHERE corp_num = """ + self.get_db_sql_param() + """ and op_state.state_typ_cd = state.state_typ_cd"""
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql_state, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            corp_states = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            return corp_states
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_jurisdictions(self, corp_num):
        sql_juris = """SELECT corp_num, start_event_id, end_event_id, j.can_jur_typ_cd can_jur_typ_cd,
                                home_recogn_dt, othr_juris_desc, home_juris_num, home_company_nme,
                                short_desc, full_desc
                        FROM """ + self.get_table_prefix() + """jurisdiction j, """ + self.get_table_prefix() + """jurisdiction_type jt
                        WHERE j.corp_num = """ + self.get_db_sql_param() + """ AND j.can_jur_typ_cd = jt.can_jur_typ_cd"""
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql_juris, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            jurisdictions = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(jurisdictions) > 0:
                for jurisdiction in jurisdictions:
                    jurisdiction['start_event'] = self.get_event(corp_num, jurisdiction['start_event_id'])
                    jurisdiction['effective_start_date'] = jurisdiction['start_event']['effective_date']
                    if jurisdiction['end_event_id'] is not None:
                        jurisdiction['end_event'] = self.get_event(corp_num, jurisdiction['end_event_id'])
                        jurisdiction['effective_end_date'] = jurisdiction['end_event']['effective_date']
                    else:
                        jurisdiction['effective_end_date'] = MAX_END_DATE

                    #if jurisdiction['effective_start_date'] > jurisdiction['effective_end_date']:
                    #    LOGGER.info(">>>Data Issue:Date:" + corp_num + ":Jurisdiction:", jurisdiction)
                #self.check_same_start_date(corp_num, 'jurisdiction', jurisdictions, 'effective_start_date')
                jurisdictions = sorted(jurisdictions, key=lambda k: k['effective_end_date'])
                jurisdictions = sorted(jurisdictions, key=lambda k: int(k['start_event_id']))
                jurisdictions = sorted(jurisdictions, key=lambda k: k['effective_start_date'])
                return jurisdictions
            return []
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_office_type(self, office_typ_cd):
        sql_type = """SELECT office_typ_cd, short_desc, full_desc
                        FROM """ + self.get_table_prefix() + """office_type
                        WHERE office_typ_cd = """ + self.get_db_sql_param()
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql_type, (office_typ_cd,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            office_type = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(office_type) > 0:
                return office_type[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_corp_type(self, corp_typ_cd):
        sql_type = """SELECT corp_typ_cd, colin_ind, corp_class, short_desc, full_desc
                        FROM """ + self.get_table_prefix() + """corp_type
                        WHERE corp_typ_cd = """ + self.get_db_sql_param()
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql_type, (corp_typ_cd,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            corp_type = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(corp_type) > 0:
                return corp_type[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def addr_line(self, addr_element, delimiter):
        if addr_element is not None:
            return addr_element + delimiter
        return ''

    def get_basic_corp_info_from_lear(self, corp_num):
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
                             '' as corp_class,
                             id as record_id
                 FROM """ + self.get_sec_table_prefix() + """businesses
                 WHERE identifier = '""" + corp_num + """'"""

        cur = None
        try:
            corp = None

            if corp_num is not None and len(str(corp_num)) > 0:
                LOGGER.debug(">>> get corp info for: " + corp_num)
                cur = self.get_sec_db_connection().cursor()
                cur.execute(sql_corp)
                row = cur.fetchone()
                if row is not None:
                    LOGGER.debug("    got corp rec: " + str(row[17]) + "," + row[0] + "," + row[1])
                    corp = {}
                    corp['current_date'] = timezone.localize(datetime.datetime.now())
                    corp['corp_num'] = row[0]
                    corp['corp_typ_cd'] = row[1]
                    # corp['corp_type'] = self.get_corp_type(row[1])
                    corp['recognition_dts'] = self.to_lear_date(row[2])
                    corp['last_ar_filed_dt'] = self.to_lear_date(row[3])
                    bn_9 = ''
                    if row[4] and 9 <= len(row[4]):
                        bn_9 = row[4][:9]
                    corp['bn_9'] = bn_9
                    corp['bn_15'] = row[5]
                    corp['admin_email'] = row[6]
                    corp['last_ledger_dt'] = self.to_lear_date(row[7])
                    corp['last_event_dt'] = self.to_lear_date(row[8])
                    corp['corp_nme'] = row[9]
                    corp['corp_nme_as'] = row[10]
                    corp['corp_nme_effective_date'] = None
                    corp['can_jur_typ_cd'] = row[11]
                    corp['xpro_typ_cd'] = row[12]
                    corp['othr_juris_desc'] = row[13]
                    corp['state_typ_cd'] = STATE_CODES[row[14]] if row[14] in STATE_CODES else row[14]
                    corp['op_state_typ_cd'] = STATE_CODES[row[15]] if row[15] in STATE_CODES else row[15]
                    corp['state_typ_effective_date'] = None
                    corp['corp_class'] = row[16]
                cur.close()
                cur = None

            if corp is None:
                LOGGER.debug("No corp rec found for " + str(corp_num))
                corp = {}
                corp['corp_num'] = ''
                corp['corp_typ_cd'] = ''
                corp['recognition_dts'] = None
                corp['filing'] = {}
                corp['transaction'] = {}
                corp['effective_date'] = None

            return corp

        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading corp info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()

    def get_basic_corp_info(self, corp_num, deep_copy=True):
        sql_corp = """SELECT corp_num, corp_typ_cd, recognition_dts, last_ar_filed_dt, bn_9, bn_15, admin_email, last_ledger_dt
                 FROM """ + self.get_table_prefix() + """corporation
                 WHERE corp_num = """ + self.get_db_sql_param()

        cur = None
        try:
            corp = {}

            # assume there is just one corp record
            cur = self.get_db_connection().cursor()
            cur.execute(sql_corp, (corp_num,))
            row = cur.fetchone()
            if row is None:
                LOGGER.debug("No corp rec found for " + str(corp_num))
                corp['corp_num'] = ''
                corp['corp_typ_cd'] = ''
                corp['recognition_dts'] = ''
            else:
                corp['current_date'] = datetime.datetime.now()
                corp['corp_num'] = row[0]
                if deep_copy:
                    corp['jurisdiction'] = self.get_jurisdictions(row[0])
                corp['corp_typ_cd'] = row[1]
                corp['corp_type'] = self.get_corp_type(row[1])
                corp['recognition_dts'] = row[2]
                corp['last_ar_filed_dt'] = row[3]
                corp['bn_9'] = row[4]
                corp['bn_15'] = row[5]
                corp['admin_email'] = row[6]
                corp['last_ledger_dt'] = row[7]
                cur.close()
                cur = None
         
                if deep_copy and corp['corp_typ_cd'] in CORP_TYPES_IN_SCOPE:
                    # get corp names
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

    def to_lear_date(self, the_date):
        if not the_date:
            return the_date
        if isinstance(the_date, datetime.datetime):
            return the_date
        # print(">>> converting:", the_date)
        the_format = '%Y-%m-%d %H:%M:%S'
        if 0 <= the_date.find('.'):
            the_format += ".%f"
        if 0 <= the_date.find('+'):
            the_format += "%z"
        the_date = datetime.datetime.strptime(the_date, the_format)
        return the_date

    def get_lear_corp_version_effective_date(self, corp, txn_field: str = 'transaction', filing_field: str = 'filing'):
        effective_date = None
        if txn_field in corp and 'effective_date' in corp[txn_field]:
            effective_date =  corp[txn_field]['effective_date']
        elif filing_field and filing_field in corp and 'effective_date' in corp[filing_field]:
            effective_date =  corp[filing_field]['effective_date']
        else:
            effective_date = corp['last_event_dt']
        # remove tzinfo
        effective_date = effective_date.replace(tzinfo=None) if effective_date else effective_date
        if effective_date is None:
            print(">>> effective_date is none:", txn_field, corp)
        return effective_date

    # return the "effective date" given an event and filing
    def get_lear_event_filing_effective_date(self, event):
        ret_date = None

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

    # find a specific event, 
    # return None if not found
    def get_lear_event(self, event_id):
        sql = """SELECT id, issued_at
                    FROM """ + self.get_sec_table_prefix() + """transaction 
                    WHERE id = """ + str(event_id)
        ret_event = None
        cursor = None
        try:
            cursor = self.get_sec_db_connection().cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(event) > 0:
                ret_event = event[0]
            if ret_event is None:
                return {}
            ret_event['issued_at'] = self.to_lear_date(ret_event['issued_at'])

            # fill in filing
            if 'filing' not in ret_event:
                ret_event['filing'] = self.get_lear_filing_event(event_id, None)
            ret_event['effective_date'] = self.get_lear_event_filing_effective_date(ret_event)
            return ret_event
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_lear_filing_event(self, event_id, event_type):
        sql_filing = """SELECT filing.id, filing_type, filing_date, filing_json, filing.transaction_id, effective_date, completion_date, 
                        status, business_id, corp.identifier as corp_num 
                        from """ + self.get_sec_table_prefix() + """filings filing, 
                        """ + self.get_sec_table_prefix() + """businesses corp
                        WHERE filing.transaction_id = """ + str(event_id) + """ and corp.id = filing.business_id"""
        cursor = None
        try:
            cursor = self.get_sec_db_connection().cursor()
            cursor.execute(sql_filing)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            filing_event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(filing_event) > 0:
                the_filing = filing_event[0]
                the_filing['filing_date'] = self.to_lear_date(the_filing['filing_date'])
                the_filing['completion_date'] = self.to_lear_date(the_filing['completion_date'])
                the_filing['effective_date'] = self.to_lear_date(the_filing['effective_date'])
                return the_filing
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_bc_reg_corp_info(self, corp_num):
        sql_party = """SELECT corp_num, corp_party_id, mailing_addr_id, delivery_addr_id, party_typ_cd, start_event_id, end_event_id, cessation_dt,
                         last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt,
                         phone, reason_typ_cd
                      FROM """ + self.get_table_prefix() + """corp_party
                      WHERE (corp_num = """ + self.get_db_sql_param() + """ OR bus_company_num = """ + self.get_db_sql_param() + """)
                        """
                        #AND party_typ_cd = 'FBO'"""

        cur = None
        try:
            corp = self.get_basic_corp_info(corp_num)
            corp_type = corp['corp_typ_cd']

            # get parties
            corp['parties'] = []
            if corp_type in CORP_TYPES_IN_SCOPE:
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
                            corp_party['corp_info'] = self.get_basic_corp_info(corp_party['bus_company_num'], deep_copy=False)
                    else:
                        corp_party['corp_info'] = self.get_basic_corp_info(corp_party['corp_num'], deep_copy=False)

                    corp['parties'].append(corp_party)
                    row = cur.fetchone()
                cur.close()
                cur = None

                # need to check LEAR database for relationships, for new DBA's added/updated in LEAR
                lear_corp_num = self.corp_num_with_prefix(corp_type, corp_num)
                # print(">>> check LEAR relationships for:", lear_corp_num)
                sql_party_lear = """SELECT businesses.identifier as corp_num,
                                       parties.id as corp_party_id, 
                                       parties.mailing_address_id as mailing_addr_id, 
                                       parties.delivery_address_id as delivery_addr_id, 
                                       parties.party_type as party_typ_cd, 
                                       parties.transaction_id as transaction_id,
                                       parties.end_transaction_id as end_transaction_id,
                                       roles.cessation_date as cessation_dt,
                                       parties.last_name as last_nme, 
                                       parties.middle_initial as middle_nme, 
                                       parties.first_name as first_nme, 
                                       parties.organization_name as business_nme, 
                                       parties.identifier as bus_company_num, 
                                       parties.email as email_address, 
                                       roles.id as role_id,
                                       roles.role as role,
                                       roles.transaction_id as role_transaction_id,
                                       roles.end_transaction_id as role_end_transaction_id
                              FROM """ + self.get_sec_table_prefix() + """businesses businesses,
                                   """ + self.get_sec_table_prefix() + """parties_version parties,
                                   """ + self.get_sec_table_prefix() + """party_roles_version roles
                              WHERE businesses.id = roles.business_id
                                AND roles.party_id = parties.id 
                                AND parties.party_type = 'organization' and roles.role = 'proprietor'
                                AND (parties.identifier = '""" + lear_corp_num + """'
                                     OR roles.business_id = (select id from """ + self.get_sec_table_prefix() + """businesses
                                     where identifier = '""" + lear_corp_num + """'))
                                """

                cur = self.get_sec_db_connection().cursor()
                cur.execute(sql_party_lear)
                # print(">>> fetch party row ...", sql_party_lear)
                row = cur.fetchone()
                while row is not None:
                    corp_party = {}
                    corp_party['corp_num'] = row[0]
                    corp_party['corp_party_id'] = row[1]
                    corp_party['mailing_addr_id'] = row[2]
                    corp_party['delivery_addr_id'] = row[3]
                    corp_party['party_typ_cd'] = row[4]
                    transaction_id = row[5]
                    corp_party['transaction_id'] = transaction_id
                    if transaction_id and 0 < transaction_id:
                        transaction = self.get_lear_event(transaction_id)
                        corp_party['transaction'] = transaction
                    else:
                        corp_party['transaction'] = {}
                    corp_party['effective_start_date'] = self.get_lear_corp_version_effective_date(corp_party)
                    end_transaction_id = row[6]
                    corp_party['end_transaction_id'] = end_transaction_id
                    if end_transaction_id and 0 < end_transaction_id:
                        end_transaction = self.get_lear_event(end_transaction_id)
                        corp_party['end_transaction'] = end_transaction
                        corp_party['effective_end_date'] = self.get_lear_corp_version_effective_date(corp_party, txn_field='end_transaction', filing_field=None)
                    else:
                        corp_party['end_transaction'] = {}
                        corp_party['effective_end_date'] = MAX_END_DATE
                    corp_party['cessation_dt'] = row[7]
                    corp_party['last_nme'] = row[8]
                    corp_party['middle_nme'] = row[9]
                    corp_party['first_nme'] = row[10]
                    corp_party['business_nme'] = row[11]
                    corp_party['bus_company_num'] = row[12]
                    corp_party['email_address'] = row[13]
                    corp_party['corp_party_seq_num'] = None
                    corp_party['office_notification_dt'] = None
                    corp_party['phone'] = None
                    corp_party['reason_typ_cd'] = None
                    corp_party['role_id'] = row[14]
                    corp_party['role'] = row[15]
                    role_transaction_id = row[16]
                    corp_party['role_transaction_id'] = role_transaction_id
                    if role_transaction_id and 0 < role_transaction_id:
                        role_transaction = self.get_lear_event(role_transaction_id)
                        corp_party['role_transaction'] = role_transaction
                    else:
                        corp_party['role_transaction'] = {}
                    corp_party['role_effective_start_date'] = self.get_lear_corp_version_effective_date(corp_party, txn_field='role_transaction', filing_field=None)
                    role_end_transaction_id = row[17]
                    corp_party['role_end_transaction_id'] = role_end_transaction_id
                    if role_end_transaction_id and 0 < role_end_transaction_id:
                        role_end_transaction = self.get_lear_event(role_end_transaction_id)
                        corp_party['role_end_transaction'] = role_end_transaction
                        corp_party['role_effective_end_date'] = self.get_lear_corp_version_effective_date(corp_party, txn_field='role_end_transaction', filing_field=None)
                    else:
                        corp_party['role_end_transaction'] = {}
                        corp_party['role_effective_end_date'] = MAX_END_DATE

                    # note we are only issuing a relationship credential (with the two corp_nums) 
                    # ... so just get basic info for the "other" corp in the relationship
                    # print(">>> check for company info ...")
                    if corp_num == corp_party['corp_num'] and corp_party['bus_company_num'] is not None:
                        corp_party['corp_info'] = self.get_basic_corp_info(corp_party['bus_company_num'], deep_copy=False)
                    else:
                        corp_party['corp_info'] = self.get_basic_corp_info(corp_party['corp_num'], deep_copy=False)

                    # if the 'corp_info' doesn't exist in our "COLIN" database, check in "LEAR"
                    if corp_party['corp_info']['corp_num'] is None or corp_party['corp_info']['corp_num'] == '':
                        # print(">>> check for LEAR company info ...")
                        corp_party['corp_info'] = self.get_basic_corp_info_from_lear(corp_party['corp_num'])

                    corp['parties'].append(corp_party)
                    # print(">>> fetch party row ...")
                    row = cur.fetchone()
                cur.close()
                cur = None

            return corp
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading corp party info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()

    # convert object to JSON, converting data types (decimal, date) to string
    def to_json(self, data):
        ret = json.dumps(data, cls=CustomJsonEncoder)
        return ret

