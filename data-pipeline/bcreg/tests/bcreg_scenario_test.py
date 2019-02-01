
import time
import datetime
import json

from bcreg.bcregistries import BCRegistries, system_type, MIN_START_DATE, MAX_END_DATE
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

    print("# basic BC corporation with an address and no DBA's")
    assert len(my_creds) == 4

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'BC'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'BC9645624'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'RG'
    assert my_creds[1]['credential']['municipality'] == 'VANCOUVER'
    assert my_creds[1]['credential']['registration_id'] == 'BC9645624'


# basic BC corporation with an address and no DBA's
def test_scenario_basic_dba_firm():
    my_corp_num = 'FM7768377'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic BC firm with an address and no DBA's")
    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'SP'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'FM7768377'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'FO'
    assert my_creds[1]['credential']['municipality'] == 'DELTA'
    assert my_creds[1]['credential']['registration_id'] == 'FM7768377'
    

# basic ex-corp with a non-BC jurisdiction and an address
def test_scenario_basic_xcorp():
    my_corp_num = 'A3781337'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic ex-corp with a non-BC jurisdiction and an address")
    assert len(my_creds) == 5

    assert my_creds[2]['cred_type'] == 'REG'
    assert my_creds[2]['credential']['entity_status'] == 'ACT'
    assert my_creds[2]['credential']['entity_type'] == 'A'
    assert my_creds[2]['credential']['home_jurisdiction'] == 'GB'
    assert my_creds[2]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[2]['credential']['registration_id'] == 'A3781337'

    assert my_creds[4]['cred_type'] == 'ADDR'
    assert my_creds[4]['credential']['address_type'] == 'HD'
    assert my_creds[4]['credential']['municipality'] == 'LONDON'
    assert my_creds[4]['credential']['civic_address'] == 'UUBCWY DKNOCDWWNEVFSCKY O, LONDON, H8IU1N, GB'
    assert my_creds[4]['credential']['registration_id'] == 'A3781337'
    

# basic ex-corp with an assumed name
def test_scenario_assumed_name():
    my_corp_num = 'A1196902'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic ex-corp with an assumed name")
    assert len(my_creds) == 3

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'A'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'ON'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A1196902'
    assert my_creds[0]['credential']['entity_name'] == 'LFQMDNIUJYCIU  DCDRDZFYXP'
    assert my_creds[0]['credential']['entity_name_assumed'] == 'UFTOBFEBMBKB  UVEUKHNGEMZ'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'HD'
    assert my_creds[1]['credential']['municipality'] == 'Toronto'
    assert my_creds[1]['credential']['registration_id'] == 'A1196902'
    

# basic BC corp with a translated name
def test_scenario_trans_name():
    my_corp_num = '4241301'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic BC corp with a translated name")
    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'BC'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'BC4241301'
    assert my_creds[0]['credential']['entity_name'] == 'XCUBPIM YRSWHAWTLUMFRPRUZ'
    # assert my_creds[0]['credential']['entity_name_trans'] == 'MMRTKDCWLGXOFULSZYEIIHKRO'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'RG'
    assert my_creds[1]['credential']['municipality'] == 'Kelowna'
    assert my_creds[1]['credential']['registration_id'] == 'BC4241301'
    

# basic corp with 1 DBA (no DBA address)
def test_scenario_single_dba():
    my_corp_num = '2201720'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic corp with 1 DBA (no DBA address)")
    assert len(my_creds) == 5

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[3]['cred_type'] == 'ADDR'
    assert my_creds[4]['cred_type'] == 'REL'

    my_dba_num = 'FM3035075'
    my_corp_dict['corp_num'] = my_dba_num
    dba_creds = generate_creds_for_corp(my_corp_dict)
    assert len(dba_creds) == 2
    
    assert dba_creds[0]['cred_type'] == 'REG'


# basic corp with 1 DBA with an address
def test_scenario_dba_with_address():
    my_corp_num = 'C6020509'  
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic corp with 1 DBA with an address")
    assert len(my_creds) == 7

    my_dba_num = 'FM9129945'
    my_corp_dict['corp_num'] = my_dba_num
    dba_creds = generate_creds_for_corp(my_corp_dict)
    assert len(dba_creds) == 5
    
    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'CUL'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'C6020509'

    assert my_creds[3]['cred_type'] == 'ADDR'
    assert my_creds[3]['credential']['address_type'] == 'RG'
    assert my_creds[3]['credential']['municipality'] == 'testcity'
    assert my_creds[3]['credential']['registration_id'] == 'C6020509'

    assert my_creds[4]['cred_type'] == 'REL'
    assert my_creds[4]['credential']['registration_id'] == 'C6020509'
    assert my_creds[4]['credential']['associated_registration_id'] == 'FM9129945'
    assert my_creds[4]['credential']['relationship'] == 'Owns'
    assert my_creds[4]['credential']['relationship_description'] == 'Does Business As'
    assert my_creds[4]['credential']['relationship_status'] == 'ACT'

    assert dba_creds[0]['cred_type'] == 'REG'
    assert dba_creds[0]['credential']['entity_status'] == 'ACT'
    assert dba_creds[0]['credential']['entity_type'] == 'SP'
    assert dba_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert dba_creds[0]['credential']['registration_id'] == 'FM9129945'

    assert dba_creds[1]['cred_type'] == 'ADDR'
    assert dba_creds[1]['credential']['address_type'] == 'FO'
    assert dba_creds[1]['credential']['municipality'] == 'VANCOUVER'
    assert dba_creds[1]['credential']['registration_id'] == 'FM9129945'


# basic corp with multiple DBA's (3)
def test_scenario_multi_dbas():
    my_corp_num = 'A5589691'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic corp with multiple DBA's (3)")
    assert len(my_creds) == 6

    assert my_creds[1]['cred_type'] == 'REG'
    assert my_creds[2]['cred_type'] == 'ADDR'
    assert my_creds[3]['cred_type'] == 'REL'
    assert my_creds[4]['cred_type'] == 'REL'
    assert my_creds[5]['cred_type'] == 'REL'

    my_dba_nums = ['FM3834099','FM8823648','FM9877026']
    my_dba_ct = [2,2,3]
    i = 0
    for my_dba_num in my_dba_nums:
        my_corp_dict['corp_num'] = my_dba_num
        dba_creds = generate_creds_for_corp(my_corp_dict)
        assert len(dba_creds) == my_dba_ct[i]
        assert dba_creds[0]['cred_type'] == 'REG'
        i = i + 1

# basic corp with empty date(s)
def test_scenario_empty_dates():
    my_corp_num = '6763577'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# basic corp with empty dates")
    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[1]['cred_type'] == 'ADDR'


# utility method to process the selected corp and generate credentails
def generate_creds_for_corp(corp_dict):
    corp_num = corp_dict['corp_num']
    corp_sqls = corp_dict['sqls']

    with BCRegistries(True) as cached_bc_reg:
        cached_bc_reg.cache_bcreg_code_tables()
        cached_bc_reg.insert_cache_sqls(corp_sqls)
        corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num)

    start_event = {'event_id':0, 'event_date':MIN_START_DATE}
    end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
    with EventProcessor() as event_processor:
        corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp_num, corp_info)

    #print("Corp: " + corp_num + " generated " + str(len(corp_creds)) + " credentials")
    #print(json.dumps(corp_creds, cls=DateTimeEncoder, indent=4, sort_keys=True))

    return corp_creds
