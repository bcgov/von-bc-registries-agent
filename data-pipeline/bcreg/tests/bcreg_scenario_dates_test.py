
import time
import datetime
import json

from bcreg.bcregistries import BCRegistries, system_type, MIN_START_DATE, MAX_END_DATE
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps_dates import sample_test_dates_corps


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
def test_scenario_dates_1():
    my_corp_num = '1529559'
    my_corp_dict = sample_test_dates_corps['corp_' + my_corp_num]
    my_creds = generate_creds_for_corp(my_corp_dict)

    assert len(my_creds) == 8

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'BC'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'BC1529559'

    assert my_creds[1]['cred_type'] == 'ADDR'
    assert my_creds[1]['credential']['address_type'] == 'RG'
    assert my_creds[1]['credential']['registration_id'] == 'BC1529559'


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
