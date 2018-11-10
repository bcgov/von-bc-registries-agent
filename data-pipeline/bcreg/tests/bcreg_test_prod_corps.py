
import time

from bcreg.bcregistries import BCRegistries, system_type, MIN_START_DATE, MAX_END_DATE
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps import sample_test_corps


def test_dev_corp_sql1():
    specific_corps = [
                    'FM0128548',
                   ]

    # try caching everything
    #with BCRegistries(True) as bc_registries:
    #    bc_registries.cache_bcreg_corps(specific_corps)

#def test_dev_corp_sql():
#    specific_corps = [
#                    'C1033288','C1043095'
#                    ]

    # go one-by-one
    with BCRegistries() as bc_registries:
        for corp in specific_corps:
            start_event = {'event_id':0, 'event_date':MIN_START_DATE}
            end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
 
            # try running with dummy event id zero 
            corp_info = bc_registries.get_bc_reg_corp_info(corp)
            print('-------------------------')
            print('corp_info:')
            print(corp_info)
            print('-------------------------')

        with EventProcessor() as event_processor:
            corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp, corp_info)
            print('-------------------------')
            print('corp_creds:')
            print(corp_creds)
            print('-------------------------')

def _test_dev_corp_sql2():
    specific_corps = [
                    'A0073185',
                   ]

    # try caching everything
    #with BCRegistries(True) as bc_registries:
    #    bc_registries.cache_bcreg_corps(specific_corps)

#def test_dev_corp_sql():
#    specific_corps = [
#                    'C1033288','C1043095'
#                    ]

    # go one-by-one
    with BCRegistries(True) as bc_registries:
        for corp in specific_corps:
            #print('=========================')
            print('===== ',  corp)
            bc_registries.cache_bcreg_corp_tables([corp], True)
            sqls = bc_registries.generated_sqls
            fake_corp_num = bc_registries.add_generated_corp_num(corp)
            print('=============>>> ', fake_corp_num)
            #print('=========================')
            #print('sqls:')
            #for sql in sqls:
            #    print('"""' + sql.replace(' values ', '\nvalues\n') + '""",')
            #print('=========================')

            start_event = {'event_id':0, 'event_date':MIN_START_DATE}
            end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
 
            with BCRegistries(True) as cached_bc_reg:
                cached_bc_reg.cache_bcreg_code_tables()
                cached_bc_reg.insert_cache_sqls(sqls)

                # try running with dummy event id zero 
                corp_info = cached_bc_reg.get_bc_reg_corp_info(fake_corp_num)
                print('-------------------------')
                print('corp_info:')
                print(corp_info)
                print('-------------------------')

            with EventProcessor() as event_processor:
                corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, fake_corp_num, corp_info)
                print('-------------------------')
                print('corp_creds:')
                print(corp_creds)
                print('-------------------------')

