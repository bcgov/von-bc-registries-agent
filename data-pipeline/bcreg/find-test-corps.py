#!/usr/bin/python
import psycopg2
import datetime
import os
import logging

from bcreg.config import config
from bcreg.eventprocessor import EventProcessor
from bcreg.bcregistries import BCRegistries, system_type, CORP_TYPES_IN_SCOPE

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


specific_corps = [ '0176097', '0318626', '0178676', 'A0027307',
'0850561', 'S0022307', '0985072', 'FM0642692', '0235191', '0776468', '0964721', 'CP0002142', '1201327', '0162193', 
'0892096', '1127323', '1144899', '1229738', 'FM0806913', 'FM0830112', '0035275', '0198595', '1021665', '1180036', 
'FM0804695', 'FM0828031', 'FM0830348', '0542088', '0568848', 'S0032541', '0940071', '0952499', 'CP0002237', '1245938', 
'FM0799231', '1238236', 'A0016625', '0417313', '0610234', '1219686', 'FM0837580', 'FM0805900', '0587568', '0908923', 
'1158210', '1234789', '1033110', 'FM0827327', 'A0111729', 'FM0814754', '0057932', '0725023', '0760854', 'FM0822126', 
'0088656', 'FM0419486', '0991963', 'FM0815856', '0200021', '0603291', '1067184', 'FM0818374', 'C1248832', '0322577', 
'FM0826478', 'FM0808080', '0541894', '0651522', '0681303', '0849645', '1011412', 'CP0002337', '0855250', '1273661', 
'FM0809164', '0760609', 'FM0803272', 'C1248024', '0591347', 'FM0644889', '1011166', 'CP0002069', 'CP0002232', 'FM0803309', 
'FM0804348', '0354564', '0757904', '0766824', '0835393', 'S0049674', 'FM0759498', '0177353', '0423581', '0717689', 
'0826129', '0862700', 'FM0784632', 'FM0828597', '0413649', '0915930', 'FM0725913', 'FM0810088', '1247184', '0688148', 
'FM0418993', '0933377', '0940325', '0975572', '1069906', 'C1153116', 'CP0001794',
'0045728', '0071773', '0055099', '0891085', '0036860', '0007021', '0108610', 'S0001104', '0025099', '0040909', 'A0113685', 'A0113677',
'XP0538736', 'A0117171', 'XS0073189', 'LLC0001117', 'A0062479', 'A0016173',
'1255957',
'0550474','0610101','0641159','A0041040','A0070209','A0075317','0598327','0757892',
]

specific_corps_2 = [
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
                    '0277447',   # missing in prod
                    'FM0780183', # dba for the above
                    '0276176',   # quartech
                    'S1000224',  # errored out in test
                    'FM1000148',
                    'FM1000145',
                    'FM1000020',
                    'FM1000019',
                    'FM1000331',
                    'FM1000146',
                    'FM1000018',
                    'FM1000200',
                    'FM0743811', # potential deadlock issues
                    '0964770',
                    'FM0653232',
                    'FM0784088',
                    'FM0769586',
                    'FM0784089',
                    'FM0649949',
                    'FM0649943',
                    'FM0649946',
                    'C1218404',
                    'FM0784092',
                    'FM0783805',
                    'FM0784112',
                    '1136244',
'0786125', '0805487', '0857035', '1146610', '1221189', 'LL0001586', '1146432', 'FM0786101', '0788664', 'FM0786068', 'C1221192', '1221199', 'FM0786071', '1050538', 'FM0786094', '0712502', '0921740', '1073125', '1113564', '1191606', '1220807', 'A0110897', 'FM0786099', '0714019', '0803629', '1170226', '0989579', '1050151', '1146495', 'FM0786104', '0733489', '1139377', '1203043', 'A0110898', '0747068', '0842810', '1053874', '1080979', 'FM0786103', 'FM0786105', 'FM0786107', '0728412', '0773237', '0909072', '1146905', '0764208', '0981555', '1059466', '0951462', '0958642', '0978647', '1196759', '1221191', '0804112', '0865102', '1011794', 'FM0786070', '0392781', '0886926', '0929091', '1044485', '1146454', '0788671', '0803927', '0820240', '0820773', '0914456', '1062602', '1221195', 'FM0786098', '0811943', '1196120', '1202694', '1221188', '1219810', 'FM0786096', 'FM0786069', '1062713', '0857107', '0872623', '1041100', '1047420', '1221091', '1221198', 'FM0786102', '0779758', '0979020', '1023677', '1059918', '1154479', '1205923', '1217785', 'A0110899', 'FM0786097', '0898643', '1032093', '1041245', '0941797', '1158755', '1217934', '1221197', 'FM0786100', 'FM0786095', '0899190', '1081464', 'A0110896', '0818116', '0938923', '1053137', '1191976', 'FM0786074', 'FM0786106', '1125622', '1221200', '1221193', '0693705', '0747568', '0931646', '0733162', '0788683', '0801423', '1221190', '1221196', '1221194', '0738753', '1191667', '1209635', '1217177', '0842348', '1101251', '1219655', 'FM0786072', '1011546', '1009629', '1146464',
'A0080609', '1099982', '0730805', 'A0077091', '1091495', '0332563', '0378593', '0317167', '0618270', '0798257', '0953267', '1162048', 'A0091542', 'A0101682', 'A0071533', '0965000', 'A0098806', '1125543', '1194624', '1215860', '0730937', 'A0067077', '0458948', '1057027', '1213440', '0852418', '0978351', 'A0106584', 'A0053149', '1219032', '1028915', '1213465', '0530692', '0704567', '1110376', '0703754', '0979990', 'FM0760271', '0207899', '0718055', '0504939', '0636414', '1028921', '0775430', '0916103', 'A0097981', '1131823', '0479710', '0454816', '0788674',
                    '1225093', # ticket # 847
                    'FM0514501',
                    'A0067332',
                    'C1224093',
                    'S0001569',
                    'FM0783403',  # latest batch of test data
                    'FM0782737',
                    '1214962',
                    '1215240',
                    'FM0783301',
                    'FM0781697',
                    '1217143',
                    '1217769',
                    'FM0781343',
                    'A0110609',
                    'LP0781421',
                    '1217576',
                    '1214853',
                    'XP0782410',
                    '1217989',
                    '1216391',
                    '1216440',
                    '1214861',
                    '1214854',
                    '1215239',
                    'A0110364',
                    'A0110579',
                    'XP0783279',
                    'FM0781564',
                    'FM0783319',
                    '1217306',
                    'FM0782128',
                    'FM0782631',
                    'A0110346',
                    '1216444',
                    '1216882',
                    '1216439',
                    'FM0782551',
                    '1216443',
                    'S0071602',
                    'FM0781674',
                    'FM0781671',
                    '1215396',
                    '1214599',
                    '1214434',
                    'FM0782584',
                    'S0071582',
                    'A0110363',
                    '1217577',
                    '1215060',
                    '1217554',
                    '1217112',
                    'A0043183', # additional test corps
                    'FM0251249',
                    'FM0606634',
                    'FM0251484',
                    'LP0438693',
                    '1219655',
                    '1219810',
                    'FM0130037',
                    '0786125', '0805487', '0857035', '1146610', '1221189', 'LL0001586', '1146432', 'FM0786101', '0788664', 'FM0786068', 'C1221192', '1221199', 'FM0786071', '1050538', 'FM0786094', '0712502', '0921740', '1073125', '1113564', '1191606', '1220807', 'A0110897', 'FM0786099', '0714019', '0803629', '1170226', '0989579', '1050151', '1146495', 'FM0786104', '0733489', '1139377', '1203043', 'A0110898', '0747068', '0842810', '1053874', '1080979', 'FM0786103', 'FM0786105', 'FM0786107', '0728412', '0773237', '0909072', '1146905', '0764208', '0981555', '1059466', '0951462', '0958642', '0978647', '1196759', '1221191', '0804112', '0865102', '1011794', 'FM0786070', '0392781', '0886926', '0929091', '1044485', '1146454', '0788671', '0803927', '0820240', '0820773', '0914456', '1062602', '1221195', 'FM0786098', '0811943', '1196120', '1202694', '1221188', '1219810', 'FM0786096', 'FM0786069', '1062713', '0857107', '0872623', '1041100', '1047420', '1221091', '1221198', 'FM0786102', '0779758', '0979020', '1023677', '1059918', '1154479', '1205923', '1217785', 'A0110899', 'FM0786097', '0898643', '1032093', '1041245', '0941797', '1158755', '1217934', '1221197', 'FM0786100', 'FM0786095', '0899190', '1081464', 'A0110896', '0818116', '0938923', '1053137', '1191976', 'FM0786074', 'FM0786106', '1125622', '1221200', '1221193', '0693705', '0747568', '0931646', '0733162', '0788683', '0801423', '1221190', '1221196', '1221194', '0738753', '1191667', '1209635', '1217177', '0842348', '1101251', '1219655', 'FM0786072', '1011546', '1009629', '1146464',
                    'A0080609', '1099982', '0730805', 'A0077091', '1091495', '0332563', '0378593', '0317167', '0618270', '0798257', '0953267', '1162048', 'A0091542', 'A0101682', 'A0071533', '0965000', 'A0098806', '1125543', '1194624', '1215860', '0730937', 'A0067077', '0458948', '1057027', '1213440', '0852418', '0978351', 'A0106584', 'A0053149', '1219032', '1028915', '1213465', '0530692', '0704567', '1110376', '0703754', '0979990', 'FM0760271', '0207899', '0718055', '0504939', '0636414', '1028921', '0775430', '0916103', 'A0097981', '1131823', '0479710', '0454816', '0788674',
                    '1196236',
                    'FM0786693', '0392781', '1222085', '1221842', '1221944', '1221909', '1221947',
                    '0686268','FM0621367',
                    'FM0789723',
                    '1237010',
                    '1237089',
                    '1237149',
                    '1237164',
                    '1237228',
                    '1237234',
                    '1237247',
                    '1235577',
                    '1236975',
                    '1237281',
                    '1236398',
                    '0036103',
                    '0014947',
                    '0020288',
                    '0163588',
                    '0187871',
                    '0640905',
                    '0131809',
                    '0337062',
                    '0496513',
                    '0337062',
                    '1156638',
                    '1164820',
                    '1052899', # test cases Sept 1
                    'S0073442',
                    'FM0810412',
                    '1256313',
                    'FM0810423',
                    '1257153',
                    'A0113969',
                    'FM0810236',
                    'C1257482',
                    '1257499',
                    '1257336',
                    'FM0810201',
                    'FM0811249',
                    'FM0811249',
                    'C1256334',
                    'CP0002369',
                    'S0073434',
                    '1263326',
                    '1265645',
                    '0003938',
                    '0837735',
                    '1016676',
                    '1052899',
                    'A0010928',
                    'FM0406835',
                    'FM0550116',
                    'FM0167199',
                    '0102493',
                    '1331277',
]


num_corps_per_type = 5


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
       n_corps = min(len(corps), num_corps_per_type)
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
        corps_2 = bc_registries.get_specific_corps(specific_corps_2)
        corps.extend(corps_2)

        print("Find unprocessed events for each corp")
        last_event_dt = bc_registries.get_event_effective_date(prev_event_id)
        max_event_dt = bc_registries.get_event_effective_date(max_event_id)
        corps = bc_registries.get_unprocessed_corp_events(prev_event_id, last_event_dt, max_event_id, max_event_dt, corps)
        
        print("Update our queue")
        event_processor.update_corp_event_queue(system_type, corps, max_event_id, max_event_date)
