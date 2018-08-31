
import time

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps import sample_test_corps


# basic BC corporation with an address and no DBA's
def test_scenario_basic_bc_corp():
    my_corp_num = '9645624'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic BC corporation with an address and no DBA's")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic BC corporation with an address and no DBA's
def test_scenario_basic_dba_firm():
    my_corp_num = 'FM7768377'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic BC corporation with an address and no DBA's")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic ex-corp with a non-BC jurisdiction and an address
def test_scenario_basic_xcorp():
    my_corp_num = 'A3781337'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic ex-corp with a non-BC jurisdiction and an address")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic ex-corp with an assumed name
def test_scenario_assumed_name():
    my_corp_num = 'A1196902'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic ex-corp with an assumed name")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic BC corp with a translated name
def test_scenario_trans_name():
    my_corp_num = '4241301'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic BC corp with a translated name")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 2
    

# basic corp with 1 DBA (no DBA address)
def test_scenario_single_dba():
    my_corp_num = '2201720'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic corp with 1 DBA (no DBA address)")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 3
    

# basic corp with 1 DBA with an address
def test_scenario_dba_with_address():
    my_corp_num = 'C6020509'  
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic corp with 1 DBA with an address")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(my_creds)
    assert len(my_creds) == 3
    

# basic corp with multiple DBA's (3)
def test_scenario_multi_dbas():
    my_corp_num = 'A5589691'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic corp with multiple DBA's (3)")
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
