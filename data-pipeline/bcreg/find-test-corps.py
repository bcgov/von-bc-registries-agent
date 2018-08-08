#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type


specific_corps = [
                    '0641655',
                    '0820416',
                    '0700450',
                    '0803224',
                    'LLC0000192',
                    'C0277609',
                    'A0072972',
                    'A0051862',
                    'C0874156',
                    '0874244',
                    '0593707',
                    'A0068919',
                    'A0064760',
                    'LLC0000234',
                    'A0077118',
                    'A0062459',
                    '0708325',
                    '0679026',
                    '0707774',
                    'C0874057',
                    'A0028374',
                    'A0053381',
                    'A0051632',
                    '0578221',
                    'A0032100',
                    '0874088',
                    '0803207',
                    '0873646',
#                    '0454097',
#                    '0873476',
#                    '0497648',
#                    '0873490',
#                    '0752246',
#                    '0644440',
#                    '0086128',
#                    'A0038634',
#                    'A0052296',
#                    'A0059958',
#                    'A0066549',
#                    '0136093',
#                    'A0020613',
#                    '0385191',
#                    'A0060574',
#                    'A0077151',
#                    '0283339',
#                    '0407802',
#                    'A0035475',
#                    'A0067161',
#                    '0081818',
#                    '0515727',
#                    '0798904',
#                    'A0023055',
#                    'A0043981',
#                    'A0051697',
#                    'A0063075',
#                    '0083251',
#                    '0301510',
#                    '0616986',
#                    'A0021989',
#                    'A0058845',
#                    'A0068960',
#                    'FM1000795',
#                    '0083494',
#                    '0354281',
#                    '0471961',
#                    '0581137',
#                    '0754041',
#                    '0873556',
#                    'A0025804',
#                    'A0037089',
#                    'A0051728',
#                    'A0071006',
#                    '0211314',
#                    '0332099',
#                    '0429657',
#                    '0533282',
#                    '0548694',
#                    '0873484',
#                    '0873573',
#                    'A0013794',
#                    'A0041891',
#                    'A0054033',
                    ]

with BCRegistries() as bc_registries:
    with EventProcessor() as event_processor:
        print("Get last processed event")
        prev_event_id = 0

        print("Get last max event")
        max_event_id = bc_registries.get_max_event()
        
        # get specific test corps (there are about 6)
        print("Get specific corps")
        corps = bc_registries.get_specific_corps(specific_corps)
        
        print("Find unprocessed events for each corp")
        corps = bc_registries.get_unprocessed_corp_events(prev_event_id, max_event_id, corps)
        
        print("Update our queue")
        event_processor.update_corp_event_queue(system_type, corps, max_event_id)
