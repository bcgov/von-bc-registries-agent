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

from bcreg.bcreg_core import BCReg_Core, MAX_WHERE_IN, CORP_WITHDRAWN_STATE
from bcreg.config import config
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


lear_system_type = 'BCREG_LEAR'

BC_REGISTRIES_DATABASE_NAME = 'bc_reg_lear'
BC_REG_COLIN_TABLE_PREFIX = 'bc_registries.'
BC_REG_COLIN_DATABASE_NAME = 'bc_registries'
BC_REGISTRIES_TIMEZONE = 'PST8PDT'

MIN_START_DATE = datetime.datetime(datetime.MINYEAR+1, 1, 1)
MAX_END_DATE   = datetime.datetime(datetime.MAXYEAR-1, 12, 31)

# for now, we are in PST time
timezone = pytz.timezone("PST8PDT")

MIN_START_DATE_TZ = timezone.localize(MIN_START_DATE)
MAX_END_DATE_TZ   = timezone.localize(MAX_END_DATE)

LOGGER = logging.getLogger(__name__)

LEAR_CORP_TYPES_IN_SCOPE = {
    "GP":  "PARTNERSHIP",
    "SP":  "SOLE PROP",
}

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
                #LOGGER.error(error)
                #LOGGER.error(traceback.print_exc())
                #raise error
                if o.year <= datetime.MINYEAR+1:
                    return MIN_START_DATE_TZ.astimezone(pytz.utc).isoformat()
                elif o.year >= datetime.MAXYEAR-1:
                    return MAX_END_DATE_TZ.astimezone(pytz.utc).isoformat()
                return o.isoformat()
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
        self.source_system_type = lear_system_type
        self.SEC_DB_TABLE_PREFIX = BC_REG_COLIN_TABLE_PREFIX
        self.SEC_PG_DATABASE_NAME = BC_REG_COLIN_DATABASE_NAME
        super().__init__(cache)


    ###########################################################################
    # load all bc registries data for the specified corps into our in-mem cache
    ###########################################################################

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corps(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            self.cache_lear_bcreg_corps(specific_corps, generate_individual_sql=generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corp_tables(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            self.cache_lear_bcreg_corp_tables(specific_corps, generate_individual_sql=generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_code_tables(self, generate_individual_sql=False):
        if self.use_local_cache():
            self.cache_lear_bcreg_code_tables(generate_individual_sql=generate_individual_sql)

    # clear in-mem cache - delete all existing data
    def cache_cleanup(self):
        for table in self.lear_corp_tables:
            self.cache_cleanup_data(table)
        for table in self.lear_other_tables:
            self.cache_cleanup_data(table)
        for table in self.lear_other_other_tables:
            self.cache_cleanup_data(table)
        for table in self.lear_other_other_other_tables:
            self.cache_cleanup_data(table)
        for table in self.lear_code_tables:
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
                cur.execute("""SELECT max(issued_at) FROM """ + self.DB_TABLE_PREFIX + """transaction""")
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
        sql1 = """SELECT parties.identifier corp_num
                  FROM businesses businesses,
                       parties_version parties, 
                       party_roles_version roles
                  WHERE businesses.id = roles.business_id
                    AND roles.party_id = parties.id 
                    AND parties.party_type = 'organization' and roles.role = 'proprietor'
                    AND (parties.identifier = %s
                         OR roles.business_id = (select id from businesses where identifier = %s))"""
        new_corps = []
        for corp in corps:
            cur = None
            try:
                # LOGGER.info("Executing: " + sql1 + " with" + str(corp['CORP_NUM']))
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

    # return the "effective date" given an event and filing
    def get_event_filing_effective_date(self, event, corp_type_cd=None):
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

    # return the "effective date" given an event id
    def get_event_effective_date(self, event_id):
        # note that corp_num is ignored in the following queries
        if event_id == 0:
            return datetime.datetime(datetime.MINYEAR, 1, 1) # MIN_START_DATE
        event = self.get_event('0', event_id)
        return self.to_lear_date(event['issued_at'])

    # find a specific event, 
    # return None if not found
    def get_event(self, corp_num, event_id, corp_type_cd=None):
        sql = """SELECT id, issued_at
                    FROM """ + self.get_table_prefix() + """transaction 
                    WHERE id = """ + self.get_db_sql_param()
        ret_event = None
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql, (event_id,))
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
                ret_event['filing'] = self.get_filing_event(corp_num, event_id, None)
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

    def get_filing_event(self, corp_num, event_id, event_type):
        sql_filing = """SELECT filing.id, filing_type, filing_date, filing_json, filing.transaction_id, effective_date, completion_date, 
                        status, business_id, corp.identifier as corp_num 
                        from """ + self.get_table_prefix() + """filings filing, """ + self.get_table_prefix() + """businesses corp
                        WHERE filing.transaction_id = """ + self.get_db_sql_param() + """ and corp.id = filing.business_id"""
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql_filing, (event_id,))
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
                    "filing_date": self.to_lear_date(row[2]),
                    "filing_json": row[3],
                    "transaction_id": row[4],
                    "business_id": row[5],
                    "status": row[6],
                    "completion_date": self.to_lear_date(row[7]),
                    "effective_date": self.to_lear_date(row[8]),
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

    def get_corp_version_effective_date(self, corp, txn_field: str = 'transaction', filing_field: str = 'filing'):
        effective_date = None
        if txn_field in corp and 'effective_date' in corp[txn_field]:
            effective_date =  corp[txn_field]['effective_date']
        elif filing_field and filing_field in corp and 'effective_date' in corp[filing_field]:
            effective_date =  corp[filing_field]['effective_date']
        else:
            effective_date = corp['last_event_dt']
        if effective_date.tzinfo is None or effective_date.tzinfo.utcoffset(effective_date) is None:
            effective_date = effective_date.replace(tzinfo=pytz.utc)
        return effective_date

    def get_basic_corp_info_from_colin(self, corp_num):
        srch_corp_num = corp_num[2:] if corp_num.startswith('BC') else corp_num
        sql_corp = """SELECT c.corp_num corp_num, corp_typ_cd, recognition_dts, last_ar_filed_dt, bn_9, bn_15, 
                      admin_email, last_ledger_dt, s.state_typ_cd state_typ_cd
                 FROM """ + self.get_sec_table_prefix(force_query_remote=True) + """corporation c,
                      """ + self.get_sec_table_prefix(force_query_remote=True) + """corp_state s
                 WHERE c.corp_num = '""" + srch_corp_num + """'
                   AND s.corp_num = c.corp_num and s.end_event_id is null""" 
        # print(">>> looking for COLIN corp:", sql_corp)
        corp = {}
        corp['corp_num'] = ''
        corp['corp_typ_cd'] = ''
        corp['recognition_dts'] = None
        corp['filing'] = {}
        corp['transaction'] = {}
        corp['effective_date'] = None

        cur = None
        try:
            # assume there is just one corp record
            cur = self.get_sec_db_connection(force_query_remote=True).cursor()
            cur.execute(sql_corp)
            row = cur.fetchone()
            if row is None:
                LOGGER.debug("No corp rec found for " + str(corp_num))
            elif row[8] == CORP_WITHDRAWN_STATE:
                LOGGER.info("Corporation is withdrawn, skipping for " + str(corp_num))
            else:
                corp['current_date'] = datetime.datetime.now()
                corp['corp_num'] = row[0]
                corp['corp_typ_cd'] = row[1]
                # TODO may need another query to get this info from COLIN
                corp['corp_type'] = {
                    "corp_typ_cd":corp['corp_typ_cd'],
                    "colin_ind": "",
                    "corp_class": "",
                    "short_desc": corp['corp_typ_cd'],
                    "full_desc": corp['corp_typ_cd'],
                }
                corp['recognition_dts'] = row[2]
                corp['last_ar_filed_dt'] = row[3]
                corp['bn_9'] = row[4]
                corp['bn_15'] = row[5]
                corp['admin_email'] = row[6]
                corp['last_ledger_dt'] = row[7]
                corp['state_typ_cd'] = row[8]
            cur.close()
            cur = None
            #LOGGER.error("Returning corp from COLIN: {corp}")
            return corp
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
                             '' as corp_class,
                             id as record_id""" + bus_ver_columns + """
                 FROM """ + self.get_table_prefix() + bus_table + """
                 WHERE identifier = """ + self.get_db_sql_param()

        cur = None
        try:
            corps = []
            corp = None

            if corp_num is not None and len(str(corp_num)) > 0:
                LOGGER.debug(">>> get corp info for: " + corp_num + "," + str(versions))
                cur = self.get_db_connection().cursor()
                cur.execute(sql_corp, (corp_num,))
                row = cur.fetchone()
                while row is not None:
                    LOGGER.debug("    got corp rec: " + str(row[17]) + "," + row[0] + "," + row[1])
                    corp = {}
                    corp['current_date'] = timezone.localize(datetime.datetime.now())
                    corp['corp_num'] = row[0]
                    if deep_copy:
                        # TODO
                        # corp['jurisdiction'] = self.get_jurisdictions(row[0])
                        pass
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
                    if versions:
                        LOGGER.debug("    get filings etc ...")
                        state_filing_id = row[18]
                        corp['state_filing_id'] = state_filing_id
                        if state_filing_id and 0 < state_filing_id:
                            filings = self.get_corp_filings(filing_id=corp['state_filing_id'])
                            corp['filing'] = filings[0] if 0 < len(filings) else {}
                        else:
                            corp['filing'] = {}
                        transaction_id = row[19]
                        if transaction_id and 0 < transaction_id:
                            transaction = self.get_event(corp['corp_num'], transaction_id)
                            corp['transaction'] = transaction
                        else:
                            corp['transaction'] = {}
                        corp['effective_date'] = self.get_corp_version_effective_date(corp)

                    if versions:
                        corps.append(corp)
                        row = cur.fetchone()
                    else:
                        row = None

                    if deep_copy:
                        corp['office'] = []

                cur.close()
                cur = None

            if (not versions) and corp is None:
                LOGGER.debug("No corp rec found for " + str(corp_num))
                corp = {}
                corp['corp_num'] = ''
                corp['corp_typ_cd'] = ''
                corp['recognition_dts'] = None
                corp['filing'] = {}
                corp['transaction'] = {}
                corp['effective_date'] = None

            if versions:
                # fill in effective dates for versions (name, status)
                LOGGER.debug("    sort version records for: " + corp_num)
                corps = sorted(corps, key=lambda k: k['effective_date'])
                # print(">>> sorted versions:", corps)
                corp_nme = None
                corp_nme_effective_date = None
                state_typ_cd = None
                state_typ_effective_date = None
                for corp_v in corps:
                    if (not corp_nme) or corp_v['corp_nme'] != corp_nme:
                        corp_v['corp_nme_effective_date'] = corp_v['effective_date']
                        corp_nme = corp_v['corp_nme']
                        corp_nme_effective_date = corp_v['corp_nme_effective_date']
                    else:
                        corp_v['corp_nme_effective_date'] = corp_nme_effective_date
                    if (not state_typ_cd) or corp_v['state_typ_cd'] != state_typ_cd:
                        corp_v['state_typ_effective_date'] = corp_v['effective_date']
                        state_typ_cd = corp_v['state_typ_cd']
                        state_typ_effective_date = corp_v['state_typ_effective_date']
                    else:
                        corp_v['state_typ_effective_date'] = state_typ_effective_date
                LOGGER.debug("    done.")
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

    def get_lear_relationship_info(self, corp_info):
        sql_party = """SELECT businesses.identifier as corp_num,
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
                      FROM """ + self.get_table_prefix() + """businesses businesses,
                           """ + self.get_table_prefix() + """parties_version parties, 
                           """ + self.get_table_prefix() + """party_roles_version roles
                      WHERE businesses.id = roles.business_id
                        AND roles.party_id = parties.id 
                        AND parties.party_type = 'organization' and roles.role = 'proprietor'
                        AND (parties.identifier = """ + self.get_db_sql_param() + """ 
                             OR roles.business_id = (select id from """ + self.get_table_prefix() + """businesses where identifier = """ + self.get_db_sql_param() + """))
                        """

        corp_num = corp_info['corp_num']
        cur = None
        try:
            cur = self.get_db_connection().cursor()
            # print(">>>", corp_num, corp_num, sql_party)
            cur.execute(sql_party, (corp_num, corp_num,))
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
                    transaction = self.get_event(corp_party['corp_num'], transaction_id)
                    corp_party['transaction'] = transaction
                else:
                    corp_party['transaction'] = {}
                corp_party['effective_start_date'] = self.get_corp_version_effective_date(corp_party)
                end_transaction_id = row[6]
                corp_party['end_transaction_id'] = end_transaction_id
                if end_transaction_id and 0 < end_transaction_id:
                    end_transaction = self.get_event(corp_party['corp_num'], end_transaction_id)
                    corp_party['end_transaction'] = end_transaction
                    corp_party['effective_end_date'] = self.get_corp_version_effective_date(corp_party, txn_field='end_transaction', filing_field=None)
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
                    role_transaction = self.get_event(corp_party['corp_num'], role_transaction_id)
                    corp_party['role_transaction'] = role_transaction
                else:
                    corp_party['role_transaction'] = {}
                corp_party['role_effective_start_date'] = self.get_corp_version_effective_date(corp_party, txn_field='role_transaction', filing_field=None)
                role_end_transaction_id = row[17]
                corp_party['role_end_transaction_id'] = role_end_transaction_id
                if role_end_transaction_id and 0 < role_end_transaction_id:
                    role_end_transaction = self.get_event(corp_party['corp_num'], role_end_transaction_id)
                    corp_party['role_end_transaction'] = role_end_transaction
                    corp_party['role_effective_end_date'] = self.get_corp_version_effective_date(corp_party, txn_field='role_end_transaction', filing_field=None)
                else:
                    corp_party['role_end_transaction'] = {}
                    corp_party['role_effective_end_date'] = MAX_END_DATE

                # note we are only issuing a relationship credential (with the two corp_nums) 
                # ... so just get basic info for the "other" corp in the relationship
                if corp_num == corp_party['corp_num'] and corp_party['bus_company_num'] is not None:
                    corp_party['corp_info'] = self.get_basic_corp_info(corp_party['bus_company_num'], deep_copy=False, versions=False)
                else:
                    corp_party['corp_info'] = self.get_basic_corp_info(corp_party['corp_num'], deep_copy=False, versions=False)

                # if the 'corp_info' doesn't exist in our "LEAR" database, check in "COLIN"
                if corp_party['corp_info']['corp_num'] is None or corp_party['corp_info']['corp_num'] == '':
                    if corp_num == corp_party['corp_num'] and corp_party['bus_company_num'] is not None:
                        corp_party['corp_info'] = self.get_basic_corp_info_from_colin(corp_party['bus_company_num'])

                # if there is no corp info (cant find related corp) don't add the relationship
                if not (corp_party['corp_info'] is None or corp_party['corp_info']['corp_num'] is None or corp_party['corp_info']['corp_num'] == ''):
                    corp_info['parties'].append(corp_party)

                row = cur.fetchone()
            cur.close()
            cur = None

            return corp_info
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading corp party info from DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()


    def get_bc_reg_corp_info(self, corp_num):
        corp = self.get_basic_corp_info(corp_num, versions=False)
        corp_type = corp['corp_typ_cd']
        if (not corp_type or corp_type == ''):
            # corp not found in LEAR, return basic data from COLIN
            corp = self.get_basic_corp_info_from_colin(corp_num)
            corp['versions'] = {}
            corp['parties'] = []
            return corp
        elif corp_type in LEAR_CORP_TYPES_IN_SCOPE:
            corp['versions'] = self.get_basic_corp_info(corp_num, versions=True)
        else:
            corp['versions'] = {}

        # get parties
        corp['parties'] = []
        corp = self.get_lear_relationship_info(corp)

        return corp


    # convert object to JSON, converting data types (decimal, date) to string
    def to_json(self, data):
        ret = json.dumps(data, cls=CustomJsonEncoder)
        return ret

