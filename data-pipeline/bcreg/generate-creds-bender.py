#!/usr/bin/python
import psycopg2
import datetime
import json
from jsonbender import bend, K, F, S, Filter, Reduce, Forall
from jsonbender.list_ops import ForallBend, FlatForall
from jsonbender.control_flow import Alternation, If, Switch
import ast
from bcreg.config import config

system_type = 'BC_REG'


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


def load_json_mappers(system_typ_cd):
    # load mappers for each credential type
    sql = """SELECT RECORD_ID, SYSTEM_TYPE_CD, CREDENTIAL_TYPE_CD, MAPPING_TRANSFORM, SCHEMA_NAME, SCHEMA_VERSION
             FROM CREDENTIAL_TRANSFORM
             WHERE SYSTEM_TYPE_CD = %s"""

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
        cur.execute(sql, (system_typ_cd,))
        row = cur.fetchone()
        transforms = []
        while row is not None:
            # print(row)
            transforms.append({'SYSTEM_TYPE_CD':row[1], 'CREDENTIAL_TYPE_CD':row[2], 'MAPPING_TRANSFORM':row[3],
                                'SCHEMA_NAME':row[4], 'SCHEMA_VERSION':row[5]})
            row = cur.fetchone()

        cur.close()
        cur = None

        return transforms

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            print('Cursor closed.')
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def get_corp_credentials(corp_num, corp_json, creds_mapper):
    print("Mapping ...")
    creds_json = bend(eval(creds_mapper), corp_json)
    print(json.dumps(creds_json))
    return creds_json

def process_corp_history_queue(transforms):
    sql = """SELECT RECORD_ID, SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CORP_JSON, ENTRY_DATE
             FROM CORP_HISTORY_LOG
             WHERE PROCESS_DATE is null"""

    sql2 = """INSERT INTO CREDENTIAL_LOG (SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CREDENTIAL_TYPE_CD, 
                SCHEMA_NAME, SCHEMA_VERSION, CREDENTIAL_JSON, ENTRY_DATE)
              VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING RECORD_ID;"""

    sql3 = """UPDATE CORP_HISTORY_LOG
              SET PROCESS_DATE = %s
              WHERE RECORD_ID = %s"""

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

            for j,transform in enumerate(transforms):
                corp_creds = get_corp_credentials(corp['CORP_NUM'], corp['CORP_JSON'], transform['MAPPING_TRANSFORM'])
                print(corp_creds)

                # create row(s) for corp creds json info
                cur = conn.cursor()
                cur.execute(sql2, (corp['SYSTEM_TYPE_CD'], corp['PREV_EVENT_ID'], corp['LAST_EVENT_ID'], corp['CORP_NUM'], transform['CREDENTIAL_TYPE_CD'], 
                            transform['SCHEMA_NAME'], transform['SCHEMA_VERSION'], json.dumps(corp_creds, cls=DateTimeEncoder), datetime.datetime.now(),))
                cur.close()
                cur = None

            # update process date
            cur = conn.cursor()
            cur.execute(sql3, (datetime.datetime.now(), corp['RECORD_ID'], ))
            cur.close()
            cur = None

            # commit the changes to the database
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            print('Cursor closed.')
        if conn is not None:
            conn.close()
            print('Database connection closed.')


#with EventProcessor() as event_processor:
transforms = load_json_mappers(system_type)
process_corp_history_queue(transforms)


