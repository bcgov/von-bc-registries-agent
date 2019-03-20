#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type


def csv_header(corp):
    header = []
    header_line = ""
    for key in corp:
        if len(header_line) > 0:
            header_line = header_line + ','
        header.append(key)
        header_line = header_line + key
    return (header, header_line)

def csv_line(header, corp):
    line = ""
    for key in header:
        if len(line) > 0:
            line = line + ','
        line = line + corp[key]
    return line

# load BC Registries with local cache enabled
with BCRegistries(True) as bc_registries:
    sql1 = """
            select corp_num, party_typ_cd, count(*) party_count
            from bc_registries.corp_party
            where end_event_id is null
              and party_typ_cd in ('OFF', 'DIR')
            group by corp_num, party_typ_cd
           """
    sql2 = """
            SELECT corp.corp_num corp_num, typ.corp_class corp_class, op_state.op_state_typ_cd op_state_typ_cd
            from bc_registries.corporation corp, 
                 bc_registries.corp_type typ,
                 bc_registries.corp_state state,
                 bc_registries.corp_op_state op_state
            where corp.corp_typ_cd = typ.corp_typ_cd 
              and corp.corp_num = state.corp_num
              and state.end_event_id is null
              and op_state.state_typ_cd = state.state_typ_cd
              and op_state.op_state_typ_cd = 'ACT'
              and typ.corp_class in ('BC','XPRO')
           """

    print("Get officers and directors", datetime.datetime.now())
    parties = bc_registries.get_bcreg_sql("parties", sql1, cache=True)

    print("Get active BC corporations", datetime.datetime.now())
    corps = bc_registries.get_bcreg_sql("corps", sql2, cache=True)

    print("Do a query to verify local cached data", datetime.datetime.now())
    p_count = bc_registries.get_adhoc_query("select count(*) count from parties")
    print("Party count =", p_count, datetime.datetime.now())
    c_count = bc_registries.get_adhoc_query("select count(*) count from corps")
    print("Corp count =", c_count, datetime.datetime.now())

    print("Fetch all corps and then get officer/director info for each")
    sql3 = """
            select corps.corp_num corp_num, corp_class, op_state_typ_cd, party_typ_cd, party_count
            from corps, parties
            where corps.corp_num = parties.corp_num
           """
    corps = bc_registries.get_adhoc_query(sql3)
    print_header = False
    histogram = {}
    for corp in corps:
        if not print_header:
            (header, header_line) = csv_header(corp)
            #print(header_line)
            print_header = True
        #print(csv_line(header, corp))
        if corp['party_typ_cd'] in histogram:
            party_hist = histogram[corp['party_typ_cd']]
        else:
            party_hist = {}
        if corp['party_count'] in party_hist:
            party_hist[corp['party_count']] = party_hist[corp['party_count']] + 1
        else:
            party_hist[corp['party_count']] = 1
        histogram[corp['party_typ_cd']] = party_hist
    #print(histogram)
    print("party,number,corps")
    for key_type in histogram:
        for key_count in histogram[key_type]:
            print(key_type + ',' + key_count + ',' + str(histogram[key_type][key_count]))

