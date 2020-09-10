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
    print("Events", datetime.datetime.now())
    parties = bc_registries.get_bcreg_sql("event", "select * from bc_registries.event", cache=True)

    print("States", datetime.datetime.now())
    parties = bc_registries.get_bcreg_sql("corp_state", "select * from bc_registries.corp_state", cache=True)

    print("Fetch all incorrect events")
    sql2 = """
            SELECT *
            from event, corp_state
            where event.event_id = corp_state.start_event_id
              and event.corp_num != corp_state.corp_num;
           """
    events = bc_registries.get_adhoc_query(sql2)
    for event in events:
        print(event)
    print(len(events), "incorect events")
