
import time

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps import sample_test_corps


# basic BC corporation with an address and no DBA's
def test_scenario_basic_bc_corp():
    my_corp_num = '8539182'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic BC corporation with an address and no DBA's
def test_scenario_basic_dba_firm():
    my_corp_num = 'FM7980803'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic ex-corp with a non-BC jurisdiction and an address
def test_scenario_basic_xcorp():
    my_corp_num = 'A4138183'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic ex-corp with an assumed name
def test_scenario_assumed_name():
    my_corp_num = 'A4031472'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic BC corp with a translated name
def test_scenario_trans_name():
    my_corp_num = '3394994'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic corp with 1 DBA (no DBA address)
def test_scenario_single_dba():
    my_corp_num = '9260984'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 3
    

# basic corp with 1 DBA with an address
def test_scenario_dba_with_address():
    my_corp_num = 'C1208664'  
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 3
    

# basic corp with multiple DBA's (3)
def test_scenario_multi_dbas():
    my_corp_num = 'A7330600'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 5


# utility method to process the selected corp and generate credentails
def generate_creds_for_corp(corp_dict):
    corp_num = corp_dict['corp_num']
    corp_sqls = corp_dict['sqls']

    with BCRegistries(True) as cached_bc_reg:
        cached_bc_reg.cache_bcreg_code_tables()
        cached_bc_reg.insert_cache_sqls(corp_sqls)
        corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num, 0)

    with EventProcessor() as event_processor:
        corp_creds = event_processor.generate_credentials(system_type, 0, 0, corp_num, corp_info)

    return corp_creds
