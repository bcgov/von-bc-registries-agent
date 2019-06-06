#!/usr/bin/python
import psycopg2
import datetime
from bcreg.config import config
from bcreg.eventprocessor import EventProcessor, CORP_TYPES_IN_SCOPE
from bcreg.bcregistries import BCRegistries, system_type

specific_corps = [ 
                    '0641655',
                    '0820416',
                    '0700450',
                    '0803224',
                    'LLC0000192',
                    'C0277609',
                    'A0072972',
                    'A0051862',
                    'C0874156',
                    '0874244',
                    '0593707',
                    'A0068919',
                    'A0064760',
                    'LLC0000234',
                    'A0077118',
                    'A0062459',
                    '0708325',
                    '0679026',
                    '0707774',
                    'C0874057',
                    'A0028374',
                    'A0053381',
                    'A0051632',
                    '0578221',
                    'A0032100',
                    '0874088',
                    '0803207',
                    '0873646',
                    '0078162',
                    '0754041',
                    'XS1000180',
                    'LP1000140',
                    'A0059911',
                    'S1000080',
                    '0637981',
                    'A0051632',
                    '0578221',
                    '0497648',
                    'A0038634',
                    '0136093',
                    '0869404',
                    '0641396',
                    'LP0745132',
                    'C0283576',
                    '0860306',
                    '0673578',
                    '0763302',
                    '0860695',
                    'A0039853',
                    'A0036994',
                    '1185488',
                    '0979020',
                    '0354136',
                    '1164165',
                    '1059630',
                    '0093733',
                    '0197646',
                    'A0082127',
                    '0206786',
                    '0908182',
                    'FM005513',
                    '0616651',
                    'FM0418446',
                    'FM0464421',
                    'FM0464206',
                    '0143311',
                    '0006965',
                    'A0008669',
                    '0206483',
                    '0287583',
                    '0517093',
                    '0046062',
                    '0545062',
                    'A0027307',
                    '0046397',
                    '0503852',
                    'A0053913',
                    '0358554',
                    'C0184104',
                    'C0429174',
                    'A0020540',
                    '0693705',
                    '1101218',
                    '0650761',
                    '0928747',
                    '0347474',
                    '1101218',
                    '0450252',
                    'A0056744',
                    'A0087698',
                    'A0087699',
                    '0296354',
                    '0859276',
                    'A0045786',
                    '0791684',
                    '0675400',
                    '0675765',
                    'A0107449',
                    'A0107446',
                    'A0107438',
                    '1181944',
                    'A0107427',
                    'A0107426',
                    'A0107424',
                    'A0107423',
                    '0142362',
                    'FM0550949',
                    'FM0501860',
                    '0643505',
                    '0510537',
                    'C0733137',
                    'FM0327778',
                    'FM0327777',
                    'FM0327770',
                    'FM0327756',
                    '1188712',
                    '0855234',
                    'A0093289',
                    'A0053723',
                    'A0082657',
                    '0319629',
                    '0747962',
                    'A0011423',
                    'A0080841',
                    '0945957',
                    'A0092209',
                    'A0070194',
                    '0338518',
                    '1199242',
                    '0072808',
                    '0946908',
                    '0730909',
                    '1198849',
                    '0149514',
                    '0390058',
                    # more test data from the additional company types
                    '1071287', # very short credential effective periods
                    '1001845',
                    'FM0472969', # for Dissolution effective date -> event.trigger_dts field for the dissolution filing event
                    'FM0345136', # for Each section of the timeline should reference the name at that point in time
                    'XP0068811', # for It is not accurate to say a firm is related to itself
                    'FM0547930', # for A number of PROD entities I attempted to test with do not appear in VON
                    'FM0027827', 'LP0043506', 'LP0004424', 'XP0646920', 'LL0000038', 'LL0000063', 'MF0000041', 'MF0000022',
                    'LL0000145', # for All status changes (from active to historical and vice versa) should be displayed in the timeline
                    'S0000009', 
                    'S0000872', # for “0001-01-01” displays as “Dec 31, 1” on the Organization data.  Displays as “Dec 31, 1, 11:40 PM” on the Credential data
                    'XS0054137', # forThey reinstated (became active) and then 10 minutes later changed jurisdiction.  The reinstatement is either missing or not visible on the timeline. Home Jurisdiction is British Columbia on the first credential and should be Ontario.  Home Jurisdiction is British Columbia on the second credential and should be Federal
                    'XS0059885', # for Has 2 credentials because of a change of jurisdiction. Home Jurisdiction is British Columbia on the first credential and should be Ontario.  Home Jurisdiction is British Columbia on the second credential and should be Federal.
                    '1047742', # for had a “Correction - Put Back On” on March 16 making it active.  It is currently active in COLIN.  However the Orgbook shows it as historical
                    'FM0688355', # Relationships are not consistently showing. FM0688355 is a firm owned by CP0001939 ...
                    'CP0001939', # 
                    'FM0415725', # FM0415725, is also now only showing relationships on the corporate owner
                    'A0101881', # owner of FM0415725
                    'XS0015243', # Home jurisdiction is displaying as 'BC' when no record exists in CPRD.Jurisdiction. In these cases we are better off to have nothing display at all. E.g. XS0015243.
                    'CP0000527', # Registration type shows as CO-OPS when looking up CO-OP records. For corp_typ_cd 'A' or 'BC' we use the corp_type.full_desc from the DB. CO-OPS should also use the full_desc (Cooperative). E.g. CP0000527.
                    'CP0000527', # Credential reason is rendering with code for certain COOP records. E.g. for CP0000527
                    'CP0000103', #
                    'CP0000851', # In the DB the entity became historical due to amalgamation (HAM) as of event ID 102030389 which occurred on 1976-12-31 00:00:00. In VON we are seeing the status of HIS as a result of a System to D2 event on Feb 26, 2019.
                    'CP0001048', # In the DB the date for the creation event which set the entity to active and listed the first name is 1899-12-31. In VON the main search shows the name effective date as a day earlier – 1899-12-30. Date issue also exists when you select the first section of the timeline and in that case both the date and the time are wrong.
                    'FM0745134', # Error'ed in Prod
                    'FM0485314',
                    'FM0616907',
                    'FM0429408',
                    'FM0415725',
                    'FM0485314',
                    'FM0616907',
                    'FM0429408',
                    '1204452',  # relationship issues between these next 3
                    'FM0777306',
                    'FM0776052',
                    'FM0368694', # didn't show up in test
                    'S0047404',
                    'PA0000027', # last round of test corps
                    'PA0000139',
                    'PA0000159',
                    'PA0000375',
                    ]

with BCRegistries() as bc_registries:
    # get 5 corps for each type in scope (in addition to the above list)
    for corp_type in CORP_TYPES_IN_SCOPE:
        print(corp_type)
        sql = """
                select corp_num
                from bc_registries.corporation
                where corp_typ_cd = '""" + corp_type + """'
                order by corp_num desc
               """
        corps = bc_registries.get_bcreg_sql("corps_by_type", sql, cache=False)
        n_corps = min(len(corps), 5)
        for i in range(n_corps):
            specific_corps.append(corps[i]['corp_num'])

    with EventProcessor() as event_processor:
        print("Get last processed event")
        prev_event_id = 0

        print("Get last max event")
        max_event_date = bc_registries.get_max_event_date()
        max_event_id = bc_registries.get_max_event(max_event_date)
        #max_event_id = 101944500 
        #max_event_date = bc_registries.get_event_id_date(max_event_id)
        
        # get specific test corps (there are about 6)
        print("Get specific corps")
        corps = bc_registries.get_specific_corps(specific_corps)
        
        print("Find unprocessed events for each corp")
        last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
        max_event_dt = bc_registries.get_event_effective_date(max_event_id)
        corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id, max_event_dt, corps)
        
        print("Update our queue")
        event_processor.update_corp_event_queue(system_type, corps, max_event_id, max_event_date)
