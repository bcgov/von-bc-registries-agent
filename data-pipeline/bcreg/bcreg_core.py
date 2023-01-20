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

from bcreg.config import config
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


INMEM_CACHE_TABLE_PREFIX = 'x_'
INMEM_CACHE_SEC_TABLE_PREFIX = 'x_sec_'
MAX_WHERE_IN = 1000

COLIN_SYSTEM_TYPE = 'BC_REG'
LEAR_SYSTEM_TYPE = 'BCREG_LEAR'

LOGGER = logging.getLogger(__name__)


def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return decimal.Decimal(s)


class BCReg_Core:
    sql_local_cache = False
    cache_miss = []
    generated_sqls = []
    generated_corp_nums = {}
    source_system_type = None

    DB_TABLE_PREFIX = ""
    PG_DATABASE_NAME = ""
    SEC_DB_TABLE_PREFIX = ""
    SEC_PG_DATABASE_NAME = ""

    conn = None


    def __init__(self, cache=False):
        try:
            params = config(section=self.PG_DATABASE_NAME)
            self.conn = psycopg2.connect(**params)
            self.conn.set_session(readonly=True)
            self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)

            # Register the adapter
            sqlite3.register_adapter(decimal.Decimal, adapt_decimal)
            # Register the converter
            sqlite3.register_converter("decimal", convert_decimal)
            # connect to in-memory database
            self.cache = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

            # connect secondary datasource
            secondary_params = config(section=self.SEC_PG_DATABASE_NAME)
            self.sec_conn = psycopg2.connect(**secondary_params)
            self.sec_conn.set_session(readonly=True)
            self.sec_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
        except (Exception) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            self.conn = None
            self.cache = None
            self.sec_conn = None
            log_error("BCRegistries exception connecting to DB: " + str(error))
            raise

    def __del__(self):
        if self.conn:
            self.conn.close()
        if self.cache:
            self.cache.close()
        if self.sec_conn:
            self.sec_conn.close()

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

    def get_sec_db_connection(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return self.cache
        else:
            return self.sec_conn

    def get_db_sql_param(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return '?'
        else:
            return '%s'

    def get_table_prefix(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return INMEM_CACHE_TABLE_PREFIX
        else:
            return self.DB_TABLE_PREFIX

    def get_sec_table_prefix(self, force_query_remote=False):
        if self.use_local_cache() and (not force_query_remote):
            return INMEM_CACHE_SEC_TABLE_PREFIX
        else:
            return self.SEC_DB_TABLE_PREFIX

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
    def get_bcreg_table_struct(self, table, where="", use_sec=False):
        pfx = self.SEC_DB_TABLE_PREFIX if use_sec else self.DB_TABLE_PREFIX
        sql = "SELECT * from " + pfx + table
        if 0 < len(where):
            sql = sql + " WHERE " + where
        # print(">>> caching data with:", sql)
        cursor = None
        try:
            if use_sec:
                cursor = self.sec_conn.cursor()
            else:
                cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            cursor.close()
            cursor = None
            return desc
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None

    # return a sql to create an in-mem sqlite table
    def create_table_sql(self, table, table_desc, use_sec=False):
        pfx = INMEM_CACHE_SEC_TABLE_PREFIX if use_sec else INMEM_CACHE_TABLE_PREFIX
        table_sql = 'create table if not exists ' + pfx + table + ' ('
        i = 0
        for col in table_desc:
            col_name = col[0]
            col_type = self.get_sql_col_type(col[1], use_sec=use_sec)
            _col_len = col[3]
            table_sql = table_sql + col_name + ' ' + col_type 
            i = i + 1
            if i < len(table_desc):
                table_sql = table_sql + ', '
            else:
                table_sql = table_sql + ')'
        return table_sql

    def get_sql_col_type(self, pg_type, use_sec=False):
        if pg_type == 1042:  # CHAR
            return 'text'  
        if pg_type == 1043:  # VARCHAR
            return 'text'
        if pg_type == 1700:  # NUMBER(38)
            return 'numeric'
        if pg_type == 23 or pg_type == 21 or pg_type == 20:    # INT*
            return 'integer'
        if pg_type == 1114 or pg_type == 1184:  # DATE or DATETIME (or TZ)
            if self.source_system_type == LEAR_SYSTEM_TYPE or (self.source_system_type == COLIN_SYSTEM_TYPE and use_sec):
                return 'text'
            else:
                return 'timestamp'
        if pg_type == 114 or pg_type == 3802:  # json or jsonb
            return 'text'
        # default for now
        return 'text'

    def stringify(self, s_val):
        if "'" in s_val:
            s_val = s_val.replace("'", "''")
        return str(s_val)

    def get_sql_insert_value(self, col_value, pg_type):
        if pg_type == 114 or pg_type == 3802:  # json or jsonb
            return json.dumps(col_value)
        return col_value

    def get_sql_col_value(self, col_value, pg_type):
        if col_value is None:
            return 'null'
        if pg_type == 1042:  # CHAR
            return "'" + self.stringify(col_value) + "'"  
        if pg_type == 1043:  # VARCHAR
            return "'" + self.stringify(col_value) + "'"  
        if pg_type == 1700:  # NUMBER(38)
            return str(col_value)
        if pg_type == 23 or pg_type == 21 or pg_type == 20:    # INT*
            return str(col_value)
        if pg_type == 1114 or pg_type == 1184:  # DATE or DATETIME (or TZ)
            return "'" + str(col_value) + "'"
        if pg_type == 114 or pg_type == 3802:  # json or jsonb
            return "'" + json.dumps(col_value) + "'"
        # default for now
        return "'" + str(col_value) + "'"

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
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
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
    def cache_bcreg_data(self, table, desc, rows, generate_individual_sql=False, use_sec=False):
        pfx = INMEM_CACHE_SEC_TABLE_PREFIX if use_sec else INMEM_CACHE_TABLE_PREFIX
        create_sql = self.create_table_sql(table, desc, use_sec=use_sec)
        # print("Creating cache table:", create_sql)
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
                insert_row_vals.append(self.get_sql_insert_value(row[key], desc[i][1]))
                if generate_individual_sql:
                    insert_values = insert_values + self.get_sql_col_value(gen_row[key], desc[i][1])
                i = i + 1
                if generate_individual_sql and i < len(col_keys):
                    insert_values = insert_values + ', '
            inserts.append(insert_row_vals)
            if generate_individual_sql:
                insert_sqls.append('insert into ' + pfx + table + ' (' + insert_keys + ') values (' + insert_values + ')')
        insert_sql = 'insert into ' + pfx + table + ' (' + insert_keys + ') values (' + insert_placeholders + ')'
        # print("Inserting in cache:", insert_sql)
        # print("                  :", inserts)

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
                LOGGER.error(error)
                LOGGER.error(traceback.print_exc())
                log_error("BCRegistries exception loading table: " + table)
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
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
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
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
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
            id_list = id_list + delimiter + str(the_id) + delimiter
            i = i + 1
            if i < len(ids):
                id_list = id_list  + ', '
        return id_list


    ###########################################################################
    # utility methods to query bc registries data
    ###########################################################################

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes a WHERE clause and ORDER BY clause (must be valid SQL)
    def get_bcreg_sql(self, table, sql, cache=False, generate_individual_sql=False, use_sec=False):
        cursor = None
        try:
            if use_sec:
                cursor = self.sec_conn.cursor()
            else:
                cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            rows = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if self.use_local_cache() and cache:
                self.cache_bcreg_data(table, desc, rows, generate_individual_sql, use_sec=use_sec)
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()
            cursor = None

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes a WHERE clause and ORDER BY clause (must be valid SQL)
    def get_bcreg_table(self, table, where="", orderby="", cache=False, generate_individual_sql=False, use_sec=False):
        pfx = self.SEC_DB_TABLE_PREFIX if use_sec else self.DB_TABLE_PREFIX
        sql = "SELECT * FROM " + pfx + table
        if 0 < len(where):
            sql = sql + " WHERE " + where
        if 0 < len(orderby):
            sql = sql + " ORDER BY " + orderby
        # print(">>> caching data with:", sql)
        return self.get_bcreg_sql(table, sql, cache, generate_individual_sql, use_sec=use_sec)

    # get all records and return in an array of dicts
    # returns a zero-length array if none found
    # optionally takes a WHERE clause and ORDER BY clause (must be valid SQL)
    def get_bcreg_corp_table(self, table, corp_num, where="", orderby="", cache=False, generate_individual_sql=False, use_sec=False):
        subwhere = "corp_num = '" + corp_num + "'"
        if 0 < len(where):
            subwhere = subwhere + " AND " + where
        return self.get_bcreg_table(table, subwhere, orderby, cache, generate_individual_sql, use_sec=use_sec)


    ###########################################################################
    # methods to run corporation-specific queries 
    # (can run against the in-memory cache 
    #  or against bc registries database directly)
    ###########################################################################

    # get the corporation's current state
    def get_adhoc_query(self, sql, use_sec=False):
        cursor = None
        try:
            if use_sec:
                cursor = self.get_sec_db_connection().cursor()
            else:
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
            LOGGER.error(error)
            LOGGER.error(traceback.print_exc())
            log_error("BCRegistries exception reading DB: " + str(error))
            raise 
        finally:
            if cursor is not None:
                cursor.close()


    ###########################################################################
    # some LEAR-specific queries
    ###########################################################################

    # load everything:
    lear_code_tables =  ['corp_types']
    # load by identifier (was corp_num)
    lear_corp_tables =  ['businesses',
                    'businesses_version']
    # load by business_id (id on businesses_version table)
    lear_other_tables = ['filings',
                    'aliases',
                    'aliases_version',
                    'party_roles',
                    'party_roles_version']
    # custom load
    lear_other_other_tables = ['parties',
                          'parties_version',]
    lear_other_other_other_tables = ['transaction',]

    # in colin if the corp_num is numeric we pre-pend 'BC' to it
    def bc_ifiy(self, specific_corps):
        corp_nums = []
        for corp_num in specific_corps:
            try:
                i = int(corp_num)
                corp_nums.append('BC' + corp_num)
            except:
                corp_nums.append(corp_num)
        return corp_nums

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_lear_bcreg_corps(self, specific_corps, generate_individual_sql=False, use_sec=False):
        if self.use_local_cache():
            self.cache_lear_bcreg_corp_tables(specific_corps, generate_individual_sql=generate_individual_sql, use_sec=use_sec)
            self.cache_lear_bcreg_code_tables(generate_individual_sql=generate_individual_sql, use_sec=use_sec)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_lear_bcreg_corp_tables(self, specific_corps, generate_individual_sql=False, use_sec=False):
        if self.use_local_cache():
            # ensure we have a unique list
            specific_corps = list({s_corp for s_corp in specific_corps})
            specific_corps = self.bc_ifiy(specific_corps)
            specific_corps_lists = self.split_list(specific_corps, MAX_WHERE_IN)

            LOGGER.info('Caching data for parties and events ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            LOGGER.info('Caching data for corporations ...')
            for corp_nums_list in specific_corps_lists:
                bus_ids_list = []
                txn_ids_list = []
                corp_nums_list_str = self.id_where_in(corp_nums_list, True)
                corp_num_where = 'identifier in (' + corp_nums_list_str + ')' if 0 < len(corp_nums_list_str) else "identifier = ''"
                corp_num_where_ex = corp_num_where + " or id in (select business_id from party_roles, parties where party_roles.party_id = parties.id and parties." + corp_num_where + ")"
                for corp_table in self.lear_corp_tables:
                    _rows = self.get_bcreg_table(corp_table, corp_num_where_ex, '', True, generate_individual_sql, use_sec=use_sec)
                    if corp_table == 'businesses':
                        for _row in _rows:
                            bus_ids_list.append(_row['id'])
                    elif corp_table == 'businesses_version':
                        for _row in _rows:
                            if _row['transaction_id'] is not None:
                                txn_ids_list.append(_row['transaction_id'])

                party_ids_list = []
                bus_id_where = 'business_id in (' + self.id_where_in(bus_ids_list, True) + ')' if 0 < len(bus_ids_list) else "business_id = 0"
                bus_id_where += " or business_id in (select business_id from party_roles, parties where party_roles.party_id = parties.id and parties." + corp_num_where + ")"
                for other_table in self.lear_other_tables:
                    _rows = self.get_bcreg_table(other_table, bus_id_where, '', True, generate_individual_sql, use_sec=use_sec)
                    if other_table == 'party_roles':
                        for _row in _rows:
                            if _row['party_id'] is not None:
                                party_ids_list.append(_row['party_id'])
                    elif other_table == 'filings':
                        for _row in _rows:
                            if _row['transaction_id'] is not None:
                                txn_ids_list.append(_row['transaction_id'])

                additional_identifiers = []
                party_id_where = 'id in (' + self.id_where_in(party_ids_list, True) + ')' if 0 < len(party_ids_list) else "id = 0"
                party_id_where += " or identifier in (" + self.id_where_in(corp_nums_list, True) + ")"
                for other_table in self.lear_other_other_tables:
                    _rows = self.get_bcreg_table(other_table, party_id_where, '', True, generate_individual_sql, use_sec=use_sec)
                    if other_table == 'parties':
                        for _row in _rows:
                            if _row['identifier'] is not None and 0 < len(_row['identifier']):
                                additional_identifiers.append(_row['identifier'])
                if 0 < len(additional_identifiers):
                    corp_nums_list_str = self.id_where_in(additional_identifiers, True)
                    corp_num_where = 'identifier in (' + corp_nums_list_str + ')'
                    for corp_table in self.lear_corp_tables:
                        _rows = self.get_bcreg_table(corp_table, corp_num_where, '', True, generate_individual_sql, use_sec=use_sec)

                txn_id_where = 'id in (' + self.id_where_in(txn_ids_list, True) + ')' if 0 < len(txn_ids_list) else "id = 0"
                for other_table in self.lear_other_other_other_tables:
                    _rows = self.get_bcreg_table(other_table, txn_id_where, '', True, generate_individual_sql, use_sec=use_sec)

    # load all bc registries data for the specified corps into our in-mem cache
    def cache_lear_bcreg_code_tables(self, generate_individual_sql=False, use_sec=False):
        if self.use_local_cache():
            LOGGER.info('Caching data for code tables ...')
            self.generated_sqls = []
            self.generated_corp_nums = {}
            for code_table in self.lear_code_tables:
                _rows = self.get_bcreg_table(code_table, '', '', True, generate_individual_sql, use_sec=use_sec)

