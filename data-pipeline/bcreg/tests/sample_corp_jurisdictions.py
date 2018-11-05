
sample_test_jurisdiction_corps = {
    "corp_A5215485": {
            "corp_num":'A5215485', "corp_typ_cd":'A', "state_typ_cd":'RCF', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290453, 255713, 255713, 'A5215485', 'ATT', 605584, null, null, null, null, null, null, 'BENTZ ', null, 'BRIAN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290454, 255714, 255714, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'BENTZ', null, 'BRIAN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290455, 255715, 255715, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'CHALLENGER', null, 'PAUL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290456, 255716, 255716, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'CHAMBERLAIN', null, 'JANET P.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290457, 255717, 255717, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'DODD', null, 'PHILIP J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290458, 255718, 255718, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'EARLY', null, 'JOHN D.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290459, 255719, 255719, 'A5215485', 'OFF', 605584, null, null, null, null, null, null, 'FIDLER', null, 'CHRISTOPHER L.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290460, 255720, 255720, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'HODKINSON', null, 'DAVID J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290461, 255721, 255721, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'O''BRIEN', null, 'DANIEL T.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290462, 255722, 255722, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'POPE', null, 'BARRY R.B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290463, 255723, 255723, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'ROGERS', null, 'PETER A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (290464, 255724, 255724, 'A5215485', 'DIR', 605584, null, null, null, null, null, null, 'WOLSTENHOLME', null, 'IAN J.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6618689, 'A5215485', 'SYSD1', '2005-10-12 16:09:05', '2005-11-23 16:09:05')""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6676781, 'A5215485', 'ADMIN', '2005-11-08 15:36:42', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6802251, 'A5215485', 'SYSDF', '2006-01-09 23:20:36', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6717755, 'A5215485', 'SYSD2', '2005-11-28 23:16:49', '2006-01-09 23:16:49')""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (605584, 'A5215485', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (605585, 'A5215485', 'FILE', '2003-08-05 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (605585, 'CONVL', '2003-08-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A5215485', null, 'A', '2003-08-05 00:00:00', null, null, null, null, null, 'XAHDBZCK', 'AJPOVKDU', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A5215485', 605584, 6618689, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A5215485', 6618689, 6717755, 'D1F', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A5215485', 6802251, null, 'RCF', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A5215485', 6717755, 6802251, 'D2F', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A5215485', 605584, null, null, 'OT', 'COR', '1991-06-11 00:00:00', 'GB', null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A5215485', 'CO', 605584, 0, null, 'NLQYNHHBCMWCYJNMMXTD', 'VLYUJXXHMFQPAJUPFLIRCWOH ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A5215485', 'HD', 605584, null, 255712, 255712, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (255712, null, null, null, 'GQACSKQWJZDWYJK D ITLV WW', 'UZNLSWYTMYQLUAJGDKDZWQZUV', 'ENGLAND  CW8 2YA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A5462935": {
            "corp_num":'A5462935', "corp_typ_cd":'A', "state_typ_cd":'RCF', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (155862, 136445, 136445, 'A5462935', 'ATT', 380019, null, null, null, null, null, null, 'ROBINSON ', null, 'BEVERLEY N.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (155863, 136446, 136446, 'A5462935', 'DIR', 380019, null, null, null, null, null, null, 'SUROWIECKI', null, 'MAJ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (155864, 136447, 136447, 'A5462935', 'DIR', 380019, null, null, null, null, null, null, 'SUROWIECKI', null, 'MATT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (155865, 136447, 136447, 'A5462935', 'OFF', 380019, null, null, null, null, null, null, 'SUROWIECKI', null, 'MATT', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (380019, 'A5462935', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (380020, 'A5462935', 'CONVCAF', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A5462935', null, 'A', '1995-01-05 00:00:00', null, null, null, null, null, 'UHXNMCEV', 'MYWFYXXI', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A5462935', 380020, null, 'RCF', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A5462935', 380019, null, null, 'OT', 'COR', '1977-08-08 00:00:00', 'US, WA', null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A5462935', 'CO', 380019, 0, null, 'OHVUZKCCEWFXOKGYLOAM', 'GQJWSMFKQVJIXFYDI XVLWJHT', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A5462935', 'HD', 380019, null, 136444, 136444, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (136444, null, null, null, 'XZVDZOLRCFHDHGGRTSJTLNLFY', 'VMUMZPQJWJJJPBPHKHLVNFIED', '98178', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A4993014": {
            "corp_num":'A4993014', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (291312, 256493, 256493, 'A4993014', 'DIR', 606678, null, null, null, null, null, null, 'REUTER', null, 'OLIVER STEVEN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (291313, 256494, 256494, 'A4993014', 'DIR', 606678, null, null, null, null, null, null, 'VOLDENG', null, 'LISA', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6121737, 'A4993014', 'FILE', '2005-02-11 14:40:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6339479, 'A4993014', 'FILE', '2005-06-07 10:08:02', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7362051, 'A4993014', 'FILE', '2006-11-07 15:40:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7347508, 'A4993014', 'SYSD1', '2006-10-27 16:52:02', '2006-12-08 16:52:02')""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7362042, 'A4993014', 'FILE', '2006-11-07 15:39:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8027832, 'A4993014', 'FILE', '2007-12-17 11:33:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (606678, 'A4993014', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (606679, 'A4993014', 'FILE', '2003-08-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8492818, 'A4993014', 'FILE', '2008-10-15 10:51:03', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (606679, 'CONVL', '2003-08-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6121737, 'ANNXP', '2005-02-11 14:40:03', null, null, '2004-08-26 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6339479, 'NOCRX', '2005-06-07 10:08:02', null, null, null, null, 'N', null, null, 'P ', 6339479, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7362042, 'ANNXP', '2006-11-07 15:39:34', null, null, '2005-08-26 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7362051, 'ANNXP', '2006-11-07 15:40:59', null, null, '2006-08-26 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8027832, 'ANNXP', '2007-12-17 11:33:59', null, null, '2007-08-26 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8492818, 'ANNXP', '2008-10-15 10:51:03', null, null, '2008-08-26 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A4993014', null, 'A', '2003-08-26 00:00:00', '2008-08-26 00:00:00', null, null, null, null, 'JSFLQWQR', 'UDQZURTT', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A4993014', 606678, 7347508, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A4993014', 7347508, 7362042, 'D1F', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A4993014', 7362042, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4993014', 606678, 6121737, null, 'FD', 'COR', '2003-05-21 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4993014', 6121737, 6339479, null, 'FD', 'COR', '2003-05-21 00:00:00', null, '609871-1', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4993014', 6339479, null, null, 'FD', 'COR', '2003-05-21 00:00:00', null, '609871-1', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A4993014', 'CO', 606678, 0, null, 'GPNOLGGBSOVLYEPICIOR', 'QPVEXISNOANJSSSQBCODEHAOM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4993014', 'HD', 606678, 6339479, 256491, 256491, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4993014', 'HD', 6339479, null, 3014703, 3014702, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (256491, null, null, 'Y5TI4W', 'IGJZQWJXEEAYJIZDBQCDWTRBX', 'XVXZGF JRKDYAESMJXYEXUYKA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3014702, 'BC', 'CA', '6SZIHK', 'XUJJZVQAQFWKUPZFISTPMAKK ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3014703, 'BC', 'CA', 'B0TOXD', 'JRQIXBSYFXPHOBWUPKLDWEAMP', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A9168630": {
            "corp_num":'A9168630', "corp_typ_cd":'A', "state_typ_cd":'HAM', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (614790, 'A9168630', 'CONVAMAL', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (614791, 'A9168630', 'FILE', '2004-01-06 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (614791, 'CONVL', '2004-01-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A9168630', null, 'A', null, null, null, null, null, null, 'KRQBLZZR', 'LENIZLVL', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A9168630', 616615, null, 'HAM', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A9168630', 614790, 616615, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A9168630', 614790, null, null, 'OT', 'COR', '2003-11-19 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A9168630', 'CO', 614790, 0, null, 'CFPBGFSGSPXVYXZVODXV', 'TEXZ NEYKFOEAZHQJJWIFUSVL', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A9168630', 'HD', 614790, null, 1, 1, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1, 'BC', 'CA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A7164764": {
            "corp_num":'A7164764', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288778, 254215, 254215, 'A7164764', 'ATT', 603723, null, null, null, null, null, null, 'SNELL ', null, 'PETER V.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288779, 254216, 254216, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'BAIRD', null, 'LAURIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288780, 254217, 254217, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'INGLIS', null, 'CAMERON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288781, 254218, 254218, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'KING', null, 'DWAINE P.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288782, 254218, 254218, 'A7164764', 'OFF', 603723, null, null, null, null, null, null, 'KING', null, 'DWAINE P.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288783, 254219, 254219, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'LAWTON', null, 'JAMES E.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288784, 254219, 254219, 'A7164764', 'OFF', 603723, null, null, null, null, null, null, 'LAWTON', null, 'JAMES E.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288785, 254220, 254220, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'MANCINI', null, 'MARK DANIEL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288786, 254220, 254220, 'A7164764', 'OFF', 603723, null, null, null, null, null, null, 'MANCINI', null, 'MARK DANIEL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288787, 254221, 254221, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'SNELL', null, 'TERRY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288788, 254222, 254222, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'STOBART', null, 'SUSAN J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288789, 254223, 254223, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'TOWNSEND', null, 'WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288790, 254223, 254223, 'A7164764', 'OFF', 603723, null, null, null, null, null, null, 'TOWNSEND', null, 'WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288791, 254224, 254224, 'A7164764', 'DIR', 603723, null, null, null, null, null, null, 'WITTMIER', null, 'ELDEN L.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (288792, 254224, 254224, 'A7164764', 'OFF', 603723, null, null, null, null, null, null, 'WITTMIER', null, 'ELDEN L.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6475540, 'A7164764', 'FILE', '2005-08-08 13:20:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7627010, 'A7164764', 'FILE', '2007-04-23 08:57:50', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7767192, 'A7164764', 'FILE', '2007-07-16 12:58:40', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (603723, 'A7164764', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (603724, 'A7164764', 'FILE', '2003-06-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5863129, 'A7164764', 'FILE', '2004-08-27 15:11:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8340522, 'A7164764', 'FILE', '2008-07-02 07:10:56', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8902832, 'A7164764', 'FILE', '2009-07-08 08:31:20', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (603724, 'CONVL', '2003-06-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5863129, 'ANNXP', '2004-08-27 15:11:58', null, null, '2004-06-30 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6475540, 'ANNXP', '2005-08-08 13:20:34', null, null, '2005-06-30 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7627010, 'ANNXP', '2007-04-23 08:57:50', null, null, '2006-06-30 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7767192, 'ANNXP', '2007-07-16 12:58:40', null, null, '2007-06-30 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8340522, 'ANNXP', '2008-07-02 07:10:56', null, null, '2008-06-30 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8902832, 'ANNXP', '2009-07-08 08:31:20', null, null, '2009-06-30 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A7164764', null, 'A', '2003-06-30 00:00:00', '2009-06-30 00:00:00', null, null, null, null, 'ZUIIBGEO', 'IYZHMFWZ', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A7164764', 603723, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A7164764', 5863129, null, null, 'MB', 'COR', '1990-03-09 00:00:00', null, '2561051', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A7164764', 603723, 5863129, null, 'MB', 'COR', '1990-03-09 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A7164764', 'CO', 603723, 0, null, 'SLHRBTKGCQPXNGIGODEL', 'FLXFEORYEMZPOYQ KALNYNFEM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A7164764', 'HD', 603723, null, 254214, 254214, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (254214, 'MB', 'CA', 'XF06LA', 'EAU LOHCHDVBKEH NZAAPPQJB', null, null, 'WINNIPEG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
}
