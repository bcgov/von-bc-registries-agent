
import time
import datetime
import json

from bcreg.bcregistries import BCRegistries, system_type, MIN_START_DATE, MAX_END_DATE
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corp_jurisdictions import sample_test_jurisdiction_corps
from bcreg.tests.sample_corps import sample_test_corps


def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# custom encoder to convert wierd data types to strings
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (list, dict, str, int, float, bool, type(None))):
            return JSONEncoder.default(self, o)        
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        if isinstance(o, set):
            return list(o)
        if isinstance(o, map):
            return list(o)
        return json.JSONEncoder.default(self, o)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


# scenarios for different jurisdictions
def test_scenario_jurisdiction_bc():
    my_corp_num = '3014589'
    my_corp_dict = sample_test_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# BC Corp")
    assert len(my_creds) == 3

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'ULC'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'BC3014589'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'RG'
    assert my_creds[1]['credential']['registration_id'] == 'BC3014589'


def test_scenario_jurisdiction_man():
    my_corp_num = 'A5215485'
    my_corp_dict = sample_test_jurisdiction_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# Home Jurisdiction United Kingdom (can_jur_typ_cd = ‘OT’ and othr_juris_desc = ‘GB’)")
    assert len(my_creds) == 3

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'A'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'GB'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A5215485'

    assert my_creds[2]['cred_type'] == 'ADDR'
    assert my_creds[2]['credential']['address_type'] == 'HD'
    assert my_creds[2]['credential']['civic_address'] == 'GQACSKQWJZDWYJK D ITLV WW, UZNLSWYTMYQLUAJGDKDZWQZUV, ENGLAND  CW8 2YA, '
    assert my_creds[2]['credential']['registration_id'] == 'A5215485'


def test_scenario_jurisdiction_washington():
    my_corp_num = 'A5462935'
    my_corp_dict = sample_test_jurisdiction_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# Home Jurisdiction Washington (can_jur_typ_cd = ‘OT’ and othr_juris_desc = ‘US, WA’)")
    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'HIS'
    assert my_creds[0]['credential']['entity_type'] == 'A'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'US, WA'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A5462935'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'HD'
    assert my_creds[1]['credential']['civic_address'] == 'XZVDZOLRCFHDHGGRTSJTLNLFY, VMUMZPQJWJJJPBPHKHLVNFIED, 98178, '
    assert my_creds[1]['credential']['registration_id'] == 'A5462935'
    

def test_scenario_jurisdiction_uk():
    my_corp_num = 'A4993014'
    my_corp_dict = sample_test_jurisdiction_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# Home Jurisdiction Federal (can_jur_typ_cd ‘FD’)")
    assert len(my_creds) == 5

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'A'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'FD'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A4993014'

    assert my_creds[4]['cred_type'] == 'ADDR'
    assert my_creds[4]['credential']['address_type'] == 'HD'
    assert my_creds[4]['credential']['municipality'] == 'VANCOUVER'
    assert my_creds[4]['credential']['registration_id'] == 'A4993014'
    

def test_scenario_jurisdiction_notonfile():
    my_corp_num = 'A9168630'
    my_corp_dict = sample_test_jurisdiction_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# Home Jurisdiction Not on File (can_jur_typ_cd ‘OT’ and othr_juris_desc = null)")
    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'HIS'
    assert my_creds[0]['credential']['entity_type'] == 'A'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'OT'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A9168630'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'HD'
    assert my_creds[1]['credential']['registration_id'] == 'A9168630'
    

def test_scenario_jurisdiction_federal():
    my_corp_num = 'A7164764'
    my_corp_dict = sample_test_jurisdiction_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    print("# Home Jurisdiction Manitoba (can_jur_typ_cd = ‘MB’)")
    assert len(my_creds) == 3

    assert my_creds[1]['cred_type'] == 'REG'
    assert my_creds[1]['credential']['entity_status'] == 'ACT'
    assert my_creds[1]['credential']['entity_type'] == 'A'
    assert my_creds[1]['credential']['home_jurisdiction'] == 'MB'
    assert my_creds[1]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[1]['credential']['registration_id'] == 'A7164764'

    assert my_creds[2]['cred_type'] == 'ADDR'
    assert my_creds[2]['credential']['address_type'] == 'HD'
    assert my_creds[2]['credential']['municipality'] == 'WINNIPEG'
    assert my_creds[2]['credential']['registration_id'] == 'A7164764'
    

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
    #print(json.dumps(corp_info, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))
    #print(json.dumps(corp_creds, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))

    return corp_creds
