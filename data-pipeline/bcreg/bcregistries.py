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

from bcreg.config import config
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

system_type = 'BC_REG'

BC_REGISTRIES_TABLE_PREFIX = 'bc_registries.'
INMEM_CACHE_TABLE_PREFIX   = ''
MAX_WHERE_IN = 1000

MIN_START_DATE = datetime.datetime(datetime.MINYEAR+1, 1, 1)
MAX_END_DATE   = datetime.datetime(datetime.MAXYEAR-1, 12, 31)
DATA_CONVERSION_DATE = datetime.datetime(2004, 3, 26)
DATA_CONVERSION_DATE_STR = "2004-03-26"

# for now, we are in PST time
timezone = pytz.timezone("PST8PDT")

MIN_START_DATE_TZ = timezone.localize(MIN_START_DATE)
MAX_END_DATE_TZ   = timezone.localize(MAX_END_DATE)
DATA_CONVERSION_DATE_TZ = timezone.localize(DATA_CONVERSION_DATE)


def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return decimal.Decimal(s)

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
class BCRegistries:
    sql_local_cache = False
    cache_miss = []
    generated_sqls = []
    generated_corp_nums = {}

    def __init__(self, cache=False):
        self.sql_local_cache = cache
        try:
            params = config(section='bc_registries')
            self.conn = psycopg2.connect(**params)

            # Register the adapter
            sqlite3.register_adapter(decimal.Decimal, adapt_decimal)
            # Register the converter
            sqlite3.register_converter("decimal", convert_decimal)
            # connect to in-memory database
            self.cache = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        except (Exception) as error:
            print(error)
            print(traceback.print_exc())
            self.conn = None
            self.cache = None
            log_error("BCRegistries exception connecting to DB: " + str(error))
            raise

    def __del__(self):
        if self.conn:
            self.conn.close()
        if self.cache:
            self.cache.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


    ###########################################################################
    # database cache configuration methods
    ###########################################################################
    def use_local_cache(self):
        return self.sql_local_cache

    def get_db_connection(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return self.cache
        else:
            return self.conn

    def get_db_sql_param(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return '?'
        else:
            return '%s'
    
    def get_table_prefix(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return INMEM_CACHE_TABLE_PREFIX
        else:
            return BC_REGISTRIES_TABLE_PREFIX

    def add_cache_miss(self, table, corp_num, row_id, row):
        miss = {'table':table, 'corp_num':corp_num, 'row_id':row_id, 'row':row}
        self.cache_miss.append(miss)
    

    ###########################################################################
    # random string methods (for generating test data)
    ###########################################################################

    def random_alpha_string(self, length, contains_spaces=False):
        if contains_spaces:
            chars = string.ascii_uppercase + ' '
        else:
            chars = string.ascii_uppercase
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    def random_numeric_string(self, length):
        chars = string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    def random_an_string(self, length, contains_spaces=False):
        if contains_spaces:
            chars = string.ascii_uppercase + string.digits + ' '
        else:
            chars = string.ascii_uppercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    def add_generated_corp_num(self, corp_num):
        if corp_num in self.generated_corp_nums:
            return self.generated_corp_nums[corp_num]

        alpha_prefix = ''
        for ch in corp_num:
            if ch.isalpha():
                alpha_prefix = alpha_prefix + ch
            else:
                break
        new_corp_num = alpha_prefix + self.random_numeric_string(len(corp_num) - len(alpha_prefix))
        self.generated_corp_nums[corp_num] = new_corp_num
        return new_corp_num


    ###########################################################################
    # methods to build and populate in-memory cache of bc registries data
    ###########################################################################

    # return the table structure of a bcreg table
    def get_bcreg_table_struct(self, table, where=""):
        sql = "SELECT * from " + BC_REGISTRIES_TABLE_PREFIX + table
        if 0 < len(where):
            sql = sql + " WHERE " + where
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            cursor.close()
            cursor = None
            return desc
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None

    # return a sql to create an in-mem sqlite table
    def create_table_sql(self, table, table_desc):
        table_sql = 'create table if not exists ' + table + ' ('
        i = 0
        for col in table_desc:
            col_name = col[0]
            col_type = self.get_sql_col_type(col[1])
            _col_len = col[3]
            table_sql = table_sql + col_name + ' ' + col_type 
            i = i + 1
            if i < len(table_desc):
                table_sql = table_sql + ', '
            else:
                table_sql = table_sql + ')'
        return table_sql

    def get_sql_col_type(self, pg_type):
        if pg_type == 1042:  # CHAR
            return 'text'  
        if pg_type == 1043:  # VARCHAR
            return 'text'
        if pg_type == 1700:  # NUMBER(38)
            return 'numeric'
        if pg_type == 23:    # NUMBER(7)
            return 'integer'
        if pg_type == 1114:  # DATE or DATETIME
            return 'timestamp'
        # default for now
        return 'text'

    def stringify(self, s_val):
        if "'" in s_val:
            s_val = s_val.replace("'", "''")
        return str(s_val)

    def get_sql_col_value(self, col_value, pg_type):
        if col_value is None:
            return 'null'
        if pg_type == 1042:  # CHAR
            return "'" + self.stringify(col_value) + "'"  
        if pg_type == 1043:  # VARCHAR
            return "'" + self.stringify(col_value) + "'"  
        if pg_type == 1700:  # NUMBER(38)
            return str(col_value)
        if pg_type == 23:    # NUMBER(7)
            return str(col_value)
        if pg_type == 1114:  # DATE or DATETIME
            return "'" + str(col_value) + "'"  
        # default for now
        return str(col_value)

    # cache data from bc registries database into a local in-mem sqlite table
    # create the table if nencessary, based on the bc registries dictionary
    def cache_cleanup_data(self, table):
        delete_sql = 'delete from ' + table
        cache_cursor = None
        try:
            cache_cursor = self.cache.cursor()
            cache_cursor.execute(delete_sql)
            cache_cursor.close()
            cache_cursor = None
        except (Exception) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cache_cursor is not None:
                cache_cursor.close()
            cache_cursor = None

    # cache data from bc registries database into a local in-mem sqlite table
    # create the table if nencessary, based on the bc registries dictionary
    # note: "generate_individual_sql" will generate and print sql statements if True
    #       to be used to generate sample data for unit testing
    def cache_bcreg_data(self, table, desc, rows, generate_individual_sql=False):
        create_sql = self.create_table_sql(table, desc)
        col_keys = []
        insert_keys = ''
        insert_placeholders = ''
        inserts = []
        insert_sqls = []
        for row in rows:
            if len(col_keys) == 0:
                i = 0
                for key in row:
                    col_keys.append(key)
                    insert_keys = insert_keys + key
                    insert_placeholders = insert_placeholders + '?'
                    i = i + 1
                    if i < len(row):
                        insert_keys = insert_keys + ', '
                        insert_placeholders = insert_placeholders + ', '

            if generate_individual_sql:
                gen_row = dict()
                gen_row.update(row)
                # depending on the table, generate some sample data and/or replace certain values
                # for the corp_party table, generate random corp nums (this table should be loaded first)
                if table == "corp_party":
                    gen_row['corp_num'] = self.add_generated_corp_num(row['corp_num'])
                    if row['bus_company_num'] is not None and 0 < len(row['bus_company_num']):
                        gen_row['bus_company_num'] = self.add_generated_corp_num(row['bus_company_num'])
                    if row['business_nme'] is not None and 0 < len(row['business_nme']):
                        if row['bus_company_num'] is not None and 0 < len(row['bus_company_num']):
                            gen_row['business_nme'] = row['bus_company_num'] + self.random_alpha_string(20, True)
                        else:
                            gen_row['business_nme'] = self.random_alpha_string(20, True)
                    if 'last_nme' in row and row['last_nme'] is not None:
                        gen_row['last_nme'] = self.random_alpha_string(20, True)
                    if 'middle_nme' in row and row['middle_nme'] is not None:
                        gen_row['middle_nme'] = self.random_alpha_string(10, True)
                    if 'first_nme' in row and row['first_nme'] is not None:
                        gen_row['first_nme'] = self.random_alpha_string(15, True)
                else:
                    # for any table, replace corp_num with the corresponding random value
                    if 'corp_num' in row:
                        gen_row['corp_num'] = self.add_generated_corp_num(row['corp_num'])

                # for corporation, corp_name and address tables, replace certain values
                if table == "corporation":
                    if 'bn_9' in row and row['bn_9'] is not None:
                        gen_row['bn_9'] = self.random_numeric_string(9)
                    if 'bn_15' in row and row['bn_15'] is not None:
                        gen_row['bn_15'] = self.random_numeric_string(15)
                    if 'corp_password' in row and row['corp_password'] is not None:
                        gen_row['corp_password'] = self.random_alpha_string(8)
                    if 'prompt_question' in row and row['prompt_question'] is not None:
                        gen_row['prompt_question'] = self.random_alpha_string(8)
                    if 'admin_email' in row and row['admin_email'] is not None:
                        gen_row['admin_email'] = self.random_alpha_string(12) + '@' + self.random_alpha_string(8) + '.com'
                if table == "corp_name":
                    if 'corp_nme' in row and row['corp_nme'] is not None:
                        gen_row['corp_nme'] = self.random_alpha_string(25, True)
                    if 'srch_nme' in row and row['srch_nme'] is not None:
                        gen_row['srch_nme'] = self.random_alpha_string(20)
                if table == "address":
                    if 'postal_cd' in row and row['postal_cd'] is not None:
                        gen_row['postal_cd'] = self.random_an_string(6)
                    if 'addr_line_1' in row and row['addr_line_1'] is not None:
                        gen_row['addr_line_1'] = self.random_alpha_string(25, True)
                    if 'addr_line_2' in row and row['addr_line_2'] is not None:
                        gen_row['addr_line_2'] = self.random_alpha_string(25, True)
                    if 'address_desc' in row and row['address_desc'] is not None:
                        gen_row['address_desc'] = self.random_alpha_string(40, True)
                    if 'address_desc_short' in row and row['address_desc_short'] is not None:
                        gen_row['address_desc_short'] = self.random_alpha_string(20, True)
                    if 'delivery_instructions' in row and row['delivery_instructions'] is not None:
                        gen_row['delivery_instructions'] = self.random_alpha_string(40, True)
                    if 'unit_no' in row and row['unit_no'] is not None:
                        gen_row['unit_no'] = self.random_numeric_string(3)
                    if 'unit_type' in row and row['unit_type'] is not None:
                        gen_row['unit_type'] = self.random_alpha_string(3)
                    if 'civic_no' in row and row['civic_no'] is not None:
                        gen_row['civic_no'] = self.random_numeric_string(3)
                    if 'civic_no_suffix' in row and row['civic_no_suffix'] is not None:
                        gen_row['civic_no_suffix'] = self.random_alpha_string(3)
                    if 'street_name' in row and row['street_name'] is not None:
                        gen_row['street_name'] = self.random_alpha_string(15)
                    if 'street_type' in row and row['street_type'] is not None:
                        gen_row['street_type'] = 'ST'
                    if 'street_direction' in row and row['street_direction'] is not None:
                        gen_row['street_direction'] = 'N'
                    if 'lock_box_no' in row and row['lock_box_no'] is not None:
                        gen_row['lock_box_no'] = self.random_numeric_string(3)
                    if 'installation_type' in row and row['installation_type'] is not None:
                        gen_row['installation_type'] = self.random_alpha_string(3)
                    if 'installation_name' in row and row['installation_name'] is not None:
                        gen_row['installation_name'] = self.random_alpha_string(10)
                    if 'installation_qualifier' in row and row['installation_qualifier'] is not None:
                        gen_row['installation_qualifier'] = self.random_alpha_string(3)
                    if 'route_service_type' in row and row['route_service_type'] is not None:
                        gen_row['route_service_type'] = self.random_alpha_string(3)
                    if 'route_service_no' in row and row['route_service_no'] is not None:
                        gen_row['route_service_no'] = self.random_numeric_string(3)

            insert_row_vals = []
            insert_values = ''
            i = 0
            for key in col_keys:
                insert_row_vals.append(row[key])
                if generate_individual_sql:
                    insert_values = insert_values + self.get_sql_col_value(gen_row[key], desc[i][1])
                    i = i + 1
                    if i < len(col_keys):
                        insert_values = insert_values + ', '
            inserts.append(insert_row_vals)
            if generate_individual_sql:
                insert_sqls.append('insert into ' + table + ' (' + insert_keys + ') values (' + insert_values + ')')
        insert_sql = 'insert into ' + table + ' (' + insert_keys + ') values (' + insert_placeholders + ')'

        if generate_individual_sql:
            self.generated_sqls.append(create_sql)
            for insert_sql in insert_sqls:
                self.generated_sqls.append(insert_sql)
        else:
            cache_cursor = None
            try:
                cache_cursor = self.cache.cursor()

                cache_cursor.execute(create_sql)
                if 0 < len(rows):
                    cache_cursor.executemany(insert_sql, inserts)

                cache_cursor.close()
                cache_cursor = None
            except (Exception) as error:
                print(error)
                print(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise 
            finally:
                if cache_cursor is not None:
                    cache_cursor.close()
                cache_cursor = None

    def get_cache_sql(self, sql):
        cursor = None
        try:
            cursor = self.cache.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            rows = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            return rows
        except (Exception) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None

    # run arbitrary sql's (create and insert) to populate in-mem cache
    # to be used to populate sample data for unit testing
    # sqls is an array of sql statements
    def insert_cache_sqls(self, sqls):
        for sql in sqls:
            self.insert_cache_sql(sql)

    # run arbitrary sql's (create and insert) to populate in-mem cache
    # to be used to populate sample data for unit testing
    # sql is an individual sql statement (string)
    def insert_cache_sql(self, sql):
        cursor = None
        try:
            cursor = self.cache.cursor()
            cursor.execute(sql)
            cursor.close()
            cursor = None
        except (Exception) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None

    # split up a List of id's into a List of Lists of no more than MAX id's
    def split_list(self, ids, max):
        ret = []
        sub_ids = []
        i = 0
        for id in ids:
            sub_ids.append(id)
            i = i + 1
            if i >= max:
                ret.append(sub_ids)
                sub_ids = []
                i = 0
        if 0 < len(sub_ids):
            ret.append(sub_ids)
        return ret

    # create a "where in" clasuse for a List of id's
    def id_where_in(self, ids, text=False):
        if text:
            delimiter = "'"
        else:
            delimiter = ''
        id_list = ''
        i = 0
        for the_id in ids:
            id_list = id_list + delimiter + the_id + delimiter
            i = i + 1
            if i < len(ids):
                id_list = id_list  + ', '
        return id_list


    ###########################################################################
    # load all bc registries data for the specified corps into our in-mem cache
    ###########################################################################

    code_tables =  ['corp_type', 
                    'corp_op_state', 
                    'party_type', 
                    'office_type', 
                    'event_type', 
                    'filing_type', 
                    'corp_name_type', 
                    'jurisdiction_type',
                    'xpro_type']
    corp_tables =  ['corporation', 
                    'corp_state', 
                    #'tilma_involved', - not currently used
                    'jurisdiction', 
                    'corp_name']
    other_tables = ['corp_party', 
                    'event', 
                    'filing',
                    'conv_event',
                    'office',
                    'address']

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corps(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            self.cache_bcreg_corp_tables(specific_corps, generate_individual_sql)
            self.cache_bcreg_code_tables(generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_corp_tables(self, specific_corps, generate_individual_sql=False):
        if self.use_local_cache():
            print('Caching data for parties and events ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            # ensure we have a unique list
            specific_corps = list({s_corp for s_corp in specific_corps})
            specific_corps_lists = self.split_list(specific_corps, MAX_WHERE_IN)

            addr_id_list = []
            for corp_nums_list in specific_corps_lists:
                corp_list = self.id_where_in(corp_nums_list, True)
                corp_party_where = 'bus_company_num in (' + corp_list + ') or corp_num in (' + corp_list + ')'
                party_rows = self.get_bcreg_table(self.other_tables[0], corp_party_where, '', True, generate_individual_sql)

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
                event_rows = self.get_bcreg_table(self.other_tables[1], event_where, '', True, generate_individual_sql)

                for event in event_rows:
                    event_ids.append(str(event['event_id']))

            # ensure we have a unique list
            event_ids = list({event_id for event_id in event_ids})
            event_ids_lists = self.split_list(event_ids, MAX_WHERE_IN)

            for ids_list in event_ids_lists:
                event_list = self.id_where_in(ids_list)
                filing_where = 'event_id in (' + event_list + ')'
                _rows = self.get_bcreg_table(self.other_tables[2], filing_where, '', True, generate_individual_sql)
                _rows = self.get_bcreg_table(self.other_tables[3], filing_where, '', True, generate_individual_sql)

            print('Caching data for corporations ...')
            for corp_nums_list in specific_corps_lists:
                corp_nums_list = self.id_where_in(corp_nums_list, True)
                corp_num_where = 'corp_num in (' + corp_nums_list + ')'
                for corp_table in self.corp_tables:
                    _rows = self.get_bcreg_table(corp_table, corp_num_where, '', True, generate_individual_sql)

                office_where = 'corp_num in (' + corp_nums_list + ')'
                office_rows = self.get_bcreg_table(self.other_tables[4], office_where, '', True, generate_individual_sql)

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
                _rows = self.get_bcreg_table(self.other_tables[5], address_where, '', True, generate_individual_sql)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_bcreg_code_tables(self, generate_individual_sql=False):
        if self.use_local_cache():
            print('Caching data for code tables ...')
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
    # utility methods to query bc registries data
    ###########################################################################

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes a WHERE clause and ORDER BY clause (must be valid SQL)
    def get_bcreg_sql(self, table, sql, cache=False, generate_individual_sql=False):
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
            if self.use_local_cache() and cache:
                self.cache_bcreg_data(table, desc, rows, generate_individual_sql)
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes a WHERE clause and ORDER BY clause (must be valid SQL)
    def get_bcreg_table(self, table, where="", orderby="", cache=False, generate_individual_sql=False):
        sql = "SELECT * FROM " + BC_REGISTRIES_TABLE_PREFIX + table
        if 0 < len(where):
            sql = sql + " WHERE " + where
        if 0 < len(orderby):
            sql = sql + " ORDER BY " + orderby
        return self.get_bcreg_sql(table, sql, cache, generate_individual_sql)

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes a WHERE clause and ORDER BY clause (must be valid SQL)
    def get_bcreg_corp_table(self, table, corp_num, where="", orderby="", cache=False, generate_individual_sql=False):
        subwhere = "corp_num = '" + corp_num + "'"
        if 0 < len(where):
            subwhere = subwhere + " AND " + where
        return self.get_bcreg_table(table, subwhere, orderby, cache, generate_individual_sql)


    ###########################################################################
    # methods to determine un-processed corporations/events
    ###########################################################################

    # get max event number from bc registries event log
    def get_max_event(self, event_date):
        cur = None
        try:
            # create a cursor
            cur = self.conn.cursor()
            cur.execute("""SELECT max(event_id) FROM """ + BC_REGISTRIES_TABLE_PREFIX + """event where event_timestmp = %s""", (event_date,))
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
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
            cur.execute("""SELECT max(event_timestmp) FROM """ + BC_REGISTRIES_TABLE_PREFIX + """event""")
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
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
            cur.execute("""SELECT event_timestmp FROM """ + BC_REGISTRIES_TABLE_PREFIX + """event where event_id = %s""", (event_id,))
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise
        finally:
            if cur is not None:
                cur.close()

    # return a specific set of corporations, based on an event range
    def get_specific_corps(self, corp_filter):
        sql = """SELECT distinct(corp_num) from """ + BC_REGISTRIES_TABLE_PREFIX + """event
                where corp_num in ({})
                order by corp_num;"""
        sql2 = """SELECT distinct(corp.corp_num) from """ + BC_REGISTRIES_TABLE_PREFIX + """corporation corp,
                            """ + BC_REGISTRIES_TABLE_PREFIX + """corp_party party
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
                # print(row)
                corps.append({'CORP_NUM':row[0],})
                row = cur.fetchone()

            sql2 = sql2.format(placeholders)
            cur.execute(sql2, tuple(corp_filter))
            row = cur.fetchone()
            while row is not None:
                # print(row)
                corps.append({'CORP_NUM':row[0],})
                row = cur.fetchone()

            cur.close()
            cur = None
            return corps
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
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
        sqls.append("""SELECT distinct(corp.corp_num) from """ + BC_REGISTRIES_TABLE_PREFIX + """corporation corp """)

        corps = []
        for sql in sqls:
            cur = None
            try:
                print("Executing: " + sql)
                cur = self.conn.cursor()
                cur.execute(sql)
                row = cur.fetchone()
                while row is not None:
                    # print(row)
                    corps.append({'CORP_NUM':row[0], 'PREV_EVENT': event_dict(last_event_id, last_event_dt), 
                                                     'LAST_EVENT': event_dict(max_event_id, max_event_dt), })
                    row = cur.fetchone()
                cur.close()
                cur = None
                print("Loaded corps: " + str(len(corps)))
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()
        return corps

    # return unprocessed corporations, based on an event range
    def get_unprocessed_corps(self, last_event_id, last_event_dt, max_event_id, max_event_dt):
        sqls = []

        # select *all* corps - we will filter in the next stage
        sqls.append("""SELECT corp_num, event_id from """ + BC_REGISTRIES_TABLE_PREFIX + """event
                        where event_timestmp >= %s""")

        corps = []
        event_ids = []
        corp_set = {}
        for sql in sqls:
            cur = None
            try:
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
                print("Loaded corps: " + str(len(corps)))
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()

        # since the event may affect more than one corp, check corp_state to see if there are any other corps to bring into scope
        sql = """SELECT corp_num from """ + BC_REGISTRIES_TABLE_PREFIX + """corp_state
                where start_event_id = %s or end_event_id = %s"""
        for event_id in event_ids:
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
                print(error)
                print(traceback.print_exc())
                log_error("BCRegistries exception reading DB: " + str(error))
                raise
            finally:
                if cur is not None:
                    cur.close()
        print("Loaded corps: " + str(len(corps)))

        return corps

    #return the (unprocessed) event range for each provided corporation
    def get_unprocessed_corp_events(self, last_event_id, last_event_dt, max_event_id, max_event_dt, corps, max=None):
        for i,corp in enumerate(corps): 
            if (i % 100 == 0) or (i+1 == len(corps)):
                print('>>> Processing {} of {} corporations.'.format(i+1, len(corps)))
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

    # get the corporation's current state
    def get_adhoc_query(self, sql):
        cursor = None
        try:
            cursor = self.get_db_connection().cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            recs = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            return recs
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

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
            print('Error ret_date is None', event)

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
                    FROM """ + self.get_table_prefix(force_query_remote) + """event, """ + self.get_table_prefix(force_query_remote) + """event_type
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
            print(error)
            print(traceback.print_exc())
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
            #   print('Cache miss for conv_event ', event_type)
            #    conv_event = self.get_conv_event(corp_num, event_id, event_type, True)
            #    self.add_cache_miss('conv_event', corp_num, event_id, conv_event)
            #    return conv_event
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_filing_event(self, corp_num, event_id, event_type, force_query_remote=False):
        if event_type != 'FILE':
            return {}
        sql_filing = """SELECT event_id, filing.filing_typ_cd, effective_dt, new_corp_num, filing_typ_class, short_desc, full_desc 
                        from """ + self.get_table_prefix(force_query_remote) + """filing, """ + self.get_table_prefix(force_query_remote) + """filing_type 
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
            print(error)
            print(traceback.print_exc())
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
            print(">>>Data Issue:Same Start Date:" + corp_num + ":" + record_type + ":", records)
        if active_id is not None and active_id != len(sorted_records):
            print(">>>Data Issue:Active Record:" + corp_num + ":" + record_type + ":", records)

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
                #    print(">>>Data Issue:Date:" + corp_num + ":Office:", office)

            #self.check_same_start_date(corp_num, 'office', offices, 'effective_start_date')
            return offices
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
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
            print(error)
            print(traceback.print_exc())
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
                    #print(">>>Data Issue:Date:" + corp_num + ":Corp_Name:", corp_name)
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
            print(error)
            print(traceback.print_exc())
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
            print(error)
            print(traceback.print_exc())
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
                    #    print(">>>Data Issue:Date:" + corp_num + ":Jurisdiction:", jurisdiction)
                #self.check_same_start_date(corp_num, 'jurisdiction', jurisdictions, 'effective_start_date')
                jurisdictions = sorted(jurisdictions, key=lambda k: k['effective_end_date'])
                jurisdictions = sorted(jurisdictions, key=lambda k: int(k['start_event_id']))
                jurisdictions = sorted(jurisdictions, key=lambda k: k['effective_start_date'])
                return jurisdictions
            return []
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
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
            print(error)
            print(traceback.print_exc())
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
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def addr_line(self, addr_element, delimiter):
        if addr_element is not None:
            return addr_element + delimiter
        return ''

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
                # TODO maybe check BC Reg database if the corp is not in the cache?
                print("No corp rec found for ", corp_num)
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
         
                if deep_copy:
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
                        #    print(">>>Data Issue:Date:" + corp_num + ":Corp_State:", corp_state)
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
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading corp info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()


    ###########################################################################
    # primary method to load all bc registries data for the specified corporation
    ###########################################################################

    def get_bc_reg_corp_info(self, corp_num):
        sql_party = """SELECT corp_num, corp_party_id, mailing_addr_id, delivery_addr_id, party_typ_cd, start_event_id, end_event_id, cessation_dt,
                         last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt,
                         phone, reason_typ_cd
                      FROM """ + self.get_table_prefix() + """corp_party
                      WHERE (corp_num = """ + self.get_db_sql_param() + """ OR bus_company_num = """ + self.get_db_sql_param() + """)
                        AND party_typ_cd = 'FBO'"""

        cur = None
        try:
            corp = self.get_basic_corp_info(corp_num)
            corp_type = corp['corp_typ_cd']

            # get parties
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
                    if corp_party['bus_company_num'] is not None:
                        corp_party['corp_info'] = self.get_basic_corp_info(corp_party['bus_company_num'], False)
                else:
                    corp_party['corp_info'] = self.get_basic_corp_info(corp_party['corp_num'], False)

                corp['parties'].append(corp_party)
                row = cur.fetchone()
            cur.close()
            cur = None

            return corp
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print(traceback.print_exc())
            log_error("BCRegistries exception reading corp party info from DB: " + str(error))
            raise 
        finally:
            if cur is not None:
                cur.close()

    # convert object to JSON, converting data types (decimal, date) to string
    def to_json(self, data):
        ret = json.dumps(data, cls=CustomJsonEncoder)
        return ret

