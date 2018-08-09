#!/usr/bin/python
import os
import psycopg2
import datetime
import json
from jsonbender import bend, K, F, S, Filter, Reduce, Forall
from jsonbender.list_ops import ForallBend, FlatForall
from jsonbender.control_flow import Alternation, If, Switch
import ast
from bcreg.config import config

system_type = 'BC_REG'


def dumpfile(path, filename, data):
    #print(path + path)
    if not os.path.exists(path):
        os.makedirs(path)    
    text_file = open(path + filename, "w")
    text_file.write(json.dumps(data, indent=4))
    text_file.close()


def dump_corp_history_queue(path):
    sql = """SELECT RECORD_ID, SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_JSON, ENTRY_DATE
             FROM CORP_HISTORY_LOG"""

    """ Connect to the PostgreSQL database server """
    conn = None
    cur = None
    try:
        # read connection parameters
        params = config(section='event_processor')
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        corps = []
        while row is not None:
            # print(row)
            corps.append({'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'PREV_EVENT_ID':row[2], 'LAST_EVENT_ID':row[3], 'CORP_NUM':row[4], 
                        'CORP_JSON':row[5], 'ENTRY_DATE':row[6]})
            row = cur.fetchone()

        cur.close()
        cur = None

        for i,corp in enumerate(corps): 
            print(corp)
            filename = corp['CORP_NUM'] + '.json'
            dumpfile(path, filename, corp['CORP_JSON'])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            print('Cursor closed.')
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def dump_corp_credential_queue(path):
    sql = """SELECT RECORD_ID, SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CREDENTIAL_TYPE_CD, 
                SCHEMA_NAME, SCHEMA_VERSION, CREDENTIAL_JSON, ENTRY_DATE
              FROM CREDENTIAL_LOG"""

    """ Connect to the PostgreSQL database server """
    conn = None
    cur = None
    try:
        # read connection parameters
        params = config(section='event_processor')
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        creds = []
        while row is not None:
            # print(row)
            creds.append({'RECORD_ID':row[0], 'SYSTEM_TYPE_CD':row[1], 'PREV_EVENT_ID':row[2], 'LAST_EVENT_ID':row[3], 'CORP_NUM':row[4], 
                        'CREDENTIAL_TYPE_CD':row[5], 'SCHEMA_NAME':row[6], 'SCHEMA_VERSION':row[7], 'CREDENTIAL_JSON':row[8], 'ENTRY_DATE':row[9]})
            row = cur.fetchone()

        cur.close()
        cur = None

        for i,cred in enumerate(creds): 
            filename = cred['CORP_NUM'] + '.' + str(cred['RECORD_ID']) + '.' + cred['SCHEMA_NAME'] + '.' + cred['SCHEMA_VERSION'] + '.json'
            dumpfile(path, filename, cred['CREDENTIAL_JSON'])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            print('Cursor closed.')
        if conn is not None:
            conn.close()
            print('Database connection closed.')


dump_corp_history_queue('../bcreg-x/testdata/corps/')
dump_corp_credential_queue('../bcreg-x/testdata/creds/')

