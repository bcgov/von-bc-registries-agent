
import time
import datetime
import json

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps_history import sample_history_corps


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
def test_scenario_history_1():
    my_corp_num = 'A0212812'
    my_corp_dict = sample_history_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'Extraprovincial Company'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'ON'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A0212812'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'Head Office'
    assert my_creds[1]['credential']['registration_id'] == 'A0212812'

def test_scenario_history_2():
    my_corp_num = '5993202'
    my_corp_dict = sample_history_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    assert len(my_creds) == 2

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'BC Company'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'BC5993202'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'Registered Office'
    assert my_creds[1]['credential']['registration_id'] == 'BC5993202'


# utility method to process the selected corp and generate credentails
def generate_creds_for_corp(corp_dict):
    corp_num = corp_dict['corp_num']
    corp_sqls = corp_dict['sqls']

    with BCRegistries(True) as cached_bc_reg:
        cached_bc_reg.cache_bcreg_code_tables()
        cached_bc_reg.insert_cache_sqls(corp_sqls)
        corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num, 0)

    print("Corp: " + corp_num + " loaded.")
    print(json.dumps(corp_info, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))

    with EventProcessor() as event_processor:
        corp_creds = event_processor.generate_credentials(system_type, 0, 0, corp_num, corp_info)

    print("Corp: " + corp_num + " generated " + str(len(corp_creds)) + " credentials.")
    print(json.dumps(corp_creds, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))

    return corp_creds
