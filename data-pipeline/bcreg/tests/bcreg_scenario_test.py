
import time
import datetime
import json

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps import sample_test_corps


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


# basic BC corporation with an address and no DBA's
def test_scenario_basic_bc_corp():
    my_corp_num = '9645624'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic BC corporation with an address and no DBA's")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 2
    

# basic BC corporation with an address and no DBA's
def test_scenario_basic_dba_firm():
    my_corp_num = 'FM7768377'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic BC corporation with an address and no DBA's")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 2
    

# basic ex-corp with a non-BC jurisdiction and an address
def test_scenario_basic_xcorp():
    my_corp_num = 'A3781337'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic ex-corp with a non-BC jurisdiction and an address")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 2
    

# basic ex-corp with an assumed name
def test_scenario_assumed_name():
    my_corp_num = 'A1196902'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic ex-corp with an assumed name")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 2
    

# basic BC corp with a translated name
def test_scenario_trans_name():
    my_corp_num = '4241301'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic BC corp with a translated name")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 2
    

# basic corp with 1 DBA (no DBA address)
def test_scenario_single_dba():
    my_corp_num = '2201720'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic corp with 1 DBA (no DBA address)")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 3

    my_dba_num = 'FM3035075'
    my_corp_dict['corp_num'] = my_dba_num
    dba_creds = generate_creds_for_corp(my_corp_dict)
    print("Corp: " + my_dba_num + " generated " + str(len(dba_creds)) + " credentials")
    print(json.dumps(dba_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(dba_creds) == 1
    

# basic corp with 1 DBA with an address
def test_scenario_dba_with_address():
    my_corp_num = 'C6020509'  
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic corp with 1 DBA with an address")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 3

    my_dba_num = 'FM9129945'
    my_corp_dict['corp_num'] = my_dba_num
    dba_creds = generate_creds_for_corp(my_corp_dict)
    print("Corp: " + my_dba_num + " generated " + str(len(dba_creds)) + " credentials")
    print(json.dumps(dba_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(dba_creds) == 2
    

# basic corp with multiple DBA's (3)
def test_scenario_multi_dbas():
    my_corp_num = 'A5589691'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    # TODO run some assertions based on what we expect
    print("# basic corp with multiple DBA's (3)")
    print("Corp: " + my_corp_num + " generated " + str(len(my_creds)) + " credentials")
    print(json.dumps(my_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
    assert len(my_creds) == 5

    my_dba_nums = ['FM3834099','FM8823648','FM9877026']
    my_dba_ct = [1,1,2]
    i = 0
    for my_dba_num in my_dba_nums:
        my_corp_dict['corp_num'] = my_dba_num
        dba_creds = generate_creds_for_corp(my_corp_dict)
        print("Corp: " + my_dba_num + " generated " + str(len(dba_creds)) + " credentials")
        print(json.dumps(dba_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))
        assert len(dba_creds) == my_dba_ct[i]
        i = i + 1


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
