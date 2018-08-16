#!/usr/bin/env python3
#
# Copyright 2017-2018 Government of Canada
# Public Services and Procurement Canada - buyandsell.gc.ca
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import psycopg2
import asyncio
import datetime
import json
import os
import sys
import aiohttp
from bcreg.config import config

AGENT_URL = os.environ.get('VONX_API_URL', 'http://localhost:5000/bcreg')

CREDS_BATCH_SIZE = 500


async def submit_cred(http_client, attrs, schema, version):
    #print(attrs)

    try:
        response = await http_client.post(
            '{}/issue-credential'.format(AGENT_URL),
            params={'schema': schema, 'version': version},
            json=attrs
        )
        if response.status != 200:
            raise RuntimeError(
                'Credential could not be processed: {}'.format(await response.text())
            )
        result_json = await response.json()
        print('Response from von-x:\n{}\n'.format(result_json))
        return result_json
    except Exception as exc:
        print(exc)
        raise
        # raise RuntimeError('Could not submit credential. Are von-x and TheOrgBook running?') from exc


async def process_credential_queue(http_client):
    sql1 = """SELECT RECORD_ID, SYSTEM_TYPE_CD, PREV_EVENT_ID, LAST_EVENT_ID, CORP_NUM, CREDENTIAL_TYPE_CD, 
                    CREDENTIAL_JSON, SCHEMA_NAME, SCHEMA_VERSION, ENTRY_DATE
              FROM CREDENTIAL_LOG 
              WHERE PROCESS_DATE is null
              LIMIT """ + str(CREDS_BATCH_SIZE)

    sql1a = """SELECT count(*) cnt
              FROM CREDENTIAL_LOG 
              WHERE PROCESS_DATE is null"""

    sql2 = """UPDATE CREDENTIAL_LOG
              SET PROCESS_DATE = %s, PROCESS_SUCCESS = 'Y'
              WHERE RECORD_ID = %s"""

    sql3 = """UPDATE CREDENTIAL_LOG
              SET PROCESS_DATE = %s, PROCESS_SUCCESS = 'N', PROCESS_MSG = %s
              WHERE RECORD_ID = %s"""

    """ Connect to the PostgreSQL database server """
    conn = None
    cur = None
    cur2 = None
    try:
        params = config(section='event_processor')
        conn = psycopg2.connect(**params)

        # create a cursor
        cred_count = 0
        cur = conn.cursor()
        cur.execute(sql1a)
        row = cur.fetchone()
        if row is not None:
            cred_count = row[0]
        cur.close()
        cur = None

        i = 0
        cred_count_remaining = cred_count

        while 0 < cred_count_remaining:
            # create a cursor
            cur = conn.cursor()
            cur.execute(sql1)
            row = cur.fetchone()
            while row is not None:
                i = i + 1
                print('>>> Processing {} of {} credentials.'.format(i, cred_count))
                credential = {'RECORD_ID':row[0], 'SYSTEM_TYP_CD':row[1], 'PREV_EVENT_ID':row[2], 'LAST_EVENT_ID':row[3], 'CORP_NUM':row[4], 
                              'CREDENTIAL_TYPE_CD':row[5], 'CREDENTIAL_JSON':row[6], 'SCHEMA_NAME':row[7], 'SCHEMA_VERSION':row[8], 'ENTRY_DATE':row[9]}
                
                # post credential
                try:
                    result_json = await submit_cred(http_client, credential['CREDENTIAL_JSON'], credential['SCHEMA_NAME'], credential['SCHEMA_VERSION'])

                    result = result_json # json.loads(result_json)[0]
                    if result['success']:
                        #print("log success to database")
                        cur2 = conn.cursor()
                        cur2.execute(sql2, (datetime.datetime.now(), credential['RECORD_ID'],))
                        conn.commit()
                        cur2.close()
                        cur2 = None
                    else:
                        #print("log error to database")
                        cur2 = conn.cursor()
                        if 255 < len(result['result']):
                            res = result['result'][:250] + '...'
                        else:
                            res = result['result']
                        cur2.execute(sql3, (datetime.datetime.now(), res, credential['RECORD_ID'],))
                        conn.commit()
                        cur2.close()
                        cur2 = None

                except (Exception) as error:
                    #print("log exception to database")
                    cur2 = conn.cursor()
                    cur2.execute(sql3, (datetime.datetime.now(), str(error), credential['RECORD_ID'],))
                    conn.commit()
                    cur2.close()
                    cur2 = None

                row = cur.fetchone()

            cur.close()
            cur = None

            cur = conn.cursor()
            cur.execute(sql1a)
            row = cur.fetchone()
            if row is not None:
                cred_count_remaining = row[0]
            cur.close()
            cur = None
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if cur2 is not None:
            cur2.close()
        if conn is not None:
            conn.commit()
            conn.close()

async def submit_all():
    async with aiohttp.ClientSession() as http_client:
        await process_credential_queue(http_client)

asyncio.get_event_loop().run_until_complete(submit_all())
