
import time

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor


def test_generate_corp_sql():
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
                    ]
    
    with BCRegistries(True) as bc_registries:
        for corp in specific_corps:
            print(corp)
            bc_registries.cache_bcreg_corp_tables([corp], True)
            sqls = bc_registries.generated_sqls

            with BCRegistries(True) as cached_bc_reg:
                cached_bc_reg.cache_bcreg_code_tables(True)
                cached_bc_reg.insert_cache_sqls(sqls)

                #corp_info = cached_bc_reg.get_bc_reg_corp_info(corp['CORP_NUM'], corp['LAST_EVENT_ID'])

