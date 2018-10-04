
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
						      and corp.corp_typ_cd in ('A','LLC','BC','C','CUL','ULC','SP')))
						order by corp.corp_num"""

select_corp_scenario_sql = """select corp.corp_num, corp.corp_typ_cd, state.state_typ_cd
						  from bc_registries.corporation corp, bc_registries.corp_state state
						where corp.corp_num = state.corp_num
						  and state.end_event_id is null
						  and corp.corp_num in ( %s )"""

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

def _generate_corp_nums():
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

            print(corp['corp_num'] + ', ' + corp['corp_typ_cd'] + ', ' + corp['state_typ_cd'] + ', ' + 
	            	str(party_ct[0]['count']) + ', ' + str(party_addr_ct[0]['count']) + ', ' + 
	                str(name_ct[0]['count']) + ', ' + str(name_assumed_ct[0]['count']) + ', ' + 
	                str(name_trans_ct[0]['count']) + ', ' + str(tilma_ct[0]['count']) + ', ' +
	                str(juisdiction_ct[0]['count']) + ', ')

def test_generate_corp_nums():
    selected_corps = ['0628960','C1136065','C1102200','C1043095','0194696','0200463','0123383','0030194',] # 0194696', 'A0059733','A0040189','A0059933','A0060938','A0060045',]
    """
						'LP0450925',
						'FM0525021',
						'FM0508782',
						'FM0491681',
						'FM0491646',
						'FM0476264',
						'FM0443902',
						'FM0431330',
						'FM0407348',
						'FM0355592',
						'FM0283294',
						'FM0283292',
						'FM0137005',
						'0043687',
						'0384698',
						'0446323',
						'0613083',
						'0614205',
						'0713939',
						'0765995',
						'0790280',
						'0827071',
						'0830501',
						'0858892',
						'0874259',
						'0874260',
						'A0031179',
						'A0039015',
						'A0053427',
						'A0053864',
						'A0057212',
						'A0078116',
						'C0499505',
						'C0610814',
						'C0874156',
						'LLC0000221',
					  ]
    """
    selected_corp_list = ''
    i = 0
    for corp in selected_corps:
        selected_corp_list = selected_corp_list + "'" + corp + "'"
        i = i + 1
        if i < len(selected_corps):
            selected_corp_list = selected_corp_list + ', '
    with BCRegistries(False) as bc_registries:
        sql = select_corp_scenario_sql.replace('%s', selected_corp_list)
        corp_rows = bc_registries.get_bcreg_sql('event', sql)
        print('sample_test_corps = {')
        for corp in corp_rows:
            party_ct        = bc_registries.get_bcreg_sql('corp_party', run_corp_sql(corp['corp_num'], select_party_recs))
            party_addr_ct   = bc_registries.get_bcreg_sql('office', run_corp_sql(corp['corp_num'], select_party_addr_recs))
            name_ct         = bc_registries.get_bcreg_sql('name', run_corp_sql(corp['corp_num'], select_name_recs))
            name_assumed_ct = bc_registries.get_bcreg_sql('name', run_corp_sql(corp['corp_num'], select_name_assumed_recs))
            name_trans_ct   = bc_registries.get_bcreg_sql('name', run_corp_sql(corp['corp_num'], select_name_trans_recs))
            tilma_ct        = [{'count':0}] # bc_registries.get_bcreg_sql('tilma_involved', run_corp_sql(corp['corp_num'], select_tilma_recs))
            juisdiction_ct  = bc_registries.get_bcreg_sql('jurisdiction', run_corp_sql(corp['corp_num'], select_jurisdiction_recs))

            with BCRegistries(True) as bc_cache_reg:
	            bc_cache_reg.cache_bcreg_corp_tables([corp['corp_num']], True)
	            sqls = bc_cache_reg.generated_sqls
	            fake_corp_num = bc_cache_reg.add_generated_corp_num(corp['corp_num'])

            print('    "corp_' + fake_corp_num + '": {')
            print('            "corp_num":' + "'" + fake_corp_num + "'" + ', ' + '"corp_typ_cd":' + "'" + corp['corp_typ_cd'] + "'" + ', ' + 
            	    '"state_typ_cd":' + "'" + corp['state_typ_cd'] + "'" + ', ' + 
	            	'"party_ct":' + str(party_ct[0]['count']) + ', ' + '"party_addr_ct":' + str(party_addr_ct[0]['count']) + ', ' + 
	                '"name_ct":' + str(name_ct[0]['count']) + ', ' + '"name_assumed_ct":' + str(name_assumed_ct[0]['count']) + ', ' + 
	                '"name_trans_ct":' + str(name_trans_ct[0]['count']) + ', ' + '"tilma_ct":' + str(tilma_ct[0]['count']) + ', ' +
	                '"juisdiction_ct":' + str(juisdiction_ct[0]['count']) + ', ')
            print('             "sqls": [')
            for sql in sqls:
                print('                    """' + sql.replace(' values ', '\n                    values\n                    ') + '""",')
            print('                   ]')
            print('             },')
        
        print('}')

