
sample_test_corps = {
    "corp_0370181": {
            "corp_num":'0370181', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (381551, 333495, 333495, '0370181', 'LIQ', 1054033, null, null, null, null, '1987-12-23 00:00:00', null, null, null, null, 'IAZXZUPKFBGRWCDOEZIC', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (381552, 333496, 333496, '0370181', 'DIR', 1054033, null, null, null, null, null, null, 'COUVELIER', null, 'DEBRA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (381553, 333497, 333497, '0370181', 'OFF', 1054033, null, null, null, null, null, null, 'COUVELIER', null, 'MELVILLE B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830099, null, null, '0370181', 'DIR', 1054033, 1054033, null, null, null, null, '1987-12-31 00:00:00', 'COUVELIER', null, 'RODNEY STEVEN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830100, null, null, '0370181', 'DIR', 1054033, 1054033, null, null, null, null, '1983-04-07 00:00:00', 'COUVELIER', null, 'MILDRED ANN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830101, null, null, '0370181', 'DIR', 1054033, 1054033, null, null, null, null, '1989-10-20 00:00:00', 'COUVELIER', null, 'MELVILLE B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830102, null, null, '0370181', 'DIR', 1054033, 1054033, null, null, null, null, '1989-10-20 00:00:00', 'COUVELIER', null, 'DEBRA', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054033, '0370181', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054034, '0370181', 'FILE', '1990-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054035, '0370181', 'FILE', '1990-11-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054036, '0370181', 'FILE', '1988-01-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054037, '0370181', 'FILE', '1987-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054038, '0370181', 'FILE', '1987-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054039, '0370181', 'FILE', '1987-02-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054040, '0370181', 'FILE', '1987-02-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054041, '0370181', 'FILE', '1986-01-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054042, '0370181', 'FILE', '1985-01-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054043, '0370181', 'FILE', '1983-12-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054044, '0370181', 'FILE', '1983-12-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054045, '0370181', 'FILE', '1983-04-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054046, '0370181', 'FILE', '1982-01-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054047, '0370181', 'FILE', '1981-06-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054048, '0370181', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054049, '0370181', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054050, '0370181', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054034, 'CONVL', '1990-12-31 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054035, 'CONVL', '1990-11-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054036, 'CONVL', '1988-01-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054037, 'CONVL', '1987-12-31 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054038, 'CONVL', '1987-12-31 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054039, 'CONVL', '1987-02-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054040, 'CONVL', '1987-02-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054041, 'CONVL', '1986-01-03 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054042, 'CONVL', '1985-01-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054043, 'CONVL', '1983-12-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054044, 'CONVL', '1983-12-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054045, 'CONVL', '1983-04-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054046, 'CONVL', '1982-01-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1054047, 'CONVL', '1981-06-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('0370181', null, 'BC', '1973-11-30 00:00:00', '1986-11-30 00:00:00', null, '325491868', '486599746923693', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0370181', 1054050, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0370181', 1054049, 1054050, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0370181', 1054048, 1054049, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0370181', 'CO', 1054033, 0, null, 'ERJGEXVSARMFYKTLKAQH', 'EBTIYMZ RSFAQEPVVYSZIDIZ ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0370181', 'RG', 1054033, null, 333494, 333494, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0370181', 'RC', 1054033, null, 333494, 333494, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (333494, 'BC', 'CA', 'VUSWZP', 'WLTESTQGHCVTMDXNNKDJGMB  ', 'DXRESPJZEVIIO NYPUAFXFIOM', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_6720666": {
            "corp_num":'6720666', "corp_typ_cd":'BC', "state_typ_cd":'HDF', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (450249, 392373, 392373, '6720666', 'OFF', 1410118, null, null, null, null, null, null, 'MEADOWS', null, 'CAROL R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (450250, 392374, 392374, '6720666', 'DIR', 1410118, null, null, null, null, null, null, 'MEADOWS', null, 'STEWART J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (450251, 392374, 392374, '6720666', 'OFF', 1410118, null, null, null, null, null, null, 'MEADOWS', null, 'STEWART J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (100570415, null, null, 'FM7882468', 'FBO', 100349136, null, null, null, null, '1984-03-19 00:00:00', null, null, null, null, '0168817IUKOCDUPHTSVTRGRUDBQ', '6720666', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5940574, null, null, '6720666', 'DIR', 1410118, 1410118, null, null, null, null, '1993-04-30 00:00:00', 'MEADOWS', null, 'CAROL R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5940575, null, null, '6720666', 'DIR', 1410118, 1410118, null, null, null, null, '1993-04-30 00:00:00', 'MEADOWS', null, 'STEWART J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5940576, null, null, '6720666', 'DIR', 1410118, 1410118, null, null, null, null, '1989-04-28 00:00:00', 'MEADOWS', null, 'STEWART J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5940577, null, null, '6720666', 'DIR', 1410118, 1410118, null, null, null, null, '1989-04-28 00:00:00', 'MEADOWS', null, 'CAROL R.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1410118, '6720666', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1410119, '6720666', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1410120, '6720666', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1410121, '6720666', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (100349136, 'FM7882468', 'CONVFMREGI', '1984-03-19 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (100349136, 'FRREG', '1984-03-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('6720666', null, 'BC', '1977-12-07 00:00:00', '1989-12-07 00:00:00', null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM7882468', null, 'SP', '1984-03-19 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6720666', 1410121, null, 'HDF', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6720666', 1410120, 1410121, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6720666', 1410119, 1410120, 'HDF', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM7882468', 100349136, null, 'ACT', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('6720666', 'CO', 1410118, 0, null, 'YEMRXXEXREMQRHUSZINF', 'BYYZFOKERABMVDITHDUYAGYQO', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM7882468', 'CO', 100349136, 0, null, 'WGOAXAYOMXYFAFJPNJMU', 'N ZGWUSBDIFRGYXVLURAQZCCF', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6720666', 'RG', 1410118, null, 392372, 392372, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6720666', 'RC', 1410118, null, 392372, 392372, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (392372, 'BC', 'CA', 'AV2IQA', 'CIHDKQPCAFQJSCUWGXLGLUH B', 'ZRQLNSTYQJB DMHFUFAYDJKRF', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_0897281": {
            "corp_num":'0897281', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (461999, 402448, 402448, '0897281', 'LIQ', 1468106, null, null, null, null, '1998-09-24 00:00:00', null, null, null, null, 'PPQNSQVFUEXFHN QQD K', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (462000, 402449, 402449, '0897281', 'DIR', 1468106, null, null, null, null, null, null, 'MACDONALD', null, 'ARTHUR WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (462001, 402450, 402450, '0897281', 'DIR', 1468106, null, null, null, null, null, null, 'MACDONALD', null, 'DALLAS MARY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (462002, 402451, 402451, '0897281', 'OFF', 1468106, null, null, null, null, null, null, 'SLOAN', null, 'GERALD STANLEY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (462003, 402452, 402452, '0897281', 'OFF', 1468106, null, null, null, null, null, null, 'SLOAN', null, 'SHARON MAXINE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957414, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1988-11-18 00:00:00', 'MACDONALD', null, 'JOHN FREDERICK', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957415, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1989-11-17 00:00:00', 'MACDONALD', null, 'JOHN FREDERICK', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957416, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1992-09-03 00:00:00', 'NAMETH', null, 'ANDREW', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957417, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1992-09-03 00:00:00', 'TOMLIN', null, 'DENNIS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957418, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1992-07-06 00:00:00', 'TOMLIN', null, 'JEANNETTE R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957419, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1988-11-18 00:00:00', 'MACDONALD', null, 'ARTHUR WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5957420, null, null, '0897281', 'DIR', 1468106, 1468106, null, null, null, null, '1989-11-17 00:00:00', 'MACDONALD', null, 'ARTHUR WAYNE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468106, '0897281', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468107, '0897281', 'FILE', '1998-10-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468108, '0897281', 'FILE', '1998-09-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468109, '0897281', 'FILE', '1998-09-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468110, '0897281', 'FILE', '1998-09-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468111, '0897281', 'FILE', '1998-07-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468112, '0897281', 'FILE', '1998-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468113, '0897281', 'FILE', '1998-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468114, '0897281', 'FILE', '1998-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468115, '0897281', 'FILE', '1998-01-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468116, '0897281', 'FILE', '1997-07-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468117, '0897281', 'FILE', '1995-11-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468118, '0897281', 'FILE', '1994-08-25 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468119, '0897281', 'FILE', '1993-07-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468120, '0897281', 'FILE', '1992-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468121, '0897281', 'FILE', '1992-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468122, '0897281', 'FILE', '1992-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468123, '0897281', 'FILE', '1992-06-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468124, '0897281', 'FILE', '1992-06-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468125, '0897281', 'FILE', '1990-10-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468126, '0897281', 'FILE', '1989-11-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468127, '0897281', 'FILE', '1986-04-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468128, '0897281', 'FILE', '1985-07-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468129, '0897281', 'FILE', '1983-06-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468130, '0897281', 'FILE', '1982-06-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468131, '0897281', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468132, '0897281', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1468133, '0897281', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468107, 'CONVL', '1998-10-09 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468108, 'CONVL', '1998-09-23 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468109, 'CONVL', '1998-09-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468110, 'CONVL', '1998-09-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468111, 'CONVL', '1998-07-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468112, 'CONVL', '1998-03-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468113, 'CONVL', '1998-03-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468114, 'CONVL', '1998-03-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468115, 'CONVL', '1998-01-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468116, 'CONVL', '1997-07-23 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468117, 'CONVL', '1995-11-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468118, 'CONVL', '1994-08-25 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468119, 'CONVL', '1993-07-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468120, 'CONVL', '1992-08-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468121, 'CONVL', '1992-08-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468122, 'CONVL', '1992-07-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468123, 'CONVL', '1992-06-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468124, 'CONVL', '1992-06-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468125, 'CONVL', '1990-10-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468126, 'CONVL', '1989-11-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468127, 'CONVL', '1986-04-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468128, 'CONVL', '1985-07-03 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468129, 'CONVL', '1983-06-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1468130, 'CONVL', '1982-06-24 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('0897281', null, 'BC', '1978-05-25 00:00:00', '1998-05-25 00:00:00', null, '088605307', '288319807741856', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0897281', 1468133, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0897281', 1468132, 1468133, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0897281', 1468131, 1468132, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0897281', 'CO', 1468106, 0, null, 'ESCWSFACYTLSXGKKGLSV', 'WQVICDLDANOTIBPUWSXYZO PI', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0897281', 'RG', 1468106, null, 402447, 402447, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0897281', 'RC', 1468106, null, 402447, 402447, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (402447, 'BC', 'CA', '5536CF', 'DLIXMFQYNHPW  OPZIO LUHQG', 'EHUXTCAJIYG DCFASKAMOTSGG', 'OLIVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_4187563": {
            "corp_num":'4187563', "corp_typ_cd":'BC', "state_typ_cd":'HDF', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6114973, null, null, '4187563', 'DIR', 1912682, 1912682, null, null, null, null, '1985-08-02 00:00:00', 'FROUD', null, 'PAUL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6114974, null, null, '4187563', 'DIR', 1912682, 1912682, null, null, null, null, '1985-08-02 00:00:00', 'FROUD', null, 'TRACEY', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1912682, '4187563', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1912683, '4187563', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('4187563', null, 'BC', '1981-02-23 00:00:00', null, null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('4187563', 1912683, null, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4187563', 'CO', 1912682, 0, null, 'OETMZVMYQNATKDSNDGLQ', 'KXCBIVMJXOBTHNLNFUFTBRHTA', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4187563', 'RG', 1912682, null, 1, 1, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1, 'BC', 'CA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_1935016": {
            "corp_num":'1935016', "corp_typ_cd":'BC', "state_typ_cd":'HDO', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (382246, '1935016', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (382247, '1935016', 'CONVDSO', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('1935016', null, 'BC', null, null, null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1935016', 382247, null, 'HDO', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('1935016', 'CO', 382246, 0, null, 'HDKRHBUYOCSFJXCDWSEQ', 'JSGGSPFQFOBY HUFARASNNHKL', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1935016', 'RG', 382246, null, 1, 1, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1, 'BC', 'CA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_1596472": {
            "corp_num":'1596472', "corp_typ_cd":'BC', "state_typ_cd":'HDF', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (568437, 494233, 494233, '1596472', 'DIR', 1960515, null, null, null, null, null, null, 'MASON', null, 'GERALD S.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (568438, 494233, 494233, '1596472', 'OFF', 1960515, null, null, null, null, null, null, 'MASON', null, 'GERALD S.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6133911, null, null, '1596472', 'DIR', 1960515, 1960515, null, null, null, null, '1982-10-12 00:00:00', 'MCAFEE', null, 'A. RONALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6133912, null, null, '1596472', 'DIR', 1960515, 1960515, null, null, null, null, '1998-10-02 00:00:00', 'MASON', null, 'GERALD S.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1960515, '1596472', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1960516, '1596472', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('1596472', null, 'BC', '1981-04-27 00:00:00', '1995-04-27 00:00:00', null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1596472', 1960516, null, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('1596472', 'CO', 1960515, 0, null, 'EXHTMYIUQLWMWIUBJQDK', 'UHFRXWXAERPICUNKAOSJNIPBL', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1596472', 'RG', 1960515, null, 494232, 494232, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1596472', 'RC', 1960515, null, 494232, 494232, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (494232, 'BC', 'CA', 'QMQ7NQ', 'JIV SZRHMPEUB TEZEQBPSROP', 'OQAFVUHIZ NQISINZRFTKPSQH', 'NANAIMO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_0599160": {
            "corp_num":'0599160', "corp_typ_cd":'BC', "state_typ_cd":'HDO', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (574409, 499345, 499345, '0599160', 'DIR', 1985146, null, null, null, null, null, null, 'LONQUIST', null, 'LILLIAN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (574410, 499345, 499345, '0599160', 'OFF', 1985146, null, null, null, null, null, null, 'LONQUIST', null, 'LILLIAN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6144078, null, null, '0599160', 'DIR', 1985146, 1985146, null, null, null, null, '1987-07-02 00:00:00', 'LONQUIST', null, 'RUDOLPH', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6144079, null, null, '0599160', 'DIR', 1985146, 1985146, null, null, null, null, '1991-12-31 00:00:00', 'LONQUIST', null, 'LILLIAN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6144080, null, null, '0599160', 'DIR', 1985146, 1985146, null, null, null, null, '1990-10-19 00:00:00', 'LONQUIST', null, 'LILLIAN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6144081, null, null, '0599160', 'DIR', 1985146, 1985146, null, null, null, null, '1981-07-09 00:00:00', 'BOWERS', null, 'SHARON', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1985146, '0599160', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1985147, '0599160', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1985148, '0599160', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1985149, '0599160', 'CONVDSO', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('0599160', null, 'BC', '1981-06-02 00:00:00', '1987-06-02 00:00:00', null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0599160', 1985149, null, 'HDO', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0599160', 1985148, 1985149, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0599160', 1985147, 1985148, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0599160', 'CO', 1985146, 0, null, 'HGJRHFSPPCVUPSUBHMGL', 'J PQOKIHJPYIPLYQFKETUXLMK', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0599160', 'RG', 1985146, null, 499344, 499344, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0599160', 'RC', 1985146, null, 499344, 499344, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (499344, 'BC', 'CA', 'FSSM6R', 'FCIOSUSATYDRKRJVO ULWRXGX', 'CBDAWAYCLWQESJRKMAWZUPBFM', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_1191380": {
            "corp_num":'1191380', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495427, 431310, 431310, '1191380', 'LIQ', 1631095, null, null, null, null, '1991-01-29 00:00:00', null, null, null, null, 'JPHLHDQYOREVTDOECXDY', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495428, 431311, 431311, '1191380', 'DIR', 1631095, null, null, null, null, null, null, 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495429, 431311, 431311, '1191380', 'OFF', 1631095, null, null, null, null, null, null, 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6005579, null, null, '1191380', 'DIR', 1631095, 1631095, null, null, null, null, '1988-01-29 00:00:00', 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631095, '1191380', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631096, '1191380', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631097, '1191380', 'FILE', '1991-01-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631098, '1191380', 'FILE', '1990-12-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631099, '1191380', 'FILE', '1990-12-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631100, '1191380', 'FILE', '1989-07-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631101, '1191380', 'FILE', '1989-04-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631102, '1191380', 'FILE', '1987-10-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631103, '1191380', 'FILE', '1985-01-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631104, '1191380', 'FILE', '1983-10-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631105, '1191380', 'FILE', '1982-08-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631106, '1191380', 'FILE', '1981-09-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631107, '1191380', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631108, '1191380', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631109, '1191380', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631096, 'CONVL', '1991-03-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631097, 'CONVL', '1991-01-31 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631098, 'CONVL', '1990-12-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631099, 'CONVL', '1990-12-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631100, 'CONVL', '1989-07-27 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631101, 'CONVL', '1989-04-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631102, 'CONVL', '1987-10-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631103, 'CONVL', '1985-01-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631104, 'CONVL', '1983-10-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631105, 'CONVL', '1982-08-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1631106, 'CONVL', '1981-09-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('1191380', null, 'BC', '1979-07-31 00:00:00', '1990-07-31 00:00:00', null, '319405734', '150154925763054', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1191380', 1631109, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1191380', 1631108, 1631109, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1191380', 1631107, 1631108, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('1191380', 'CO', 1631095, 0, null, 'MGVDTBMWPSCRKTFOFAFA', 'NSM YTNOXBOIHZTQZZXIZUTNU', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1191380', 'RG', 1631095, null, 431309, 431309, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1191380', 'RC', 1631095, null, 431309, 431309, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (431309, 'BC', 'CA', 'SMHUF8', 'MRY  XHX RDCFDXUPXRHS SFK', 'JGWVKVMO OTLSAGVBAUMHDINB', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_3859483": {
            "corp_num":'3859483', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91069, 79291, 79291, '3859483', 'LIQ', 253983, null, null, null, null, '1987-03-10 00:00:00', null, null, null, null, 'CUBCO SIJLHNZBCI OXP', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91070, 79292, 79292, '3859483', 'DIR', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'JULIETTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91071, 79292, 79292, '3859483', 'OFF', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'JULIETTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91072, 79293, 79293, '3859483', 'DIR', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'LESLIE ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91073, 79293, 79293, '3859483', 'OFF', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'LESLIE ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683604, null, null, '3859483', 'DIR', 253983, 253983, null, null, null, null, '1985-05-08 00:00:00', 'JANUSSON', null, 'BERGON B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683605, null, null, '3859483', 'DIR', 253983, 253983, null, null, null, null, '1983-10-28 00:00:00', 'JANUSSON', null, 'AMY E.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683606, null, null, '3859483', 'DIR', 253983, 253983, null, null, null, null, '1987-12-21 00:00:00', 'JANUSSON', null, 'JULIETTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683607, null, null, '3859483', 'DIR', 253983, 253983, null, null, null, null, '1987-12-21 00:00:00', 'JANUSSON', null, 'LESLIE ROBERT', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253983, '3859483', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253984, '3859483', 'FILE', '1988-01-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253985, '3859483', 'FILE', '1987-09-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253986, '3859483', 'FILE', '1987-06-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253987, '3859483', 'FILE', '1987-03-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253988, '3859483', 'FILE', '1987-03-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253989, '3859483', 'FILE', '1987-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253990, '3859483', 'FILE', '1986-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253991, '3859483', 'FILE', '1985-07-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253992, '3859483', 'FILE', '1985-05-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253993, '3859483', 'FILE', '1985-05-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253994, '3859483', 'FILE', '1983-10-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253995, '3859483', 'FILE', '1983-01-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253996, '3859483', 'FILE', '1982-09-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253997, '3859483', 'FILE', '1981-08-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253998, '3859483', 'FILE', '1980-07-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253999, '3859483', 'CONVDSO', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (254000, '3859483', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (254001, '3859483', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253984, 'CONVL', '1988-01-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253985, 'CONVL', '1987-09-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253986, 'CONVL', '1987-06-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253987, 'CONVL', '1987-03-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253988, 'CONVL', '1987-03-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253989, 'CONVL', '1987-03-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253990, 'CONVL', '1986-05-27 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253991, 'CONVL', '1985-07-09 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253992, 'CONVL', '1985-05-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253993, 'CONVL', '1985-05-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253994, 'CONVL', '1983-10-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253995, 'CONVL', '1983-01-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253996, 'CONVL', '1982-09-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253997, 'CONVL', '1981-08-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (253998, 'CONVL', '1980-07-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('3859483', null, 'BC', '1953-05-13 00:00:00', '1986-05-13 00:00:00', null, '869078461', '219331205781956', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3859483', 254001, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3859483', 254000, 254001, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3859483', 253999, 254000, 'HDO', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('3859483', 'CO', 253983, 0, null, 'WWBJTCDMQPEVPZAPSCAE', 'XI SMBDYZJLX IZCXILGDRICB', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3859483', 'RG', 253983, null, 79290, 79290, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3859483', 'RC', 253983, null, 79290, 79290, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (79290, 'BC', 'CA', null, 'KULRJVAVVEOJIJOMQPZZAQTLG', 'YDWFSLFTUHWUTEJQVQGELYOQQ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_6107383": {
            "corp_num":'6107383', "corp_typ_cd":'BC', "state_typ_cd":'HDF', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (568888, 494623, 494623, '6107383', 'DIR', 1962154, null, null, null, null, null, null, 'SWANNEY', null, 'JAMES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (568889, 494623, 494623, '6107383', 'OFF', 1962154, null, null, null, null, null, null, 'SWANNEY', null, 'JAMES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6134604, null, null, '6107383', 'DIR', 1962154, 1962154, null, null, null, null, '1994-03-18 00:00:00', 'SWANNEY', null, 'NICOLA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6134605, null, null, '6107383', 'DIR', 1962154, 1962154, null, null, null, null, '1999-10-01 00:00:00', 'SWANNEY', null, 'JAMES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6134606, null, null, '6107383', 'DIR', 1962154, 1962154, null, null, null, null, '1987-08-18 00:00:00', 'SWANNEY', null, 'CHARLOTTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6134607, null, null, '6107383', 'DIR', 1962154, 1962154, null, null, null, null, '1981-08-20 00:00:00', 'DUIGNAN', null, 'JAMES LAWRENCE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1962154, '6107383', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1962155, '6107383', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('6107383', null, 'BC', '1981-04-29 00:00:00', '1996-04-29 00:00:00', null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6107383', 1962155, null, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('6107383', 'CO', 1962154, 0, null, 'QMGERIKZHPFDRNDTCNBX', 'YBDRRGCWUOL OHOCFTSKUXHFO', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6107383', 'RG', 1962154, null, 494622, 494622, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6107383', 'RC', 1962154, null, 494622, 494622, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (494622, 'BC', 'CA', '3SK43C', 'QLVZZVNGJYZIAJDJAKHMYXPIJ', 'NSWMOT BRNWORZOTHHUGZAPME', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_0161104": {
            "corp_num":'0161104', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (506019, 440484, 440484, '0161104', 'LIQ', 1678556, null, null, null, null, '2000-05-24 00:00:00', null, null, null, null, ' XYABAGICHWEMTHQKGDO', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (506020, 440485, 440485, '0161104', 'DIR', 1678556, null, null, null, null, null, null, 'CARSON', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (506021, 440485, 440485, '0161104', 'OFF', 1678556, null, null, null, null, null, null, 'CARSON', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021588, null, null, '0161104', 'DIR', 1678556, 1678556, null, null, null, null, '1985-05-03 00:00:00', 'PETERS', null, 'FREDERICK A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021589, null, null, '0161104', 'DIR', 1678556, 1678556, null, null, null, null, '2000-02-08 00:00:00', 'JEFFERD', null, 'RAYMOND', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021590, null, null, '0161104', 'DIR', 1678556, 1678556, null, null, null, null, '1994-08-22 00:00:00', 'BOYCE', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021591, null, null, '0161104', 'DIR', 1678556, 1678556, null, null, null, null, '1985-05-03 00:00:00', 'BOYCE', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678556, '0161104', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678557, '0161104', 'FILE', '2000-07-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678558, '0161104', 'FILE', '2000-03-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678559, '0161104', 'FILE', '2000-02-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678560, '0161104', 'FILE', '1999-08-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678561, '0161104', 'FILE', '1999-07-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678562, '0161104', 'FILE', '1999-07-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678563, '0161104', 'FILE', '1998-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678564, '0161104', 'FILE', '1997-07-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678565, '0161104', 'FILE', '1996-12-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678566, '0161104', 'FILE', '1996-02-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678567, '0161104', 'FILE', '1995-02-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678568, '0161104', 'FILE', '1994-08-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678569, '0161104', 'FILE', '1993-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678570, '0161104', 'FILE', '1991-12-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678571, '0161104', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678572, '0161104', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678573, '0161104', 'FILE', '1988-12-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678574, '0161104', 'FILE', '1988-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678575, '0161104', 'FILE', '1987-01-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678576, '0161104', 'FILE', '1985-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678577, '0161104', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678578, '0161104', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678579, '0161104', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6637862, '0161104', 'ADMIN', '2005-10-21 10:15:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6637857, '0161104', 'ADCORP', '2005-10-21 10:14:01', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678557, 'CONVL', '2000-07-24 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678558, 'CONVL', '2000-03-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678559, 'CONVL', '2000-02-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678560, 'CONVL', '1999-08-23 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678561, 'CONVL', '1999-07-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678562, 'CONVL', '1999-07-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678563, 'CONVL', '1998-07-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678564, 'CONVL', '1997-07-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678565, 'CONVL', '1996-12-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678566, 'CONVL', '1996-02-20 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678567, 'CONVL', '1995-02-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678568, 'CONVL', '1994-08-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678569, 'CONVL', '1993-01-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678570, 'CONVL', '1991-12-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678571, 'CONVL', '1991-03-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678572, 'CONVL', '1991-03-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678573, 'CONVL', '1988-12-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678574, 'CONVL', '1988-01-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678575, 'CONVL', '1987-01-20 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (1678576, 'CONVL', '1985-12-31 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('0161104', null, 'BC', '1979-11-23 00:00:00', '1999-11-23 00:00:00', null, '658030880', '347655993503881', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0161104', 1678579, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0161104', 1678578, 1678579, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0161104', 1678577, 1678578, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0161104', 'CO', 1678556, 0, null, 'XIIBAZQDYAZDYRNIAKYQ', 'QOGWDQKZRKYULLPFOMZCWZHCM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0161104', 'RG', 1678556, null, 440483, 440483, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0161104', 'RC', 1678556, null, 440483, 440483, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (440483, 'BC', 'CA', '35Q1WK', 'IHJZKNRCZNPRMJTYJYVKXUYDJ', 'SMBUDDXLSDNDSXSOHKSQFXVTS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_6325372": {
            "corp_num":'6325372', "corp_typ_cd":'BC', "state_typ_cd":'HDF', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6068324, null, null, '6325372', 'DIR', 1801067, 1801067, null, null, null, null, '1980-09-02 00:00:00', 'MIRON', null, 'MARIE LOUISE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6068325, null, null, '6325372', 'DIR', 1801067, 1801067, null, null, null, null, '1985-06-14 00:00:00', 'CLARKSON', null, 'BRIAN', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1801067, '6325372', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1801068, '6325372', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('6325372', null, 'BC', '1980-08-13 00:00:00', null, null, null, null, null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6325372', 1801068, null, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('6325372', 'CO', 1801067, 0, null, 'XVFOJLJLRCHVEOYOLAYZ', 'YXQQCPGWEYAX CPRQPOTJFOXS', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6325372', 'RG', 1801067, null, 1, 1, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1, 'BC', 'CA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
}
