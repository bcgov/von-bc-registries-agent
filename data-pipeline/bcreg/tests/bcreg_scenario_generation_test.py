
import time

from bcreg.bcregistries import BCRegistries, system_type, MIN_START_DATE, MAX_END_DATE
from bcreg.eventprocessor import EventProcessor
from bcreg.tests.sample_corps import sample_test_corps


def test_generate_corp_sql():
    specific_corps = [
                    'A0059733','A0040189','A0059933','A0060938','A0060045',
                    ]
    
    with BCRegistries(True) as bc_registries:
        for corp in specific_corps:
            #print('=========================')
            print('===== ',  corp)
            bc_registries.cache_bcreg_corp_tables([corp], True)
            sqls = bc_registries.generated_sqls
            fake_corp_num = bc_registries.add_generated_corp_num(corp)
            print('=============>>> ', fake_corp_num)
            #print('=========================')
            #print('sqls:')
            #for sql in sqls:
            #    print('"""' + sql.replace(' values ', '\nvalues\n') + '""",')
            #print('=========================')
 
            with BCRegistries(True) as cached_bc_reg:
                cached_bc_reg.cache_bcreg_code_tables()
                cached_bc_reg.insert_cache_sqls(sqls)

                # try running with dummy event id zero 
                corp_info = cached_bc_reg.get_bc_reg_corp_info(fake_corp_num)
                #print('-------------------------')
                #print('corp_info:')
                #print(corp_info)
                #print('-------------------------')

            start_event = {'event_id':0, 'event_date':MIN_START_DATE}
            end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
            with EventProcessor() as event_processor:
                corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, fake_corp_num, corp_info)
                #print('-------------------------')
                #print('corp_creds:')
                #print(corp_creds)
                #print('-------------------------')

def test_specific_corp_scenario():
    corp_num = '6096127'
    corp_sqls = [
            """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
            """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
            values
            (105820465, null, null, 'FM8694883', 'FBO', 105039871, null, null, null, null, '1981-07-03 00:00:00', null, null, null, null, '0641655Y QDSSDFWICJOJESKXZ ', '6096127', null, null, null, null, null)""",
            """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (5511129, '6096127', 'CONVICORP', '2004-03-26 20:36:00', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (5511130, '6096127', 'FILE', '2004-03-10 00:00:00', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (5511131, '6096127', 'FILE', '2004-03-10 00:00:00', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (5511132, '6096127', 'FILE', '2002-02-06 00:00:00', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (6245683, '6096127', 'ADCORP', '2005-04-20 16:02:27', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (6245701, '6096127', 'FILE', '2005-04-20 16:06:43', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (7055682, '6096127', 'FILE', '2006-04-12 14:37:52', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (7549434, '6096127', 'FILE', '2007-03-05 09:00:12', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (7591037, '6096127', 'FILE', '2007-03-28 15:16:53', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (9141401, '6096127', 'FILE', '2009-12-15 16:51:57', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (6245023, '6096127', 'FILE', '2005-04-20 15:48:29', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (8257866, '6096127', 'FILE', '2008-05-08 12:16:30', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (8855073, '6096127', 'FILE', '2009-06-04 10:32:15', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (8855876, '6096127', 'FILE', '2009-06-04 15:02:00', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (8855913, '6096127', 'FILE', '2009-06-04 15:11:53', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (9235934, '6096127', 'FILE', '2012-02-03 11:53:59', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (9235935, '6096127', 'FILE', '2012-02-03 11:54:30', null)""",
            """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
            values
            (105039871, 'FM8694883', 'CONVFMREGI', '1981-07-03 00:00:00', null)""",
            """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (5511130, 'CONVL', '2004-03-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (5511131, 'CONVL', '2004-03-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (5511132, 'CONVL', '2002-02-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (6245023, 'ANNBC', '2005-04-20 15:48:29', null, null, '2005-02-06 00:00:00', null, 'N', null, null, 'F ', null, '102532462', null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (6245701, 'TRANS', '2005-04-20 16:06:43', null, null, null, null, 'N', null, null, 'F ', 6245701, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (7055682, 'ANNBC', '2006-04-12 14:37:52', null, null, '2006-02-06 00:00:00', null, 'N', null, null, 'F ', null, '105437040', null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (7549434, 'ANNBC', '2007-03-05 09:00:12', null, null, '2007-02-06 00:00:00', null, 'N', null, null, 'F ', null, '108353590', null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (7591037, 'NOALA', '2007-03-28 15:16:53', null, null, null, null, 'N', null, null, 'F ', 7591037, null, 'NR6422424', null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (8257866, 'ANNBC', '2008-05-08 12:16:30', null, null, '2008-02-06 00:00:00', null, 'N', null, null, 'F ', null, '111282232', null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (8855073, 'ANNBC', '2009-06-04 10:32:15', null, null, '2009-02-06 00:00:00', null, 'N', null, null, 'F ', null, '114301161', null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (8855876, 'NOALU', '2009-06-04 15:02:00', null, null, null, null, 'N', null, null, 'F ', 8855876, null, 'NR8796381', null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (8855913, 'NOCDR', '2009-06-04 15:11:53', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (9141401, 'NOCAD', '2009-12-16 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (9235934, 'ANNBC', '2012-02-03 11:53:59', null, null, '2010-02-06 00:00:00', null, 'N', null, null, 'F ', null, '117411967', null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (9235935, 'ANNBC', '2012-02-03 11:54:30', null, null, '2011-02-06 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
            """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
            values
            (105039871, 'FRREG', '1981-07-03 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
            """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
            """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
            values
            ('6096127', null, 'ULC', '2002-02-06 00:00:00', '2011-02-06 00:00:00', '2005-04-20 16:06:43', null, null, null, 'DXACRIXX', 'IKMQPBMP', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
            """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
            values
            ('FM8694883', null, 'SP', '1981-07-03 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
            """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
            """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
            """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
            values
            ('6096127', 5511129, null, 'ACT', null)""",
            """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
            values
            ('FM8694883', 105039871, null, 'ACT', null)""",
            """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
            """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
            """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
            """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
            values
            ('6096127', 'CO', 8855876, 1, null, 'ZRNSHTSBJWOFBYGLINWP', 'QZITQDNKIDIZKUWBCR RHFJMH', null)""",
            """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
            values
            ('6096127', 'CO', 5511129, 0, 7591037, 'PYWAJCFUEPLUIRTCNQQB', 'OSZUOXJZVZSYKYTAADRNOPHPR', null)""",
            """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
            values
            ('6096127', 'CO', 7591037, 1, 8855876, 'SXDEUETULEXXDMCYWTYK', 'BTNLFMWTESSLUJCWYI GBLQAY', null)""",
            """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
            values
            ('FM8694883', 'CO', 105039871, 0, null, 'TPTPYBIICTYEVFMKKPCF', 'FLOHTOGCRGKGIPWBZHDUZLFZC', null)""",
            """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
            """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
            values
            ('6096127', 'RC', 6245701, 9141401, 2836997, 2836996, null, null)""",
            """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
            values
            ('6096127', 'RG', 6245701, 9141401, 2836999, 2836998, null, null)""",
            """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
            values
            ('6096127', 'RG', 5511129, 6245701, 1606746, 1606746, null, null)""",
            """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
            values
            ('6096127', 'RC', 5511129, 6245701, 1606746, 1606746, null, null)""",
            """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
            values
            ('6096127', 'RG', 9141401, null, 7404645, 7404644, null, null)""",
            """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
            values
            ('6096127', 'RC', 9141401, null, 7404643, 7404642, null, null)""",
            """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (1606746, 'BC', 'CA', 'MHIFWS', 'JYFSNUJMIOZINBMIQYCUDUSAR', 'BAMEPDCRMR YDZWOJPGVFWLTJ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (2836996, 'BC', 'CA', '5JFPB2', 'VPDBKQIF XSDDIFT NLPEIOMV', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (2836997, 'BC', 'CA', 'A645UW', 'PNIVFCTTGZSTCNCLSUFCHG ZK', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (2836998, 'BC', 'CA', 'TNOGDH', ' WCYXRKOAAPNTOKSB WFYGGEV', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (2836999, 'BC', 'CA', '4OK4EI', ' HELE CXXVVWCNATIDDBXAEEU', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (7404642, 'BC', 'CA', 'VSX7G8', 'AADWCOLUFJSASZQBFCWMOHJHN', 'WTVJIGYKXAHGZTYEEBRGLIDLO', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (7404643, 'BC', 'CA', 'C8886D', 'ZXXIBPHZQJBRXTTQRO HCSRAI', 'BYSCABJETMIFAX MIHLBTBAAE', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (7404644, 'BC', 'CA', 'VYXN94', 'RIILJCAEYEHMTZFGLJMLEOPHE', 'RNVOLRLYGKSWKKOUUEE FYOUO', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
            """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
            values
            (7404645, 'BC', 'CA', '2IFBB1', 'QUAETPPSJOXNSKSYYVY NWPHK', 'IWLXVNQKIAYDNUUGKDZRVSBYM', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
    ]

    with BCRegistries(True) as cached_bc_reg:
        cached_bc_reg.cache_bcreg_code_tables()
        cached_bc_reg.insert_cache_sqls(corp_sqls)

        # try running with dummy event id zero 
        corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num)
        #print('-------------------------')
        #print('corp_info:')
        #print(corp_info)
        #print('-------------------------')

    start_event = {'event_id':0, 'event_date':MIN_START_DATE}
    end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
    with EventProcessor() as event_processor:
        corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp_num, corp_info)
        #print('-------------------------')
        #print('corp_creds:')
        #print(corp_creds)
        #print('-------------------------')

# no assertions, just make sure all test data is working
def test_preset_corp_scenario_all():
    for test_corp in sample_test_corps.keys():
        corp_num = sample_test_corps[test_corp]['corp_num']
        corp_sqls = sample_test_corps[test_corp]['sqls']

        with BCRegistries(True) as cached_bc_reg:
            cached_bc_reg.cache_bcreg_code_tables()
            cached_bc_reg.insert_cache_sqls(corp_sqls)
            corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num)

        start_event = {'event_id':0, 'event_date':MIN_START_DATE}
        end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
        with EventProcessor() as event_processor:
            corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp_num, corp_info)

        #print("Corp: " + corp_num + " generated " + str(len(corp_creds)) + " credentials")

# load a specific corporation and make some assertions on the generated credentials
def test_preset_corp_scenario_3dbas():
    # use corp corp_A5589691
    corp_num = sample_test_corps['corp_A5589691']['corp_num']
    corp_sqls = sample_test_corps['corp_A5589691']['sqls']

    with BCRegistries(True) as cached_bc_reg:
        cached_bc_reg.cache_bcreg_code_tables()
        cached_bc_reg.insert_cache_sqls(corp_sqls)
        corp_info = cached_bc_reg.get_bc_reg_corp_info(corp_num)

    start_event = {'event_id':0, 'event_date':MIN_START_DATE}
    end_event   = {'event_id':9999999999, 'event_date':MAX_END_DATE}
    with EventProcessor() as event_processor:
        corp_creds = event_processor.generate_credentials(system_type, start_event, end_event, corp_num, corp_info)

    #print(corp_creds)
    assert len(corp_creds) == 6
    assert corp_creds[1]['cred_type'] == 'REG'
    assert corp_creds[2]['cred_type'] == 'ADDR'
    assert corp_creds[3]['cred_type'] == 'REL'
    assert corp_creds[4]['cred_type'] == 'REL'
    assert corp_creds[5]['cred_type'] == 'REL'
