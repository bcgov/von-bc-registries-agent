#!/usr/bin/python
import psycopg2
import datetime
import time
import json
import decimal
import requests
import csv

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor, CORP_TYPES_IN_SCOPE
from bcreg.bcregistries import BCRegistries


QUERY_LIMIT = '200000'
REPORT_COUNT = 10000
ERROR_THRESHOLD_COUNT = 5

ORGBOOK_API_URL = "https://orgbook.gov.bc.ca/api/v3"
TOPIC_QUERY = "/topic/registration.registries.ca/"
TOPIC_NAME_SEARCH = "/search/topic?inactive=false&latest=true&revoked=false&name="
TOPIC_ID_SEARCH = "/search/topic?inactive=false&latest=true&revoked=false&topic_id="


"""
Detail audit report - final step.
Reads from the orgbook database and compares:
- corps in BC Reg that are not in orgbook (or that are in orgbook with a different corp type)
- corps in orgbook that are *not* in BC Reg database (maybe have been removed?)
- corps in event processor audit logs that are not in BC Reg database (maybe have been removed?)
- corps in BC Reg database that are not in the event processor audit logs
"""

def corp_num_with_prefix(corp_typ_cd, corp_num):
    p_corp_num = corp_num
    if corp_typ_cd == 'BC':
        p_corp_num = 'BC' + corp_num
    elif corp_typ_cd == 'ULC':
        p_corp_num = 'BC' + corp_num
    elif corp_typ_cd == 'CC':
        p_corp_num = 'BC' + corp_num
    elif corp_typ_cd == 'BEN':
        p_corp_num = 'BC' + corp_num
    return p_corp_num

def bare_corp_num(corp_num):
    if corp_num.startswith("BC"):
        return corp_num[2:]
    else:
        return corp_num

conn = None
try:
    params = config(section='org_book')
    conn = psycopg2.connect(**params)
except (Exception) as error:
    print(error)
    raise

# get all the corps from orgbook
print("Get corp stats from OrgBook DB", datetime.datetime.now())
sql4 = """select topic.source_id, attribute.value from topic 
          left join credential on credential.topic_id = topic.id and credential.latest = true and credential_type_id = 1
          left join attribute on attribute.credential_id = credential.id and attribute.type = 'entity_type'"""
corp_types = {}
try:
    cur = conn.cursor()
    cur.execute(sql4)
    for row in cur:
        corp_types[row[0]] = row[1]
    cur.close()
except (Exception) as error:
    print(error)
    raise

# corps that are still in the event processor queue waiting to be processed (won't be in orgbook yet)
future_corps = {}
with open('event_future_corps.csv', mode='r') as corp_file:
    corp_reader = csv.DictReader(corp_file)

    row_count = 0
    for row in corp_reader:
        if row_count == 0:
            print(f'Column names are {", ".join(row)}')
            row_count += 1
        future_corps[row["corp_num"]] = row["corp_num"]

# check if all the BC Reg corps are in orgbook (with the same corp type)
bc_reg_corps = {}
with open('bc_reg_corps.csv', mode='r') as corp_file:
    corp_reader = csv.DictReader(corp_file)

    start_time = time.perf_counter()
    processed_count = 0
    row_count = 0
    bc_reg_count = 0
    for row in corp_reader:
        if row_count == 0:
            print(f'Column names are {", ".join(row)}')
            row_count += 1
        bc_reg_corps[row["corp_num"]] = row["corp_type"]
        if bare_corp_num(row["corp_num"]) in future_corps:
            #print("Future corp ignore:", row["corp_num"])
            pass
        elif not row["corp_num"] in corp_types:
            #print("Topic not found for:", row)
            print("./manage -e prod queueOrganization " + bare_corp_num(row["corp_num"]))
        elif (not corp_types[row["corp_num"]]) or (corp_types[row["corp_num"]] != row["corp_type"]):
            #print("Corp Type mis-match for:", row, corp_types[row["corp_num"]])
            print("./manage -p bc -e prod deleteTopic " + row["corp_num"])
            print("./manage -e prod requeueOrganization " + bare_corp_num(row["corp_num"]))

# now check if there are corps in orgbook that are *not* in BC Reg database
for orgbook_corp in corp_types:
    if not (orgbook_corp in bc_reg_corps):
        print("OrgBook corp not in BC Reg:", orgbook_corp)

# now check if there are corps in event processor that are *not* in bc reg database
audit_corps = {}
with open('event_audit_corps.csv', mode='r') as audit_file:
    corp_reader = csv.DictReader(audit_file)

    start_time = time.perf_counter()
    processed_count = 0
    row_count = 0
    bc_reg_count = 0
    for row in corp_reader:
        if row_count == 0:
            print(f'Column names are {", ".join(row)}')
            row_count += 1
        audit_corps[corp_num_with_prefix(row['corp_type'], row['corp_num'])] = row['corp_type']
        if not (corp_num_with_prefix(row['corp_type'], row['corp_num']) in bc_reg_corps):
            print("Event Processor corp not in BC Reg:", row['corp_num'], row['corp_type'])

# check who is in bc reg and not in event processor
for bcreg_corp in bc_reg_corps:
    if bcreg_corp not in audit_corps and bare_corp_num(bcreg_corp) not in future_corps:
        print("BC Reg corp not in Event Processor :", bcreg_corp)
