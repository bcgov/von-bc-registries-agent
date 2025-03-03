#!/usr/bin/python
import psycopg2
import datetime
import os
import logging

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type, LEAR_CORP_TYPES_IN_SCOPE

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


specific_corps = [
    'CP0000672',
    'CP0001309',
    'CP0001311',
    'CP0001316',
    'FM0020270',
    'FM0222860',
    'FM0268275',
    'FM0272479',
    'BC0870921',
    'BC0870922',
    'FM1000038',
    'FM1000042',
    'FM1000047',
    'FM1000046',
    'FM0346897',
    'FM0346781',
    'FM0346815',
    'FM1017072',
    'BC1255957',
    'FM0814438',
    'FM0562853',
    'FM0575361',
    'FM0842476',
    'FM1004542',
    'FM1016197','FM0272889','FM0554287','FM0647554','FM0556572','FM0558680','FM0555836','FM0556028',
    'FM0840190',
]

specific_corps_2 = [
"FM1050387",
"FM1050388",
"FM1017458",
"FM1050389",
"FM0392675",
"FM1050390",
"FM0371138",
"FM0673672",
"FM0673673",
"FM0673656",
"FM1050461",
"FM1050462",
"FM1050463",
"FM0573874",
"FM1050464",
"FM0655173",
"FM1050465",
"FM1050466",
"FM0876195",
"FM0610497",
"FM0384701",
"FM1050881",
"FM1050882",
"FM1050883",
"FM1050884",
"FM1050885",
"BC1491537",
"FM1050886",
"BC1026494",
"FM0650512",
"BC1024239",
"FM1048326",
"A0132048",
"A0133092",
"FM0733881",
"FM0733880",
"FM0650512",
"FM1003299",
'FM1055223', 'FM1055224', 'FM1055225', 'FM0794864', 'FM0275010',
'FM0000137', 'FM0000181', 'FM0000185', 'FM0000049', 'FM0000108',
'FM1013156', 'FM1013154', 'FM1013158', 'FM1013155', 'FM1013159',
]


num_corps_per_type = 20


with BCReg_Lear() as bc_registries:
    # get 5 corps for each type in scope (in addition to the above list)
    corp_types_to_load = ['BEN', 'BC',]
    corp_types_to_load.extend(LEAR_CORP_TYPES_IN_SCOPE)
    for corp_type in corp_types_to_load:
        print(corp_type)
        sql = """
               select identifier as corp_num
               from businesses
               where legal_type = '""" + corp_type + """'
               order by last_modified desc
               limit 100
              """
        corps = bc_registries.get_bcreg_sql("corps_by_type", sql, cache=False)
        n_corps = min(len(corps), num_corps_per_type)
        for i in range(n_corps):
           specific_corps.append(corps[i]['corp_num'])

    with EventProcessor() as event_processor:
        print("Get last processed event")
        prev_event_id = 0

        print("Get last max event")
        max_event_date = bc_registries.get_max_event_date()
        max_event_id = bc_registries.get_max_event(max_event_date)
        print(">>> max event --> ", max_event_id, max_event_date)
        
        # get specific test corps (there are about 6)
        print("Get specific corps")
        corps = bc_registries.get_specific_corps(specific_corps)
        corps_2 = bc_registries.get_specific_corps(specific_corps_2)
        corps.extend(corps_2)

        print("Find unprocessed events for each corp")
        last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
        max_event_dt = bc_registries.get_event_effective_date(max_event_id)
        corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id, max_event_dt, corps)
        
        print("Update our queue")
        event_processor.update_corp_event_queue(lear_system_type, corps, max_event_id, max_event_date)
