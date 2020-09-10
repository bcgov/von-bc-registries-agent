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
Detail audit report - first step.
Reads all corps and corp types from the BC Reg database and writes to a csv file.
"""

# corp num with prefix
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

bc_reg_count = 0
with BCRegistries() as bc_registries:
    # run this query against BC Reg database:
    sql1 = """
    select corp.corp_num, corp.corp_typ_cd
    from bc_registries.corporation corp
    where corp.corp_num not in (
        select corp_num from bc_registries.corp_state where state_typ_cd = 'HWT');
    """

    with open('bc_reg_corps.csv', mode='w') as corp_file:
        fieldnames = ["corp_num", "corp_type"]
        corp_writer = csv.DictWriter(corp_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        corp_writer.writeheader()

        print("Get corp stats from BC Registries DB", datetime.datetime.now())
        start_time = time.perf_counter()
        processed_count = 0
        bc_reg_corps = []
        bc_reg_recs = bc_registries.get_bcreg_sql("corp_stats", sql1, cache=False)
        for bc_reg_rec in bc_reg_recs:
            if bc_reg_rec['corp_typ_cd'] in CORP_TYPES_IN_SCOPE:
                bc_reg_count = bc_reg_count + 1
                bc_reg_corp = {
                    "corp_num": corp_num_with_prefix(bc_reg_rec['corp_typ_cd'], bc_reg_rec['corp_num']),
                    "corp_type": bc_reg_rec['corp_typ_cd']
                }
                bc_reg_corps.append(bc_reg_corp)
                corp_writer.writerow(bc_reg_corp)
                processed_count = processed_count + 1
                if processed_count >= 10000:
                    processing_time = time.perf_counter() - start_time
                    print("Processing:", bc_reg_count, processing_time)
                    processed_count = 0
