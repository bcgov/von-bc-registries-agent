
import time
import datetime
import json

from bcreg.bcregistries import BCRegistries, system_type, MIN_START_DATE, MAX_END_DATE
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
def test_scenario_history():
    my_corp_num = '4888387'
    my_corp_dict = sample_history_corps['corp_' + my_corp_num]
    my_info = generate_info_for_corp(my_corp_dict)
    my_creds = generate_all_creds_for_corp(my_info)
    my_event_creds = generate_creds_for_corp_by_event(my_info)

    assert len(my_creds) == 6
    assert len(my_event_creds) == 6

    for i in range(6):
        assert my_creds[i]['cred_type'] == my_event_creds[i]['cred_type']
        assert my_creds[i]['credential'] == my_event_creds[i]['credential']

def test_scenario_history_1():
    my_corp_num = 'A0212812'
    my_corp_dict = sample_history_corps['corp_' + my_corp_num]
    my_info = generate_info_for_corp(my_corp_dict)
    my_creds = generate_all_creds_for_corp(my_info)

    assert len(my_creds) == 5

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'A'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'ON'
    assert my_creds[0]['credential']['registered_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registration_id'] == 'A0212812'

    assert my_creds[4]['cred_type'] == 'ADDR'
    assert my_creds[4]['credential']['address_type'] == 'HD'
    assert my_creds[4]['credential']['registration_id'] == 'A0212812'

def test_scenario_history_2():
    my_corp_num = '5993202'
    my_corp_dict = sample_history_corps['corp_' + my_corp_num]
    my_info = generate_info_for_corp(my_corp_dict)
    my_creds = generate_all_creds_for_corp(my_info)

    assert len(my_creds) == 5

    assert my_creds[0]['cred_type'] == 'REG'
    assert my_creds[0]['credential']['entity_status'] == 'ACT'
    assert my_creds[0]['credential']['entity_type'] == 'BC'
    assert my_creds[0]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[0]['credential']['registered_jurisdiction'] == ''
    assert my_creds[0]['credential']['registration_id'] == 'BC5993202'

    assert my_creds[3]['cred_type'] == 'ADDR'
    assert my_creds[3]['credential']['address_type'] == 'RG'
    assert my_creds[3]['credential']['registration_id'] == 'BC5993202'

def test_scenario_history_future_date():
    my_corp_num = '6217522'
    my_corp_dict = sample_history_corps['corp_' + my_corp_num]
    my_info = generate_info_for_corp(my_corp_dict)
    my_creds = generate_all_creds_for_corp(my_info)

    assert my_creds[1]['cred_type'] == 'REG'
    assert my_creds[1]['credential']['entity_status'] == 'ACT'
    assert my_creds[1]['credential']['entity_type'] == 'BC'
    assert my_creds[1]['credential']['home_jurisdiction'] == 'BC'
    assert my_creds[1]['credential']['registered_jurisdiction'] == ''
    assert my_creds[1]['credential']['registration_id'] == 'BC6217522'

    assert my_creds[3]['cred_type'] == 'ADDR'
    assert my_creds[3]['credential']['address_type'] == 'RG'
    assert my_creds[3]['credential']['registration_id'] == 'BC6217522'


# utility method to process the selected corp and generate credentails
def generate_info_for_corp(corp_dict):
    corp_num = corp_dict['corp_num']
    corp_sqls = corp_dict['sqls']

    with BCRegistries(True) as cached_bc_reg:
        cached_bc_reg.cache_bcreg_code_tables()
        cached_bc_reg.insert_cache_sqls(corp_sqls)
        corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num)

    #print("Corp: " + corp_num + " loaded.")
    #print(json.dumps(corp_info, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))

    #for corp_state in corp_info['corp_state']:
    #    print(corp_state['corp_num'], corp_state['start_event']['event_id'], 
    #            corp_state['end_event']['event_id'] if 'end_event' in corp_state else 0, 
    #            corp_state['effective_start_date'], corp_state['effective_end_date'], 
    #            corp_state['state_typ_cd'], corp_state['op_state_typ_cd'], corp_state['corp_state_effective_event']['event_typ_cd'], 
    #            corp_state['start_event']['event_typ_cd'], corp_state['start_event']['effective_date'], 
    #            corp_state['end_event']['effective_date'] if 'end_event' in corp_state else '')
    return corp_info

def generate_all_creds_for_corp(corp_info):
    corp_num = corp_info['corp_num']

    start_event = {'event_id':0, 'event_date':MIN_START_DATE}
    end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
    with EventProcessor() as event_processor:
        corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp_num, corp_info)

    #print("Corp: " + corp_num + " generated " + str(len(corp_creds)) + " credentials.")
    #print(json.dumps(corp_creds, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))
    return corp_creds

def generate_creds_for_corp_by_event(corp_info):
    corp_num = corp_info['corp_num']

    all_creds = []
    with EventProcessor() as event_processor:
        effective_events = event_processor.unique_effective_events(corp_info['corp_state'], [])
        effective_events = event_processor.unique_effective_events(corp_info['jurisdiction'], effective_events)
        effective_events = event_processor.unique_effective_events(corp_info['org_names'], effective_events)
        effective_events = event_processor.unique_effective_events(corp_info['org_name_assumed'], effective_events)
        #print("Effective_events", json.dumps(effective_events, cls=CustomJsonEncoder, default=str, indent=4))

        for i in range(len(effective_events)-1):
            start_event = {'event_id': effective_events[i]['event_id'], 'event_date':effective_events[i]['event_timestmp']}
            end_event = {'event_id': effective_events[i+1]['event_id'], 'event_date':effective_events[i+1]['event_timestmp']}
            corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp_num, corp_info)
            #print(i,len(corp_creds))
            #print("Start Event", json.dumps(start_event, cls=CustomJsonEncoder, default=str, indent=4))
            #print("End Event", json.dumps(end_event, cls=CustomJsonEncoder, default=str, indent=4))
            #print("Creds", json.dumps(corp_creds, cls=CustomJsonEncoder, default=str, indent=4))
            for corp_cred in corp_creds:
                already_present = False
                for cred in all_creds:
                    if cred['credential'] == corp_cred['credential']:
                        already_present = True
                if not already_present:
                    all_creds.append(corp_cred)

    ret_creds = []
    for cred in all_creds:
        if cred['cred_type'] == 'REG':
            ret_creds.append(cred)
    for cred in all_creds:
        if cred['cred_type'] == 'ADDR':
            ret_creds.append(cred)
    for cred in all_creds:
        if cred['cred_type'] == 'REL':
            ret_creds.append(cred)

    #print("Corp: " + corp_num + " generated " + str(len(all_creds)) + " credentials.")
    #print(json.dumps(all_creds, cls=CustomJsonEncoder, default=str, indent=4, sort_keys=True))
    return ret_creds
