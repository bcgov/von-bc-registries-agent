import re
import csv
import psycopg2
import datetime

from bcreg.config import config
from bcreg.bcregistries import BCRegistries


def remove_nulls(value):
    if value == 'NULL' or value == 'not registered':
        return ''
    return value

def is_numeric(value):
    return False

def clean_corp_num(value):
    # if starts with "BC", drop the "BC"
    if value.startswith("BC") and 2 < len(value):
        value = value[2:]

    # remove "-" and other punctuation and return
    value = value.replace("-", "")

    # if numeric, left-pad to 7 characters
    if is_numeric(value):
        tmp = ("0000000" + value)
        value = tmp[len(tmp)-7:]
        return value

    # else just return value
    return value

def corp_search_name(value):
    # all caps and remove non-alpha
    value = value.upper()
    value = re.sub(r'[^A-Z]', '', value)
    return value

def bcreg_corp_name_search(bc_registries, corp_name):
    corp_name_info = bc_registries.get_bcreg_sql("corp_name", 
        "select * from bc_registries.corp_name where srch_nme like '" + corp_name + "%' and end_event_id is null")
    if 1 == len(corp_name_info):
        # exact match
        return corp_name_info
    if 10 > len(corp_name):
        # name too short, return
        return corp_name_info
    # try searching with abbreviated corp name
    return bcreg_corp_name_search(bc_registries, corp_name[:len(corp_name)-5])


export_file = "bcreg/tests/test_data.csv"
stats_file = "bcreg/tests/test_data_stats.csv"

with BCRegistries() as bc_registries:
    with open(export_file) as csvfile, open(stats_file, 'w') as outfile:

        csv_reader = csv.reader(csvfile)
        csv_writer = csv.writer(outfile)

        header = None
        rows = []

        row_count = 0
        corp_num_count = 0
        dba_num_count = 0
        name_count = 0
        close_name_count = 0
        dba_name_count = 0
        close_dba_name_count = 0
        postal_count = 0
        unmatched_count = 0
        test_zip = False
        for row in csv_reader:
            if not header:
                header = row.copy()
                row.extend([
                        'Exact Match', 'Close Match',
                        'exact_match_on_corp_num',
                        'exact_match_on_trade_num',
                        'exact_match_on_business_name',
                        'close_match_on_business_name',
                        'exact_match_on_dba_name',
                        'close_match_on_dba_name',
                    ])
                csv_writer.writerow(row)
            else:
                matched = False
                exact_match_on_corp_num = False
                exact_match_on_trade_num = False
                exact_match_on_corp_name = False
                close_match_on_corp_name = False
                exact_match_on_dba_name = False
                close_match_on_dba_name = False
                corp = {}
                for i in range(len(header)):
                    corp[header[i]] = remove_nulls(row[i])
                rows.append(corp)
                row_count = row_count + 1

                # check the corp num(s) to see if we can get an exact match
                if 0 < len(corp['CORP_ACCESS_NUMBER']):
                    corp_num = clean_corp_num(corp['CORP_ACCESS_NUMBER'])
                    corp_info = bc_registries.get_bcreg_sql("corporation", 
                        "select * from bc_registries.corporation where corp_num = '" + corp_num + "'")
                    if 1 == len(corp_info):
                        # exact match?
                        corp_num_count = corp_num_count + 1
                        corp['CORP_NUM_EXACT_MATCH'] = corp_num
                        matched = True
                        exact_match_on_corp_num = True

                if not matched:
                    if 0 < len(corp['TRADE_NAME_NUMBER']):
                        corp_num = clean_corp_num(corp['TRADE_NAME_NUMBER'])
                        corp_info = bc_registries.get_bcreg_sql("corporation", 
                            "select * from bc_registries.corporation where corp_num = '" + corp_num + "'")
                        if 1 == len(corp_info):
                            # exact match?
                            dba_num_count = dba_num_count + 1
                            corp['TRADE_NUM_EXACT_MATCH'] = corp_num
                            matched = True
                            exact_match_on_trade_num = True

                # try for a match on the company name
                if not matched:
                    if 0 < len(corp['BUSINESS_NAME']):
                        corp_name = corp_search_name(corp['BUSINESS_NAME'])
                        corp_name_info = bcreg_corp_name_search(bc_registries, corp_name)
                        if 1 == len(corp_name_info):
                            # exact match?
                            name_count = name_count + 1
                            corp['CORP_NAME_EXACT_MATCH'] = corp_name
                            matched = True
                            exact_match_on_corp_name = True
                        elif 5 > len(corp_name_info):
                            close_name_count = close_name_count + 1
                            close_match_on_corp_name = True

                if not matched:
                    if 0 < len(corp['DOES_BUSINESS_AS']):
                        corp_name = corp_search_name(corp['DOES_BUSINESS_AS'])
                        corp_name_info = bcreg_corp_name_search(bc_registries, corp_name)
                        if 1 == len(corp_name_info):
                            # exact match?
                            dba_name_count = dba_name_count + 1
                            corp['DBA_NAME_EXACT_MATCH'] = dba_name_count
                            matched = True
                            exact_match_on_dba_name = True
                        elif 5 > len(corp_name_info):
                            close_dba_name_count = close_dba_name_count + 1
                            close_match_on_dba_name = True

                # match on postal code
                if test_zip and not matched:
                    if 0 < len(corp['ZIP_CODE']):
                        zip_code = corp['ZIP_CODE']
                        corp_addrs = bc_registries.get_bcreg_sql("address", 
                            "select addr_id from bc_registries.address where postal_cd = '" + zip_code + "'")
                        if 0 < len(corp_addrs) and 100 > len(corp_addrs):
                            addr_ids = ''
                            for addr in corp_addrs:
                                if 0 < len(addr_ids):
                                    addr_ids = addr_ids + ','
                                addr_ids = addr_ids + str(addr['addr_id'])
                            corp_nums = bc_registries.get_bcreg_sql("office", 
                                "select distinct corp_num from bc_registries.office where delivery_addr_id in (" + addr_ids + ") and end_event_id is null")
                            if 1 == len(corp_nums):
                                # exact match?
                                postal_count = postal_count + 1
                                corp['POSTAL_CD_EXACT_MATCH'] = zip_code
                                matched = True

                if not matched:
                    unmatched_count = unmatched_count + 1

                (ct, mod) = divmod(row_count, 100)
                if 0 == mod:
                    print(row_count)

                row.extend([
                        matched, (close_match_on_corp_name or close_match_on_dba_name),
                        exact_match_on_corp_num,
                        exact_match_on_trade_num,
                        exact_match_on_corp_name,
                        close_match_on_corp_name,
                        exact_match_on_dba_name,
                        close_match_on_dba_name
                    ])
                csv_writer.writerow(row)

        print("processed      ", row_count, "rows")
        print("corp_num_count ", corp_num_count)
        print("dba_num_count  ", dba_num_count)
        print("name_count     ", name_count, "(", close_name_count, ")")
        print("dba_name_count ", dba_name_count, "(", close_dba_name_count, ")")
        print("postal_count   ", postal_count)
        print("unmatched_count", unmatched_count)


