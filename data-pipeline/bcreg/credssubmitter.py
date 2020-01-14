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
import multiprocessing.pool as mpool
import datetime
import json
import os
import sys
import aiohttp
import time
import traceback
from bcreg.config import config
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

AGENT_URL = os.environ.get('CONTROLLER_URL', 'http://localhost:5002')
NOTIFY_OF_CREDENTIAL_POSTING_ERRORS = os.environ.get('NOTIFY_OF_CREDENTIAL_POSTING_ERRORS', 'false')

CREDS_BATCH_SIZE = int(os.getenv('CREDS_BATCH_SIZE', '3000'))
CREDS_REQUEST_SIZE = int(os.getenv('CREDS_REQUEST_SIZE', '5'))
MAX_CREDS_REQUESTS = int(os.getenv('MAX_CREDS_REQUESTS', '32'))
# max time to process (minutes)
MAX_PROCESSING_MINS = int(os.getenv('MAX_PROCESSING_MINS', '10'))
# how often to report status (# credentials)
PROCESS_LOOP_REPORT_CT = int(os.getenv('PROCESS_LOOP_REPORT_CT', '100'))

MAX_CORPS = 10000
CRAZY_MAX_CORPS = 100000


def notify_error(message):
    # Use NOTIFY_OF_CREDENTIAL_POSTING_ERRORS to turn error notification on(true)/off(false); off by default.
    # It's recommended to have this off during bulk data loads as errors in these situations
    # can cause an unnecessary flood of notifications.
    # Turn this on during normal agent oppertion.
    if NOTIFY_OF_CREDENTIAL_POSTING_ERRORS and NOTIFY_OF_CREDENTIAL_POSTING_ERRORS.lower() == 'true':
        log_error(message)


async def submit_cred_batch(http_client, creds):
    try:
        #print("Posting to:", '{}/issue-credential'.format(AGENT_URL))
        response = await http_client.post(
            '{}/issue-credential'.format(AGENT_URL),
            json=creds
        )
        if response.status != 200:
            raise RuntimeError(
                'Credentials could not be processed: {}'.format(await response.text())
            )
        result_json = await response.json()
        #print('Response from von-x:\n{}\n'.format(result_json))
        return result_json
    except Exception as exc:
        print(exc)
        raise

async def submit_cred(http_client, attrs, schema, version):
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
        #print('Response from von-x:\n{}\n'.format(result_json))
        return result_json
    except Exception as exc:
        print(exc)
        raise 

# add reason code to the submitted credential
def inject_reason(attributes, reason):
  attributes['reason_description'] = reason
  return attributes

async def post_credentials(http_client, conn, credentials):
    sql2 = """UPDATE CREDENTIAL_LOG
              SET PROCESS_DATE = %s, PROCESS_SUCCESS = 'Y', PROCESS_MSG = %s
              WHERE RECORD_ID = %s"""

    sql3 = """UPDATE CREDENTIAL_LOG
              SET PROCESS_DATE = %s, PROCESS_SUCCESS = 'N', PROCESS_MSG = %s
              WHERE RECORD_ID = %s"""

    success = 0
    failed = 0
    post_creds = []
    for credential in credentials:
      # need to inject reason into this process
      #if credential['CREDENTIAL_REASON'] is not None and 0 < len(credential['CREDENTIAL_REASON']):
      credential['CREDENTIAL_JSON'] = inject_reason(credential['CREDENTIAL_JSON'], credential['CREDENTIAL_REASON'])
      post_creds.append({"schema":credential['SCHEMA_NAME'], "version":credential['SCHEMA_VERSION'], "attributes":credential['CREDENTIAL_JSON']})

    # post credential
    #print('Post credential ...')
    cur2 = None
    try:
        #print('=============')
        #print(post_creds)
        #print('=============')
        # old code for submitting one credential at a time
        # result_json = await submit_cred(http_client, credential['CREDENTIAL_JSON'], credential['SCHEMA_NAME'], credential['SCHEMA_VERSION'])
        results = None
        results = await submit_cred_batch(http_client, post_creds)

        #print("Posted = ", len(credentials), ", results = ", len(results))
    except (Exception) as error:
        # everything failed :-(
        print("log exception to database:", str(error))
        print(error)
        res = str(error)
        if 0 == len(res):
            res = "Unspecified error posting to OrgBook"
        elif 255 < len(res):
            res = res[:250] + '...'
        if cur2 is not None:
            cur2.close()
            cur2 = None
        cur2 = conn.cursor()
        for i in range(len(credentials)):
            credential = credentials[i]
            cur2.execute(sql3, (datetime.datetime.now(), res, credential['RECORD_ID'],))
            failed = failed + 1
        conn.commit()
        cur2.close()
        cur2 = None

        notify_error('An exception was encountered while posting credentials:\n{}'.format(res))
        return '{' + str(success) + ',' + str(failed) + '}'
    finally:
        if cur2 is not None:
            cur2.close()

    cur2 = None
    try:
        for i in range(len(credentials)):
            credential = credentials[i]
            result = results[i]

            if result['success']:
                #print("log success to database")
                cur2 = conn.cursor()
                cur2.execute(sql2, (datetime.datetime.now(), result['result'], credential['RECORD_ID'],))
                conn.commit()
                cur2.close()
                cur2 = None
                success = success + 1
            else:
                print("log error to database")
                #print(result['result'])
                #print(credential)
                cur2 = conn.cursor()
                if 255 < len(result['result']):
                    res = result['result'][:250] + '...'
                else:
                    res = result['result']
                cur2.execute(sql3, (datetime.datetime.now(), res, credential['RECORD_ID'],))
                conn.commit()
                cur2.close()
                cur2 = None
                failed = failed + 1
                notify_error('An error was encountered while posting a credential:\n{}'.format(res))

    except (Exception) as error:
        # everything failed :-(
        print("log exception to database", str(error))
        res = str(error)
        if 0 == len(res):
            res = "Unspecified error storing credential status"
        elif 255 < len(res):
            res = res[:250] + '...'
        if cur2 is not None:
            cur2.close()
            cur2 = None
        cur2 = conn.cursor()
        for i in range(len(credentials)):
            credential = credentials[i]
            cur2.execute(sql3, (datetime.datetime.now(), res, credential['RECORD_ID'],))
            failed = failed + 1
        conn.commit()
        cur2.close()
        cur2 = None

        notify_error('An exception was encountered while posting credentials:\n{}'.format(res))
    finally:
        if cur2 is not None:
            cur2.close()
    return '{' + str(success) + ',' + str(failed) + '}'


class CredsSubmitter:
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
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
 
    async def process_credential_queue(self, single_thread=False):
        sql1 = """SELECT RECORD_ID, 
                      SYSTEM_TYPE_CD, 
                      PREV_EVENT, 
                      LAST_EVENT, 
                      CORP_NUM, 
                      CORP_STATE, 
                      CREDENTIAL_TYPE_CD, 
                      CREDENTIAL_ID, 
                      CREDENTIAL_JSON, 
                      CREDENTIAL_REASON, 
                      SCHEMA_NAME, 
                      SCHEMA_VERSION, 
                      ENTRY_DATE
                  FROM CREDENTIAL_LOG 
                  WHERE RECORD_ID IN
                  (
                      SELECT RECORD_ID
                      FROM CREDENTIAL_LOG 
                      WHERE PROCESS_DATE is null
                      AND RECORD_ID > %s
                      ORDER BY RECORD_ID
                      LIMIT """ + str(CREDS_BATCH_SIZE) + """
                  )
                  ORDER BY RECORD_ID;"""

        sql1a = """SELECT count(*) cnt
                   FROM CREDENTIAL_LOG 
                   WHERE PROCESS_DATE is null
                   AND RECORD_ID > %s"""

        """ Connect to the PostgreSQL database server """
        #conn = None
        cur = None
        # Track the current set of tasks.
        # When gathering tasks at the end we don't want to include these in the list.
        external_tasks = asyncio.Task.all_tasks()
        try:
            params = config(section='event_processor')
            pool = mpool.ThreadPool(MAX_CREDS_REQUESTS)
            loop = asyncio.get_event_loop()
            tasks = []
            max_rec_id = 0
            http_client = aiohttp.ClientSession()

            # create a cursor
            cred_count = 0
            cur = self.conn.cursor()
            cur.execute(sql1a, (max_rec_id,))
            row = cur.fetchone()
            if row is not None:
                cred_count = row[0]
            cur.close()
            cur = None

            i = 0
            cred_count_remaining = cred_count
            start_time = time.perf_counter()
            processing_time = 0
            processed_count = 0
            perf_proc_count = 0
            max_processing_time = 60 * MAX_PROCESSING_MINS

            while 0 < cred_count_remaining and processing_time < max_processing_time:
                # create a cursor
                cur = self.conn.cursor()
                cur.execute(sql1, (max_rec_id,))
                row = cur.fetchone()
                credentials = []
                cred_owner_id = ''
                while row is not None:
                    i = i + 1
                    processed_count = processed_count + 1
                    perf_proc_count = perf_proc_count + 1
                    if processed_count >= PROCESS_LOOP_REPORT_CT:
                      print('>>> Processing {} of {} credentials.'.format(i, cred_count))
                      processing_time = time.perf_counter() - start_time
                      print('Processing: ' + str(processing_time))
                      processed_count = 0
                    credential = {'RECORD_ID':row[0], 'SYSTEM_TYP_CD':row[1], 'PREV_EVENT':row[2], 'LAST_EVENT':row[3], 'CORP_NUM':row[4], 'CORP_STATE':row[5],
                                  'CREDENTIAL_TYPE_CD':row[6], 'CREDENTIAL_ID':row[7], 'CREDENTIAL_JSON':row[8], 'CREDENTIAL_REASON':row[9], 
                                  'SCHEMA_NAME':row[10], 'SCHEMA_VERSION':row[11], 'ENTRY_DATE':row[12]}
                    if max_rec_id < row[0]:
                        max_rec_id = row[0]

                    # make sure to include all credentials for the same client id within the same batch
                    if CREDS_REQUEST_SIZE <= len(credentials) and credential['CORP_NUM'] != cred_owner_id:
                        post_creds = credentials.copy()
                        creds_task = loop.create_task(post_credentials(http_client, self.conn, post_creds))
                        tasks.append(creds_task)
                        #await asyncio.sleep(1)
                        if single_thread:
                          # running single threaded - wait for each task to complete
                          await creds_task
                        else:
                          # multi-threaded, check if we are within MAX_CREDS_REQUESTS active requests
                          active_tasks = len([task for task in tasks if not task.done()])
                          #print("Added task - active = ", active_tasks, ", posted creds = ", len(post_creds))
                          while active_tasks >= MAX_CREDS_REQUESTS:
                            #await asyncio.gather(*tasks)
                            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                            active_tasks = len(pending)
                            # print("Waited task - active = ", active_tasks)
                        credentials = []
                        cred_owner_id = ''

                    credentials.append(credential)
                    cred_owner_id = credential['CORP_NUM']
                    
                    row = cur.fetchone()

                cur.close()
                cur = None

                if 0 < len(credentials):
                    post_creds = credentials.copy()
                    tasks.append(loop.create_task(post_credentials(http_client, self.conn, post_creds)))
                    credentials = []
                    cred_owner_id = ''

                # wait for the current batch of credential posts to complete
                print('>>> Processing {} of {} credentials.'.format(i, cred_count))
                processing_time = time.perf_counter() - start_time
                print('*** Processing: ' + str(processing_time))
                if perf_proc_count > 2*(CREDS_REQUEST_SIZE*MAX_CREDS_REQUESTS):
                    cpm = 60*(perf_proc_count-(0.5*CREDS_REQUEST_SIZE*MAX_CREDS_REQUESTS))/processing_time
                    print(cpm, "credentials per minute")

                cur = self.conn.cursor()
                cur.execute(sql1a, (max_rec_id,))
                row = cur.fetchone()
                if row is not None:
                    cred_count_remaining = row[0]
                cur.close()
                cur = None

            # wait for the current batch of credential posts to complete
            print(">>> Waiting for all outstanding tasks to complete ...")
            for response in await asyncio.gather(*tasks):
                pass # print('response:' + response)
            tasks = []

            print('>>> Completed.')
            processing_time = time.perf_counter() - start_time
            print('Processing: ' + str(processing_time))
            print(60*perf_proc_count/processing_time, "credentials per minute")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            log_error('An exception was encountered while processing the credential queue:\n{}'.format(str(error)))
            print(traceback.print_exc())
        finally:
            await http_client.close()

            # Gather all remaining tasks that were spawned during processing ...
            remaining_tasks = asyncio.Task.all_tasks()
            for task in external_tasks:
                # Remove any that were not created during processing ...
                remaining_tasks.discard(task)
            if len(remaining_tasks) > 0:
                await asyncio.gather(*remaining_tasks)

            if cur is not None:
                cur.close()