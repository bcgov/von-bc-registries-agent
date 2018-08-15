
import time

from bcreg.bcregistries import BCRegistries, system_type
from bcreg.eventprocessor import EventProcessor

select_corp_sql = """select corp.corp_num, corp.corp_typ_cd, state.state_typ_cd
						  from bc_registries.corporation corp, bc_registries.corp_state state
						where corp.corp_num = state.corp_num
						  and state.end_event_id is null
						  and corp.corp_num in
						(SELECT distinct(corp_num) from bc_registries.event
						  where event_id >= 9240000
						    and corp_num in
						  (SELECT corp.corp_num
						    from bc_registries.corporation corp, bc_registries.corp_state state, bc_registries.corp_op_state op_state
						    where corp.corp_num = state.corp_num
						      and state.end_event_id is null
						      and state.state_typ_cd = op_state.state_typ_cd
						      and op_state.op_state_typ_cd = 'ACT'
						      and corp.corp_typ_cd in ('A','LLC','BC','C','CUL','ULC')))
						order by corp.corp_num"""

select_party_recs = """select count(*) from bc_registries.corp_party 
						where bus_company_num = %s and end_event_id is null"""

select_party_addr_recs = """select count(*) from bc_registries.office 
				    		where office_typ_cd = 'FO' and end_event_id is null
				    		  and corp_num in (select corp_num from bc_registries.corp_party where bus_company_num = %s)"""

select_name_recs  = """select count(*) from bc_registries.corp_name 
						where corp_num = %s and end_event_id is null
						  and corp_name_typ_cd in ('CO','NB')"""

select_name_assumed_recs  = """select count(*) from bc_registries.corp_name 
						where corp_num = %s and end_event_id is null
						  and corp_name_typ_cd in ('AS')"""

select_name_trans_recs  = """select count(*) from bc_registries.corp_name 
						where corp_num = %s and end_event_id is null
						  and corp_name_typ_cd in ('TR', 'NO')"""

select_tilma_recs = """select count(*) from bc_registries.tilma_involved 
						where corp_num = %s and end_event_id is null"""

select_jurisdiction_recs = """select count(*) from bc_registries.jurisdiction 
						where corp_num = %s and end_event_id is null"""

def run_corp_sql(corp_num, sql):
	new_sql = '' + sql
	return new_sql.replace('%s', "'" + corp_num + "'")

def test_generate_corp_nums():
    print('corp_num,corp_type,corp_state,party_ct,party_addr_ct,name_ct,name_assumed_ct,name_trans_ct,tilma_ct,jurisdiction_ct')
    with BCRegistries(False) as bc_registries:
        corp_rows = bc_registries.get_bcreg_sql('event', select_corp_sql)
        for corp in corp_rows:
            party_ct        = bc_registries.get_bcreg_sql('corp_party', run_corp_sql(corp['corp_num'], select_party_recs))
            party_addr_ct   = bc_registries.get_bcreg_sql('office', run_corp_sql(corp['corp_num'], select_party_addr_recs))
            name_ct         = bc_registries.get_bcreg_sql('name', run_corp_sql(corp['corp_num'], select_name_recs))
            name_assumed_ct = bc_registries.get_bcreg_sql('name', run_corp_sql(corp['corp_num'], select_name_assumed_recs))
            name_trans_ct   = bc_registries.get_bcreg_sql('name', run_corp_sql(corp['corp_num'], select_name_trans_recs))
            tilma_ct        = bc_registries.get_bcreg_sql('tilma_involved', run_corp_sql(corp['corp_num'], select_tilma_recs))
            juisdiction_ct  = bc_registries.get_bcreg_sql('jurisdiction', run_corp_sql(corp['corp_num'], select_jurisdiction_recs))

            print(corp['corp_num'] + ',' + corp['corp_typ_cd'] + ',' + corp['state_typ_cd'] + ',' + 
	            	str(party_ct[0]['count']) + ',' + str(party_addr_ct[0]['count']) + ',' + 
	                str(name_ct[0]['count']) + ',' + str(name_assumed_ct[0]['count']) + ',' + 
	                str(name_trans_ct[0]['count']) + ',' + str(tilma_ct[0]['count']) + ',' +
	                str(juisdiction_ct[0]['count']))

