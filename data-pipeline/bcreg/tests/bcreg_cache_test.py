
import time

from bcreg.bcregistries import BCRegistries, system_type


def test_connect_bcreg():
    with BCRegistries() as bc_registries:
	    assert True

def test_table_query():
    with BCRegistries() as bc_registries:
    	datas = bc_registries.get_bcreg_table('party_type')
    	assert 24 == len(datas)

def test_corp_query():
    with BCRegistries() as bc_registries:
    	datas = bc_registries.get_bcreg_corp_table('event', '0641655')
    	assert 17 == len(datas)

def test_local_cache():
    with BCRegistries() as bc_registries:
    	datas = bc_registries.get_bcreg_table('party_type')
    	assert 24 == len(datas)

    	bc_registries.cache_data('party_type', ['party_typ_cd'], datas)

    	rec1 = bc_registries.get_cache_data_pk('party_type', ['party_typ_cd'], ['FBO'])
    	assert rec1 != None

    	datas = bc_registries.get_bcreg_corp_table('event', '0641655')
    	assert 17 == len(datas)

    	bc_registries.cache_data('event', ['event_id'], datas)

    	recs2 = bc_registries.get_cache_data_keys('event', ['event_typ_cd'], ['FILE'])
    	assert 15 == len(recs2)
