
import time

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps import sample_test_corps


def test_dev_corp_sql():
    specific_corps = [
                    #'0574972',
                    '0657791'
                    ]
    
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
 
            with BCRegistries(True) as cached_bc_reg:
                cached_bc_reg.cache_bcreg_code_tables()
                cached_bc_reg.insert_cache_sqls(sqls)

                # try running with dummy event id zero 
                corp_info = cached_bc_reg.get_bc_reg_corp_info(fake_corp_num, 0)
                #print('-------------------------')
                #print('corp_info:')
                #print(corp_info)
                #print('-------------------------')

            with EventProcessor() as event_processor:
                corp_creds = event_processor.generate_credentials(system_type, 0, 0, fake_corp_num, corp_info)
                #print('-------------------------')
                #print('corp_creds:')
                #print(corp_creds)
                #print('-------------------------')

