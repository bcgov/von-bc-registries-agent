#!/usr/bin/python
 
import psycopg2
import datetime
import json
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.eventprocessor import corp_credential, corp_schema, corp_version
from bcreg.eventprocessor import addr_credential, addr_schema, addr_version
from bcreg.eventprocessor import dba_credential, dba_schema, dba_version
from bcreg.bcregistries import system_type


CORP_MAPPING = """{
    'legal_entity_id': (S('corp_typ_cd') + S('corp_num')),
    'corp_num': (S('corp_typ_cd') + S('corp_num')),
    'effective_date': S('recognition_dts'),
    'legal_name': S('org_names', 0, 'corp_nme'),
    'org_name_effective': Alternation(S('org_names', 0, 'start_filing_event', 'effective_dt'), K(None)),
    'org_name_assumed': Alternation(S('org_name_assumed', 0, 'corp_nme'), K(None)),
    'org_name_assumed_effective': Alternation(S('org_name_assumed', 0, 'start_filing_event', 'effective_dt'), K(None)),
    'org_name_trans': Alternation(S('org_name_trans', 0, 'corp_nme'), K(None)),
    'org_name_trans_effective': Alternation(S('org_name_trans', 0, 'start_filing_event', 'effective_dt'), K(None)),
    'org_reg_status': S('corp_state', 'op_state_typ_cd'),
    'org_status_effective': Alternation(S('corp_state_dt'), K(None)),
    'org_type': S('corp_typ_cd'),
    'registered_jurisdiction': Alternation(S('registered_jurisdiction', 'can_jur_typ_cd'), K(None)),
    'registration_type': Alternation(S('tilma_involved', 'tilma_jurisdiction'), K(None)),
    'home_jurisdiction': Alternation(Switch(S('registered_jurisdiction', 'can_jur_typ_cd'), 
                            {'OT': Alternation(S('registered_jurisdiction', 'other_juris_desc'))}, 
                             default=Alternation(S('registered_jurisdiction', 'can_jur_typ_cd'))), K(None))
}"""

ADDR_MAPPING = """{
    'legal_entity_id': (S('corp_typ_cd') + S('corp_num')),
    'org_registry_id': (S('corp_typ_cd') + S('corp_num')),
    'addressee': S('org_names', 0, 'corp_nme'),
    'registered_jurisdiction': Alternation(S('registered_jurisdiction', 'can_jur_typ_cd'), K(None)),
    'addr_type': Alternation(S('office', 'office_typ_cd'), K(None)),
    'local_address': Alternation(S('office', 'local_addr'), K(None)),
    'municipality': Alternation(S('office', 'mailing_addr', 'city'), K(None)),
    'province': Alternation(S('office', 'mailing_addr', 'province'), K(None)),
    'postal_code': Alternation(S('office', 'mailing_addr', 'postal_cd'), K(None)),
    'country': Alternation(S('office', 'mailing_addr', 'country_typ_cd'), K(None)),
    'effective_date': Alternation(S('office', 'start_filing_event', 'effective_dt'), K(None)),
    'dba_name': S('org_names', 0, 'corp_nme')
}"""

DBA_MAPPING = """{
    'legal_entity_id': (S('corp_typ_cd') + S('corp_num')),
    'org_registry_id': (S('corp_typ_cd') + S('corp_num')),
    'org_name': S('org_names', 0, 'corp_nme'),
    'registered_jurisdiction': Alternation(S('registered_jurisdiction', 'can_jur_typ_cd'), K(None)),
    'dba_name': S('org_names', 0, 'corp_nme'),
    'effective_date': Alternation(S('org_names', 0, 'start_filing_event', 'effective_dt'), K(None))
}"""


with EventProcessor() as event_processor:
    # insert last event
    event_processor.insert_last_event(system_type, 9240000)
    
    # insert jsonbender mappers
    event_processor.insert_credential_transform(system_type, corp_credential, CORP_MAPPING, corp_schema, corp_version)
    event_processor.insert_credential_transform(system_type, addr_credential, ADDR_MAPPING, addr_schema, addr_version)
    event_processor.insert_credential_transform(system_type, dba_credential, DBA_MAPPING, dba_schema, dba_version)
    print("Seeded initial event processor data")

