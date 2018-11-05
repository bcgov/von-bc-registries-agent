
sample_test_corps = {
    "corp_3014589": {
            "corp_num":'3014589', "corp_typ_cd":'ULC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3379538, 7138912, null, '3014589', 'INC', 8952972, null, null, null, null, null, null, null, null, null, 'GTQHCPFBVEGWDIOFJQDX', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3379539, 7138914, 7138915, '3014589', 'DIR', 8952972, null, null, null, null, null, null, 'Bourgeois', null, 'Robert', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242653, '3014589', 'FILE', '2016-08-25 15:25:04', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8952972, '3014589', 'FILE', '2009-08-13 10:35:36', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8952972, 'ICORU', '2009-08-13 10:35:36', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242653, 'NOCAD', '2016-08-26 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('3014589', null, 'ULC', '2009-08-13 10:35:36', null, null, null, null, null, 'UYONBZOF', 'JCHHZKRZ', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3014589', 8952972, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('3014589', 'NB', 8952972, 0, null, 'MHPNKWNHITXWNGLIHEYG', 'EMBUHWHQZGEIILKRJCPJCREQE', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3014589', 'RG', 8952972, 9242653, 7138917, 7138916, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3014589', 'RC', 8952972, 9242653, 7138919, 7138918, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3014589', 'RG', 9242653, null, 7535907, 7535906, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3014589', 'RC', 9242653, null, 7535907, 7535906, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138916, 'BC', 'CA', 'RBEI3N', 'UQQAOYMDRELODOJ DIKUNQXIU', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138917, 'BC', 'CA', '4KBLJ7', 'YSCXAEXEKMRIQU YSDM ZODJO', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138918, 'BC', 'CA', 'WBGR38', 'ASGXMRFDOFHOXNVXSHVHJOVCX', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138919, 'BC', 'CA', '70H74H', 'JFZBGIFQXPW ARR UJGVYHXPO', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535906, 'BC', 'CA', 'GJIBX8', 'KEQAMBTFWSKVFWTQLVAZMSHKY', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535907, 'BC', 'CA', 'A8QCLN', 'DUDCASEEXNRTKWCAXIVWACFIT', 'L  YRKNMGIUGM IGKCACMHDFB', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A5589691": {
            "corp_num":'A5589691', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":3, "party_addr_ct":1, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682494, null, null, 'FM3834099', 'FBO', 105301927, null, null, null, null, '2001-05-09 14:29:44', null, null, null, null, 'A0031179DNHDFGCVBHITPAFICCFZ', 'A5589691', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682496, null, null, 'FM8823648', 'FBO', 105301928, null, null, null, null, '2001-05-09 14:36:16', null, null, null, null, 'A0031179VLVYKDZFACOEKEKWAGYH', 'A5589691', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510862, 7535953, 7535952, 'A5589691', 'ATT', 9242676, null, 96730, null, null, null, null, null, null, null, 'BC0121625PFBFHPIUMURZZMLKTDH ', 'BC8890234', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96730, 84222, 84222, 'A5589691', 'ATT', 265264, 9242676, null, null, null, null, null, 'FERBER', null, 'JOHN P.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96731, 84223, 84223, 'A5589691', 'OFF', 265264, null, null, null, null, null, null, 'FLAHERTY', null, 'TIMOTHY J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96732, 84224, 84224, 'A5589691', 'DIR', 265264, null, null, null, null, null, null, 'KELLY', null, 'KEVIN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96733, 84224, 84224, 'A5589691', 'OFF', 265264, null, null, null, null, null, null, 'KELLY', null, 'KEVIN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96734, 84225, 84225, 'A5589691', 'DIR', 265264, null, null, null, null, null, null, 'MORIN', null, 'JEAN PAUL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96735, 84226, 84226, 'A5589691', 'OFF', 265264, null, null, null, null, null, null, 'RASPER', null, 'WOLFGANG', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96736, 84227, 84227, 'A5589691', 'DIR', 265264, null, null, null, null, null, null, 'ROXBURGH', null, 'LORIE-ANN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96737, 84228, 84228, 'A5589691', 'OFF', 265264, null, null, null, null, null, null, 'SCHUPP', null, 'PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96738, 84229, 84229, 'A5589691', 'OFF', 265264, null, null, null, null, null, null, 'STRANG', null, 'ALLEN L.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105587336, 103538935, null, 'FM9877026', 'FBO', 104927429, null, null, null, null, '2008-04-25 00:00:00', null, null, null, null, 'A0031179ESB DAXRBHWXQVTNZOVW', 'A5589691', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6351769, 'A5589691', 'FILE', '2005-06-13 11:13:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7098741, 'A5589691', 'FILE', '2006-05-15 10:30:06', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7567036, 'A5589691', 'ADCORP', '2007-03-13 10:54:46', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7636083, 'A5589691', 'FILE', '2007-04-26 09:38:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242676, 'A5589691', 'FILE', '2017-04-04 16:19:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265264, 'A5589691', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265265, 'A5589691', 'FILE', '2003-09-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265266, 'A5589691', 'FILE', '2003-09-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265267, 'A5589691', 'FILE', '2002-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265268, 'A5589691', 'FILE', '2001-06-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265269, 'A5589691', 'FILE', '2001-04-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265270, 'A5589691', 'FILE', '2001-04-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265271, 'A5589691', 'FILE', '2000-06-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265272, 'A5589691', 'FILE', '1999-06-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265273, 'A5589691', 'FILE', '1999-06-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265274, 'A5589691', 'FILE', '1998-12-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265275, 'A5589691', 'FILE', '1998-10-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265276, 'A5589691', 'FILE', '1998-07-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265277, 'A5589691', 'FILE', '1998-05-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265278, 'A5589691', 'FILE', '1997-07-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265279, 'A5589691', 'FILE', '1996-07-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265280, 'A5589691', 'FILE', '1995-10-25 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265281, 'A5589691', 'FILE', '1995-06-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265282, 'A5589691', 'FILE', '1995-06-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265283, 'A5589691', 'FILE', '1994-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265284, 'A5589691', 'FILE', '1994-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265285, 'A5589691', 'FILE', '1993-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265286, 'A5589691', 'FILE', '1993-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265287, 'A5589691', 'FILE', '1993-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265288, 'A5589691', 'FILE', '1992-09-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265289, 'A5589691', 'FILE', '1992-09-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265290, 'A5589691', 'FILE', '1992-05-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265291, 'A5589691', 'FILE', '1991-06-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265292, 'A5589691', 'FILE', '1991-04-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265293, 'A5589691', 'FILE', '1990-04-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265294, 'A5589691', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5695631, 'A5589691', 'FILE', '2004-04-27 11:08:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8299235, 'A5589691', 'FILE', '2008-06-04 16:00:45', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8778281, 'A5589691', 'FILE', '2009-04-16 12:15:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721465, 'FM3834099', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301927, 'FM3834099', 'CONVFMACP', '2001-05-09 14:29:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721467, 'FM8823648', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301928, 'FM8823648', 'CONVFMACP', '2001-05-09 14:36:16', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104927429, 'FM9877026', 'CONVFMREGI', '2008-04-25 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265265, 'CONVL', '2003-09-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265266, 'CONVL', '2003-09-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265267, 'CONVL', '2002-06-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265268, 'CONVL', '2001-06-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265269, 'CONVL', '2001-04-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265270, 'CONVL', '2001-04-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265271, 'CONVL', '2000-06-13 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265272, 'CONVL', '1999-06-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265273, 'CONVL', '1999-06-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265274, 'CONVL', '1998-12-03 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265275, 'CONVL', '1998-10-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265276, 'CONVL', '1998-07-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265277, 'CONVL', '1998-05-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265278, 'CONVL', '1997-07-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265279, 'CONVL', '1996-07-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265280, 'CONVL', '1995-10-25 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265281, 'CONVL', '1995-06-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265282, 'CONVL', '1995-06-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265283, 'CONVL', '1994-05-27 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265284, 'CONVL', '1994-05-27 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265285, 'CONVL', '1993-11-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265286, 'CONVL', '1993-11-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265287, 'CONVL', '1993-11-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265288, 'CONVL', '1992-09-24 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265289, 'CONVL', '1992-09-24 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265290, 'CONVL', '1992-05-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265291, 'CONVL', '1991-06-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265292, 'CONVL', '1991-04-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (265293, 'CONVL', '1990-04-03 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5695631, 'ANNXP', '2004-04-27 11:08:23', null, null, '2004-04-03 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6351769, 'ANNXP', '2005-06-13 11:13:03', null, null, '2005-04-03 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7098741, 'ANNXP', '2006-05-15 10:30:06', null, null, '2006-04-03 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7636083, 'ANNXP', '2007-04-26 09:38:20', null, null, '2007-04-03 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8299235, 'ANNXP', '2008-06-04 16:00:45', null, null, '2008-04-03 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8778281, 'ANNXP', '2009-04-16 12:15:31', null, null, '2009-04-03 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242676, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104721465, 'FRREG', '2000-06-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104721467, 'FRREG', '2000-06-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104927429, 'FRREG', '2008-04-25 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105301927, 'FRMEM', '2001-05-09 14:29:44', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105301928, 'FRMEM', '2001-05-09 14:36:16', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A5589691', null, 'A', '1990-04-03 00:00:00', '2009-04-03 00:00:00', null, null, null, null, 'AWYYTYZS', 'SKTBKZZN', 'AIPKOCIFXNGJ@KZHMMRNN.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM3834099', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM8823648', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9877026', null, 'SP', '2008-04-25 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1163592, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A5589691', 265264, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM3834099', 104721465, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM8823648', 104721467, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9877026', 104927429, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A5589691', 265264, 5695631, null, 'FD', 'COR', '1989-11-21 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A5589691', 5695631, null, null, 'FD', 'COR', '1989-11-21 00:00:00', null, '254278-1', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A5589691', 'CO', 265264, 0, 265294, 'OCWDKXDPRTVMKKWBOEKJ', 'GJBEOGZOBYGWJSQCEOJCTIGYE', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A5589691', 'CO', 265294, 0, null, 'ECSRRLWZJIPRJPFVJUXG', 'RNFGPNUJVSOCEYJABJDHB QSV', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM3834099', 'CO', 104721465, 0, null, 'ADAGBZOCKKOOJNYIJXIY', 'IFUCHMUAZWKITDNTRAMPJMFOX', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM8823648', 'CO', 104721467, 0, null, 'UEZDAXBBOIYSBSKNCDYH', 'WBZKSUFYGJEUSWBCSLL  JHIY', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9877026', 'CO', 104927429, 0, null, 'PIXWVFVEMASAWYPWIMQL', 'ZYVEPPXAYOAXWYPCTGGQJIEVM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A5589691', 'HD', 265264, null, 84221, 84221, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9877026', 'FO', 104927429, null, 103248012, 103248011, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84221, 'QC', 'CA', 'W9FYR3', 'YFDVVQESFCOECSSPUGJQDGPLY', null, null, 'VILLE SAINT-LAURENT', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248011, 'BC', 'CA', '2B5QMB', null, null, null, 'VANCOUVER', 'BAS', 'NHSQJSYUMQHTVCXISNAQIINIJXQCONEXHNWKXWIH', 'UQTKAHSZALFYFOVNURRL', null, '479', null, '092', null, 'ENGKXJAOOHOYNQN', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248012, 'ON', 'CA', 'H2FBNZ', null, null, null, 'MARKHAM', 'BAS', 'LUIDCNQDUQJNYJHZYOJYEXQZHLFHYZQOJDGTNIWZ', 'GAFZIWBRG VPBEZONJWM', null, '469', null, '350', null, 'HVDOASUGZNZWGNX', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM2615931": {
            "corp_num":'FM2615931', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105351824, 103180753, null, 'FM2615931', 'FCP', 104893496, null, null, null, null, null, null, 'LAWYERS', null, 'SYNERGY BUSINESS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105552151, 103503750, null, 'FM2615931', 'FBO', 104893496, null, null, null, null, '2007-02-14 00:00:00', null, null, null, null, '0765995Z HFBQDLXTDAJACFOEVC', '2701409', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104893496, 'FM2615931', 'CONVFMREGI', '2007-02-14 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104893496, 'FRREG', '2007-02-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM2615931', null, 'SP', '2007-02-14 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1114375, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM2615931', 104893496, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM2615931', 'CO', 104893496, 0, null, 'VTKMPADZOMGWPONDZQNR', 'IAUHXIG OPVREPRWCNCDOJLLM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM2615931', 'FO', 104893496, null, 103180754, 103180754, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103180754, 'BC', 'CA', 'ZD3B8I', null, null, null, 'DELTA', 'BAS', 'QKVOMFNHOHJENYKPHPTCDOENVIYNJGPFXUWBAUZO', 'XLIE OMGMRYHGWDF IDC', null, null, null, '737', null, 'RIGLHVJIEUSSXVL', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_LP0491659": {
            "corp_num":'LP0491659', "corp_typ_cd":'LP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105772250, null, null, 'LP0491659', 'FBO', 104900882, null, null, null, null, '2007-05-15 00:00:00', null, null, null, null, '0790280XSEYNIWFEBJQQMVIIELX', '3856275', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104900882, 'LP0491659', 'CONVFMREGI', '2007-05-15 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104900882, 'LPREG', '2007-05-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('LP0491659', null, 'LP', '2007-05-15 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-05-15 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('LP0491659', 104900882, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('LP0491659', 'CO', 104900882, 0, null, 'ISRRCATEYZTRFIEIVMVU', 'WNESPY GPWJEWXXGJELBVDOHH', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
    "corp_0191294": {
            "corp_num":'0191294', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2747922, 5258703, null, '0191294', 'INC', 7651354, null, null, null, null, null, null, null, null, null, 'MTTRSXDYCCQYHJNYGPOF', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2747923, 5258705, 5258706, '0191294', 'DIR', 7651354, null, null, null, null, null, null, 'O''NEILL', 'C.', 'JOHN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2747924, 5258707, 5258708, '0191294', 'DIR', 7651354, null, null, null, null, null, null, 'O''NEILL', 'F.', 'ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105772250, null, null, 'LP0475721', 'FBO', 104900882, null, null, null, null, '2007-05-15 00:00:00', null, null, null, null, '0790280B NBQMRJROEXYVZTPIIL', '0191294', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3342812, 7030460, 7030460, '0191294', 'OFF', 8879933, null, 0, null, null, '2009-06-22 12:05:23', null, 'O''NEILL', null, 'ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3342813, 7030461, 7030461, '0191294', 'OFF', 8879933, null, 0, null, null, '2009-06-22 12:05:23', null, 'O''NEILL', null, 'JOHN', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7651354, '0191294', 'FILE', '2007-05-04 15:52:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242296, '0191294', 'FILE', '2015-07-28 14:46:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8879949, '0191294', 'FILE', '2009-06-22 12:07:54', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8879933, '0191294', 'FILE', '2009-06-22 12:05:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104900882, 'LP0475721', 'CONVFMREGI', '2007-05-15 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7651354, 'ICORP', '2007-05-04 15:52:52', null, null, null, null, 'N', null, null, 'F ', null, null, 'NR8467995', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8879933, 'ANNBC', '2009-06-22 12:05:23', null, null, '2008-05-04 00:00:00', null, 'N', null, null, 'F ', null, '112045505', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8879949, 'ANNBC', '2009-06-22 12:07:54', null, null, '2009-05-04 00:00:00', null, 'N', null, null, 'F ', null, '115094781', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242296, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104900882, 'LPREG', '2007-05-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('0191294', null, 'BC', '2007-05-04 15:52:52', '2009-05-04 00:00:00', null, null, null, null, 'VVCGROSU', 'KDBTPGAE', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('LP0475721', null, 'LP', '2007-05-15 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-05-15 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0191294', 7651354, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('LP0475721', 104900882, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0191294', 'CO', 7651354, 0, null, 'GCDSJCGQXUIQDCHOAIWW', 'ZBCE WNAQHKQOKJSHLUCCIKSP', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('LP0475721', 'CO', 104900882, 0, null, 'QDJPSKPMZRENLIVUOUML', 'TSVHRJKI QSGDGW TWVMNJSKS', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0191294', 'RG', 7651354, 9242296, 5258710, 5258709, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0191294', 'RC', 7651354, 9242296, 5258712, 5258711, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0191294', 'RG', 9242296, null, 7535430, 7535430, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0191294', 'RC', 9242296, null, 7535430, 7535430, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258709, 'BC', 'CA', 'LG4KKR', 'PVBRLWRZDHTDOCBNUTNGJQOIT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258710, 'BC', 'CA', 'MGXHBW', 'XSCIKAAZPGSMHVXHMQIIWHZHE', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258711, 'BC', 'CA', 'IHL5RG', 'ZOIX C UCSDYSSIRZTGEEFDVZ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258712, 'BC', 'CA', 'T20LDI', 'QVFUFFWAYYXWFRPTLRNBYNLQN', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535430, 'BC', 'CA', 'LXOL8Y', 'GED AB MJVCAZXFUNQEGQXTEQ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM0471065": {
            "corp_num":'FM0471065', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105340674, 103155279, null, 'FM0471065', 'FCP', 104880184, null, null, null, null, null, null, 'LAWYERS', null, 'SYNERGY BUSINESS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105538816, 103490415, null, 'FM0471065', 'FBO', 104880184, null, null, null, null, '2006-08-16 00:00:00', null, null, null, null, '0765995DJATQLCWVUXHZVPKSJIF', '1418718', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104880184, 'FM0471065', 'CONVFMREGI', '2006-08-16 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104880184, 'FRREG', '2006-08-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM0471065', null, 'SP', '2006-08-16 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1095915, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM0471065', 104880184, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM0471065', 'CO', 104880184, 0, null, 'LXHEIRMLITYPRCXTETMQ', 'QOHCHHYOTIKQQKYNFLWPQGPCY', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM0471065', 'FO', 104880184, null, 103155280, 103155280, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103155280, 'BC', 'CA', '8S9PCM', null, null, null, 'DELTA', 'BAS', 'FDUD JLOEERLDJDXESPYVGUBUREXMERSVGIQKMAO', 'CRMRBMCTQIOKVOPFAFNS', null, null, null, '084', null, 'OUIWZMFCBNNQVMV', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM1821357": {
            "corp_num":'FM1821357', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105381285, 103248010, null, 'FM1821357', 'FCP', 104927429, null, null, null, null, null, null, 'THOMSON LLP', null, 'MILLER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105587336, 103538935, null, 'FM1821357', 'FBO', 104927429, null, null, null, null, '2008-04-25 00:00:00', null, null, null, null, 'A0031179TNEUDWNMYWIFRNLECGHP', 'A0882005', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104927429, 'FM1821357', 'CONVFMREGI', '2008-04-25 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104927429, 'FRREG', '2008-04-25 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1821357', null, 'SP', '2008-04-25 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1163592, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1821357', 104927429, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1821357', 'CO', 104927429, 0, null, 'KJWGFLJJSTCMXHNUZVWE', ' GCSDDVCRUVI OKOYJDWTETWF', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM1821357', 'FO', 104927429, null, 103248012, 103248011, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248011, 'BC', 'CA', 'XMAIKR', null, null, null, 'VANCOUVER', 'BAS', 'UIN ZGMWLUQBIBQOBMKVS GNWLB NISTK ZWMRIO', 'YAYUYJZCXGESD EZFRQR', null, '021', null, '430', null, 'TZLYXJZWMFIMFZD', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248012, 'ON', 'CA', 'QNFHSN', null, null, null, 'MARKHAM', 'BAS', 'OBEEOBDOXIMVVZBLP BNDAORYASZJOBTSDLICHWE', 'BZTOCTFCGMZJIGSHEQWA', null, '856', null, '949', null, 'JSQUVDTBXRVKOUL', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A2559714": {
            "corp_num":'A2559714', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1922541, 2043487, 2043486, 'A2559714', 'ATT', 5837836, 9242706, 269581, null, null, null, null, null, null, null, 'HFMFNAHSGLASXQUWPVZA', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510892, 7536013, 7536012, 'A2559714', 'ATT', 9242706, null, 1922541, null, null, null, null, null, null, null, 'BC0121625XUMNNMDYHRSIKQ PBAGM', 'BC4443694', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269581, 237083, 237083, 'A2559714', 'ATT', 580103, 5837836, null, null, null, null, null, 'HEENAN BLAIKIE CORPORATE', null, 'SERVICES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269582, 237084, 237084, 'A2559714', 'DIR', 580103, null, null, null, null, null, null, 'KEARNS', null, 'JOHN R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269583, 237084, 237084, 'A2559714', 'OFF', 580103, null, null, null, null, null, null, 'KEARNS', null, 'JOHN R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269584, 237085, 237085, 'A2559714', 'OFF', 580103, null, null, null, null, null, null, 'LEWIS', null, 'PETER A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269585, 237086, 237086, 'A2559714', 'OFF', 580103, null, null, null, null, null, null, 'MATEAR', null, 'CAROLE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6576516, 'A2559714', 'FILE', '2005-09-22 15:01:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7254645, 'A2559714', 'FILE', '2006-08-24 10:34:27', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7896643, 'A2559714', 'FILE', '2007-10-02 10:42:47', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242706, 'A2559714', 'FILE', '2017-04-04 16:19:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580103, 'A2559714', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580104, 'A2559714', 'FILE', '2003-09-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580105, 'A2559714', 'FILE', '2003-05-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580106, 'A2559714', 'FILE', '2002-11-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580107, 'A2559714', 'FILE', '2002-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5837836, 'A2559714', 'FILE', '2004-08-10 14:33:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5836508, 'A2559714', 'FILE', '2004-08-09 16:56:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8410817, 'A2559714', 'FILE', '2008-08-19 15:39:18', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8413272, 'A2559714', 'FILE', '2008-08-20 15:21:11', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8980486, 'A2559714', 'FILE', '2009-09-02 14:49:33', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (580104, 'CONVL', '2003-09-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (580105, 'CONVL', '2003-05-23 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (580106, 'CONVL', '2002-11-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (580107, 'CONVL', '2002-07-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5836508, 'ANNXP', '2004-08-09 16:56:01', null, null, '2004-07-02 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5837836, 'CO_AT', '2004-08-10 14:33:03', null, null, null, null, 'N', null, null, 'P ', 5837836, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6576516, 'ANNXP', '2005-09-22 15:01:58', null, null, '2005-07-02 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7254645, 'ANNXP', '2006-08-24 10:34:27', null, null, '2006-07-02 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7896643, 'ANNXP', '2007-10-02 10:42:47', null, null, '2007-07-02 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8410817, 'ANNXP', '2008-08-19 15:39:18', null, null, '2008-07-02 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8413272, 'NOCRX', '2008-08-20 15:21:11', null, null, null, null, 'N', null, null, 'P ', 8413272, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8980486, 'ANNXP', '2009-09-02 14:49:33', null, null, '2009-07-02 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242706, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A2559714', null, 'A', '2002-07-02 00:00:00', '2009-07-02 00:00:00', null, null, null, null, 'HXTFTDDJ', 'YFPQSXHK', 'EQHITPSQAXIN@TQIFPTDL.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A2559714', 580103, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A2559714', 5836508, null, null, 'FD', 'COR', '1998-07-21 00:00:00', null, '351401-3', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A2559714', 580103, 5836508, null, 'FD', 'COR', '1998-07-21 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A2559714', 'CO', 580103, 0, null, 'QLHAFIBZXSTNAPHJPHWS', 'JUDIFOEUY AARDJEXGSRPSPVD', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A2559714', 'HD', 8413272, null, 6381045, 6381044, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A2559714', 'HD', 580103, 8413272, 237082, 237082, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (237082, null, null, 'F5PAE9', 'QMLJETMITBILCVPHUZACZAOUQ', 'INJOEQDGZMWECHDGRUFZRQU X', 'TORONTO ON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6381044, 'ON', 'CA', 'WM3KCD', 'SOUIVORVKNSEB EQMMWDZUQTH', null, null, 'TORONTO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6381045, 'ON', 'CA', 'JNB5Y8', 'JDOQOH UAKLMGYDAZQTDENQUD', null, null, 'TORONTO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM4999330": {
            "corp_num":'FM4999330', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105395407, 103280173, null, 'FM4999330', 'FCP', 104943427, null, null, null, null, null, null, 'BUSINESS LAWYERS', null, 'SYNERGY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604099, 103555698, null, 'FM4999330', 'FBO', 104943427, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071YMWLHSZBSXRCG MADVSQ', '1757532', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943427, 'FM4999330', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104943427, 'FRREG', '2008-12-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM4999330', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186186, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM4999330', 104943427, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM4999330', 'CO', 104943427, 0, null, 'VJWSLNOUUNUKKZDIHUQF', 'LKVRIQNOAA NXMPANSRMEICMT', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM4999330', 'FO', 104943427, null, 103280174, 103280174, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280174, null, 'CA', 'YSJ9ZP', 'GVSFUNQUCLMZ MTBSMVCPEJOJ', null, null, 'DELTA', 'FOR', 'GVIOBBMGCEVDLDCELTEFUORPRSUSWTXMOQCTKIWH', 'FUGZAESLJNLTRSLLQOQP', null, null, null, '298', null, 'YGWNXNVQIEISBJB', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_4954727": {
            "corp_num":'4954727', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":2, "party_addr_ct":1, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1669259, 1531135, 1531135, '4954727', 'DIR', 5381349, 5921183, null, null, null, null, null, 'GILLESPIE', null, 'GEOFFREY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1669260, 1531135, 1531135, '4954727', 'OFF', 5381349, null, null, null, null, null, null, 'GILLESPIE', null, 'GEOFFREY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1961692, 2196611, 2196610, '4954727', 'DIR', 5921183, null, 1669259, null, null, null, null, 'GILLESPIE', null, 'GEOFFREY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105641127, 103592726, null, 'FM1845143', 'FBO', 104977770, null, null, null, null, '2010-03-22 00:00:00', null, null, null, null, '0614205YYPC WIBKJDXWHKFZCDJ', '4954727', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105755067, null, null, 'FM6061447', 'FBO', 104799510, null, null, null, null, '2003-09-17 00:00:00', null, null, null, null, '0614205OXFKWPUZIPJLXYKR ILQ', '4954727', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6355428, '4954727', 'ADCORP', '2005-06-14 09:18:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6355556, '4954727', 'FILE', '2005-06-14 09:40:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6466334, '4954727', 'FILE', '2005-08-02 14:18:38', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6466631, '4954727', 'ADCORP', '2005-08-02 15:04:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6596448, '4954727', 'FILE', '2005-10-03 12:58:21', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7302429, '4954727', 'FILE', '2006-09-27 12:02:40', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7879279, '4954727', 'FILE', '2007-09-21 10:52:54', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242019, '4954727', 'FILE', '2015-07-28 14:46:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381350, '4954727', 'FILE', '2003-09-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381351, '4954727', 'FILE', '2002-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381352, '4954727', 'FILE', '2001-11-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381353, '4954727', 'FILE', '2000-09-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381349, '4954727', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5693022, '4954727', 'ADCORP', '2004-04-24 10:10:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5915165, '4954727', 'FILE', '2004-10-04 09:36:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5921183, '4954727', 'FILE', '2004-10-06 15:43:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5921193, '4954727', 'FILE', '2004-10-06 15:44:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8734851, '4954727', 'FILE', '2009-03-18 11:14:27', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9054719, '4954727', 'FILE', '2009-10-23 11:28:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104799510, 'FM6061447', 'CONVFMREGI', '2003-09-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104977770, 'FM1845143', 'CONVFMREGI', '2010-03-22 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5381350, 'CONVL', '2003-09-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5381351, 'CONVL', '2002-11-01 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5381352, 'CONVL', '2001-11-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5381353, 'CONVL', '2000-09-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5915165, 'ANNBC', '2004-10-04 09:36:23', null, null, '2004-09-15 00:00:00', null, 'N', null, null, 'F ', null, '101387728', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5921183, 'TRANS', '2004-10-06 15:43:00', null, null, null, null, 'N', null, null, 'F ', 5921183, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5921193, 'NOALA', '2004-10-06 15:44:33', null, null, null, null, 'N', null, null, 'F ', 5921193, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6355556, 'NOALA', '2005-06-14 09:40:34', null, null, null, null, 'N', null, null, 'F ', 6355556, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6466334, 'NOCAD', '2005-08-03 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6596448, 'ANNBC', '2005-10-03 12:58:21', null, null, '2005-09-15 00:00:00', null, 'N', null, null, 'F ', null, '104280573', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7302429, 'ANNBC', '2006-09-27 12:02:40', null, null, '2006-09-15 00:00:00', null, 'N', null, null, 'F ', null, '107182123', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7879279, 'ANNBC', '2007-09-21 10:52:54', null, null, '2007-09-15 00:00:00', null, 'N', null, null, 'F ', null, '110121969', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8734851, 'ANNBC', '2009-03-18 11:14:27', null, null, '2008-09-15 00:00:00', null, 'N', null, null, 'F ', null, '113098834', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9054719, 'ANNBC', '2009-10-23 11:28:00', null, null, '2009-09-15 00:00:00', null, 'N', null, null, 'F ', null, '116186610', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242019, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104799510, 'FRREG', '2003-09-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104977770, 'FRREG', '2010-03-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('4954727', null, 'BC', '2000-09-15 00:00:00', '2009-09-15 00:00:00', '2004-10-06 15:43:00', null, null, null, 'NTAGVUNM', 'CRLPUIFN', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM6061447', null, 'SP', '2003-09-17 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2003-09-17 00:00:00', null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1845143', null, 'SP', '2010-03-22 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1240790, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('4954727', 5381349, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM6061447', 104799510, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1845143', 104977770, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4954727', 'CO', 5381349, 0, null, 'DRCOIJKJOLNWLYNVXNCW', 'MYFLXWDIEDHSZV YV HEIUKXM', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM6061447', 'CO', 104799510, 0, null, 'JKQMSAIZRZAWYMTTTXVJ', 'JIGOHEOACVQBAHCEGQENISSPF', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1845143', 'CO', 104977770, 0, null, 'JPFNVLCRQYHLZPGSIUCQ', 'BMZSRHEGGEOVCHPPQDGMYGRMB', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RG', 9242019, null, 7535153, 7535153, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RC', 9242019, null, 7535153, 7535153, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RG', 5381349, 5921183, 1531134, 1531134, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RC', 5381349, 5921183, 1531134, 1531134, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RC', 5921183, 6466334, 2196613, 2196612, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RG', 5921183, 6466334, 2196615, 2196614, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RG', 6466334, 9242019, 3208074, 3208073, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4954727', 'RC', 6466334, 9242019, 3208072, 3208071, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM1845143', 'FO', 104977770, null, 103346956, 103346956, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1531134, 'BC', 'CA', '5AIGVO', 'PJGCLLVNOBDPWZKENCJFBXWYL', 'PDBMGZBSBEUXNHRRQXFZKDMYD', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196612, 'BC', 'CA', 'PQZZDC', 'E DVFFKNPBPHLUE LXZFBGMNS', 'WXAXOSDDAGHBWNTXZKORVPF E', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196613, 'BC', 'CA', 'SSJQ5L', 'VTDLYFOCMTATUSFJ DADTD N ', 'JBKUQBBPOTYOEYRIRZIPID TU', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196614, 'BC', 'CA', '0KJ3QK', 'DLDRYAVXUCLBTN  UDWK VWJK', 'EQPZAHHINIWDFUN KUYEFK RY', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196615, 'BC', 'CA', 'SYWQRZ', 'QUFKIEIEOHQIFV FULKSCRYDP', 'JBD RG ZFHSAJQCVGERQICOLX', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208071, 'BC', 'CA', 'ZCIGRN', ' Z WBETEAIRJDFLEFTLOVRCVR', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208072, 'BC', 'CA', 'IYTVT0', 'JARHRTWNIMXBWFVZNAUXFALI ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208073, 'BC', 'CA', 'UJ3I06', 'MCRBKFBWGOHNSNT OPACYKHHI', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208074, 'BC', 'CA', 'GTN3YW', 'MIR WJ MTHWJLLOXBDZAUATMT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535153, 'BC', 'CA', 'NSIDQI', 'VYCCXPHUOVXQTGWYKCIBHMFIV', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103346956, 'BC', 'CA', '8VJBD0', null, null, null, 'WEST VANCOUVER', 'BAS', 'GKQUISJZKEOY JWPFFCHUEBLDGXLRODMEUYBKJWR', ' YJIWCTLGOZSWJJCDXXC', null, null, null, '033', null, 'PMXUZLDJIPKHRAR', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A9592574": {
            "corp_num":'A9592574', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":1, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105778013, null, null, 'FM1227394', 'FBO', 104961111, null, null, null, null, '2009-08-12 00:00:00', null, null, null, null, 'A0053427FOBWZXDIKVMOXEEACSSF', 'A9592574', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510879, 7535987, 7535986, 'A9592574', 'ATT', 9242693, null, 241959, null, null, null, null, null, null, null, 'BC0121625RMWLGZFNVIHPMPBVPEYA', 'BC3505058', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241959, 212679, 212679, 'A9592574', 'ATT', 540651, 9242693, null, null, null, null, null, null, null, null, 'RGMVRSFOKDIZERY CKTC', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241960, 212680, 212680, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'BEATON', null, 'ELIZABETH', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241961, 212681, 212681, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'CARTER', null, 'KIM', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241962, 212682, 212682, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'CLARK', null, 'GREG', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241963, 212683, 212683, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'CORTESE', null, 'ROBERTO', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241964, 212684, 212684, 'A9592574', 'DIR', 540651, null, null, null, null, null, null, 'DOWDING', null, 'JANICE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241965, 212684, 212684, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'DOWDING', null, 'JANICE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241966, 212685, 212685, 'A9592574', 'DIR', 540651, null, null, null, null, null, null, 'MANNING', null, 'GERALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241967, 212685, 212685, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'MANNING', null, 'GERALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241968, 212686, 212686, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'RAHILL', null, 'DONNACHA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241969, 212687, 212687, 'A9592574', 'DIR', 540651, null, null, null, null, null, null, 'SCHELLENS', null, 'KAREL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241970, 212687, 212687, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'SCHELLENS', null, 'KAREL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241971, 212688, 212688, 'A9592574', 'DIR', 540651, null, null, null, null, null, null, 'SHANNON', null, 'LORRIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241972, 212688, 212688, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'SHANNON', null, 'LORRIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241973, 212689, 212689, 'A9592574', 'DIR', 540651, null, null, null, null, null, null, 'SLAATS', null, 'RONALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241974, 212689, 212689, 'A9592574', 'OFF', 540651, null, null, null, null, null, null, 'SLAATS', null, 'RONALD', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6131779, 'A9592574', 'FILE', '2005-02-17 12:52:19', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6781060, 'A9592574', 'FILE', '2005-12-29 11:26:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7463049, 'A9592574', 'FILE', '2007-01-15 11:47:02', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7657304, 'A9592574', 'ADCORP', '2007-05-09 13:45:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242693, 'A9592574', 'FILE', '2017-04-04 16:19:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540651, 'A9592574', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540652, 'A9592574', 'FILE', '2003-02-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540653, 'A9592574', 'FILE', '2002-04-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540654, 'A9592574', 'FILE', '2000-12-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5657305, 'A9592574', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5688948, 'A9592574', 'FILE', '2004-04-21 16:13:39', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8066579, 'A9592574', 'FILE', '2008-01-11 15:16:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8727866, 'A9592574', 'FILE', '2009-03-13 14:33:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9189992, 'A9592574', 'FILE', '2010-01-19 11:58:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104961111, 'FM1227394', 'CONVFMREGI', '2009-08-12 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (540652, 'CONVL', '2003-02-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (540653, 'CONVL', '2002-04-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (540654, 'CONVL', '2000-12-13 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5688948, 'ANNXP', '2004-04-21 16:13:39', null, null, '2003-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6131779, 'ANNXP', '2005-02-17 12:52:19', null, null, '2004-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6781060, 'ANNXP', '2005-12-29 11:26:17', null, null, '2005-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7463049, 'ANNXP', '2007-01-15 11:47:02', null, null, '2006-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8066579, 'ANNXP', '2008-01-11 15:16:33', null, null, '2007-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8727866, 'ANNXP', '2009-03-13 14:33:17', null, null, '2008-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9189992, 'ANNXP', '2010-01-19 11:58:00', null, null, '2009-12-13 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242693, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104961111, 'FRREG', '2009-08-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A9592574', null, 'A', '2000-12-13 00:00:00', '2009-12-13 00:00:00', null, null, null, null, 'KPPEKOSQ', 'XARPETDX', 'HMWFIXTZHTQM@TXEUZUIV.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1227394', null, 'SP', '2009-08-12 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2009-08-12 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A9592574', 540651, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1227394', 104961111, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A9592574', 540651, 6131779, null, 'FD', 'COR', '2000-07-31 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A9592574', 6131779, null, null, 'FD', 'COR', '2000-07-31 00:00:00', null, '378756-7', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A9592574', 'CO', 540651, 0, null, 'BCMNBVRKSBZBNNSZOWHP', 'NRUDTIZXYB EZRELFODJDUFXS', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A9592574', 'NO', 5657305, 0, null, 'TNEJYMTGUARVJRWOKGRD', 'WCXVORCUYYHNLIFKEROVKYEMY', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1227394', 'CO', 104961111, 0, null, 'XDHOMVSJGHYOJNYATOIC', ' XNUPLO VTTPRMJFFXBINOAJY', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A9592574', 'HD', 540651, null, 212678, 212678, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212678, 'ON', 'CA', '1QYBA0', 'BHTXGTAOMAGNRRNAMCCLQIIOY', null, null, 'OAKVILLE', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM7768377": {
            "corp_num":'FM7768377', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105395439, 103280245, null, 'FM7768377', 'FCP', 104943462, null, null, null, null, null, null, 'BUSINESS LAWYERS', null, 'SYNERGY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604136, 103555735, null, 'FM7768377', 'FBO', 104943462, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071LLNH DNNRCCCNNYWHLZU', '8267410', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943462, 'FM7768377', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104943462, 'FRREG', '2008-12-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM7768377', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186243, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM7768377', 104943462, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM7768377', 'CO', 104943462, 0, null, 'KIJAYWFMDJGNWWYXCBAJ', 'DQBOOTKLLFTGMHIUPEJQXGGJR', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM7768377', 'FO', 104943462, null, 103280246, 103280246, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280246, null, 'CA', 'WUSDL9', 'CYWTMDNFDUFBOZZROVGYWGYVO', null, null, 'DELTA', 'FOR', 'FCMBUPLGJMJRCFOVWQM VMOOVXBIZGTCSQGOPOHE', 'PTWYXEWHLFTAVC ZVMQB', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_C8555960": {
            "corp_num":'C8555960', "corp_typ_cd":'C', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1337715, 1214404, 1214404, 'C8555960', 'DIR', 4524285, 6608265, null, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1337716, 1214404, 1214404, 'C8555960', 'OFF', 4524285, 6597413, null, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2261922, 3419756, 3419756, 'C8555960', 'OFF', 6597413, 7189315, 0, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2266047, 3437285, 3437284, 'C8555960', 'DIR', 6608265, 7189306, 1337715, 'C', null, null, null, 'MOHR', 'PHILLIP', 'BRUCE ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2536266, 4600111, 4600110, 'C8555960', 'DIR', 7189306, null, 2266047, null, null, null, null, 'MOHR', 'PHILLIP', 'BRUCE ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2536274, 4600135, 4600135, 'C8555960', 'OFF', 7189315, null, 0, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6608265, 'C8555960', 'FILE', '2005-10-07 10:12:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6597413, 'C8555960', 'FILE', '2005-10-03 16:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6597431, 'C8555960', 'FILE', '2005-10-03 16:41:37', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7189306, 'C8555960', 'FILE', '2006-07-11 15:05:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7189315, 'C8555960', 'FILE', '2006-07-11 15:07:41', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7361673, 'C8555960', 'ADCORP', '2006-11-07 14:23:09', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7869174, 'C8555960', 'FILE', '2007-09-15 08:00:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242527, 'C8555960', 'FILE', '2015-07-28 14:46:42', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524285, 'C8555960', 'CONVCIN', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524286, 'C8555960', 'FILE', '2003-08-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524287, 'C8555960', 'FILE', '2002-09-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524288, 'C8555960', 'FILE', '2001-07-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524289, 'C8555960', 'FILE', '2000-08-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524290, 'C8555960', 'FILE', '1999-09-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524291, 'C8555960', 'FILE', '1998-07-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524292, 'C8555960', 'FILE', '1997-07-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524293, 'C8555960', 'FILE', '1997-07-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524294, 'C8555960', 'FILE', '1996-09-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524295, 'C8555960', 'FILE', '1996-07-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524296, 'C8555960', 'FILE', '1996-05-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524297, 'C8555960', 'FILE', '1995-06-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524298, 'C8555960', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5837762, 'C8555960', 'ADCORP', '2004-08-10 14:14:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5837768, 'C8555960', 'FILE', '2004-08-10 14:15:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8366741, 'C8555960', 'FILE', '2008-07-18 10:22:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8970759, 'C8555960', 'FILE', '2009-08-26 11:35:26', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524286, 'CONVL', '2003-08-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524287, 'CONVL', '2002-09-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524288, 'CONVL', '2001-07-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524289, 'CONVL', '2000-08-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524290, 'CONVL', '1999-09-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524291, 'CONVL', '1998-07-13 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524292, 'CONVL', '1997-07-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524293, 'CONVL', '1997-07-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524294, 'CONVL', '1996-09-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524295, 'CONVL', '1996-07-24 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524296, 'CONVL', '1996-05-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4524297, 'CONVL', '1995-06-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5837768, 'ANNBC', '2004-08-10 14:15:35', null, null, '2004-06-26 00:00:00', null, 'N', null, null, 'F ', null, '100872035', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6597413, 'ANNBC', '2005-10-03 16:36:00', null, null, '2005-06-26 00:00:00', null, 'N', null, null, 'F ', null, '103724621', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6597431, 'NOCAD', '2005-10-04 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6608265, 'TRANS', '2005-10-07 10:12:20', null, null, null, null, 'N', null, null, 'F ', 6608265, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7189306, 'NOCDR', '2006-07-11 15:05:29', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7189315, 'ANNBC', '2006-07-11 15:07:41', null, null, '2006-06-26 00:00:00', null, 'N', null, null, 'F ', null, '106593320', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7869174, 'ANNBC', '2007-09-15 08:00:22', null, null, '2007-06-26 00:00:00', null, 'N', null, null, 'F ', null, '109535484', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8366741, 'ANNBC', '2008-07-18 10:22:52', null, null, '2008-06-26 00:00:00', null, 'N', null, null, 'F ', null, '112487772', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8970759, 'ANNBC', '2009-08-26 11:35:26', null, null, '2009-06-26 00:00:00', null, 'N', null, null, 'F ', null, '115554958', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242527, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('C8555960', null, 'C', '1995-06-26 00:00:00', '2009-06-26 00:00:00', '2005-10-07 10:12:20', null, null, null, 'OVEJXXNN', 'NSMVJKYF', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C8555960', 4524285, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C8555960', 4524285, null, null, 'AB', 'COR', '1989-07-20 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C8555960', 'CO', 4524285, 0, 4524298, 'OCUFDYRQMTAPLIBQOLZA', 'KWEUOISSUJENCVUBICNPLR WP', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C8555960', 'CO', 4524298, 0, null, 'HWJISVLOJCEADGWZMGPR', 'YIIWYBQLIZGZBSAVZULBHHBAP', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8555960', 'RG', 9242527, null, 7535661, 7535661, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8555960', 'RC', 9242527, null, 7535661, 7535661, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8555960', 'RG', 4524285, 6597431, 1214403, 1214403, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8555960', 'RC', 4524285, 6597431, 1214403, 1214403, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8555960', 'RG', 6597431, 9242527, 3419781, 3419780, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8555960', 'RC', 6597431, 9242527, 3419779, 3419778, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1214403, 'BC', 'CA', '9G3E12', 'OUAUHNZEMYXT SQASKGONFCTI', 'OHUTKREKXHTSPZ VKYQJEAWGS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419778, 'BC', 'CA', 'K1NJPT', 'GOHYVNBUJHSPWRMIGVEKRUVPS', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419779, 'BC', 'CA', '9NI8QD', 'UFPDBFMYPRRZXHLLIQP BHMVQ', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419780, 'BC', 'CA', 'DLVK75', 'DXFFUZDFCYCXVUHWQDYQVYMEW', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419781, 'BC', 'CA', '9ESTEM', 'NDOUFPAQSGVHKIAAUKHAYEDYF', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535661, 'BC', 'CA', 'VXOLH9', 'QUXZFRHQIZLLIXZVTJPDXJMQP', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A1196902": {
            "corp_num":'A1196902', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":1, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510945, 7536119, 7536118, 'A1196902', 'ATT', 9242759, null, 3396139, null, null, null, null, null, null, null, 'BC0121625O  VQSZLYMODMJL  LGV', 'BC0978714', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3396139, 7187950, 7187951, 'A1196902', 'ATT', 8985982, 9242759, null, null, null, null, null, null, null, null, 'S DGLQWW TQMUYNJNIOY', null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242759, 'A1196902', 'FILE', '2017-04-04 16:19:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8985982, 'A1196902', 'FILE', '2009-09-08 12:28:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9005775, 'A1196902', 'FILE', '2009-09-22 13:15:35', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8985982, 'REGS2', '2009-09-08 12:28:58', null, null, null, null, 'N', null, null, 'P ', 8985982, null, 'NR5989362', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9005775, 'AM_XP', '2009-09-22 13:15:35', null, null, null, null, 'N', null, null, 'P ', 9005775, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242759, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A1196902', null, 'A', '2009-09-08 12:28:58', null, null, null, null, null, 'ZBRBASHB', 'CBVFKISK', 'BJZXZIHPGFYV@LVAFBLGN.com', null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A1196902', 8985982, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A1196902', 8985982, null, null, 'ON', 'COR', '2008-02-28 00:00:00', null, '1761802', null, 'HOLIDAY FILMS INC.', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A1196902', 'AS', 8985982, 0, null, 'VXWFTBAWFPJNDYJUXVOT', 'UFTOBFEBMBKB  UVEUKHNGEMZ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A1196902', 'CO', 8985982, 0, null, 'NGVGFEIXSPNANRYXYKZX', 'LFQMDNIUJYCIU  DCDRDZFYXP', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A1196902', 'HD', 9005775, null, 7217652, 7217651, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A1196902', 'HD', 8985982, 9005775, 7187949, 7187948, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7187948, 'ON', 'CA', 'EHWLA6', 'UNVXYLHAEEAERIURXPIFCQFSE', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7187949, 'ON', 'CA', 'XNKEDB', 'ZXTTMNUIJTOITA QSYNQWICUP', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7217651, 'ON', 'CA', 'CXDNCX', 'CRQNUWPOLENSFYEENAINYSCRC', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7217652, 'ON', 'CA', '7Z77EV', 'CNUVFHJKRCGPJTHBBTZJ AM E', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM9327483": {
            "corp_num":'FM9327483', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105641127, 103592726, null, 'FM9327483', 'FBO', 104977770, null, null, null, null, '2010-03-22 00:00:00', null, null, null, null, '0614205VCNFWESXFLITJEFOXWPH', '3967633', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105426618, 103346955, null, 'FM9327483', 'FCP', 104977770, null, null, null, null, null, null, 'GEOFFREY', null, 'GILLESPIE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104977770, 'FM9327483', 'CONVFMREGI', '2010-03-22 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104977770, 'FRREG', '2010-03-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9327483', null, 'SP', '2010-03-22 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1240790, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9327483', 104977770, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9327483', 'CO', 104977770, 0, null, 'EJBQGENYFCTPFAIXDQFL', 'SIOKXTTGUAUW LWBIEFKFKXTS', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9327483', 'FO', 104977770, null, 103346956, 103346956, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103346956, 'BC', 'CA', 'P6AJ7Q', null, null, null, 'WEST VANCOUVER', 'BAS', 'JEUQJMXWSXFKMZMIIOAYFMWEXMAPTSEOPSOSKMMX', 'INDUTMODFOKMROOSMQZT', null, null, null, '617', null, 'THVSTBSGUYMBUEE', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_9645624": {
            "corp_num":'9645624', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2390060, 3982722, 3982721, '9645624', 'DIR', 6889406, null, 177654, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2390051, 3982665, 3982665, '9645624', 'OFF', 6889381, null, 0, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177652, 155618, 155618, '9645624', 'DIR', 424281, null, null, null, null, null, null, 'FARRELL', null, 'RICKY WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177653, 155618, 155618, '9645624', 'OFF', 424281, null, null, null, null, null, null, 'FARRELL', null, 'RICKY WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177654, 155619, 155619, '9645624', 'DIR', 424281, 6889406, null, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177655, 155619, 155619, '9645624', 'OFF', 424281, 6889381, null, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6210660, '9645624', 'FILE', '2005-04-04 11:31:45', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6210656, '9645624', 'ADCORP', '2005-04-04 11:31:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6889381, '9645624', 'FILE', '2006-02-15 16:07:11', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6889406, '9645624', 'FILE', '2006-02-15 16:10:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7506338, '9645624', 'FILE', '2007-02-07 15:12:25', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9241789, '9645624', 'FILE', '2015-07-28 14:46:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424281, '9645624', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424282, '9645624', 'FILE', '2003-04-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424283, '9645624', 'FILE', '2003-04-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424284, '9645624', 'FILE', '2001-03-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424285, '9645624', 'FILE', '2001-01-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424286, '9645624', 'FILE', '1999-03-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424287, '9645624', 'FILE', '1998-05-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424288, '9645624', 'FILE', '1998-02-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424289, '9645624', 'FILE', '1997-02-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424290, '9645624', 'FILE', '1996-05-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424291, '9645624', 'FILE', '1996-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424292, '9645624', 'FILE', '1996-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424293, '9645624', 'FILE', '1996-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424294, '9645624', 'FILE', '1993-02-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424295, '9645624', 'FILE', '1992-04-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424296, '9645624', 'FILE', '1991-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424297, '9645624', 'FILE', '1991-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424298, '9645624', 'FILE', '1991-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424299, '9645624', 'FILE', '1988-02-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424300, '9645624', 'FILE', '1987-04-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424301, '9645624', 'FILE', '1986-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424302, '9645624', 'FILE', '1985-02-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424303, '9645624', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424304, '9645624', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424305, '9645624', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424306, '9645624', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424307, '9645624', 'FILE', '1980-07-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5706124, '9645624', 'FILE', '2004-05-05 11:35:43', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8122051, '9645624', 'FILE', '2008-02-14 11:57:16', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8875342, '9645624', 'FILE', '2009-06-18 11:20:27', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424282, 'CONVL', '2003-04-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424283, 'CONVL', '2003-04-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424284, 'CONVL', '2001-03-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424285, 'CONVL', '2001-01-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424286, 'CONVL', '1999-03-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424287, 'CONVL', '1998-05-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424288, 'CONVL', '1998-02-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424289, 'CONVL', '1997-02-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424290, 'CONVL', '1996-05-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424291, 'CONVL', '1996-04-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424292, 'CONVL', '1996-04-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424293, 'CONVL', '1996-04-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424294, 'CONVL', '1993-02-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424295, 'CONVL', '1992-04-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424296, 'CONVL', '1991-08-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424297, 'CONVL', '1991-08-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424298, 'CONVL', '1991-08-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424299, 'CONVL', '1988-02-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424300, 'CONVL', '1987-04-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424301, 'CONVL', '1986-03-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424302, 'CONVL', '1985-02-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424303, 'CONVL', '1984-04-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424304, 'CONVL', '1984-04-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424305, 'CONVL', '1984-04-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424306, 'CONVL', '1984-04-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (424307, 'CONVL', '1980-07-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5706124, 'ANNBC', '2004-05-05 11:35:43', null, null, '2004-01-23 00:00:00', null, 'N', null, null, 'F ', null, '26078413', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6210660, 'ANNBC', '2005-04-04 11:31:45', null, null, '2005-01-23 00:00:00', null, 'N', null, null, 'F ', null, '102363967', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6889381, 'ANNBC', '2006-02-15 16:07:11', null, null, '2006-01-23 00:00:00', null, 'N', null, null, 'F ', null, '105239909', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6889406, 'TRANS', '2006-02-15 16:10:48', null, null, null, null, 'N', null, null, 'F ', 6889406, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7506338, 'ANNBC', '2007-02-07 15:12:25', null, null, '2007-01-23 00:00:00', null, 'N', null, null, 'F ', null, '108223330', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8122051, 'ANNBC', '2008-02-14 11:57:16', null, null, '2008-01-23 00:00:00', null, 'N', null, null, 'F ', null, '111154670', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8875342, 'ANNBC', '2009-06-18 11:20:27', null, null, '2009-01-23 00:00:00', null, 'N', null, null, 'F ', null, '114169055', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9241789, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('9645624', null, 'BC', '1959-01-23 00:00:00', '2009-01-23 00:00:00', '2006-02-15 16:10:48', null, null, null, 'IZVPSDDA', 'KAWFKDAN', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('9645624', 424281, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('9645624', 'CO', 424281, 0, null, 'NKUPFSFAUTDZXDNDZTGA', 'MXPYQQDGLJCIVJQWUMUHZJZJK', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9645624', 'RG', 9241789, null, 7534923, 7534923, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9645624', 'RC', 9241789, null, 7534923, 7534923, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9645624', 'RG', 424281, 6889406, 155617, 155617, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9645624', 'RC', 424281, 6889406, 155617, 155617, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9645624', 'RC', 6889406, 9241789, 3982724, 3982723, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9645624', 'RG', 6889406, 9241789, 3982726, 3982725, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (155617, 'BC', 'CA', 'LFBIZE', 'A CG MWKJSZNVLECMKWQRHKUI', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982723, 'BC', 'CA', 'VR2JKM', 'A XZZKNYJNTFVMO GXHSKWDEK', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982724, 'BC', 'CA', '5YCJP4', 'VKLGWIA UQXOQMWJDPHNTYEEH', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982725, 'BC', 'CA', 'HIQKUW', 'CUUWFZCILYNKBWHYHESAZFNJS', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982726, 'BC', 'CA', 'LM9ZPV', 'DWIPETKJRRTOEQRRWEHBAPOIN', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534923, 'BC', 'CA', 'CDRDYC', 'KBOCQRIO KEVFYOGYXLDCBJGP', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_2075204": {
            "corp_num":'2075204', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511446, 7537108, null, '2075204', 'INC', 9242902, null, null, null, null, null, null, 'Phillips', null, 'Tashia', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511447, 7537110, 7537111, '2075204', 'DIR', 9242902, null, null, null, null, null, null, 'Yearwood', 'V', 'Jen', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242902, '2075204', 'FILE', '2018-07-24 13:47:53', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242902, 'ICORP', '2018-07-24 13:47:53', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('2075204', null, 'BC', '2018-07-24 13:47:53', null, null, null, null, null, 'FUJLDMMO', 'VYOPYFSN', 'RWZONLAWCXEJ@REEJLIDJ.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('2075204', 9242902, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('2075204', 'NB', 9242902, 0, null, 'JJMHNCAKLXGXHDTQSMGE', 'JGVKCRHTHCQHBUUMQXNUMLDZJ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2075204', 'RG', 9242902, null, 7537113, 7537112, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2075204', 'RC', 9242902, null, 7537115, 7537114, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537112, 'BC', 'CA', 'C8RLQ1', 'OHLCFABVHTN GCQLUEGVDCVOK', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537113, 'BC', 'CA', '15PQWF', 'IKAB SYPOOMPZRJCLRE WQDYC', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537114, 'BC', 'CA', 'PQXYPA', 'YTHTJURCDMBRPUYCSQRXLRQLC', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537115, 'BC', 'CA', 'W6OQ4X', 'WRFSRPKKXZJSLCFVUEDD OGCS', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_4241301": {
            "corp_num":'4241301', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":1, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511442, 7537095, null, '4241301', 'INC', 9242901, null, null, null, null, null, null, null, null, null, 'AVVTOZUTFXTK TABISC ', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511443, 7537097, 7537098, '4241301', 'DIR', 9242901, null, null, null, null, null, null, 'Nobu', null, 'Aiki', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511444, 7537099, 7537100, '4241301', 'DIR', 9242901, null, null, null, null, null, null, 'Ubright', 'K.', 'Adrienne', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511445, 7537101, 7537102, '4241301', 'DIR', 9242901, null, null, null, null, null, null, 'Johannsen', null, 'Gary', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242901, '4241301', 'FILE', '2018-07-24 13:39:06', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242901, 'ICORP', '2018-07-24 13:39:06', null, null, null, null, 'N', null, null, 'F ', null, null, 'NR5634946', null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('4241301', null, 'BC', '2018-07-24 13:39:06', null, null, null, null, null, 'AUVNQYCT', 'GXAWQJDX', 'IESFKIISOSQQ@RDGVFLGI.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('4241301', 9242901, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4241301', 'CO', 9242901, 0, null, 'GVJCNNMRRDLHNZOGPNIN', 'XCUBPIM YRSWHAWTLUMFRPRUZ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4241301', 'TR', 9242901, 1, null, 'NASKDBHIYSXKFRCNBWFM', 'MMRTKDCWLGXOFULSZYEIIHKRO', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4241301', 'RG', 9242901, null, 7537104, 7537103, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4241301', 'RC', 9242901, null, 7537106, 7537105, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537103, 'BC', 'CA', 'LB7WF5', 'TVZP ZWOW HIGIGKSCGSMLQKB', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537104, 'BC', 'CA', 'HAL93D', 'YJCSBP GDAPWWU NEHWNULAAD', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537105, 'BC', 'CA', 'Z9WZAL', 'UDALFWMJLQPOBQOHVZXKMCAGO', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537106, 'BC', 'CA', '1E23RB', 'GWGFLOUDQFERGBYZLARZGNTGU', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM6803359": {
            "corp_num":'FM6803359', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682496, null, null, 'FM6803359', 'FBO', 105301928, null, null, null, null, '2001-05-09 14:36:16', null, null, null, null, 'A0031179FOUBFKXNEHZOWXMRPIDF', 'A2876262', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721467, 'FM6803359', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301928, 'FM6803359', 'CONVFMACP', '2001-05-09 14:36:16', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104721467, 'FRREG', '2000-06-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105301928, 'FRMEM', '2001-05-09 14:36:16', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM6803359', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM6803359', 104721467, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM6803359', 'CO', 104721467, 0, null, 'IIBURFTKESZAKGUEXLAN', 'NTYYOTMJAOPIJZDEHMWMKXKKG', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
    "corp_FM5427060": {
            "corp_num":'FM5427060', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105755067, null, null, 'FM5427060', 'FBO', 104799510, null, null, null, null, '2003-09-17 00:00:00', null, null, null, null, '0614205HDVZHS FGQBQCHQRPGFY', '7266028', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104799510, 'FM5427060', 'CONVFMREGI', '2003-09-17 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104799510, 'FRREG', '2003-09-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM5427060', null, 'SP', '2003-09-17 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2003-09-17 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM5427060', 104799510, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM5427060', 'CO', 104799510, 0, null, 'FBRNSFKXCBZQAARIPPLX', 'JVXUZVGQMSWNUZMPAWTANBYPD', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
    "corp_A3781337": {
            "corp_num":'A3781337', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510870, 7535969, 7535968, 'A3781337', 'ATT', 9242684, null, 148741, null, null, null, null, null, null, null, 'BC0121625QEBKOPP JFBBUKUAPZHM', 'BC0461267', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148741, 130138, 130138, 'A3781337', 'ATT', 364974, 9242684, null, null, null, null, null, 'GIFFORD ', null, 'MARTIN N.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148742, 130139, 130139, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'BEALE', null, 'MARK S.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148743, 130140, 130140, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'BEATTIE', null, 'IAN J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148744, 130141, 130141, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'BRAY', null, 'TIMOTHY J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148745, 130142, 130142, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'BROWN', null, 'KEITH C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148746, 130143, 130143, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'COVINGTON', null, 'HOWARD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148747, 130144, 130144, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'KIRK', null, 'ANNA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148748, 130145, 130145, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'LEWIS', null, 'RICHARD D.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148749, 130146, 130146, 'A3781337', 'OFF', 364974, null, null, null, null, null, null, 'NEW STAR ASSET', null, 'MANAGEMENT LTD.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148750, 130147, 130147, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'RUVIGNY', null, 'RUPERT F. J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148751, 130148, 130148, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'SANDERS', null, 'CHRISTIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148752, 130149, 130149, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'SANDERS', null, 'MICHELLE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148753, 130150, 130150, 'A3781337', 'DIR', 364974, null, null, null, null, null, null, 'WEEKES', null, 'DEBORAH J.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6450564, 'A3781337', 'FILE', '2005-07-26 08:35:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6472092, 'A3781337', 'FILE', '2005-08-05 10:18:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7251378, 'A3781337', 'FILE', '2006-08-22 10:31:55', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7785800, 'A3781337', 'FILE', '2007-07-25 08:53:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7789158, 'A3781337', 'ADCORP', '2007-07-26 14:39:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242684, 'A3781337', 'FILE', '2017-04-04 16:19:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364974, 'A3781337', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364975, 'A3781337', 'FILE', '2003-08-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364976, 'A3781337', 'FILE', '2002-08-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364977, 'A3781337', 'FILE', '2002-08-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364978, 'A3781337', 'FILE', '2002-02-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364979, 'A3781337', 'FILE', '2002-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364980, 'A3781337', 'FILE', '2002-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364981, 'A3781337', 'FILE', '2001-11-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364982, 'A3781337', 'FILE', '2001-11-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364983, 'A3781337', 'FILE', '2001-11-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364984, 'A3781337', 'FILE', '2000-07-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364985, 'A3781337', 'FILE', '1999-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364986, 'A3781337', 'FILE', '1999-08-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364987, 'A3781337', 'FILE', '1999-08-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364988, 'A3781337', 'FILE', '1999-08-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364989, 'A3781337', 'FILE', '1998-11-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364990, 'A3781337', 'FILE', '1998-08-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364991, 'A3781337', 'FILE', '1998-03-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364992, 'A3781337', 'FILE', '1998-03-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364993, 'A3781337', 'FILE', '1997-12-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364994, 'A3781337', 'FILE', '1997-11-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364995, 'A3781337', 'FILE', '1997-11-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364996, 'A3781337', 'FILE', '1994-05-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364997, 'A3781337', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364998, 'A3781337', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364999, 'A3781337', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5796928, 'A3781337', 'FILE', '2004-07-12 08:41:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8343436, 'A3781337', 'FILE', '2008-07-03 10:43:14', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364975, 'CONVL', '2003-08-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364976, 'CONVL', '2002-08-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364977, 'CONVL', '2002-08-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364978, 'CONVL', '2002-02-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364979, 'CONVL', '2002-01-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364980, 'CONVL', '2002-01-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364981, 'CONVL', '2001-11-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364982, 'CONVL', '2001-11-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364983, 'CONVL', '2001-11-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364984, 'CONVL', '2000-07-13 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364985, 'CONVL', '1999-12-31 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364986, 'CONVL', '1999-08-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364987, 'CONVL', '1999-08-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364988, 'CONVL', '1999-08-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364989, 'CONVL', '1998-11-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364990, 'CONVL', '1998-08-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364991, 'CONVL', '1998-03-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364992, 'CONVL', '1998-03-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364993, 'CONVL', '1997-12-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364994, 'CONVL', '1997-11-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364995, 'CONVL', '1997-11-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (364996, 'CONVL', '1994-05-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5796928, 'ANNXP', '2004-07-12 08:41:12', null, null, '2004-05-17 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6450564, 'CO_XP', '2005-07-26 08:35:14', null, null, null, null, 'N', null, null, 'F ', 6450564, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6472092, 'ANNXP', '2005-08-05 10:18:35', null, null, '2005-05-17 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7251378, 'ANNXP', '2006-08-22 10:31:55', null, null, '2006-05-17 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7785800, 'ANNXP', '2007-07-25 08:53:17', null, null, '2007-05-17 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8343436, 'ANNXP', '2008-07-03 10:43:14', null, null, '2008-05-17 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242684, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A3781337', null, 'A', '1994-05-17 00:00:00', '2008-05-17 00:00:00', null, null, null, null, 'ZMBDLIVX', 'BATJIXRQ', 'XSHOCOPRLPVJ@MNKRMDKW.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A3781337', 364974, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A3781337', 364974, 5796928, null, 'OT', 'COR', '1985-01-23 00:00:00', 'ENGLAND', null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A3781337', 5796928, 6450564, null, 'OT', 'COR', '1985-01-23 00:00:00', 'ENGLAND', '1880176', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A3781337', 6450564, null, null, 'OT', 'COR', '1985-01-23 00:00:00', 'GB', '1880176', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A3781337', 'CO', 364974, 0, 364997, 'SNVKEUIYBRVBKCYCEDRM', 'HKPJULVNRGZXAONQQRJEWJIGL', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A3781337', 'CO', 364997, 0, 364998, 'ZURIDHLVSTPURTLYKESD', 'QFJRFVLCKKXQAVIMIYMTPCXEB', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A3781337', 'CO', 364998, 0, 364999, 'YIHPYNGGQDLDOULGQNRW', 'OYJPBTQXEYTZOCZPGWMRZZSVZ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A3781337', 'CO', 364999, 0, null, 'TIUNDMWWZEMAWHATFHMO', 'FOWELXGDIKPAGFNIJUDBWAUHM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A3781337', 'HD', 364974, 6450564, 130137, 130137, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A3781337', 'HD', 6450564, null, 3185044, 3185043, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130137, null, null, null, 'YFOTEJYIBYNYKCKTUAHPFZQR ', 'YPBYUXXOURJZGODIOHXCYZWZF', 'WC1B 4HP', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3185043, null, 'GB', 'H8IU1N', 'UUBCWY DKNOCDWWNEVFSCKY O', null, null, 'LONDON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3185044, null, 'GB', 'GKGGEP', 'AWBABLXSDOYSFRUV OLP TLWQ', null, null, 'LONDON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_0549806": {
            "corp_num":'0549806', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037327, 2494013, null, '0549806', 'INC', 6074785, null, null, null, null, null, null, null, null, null, ' FMNCKYCAUVRUBNWDYGG', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037328, 2494015, 2494016, '0549806', 'DIR', 6074785, 8431719, null, null, null, null, null, 'TINGLEY', 'H.', 'CALEB', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037329, 2494017, 2494018, '0549806', 'DIR', 6074785, 7163282, null, null, null, null, null, 'HUQ', 'E.', 'MOHAMMED', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037330, 2494019, 2494020, '0549806', 'DIR', 6074785, 8431719, null, null, null, null, null, 'TSE', 'Y.', 'GARY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2524514, 4564167, 4564166, '0549806', 'DIR', 7163282, 8431719, 2037329, 'C', null, null, null, 'HUQ', 'E.', 'MUHAMMED', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539790, 4611323, 4611323, '0549806', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539791, 4611324, 4611324, '0549806', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539792, 4611325, 4611325, '0549806', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539793, 4611326, 4611326, '0549806', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732684, 5211601, 5211601, '0549806', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732685, 5211602, 5211602, '0549806', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732686, 5211603, 5211603, '0549806', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732687, 5211604, 5211604, '0549806', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123758, 6408221, 6408221, '0549806', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123759, 6408222, 6408222, '0549806', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123760, 6408223, 6408223, '0549806', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123761, 6408224, 6408224, '0549806', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123763, 6408228, 6408227, '0549806', 'DIR', 8431719, null, 2037330, null, null, null, null, 'TSE', 'Y.', 'GARY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123764, 6408230, 6408229, '0549806', 'DIR', 8431719, null, 2524514, null, null, null, null, 'HUQ', 'E.', 'MUHAMMED', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123765, 6408232, 6408231, '0549806', 'DIR', 8431719, null, 2037328, null, null, null, null, 'TINGLEY', 'H.', 'CALEB', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288226, 6882402, 6882402, '0549806', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288227, 6882403, 6882403, '0549806', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288228, 6882404, 6882404, '0549806', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288229, 6882405, 6882405, '0549806', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6074785, '0549806', 'FILE', '2005-01-17 14:57:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7163282, '0549806', 'FILE', '2006-06-26 09:55:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7195364, '0549806', 'FILE', '2006-07-17 08:39:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7617777, '0549806', 'FILE', '2007-04-16 11:58:57', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242595, '0549806', 'FILE', '2016-08-25 15:24:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8431717, '0549806', 'FILE', '2008-09-03 12:36:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8431719, '0549806', 'FILE', '2008-09-03 12:37:09', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8782837, '0549806', 'FILE', '2009-04-20 14:34:23', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6074785, 'ICORP', '2005-01-17 14:57:58', null, null, null, null, 'N', null, null, 'F ', null, null, 'NR9444709', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7163282, 'AM_DI', '2006-06-26 09:55:14', null, null, null, null, 'N', null, null, 'P ', 7163282, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7195364, 'ANNBC', '2006-07-17 08:39:28', null, null, '2006-01-17 00:00:00', null, 'N', null, null, 'F ', null, '105235337', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7617777, 'ANNBC', '2007-04-16 11:58:57', null, null, '2007-01-17 00:00:00', null, 'N', null, null, 'F ', null, '108176959', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8431717, 'ANNBC', '2008-09-03 12:36:22', null, null, '2008-01-17 00:00:00', null, 'N', null, null, 'F ', null, '111108106', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8431719, 'NOCDR', '2008-09-03 12:37:09', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8782837, 'ANNBC', '2009-04-20 14:34:23', null, null, '2009-01-17 00:00:00', null, 'N', null, null, 'F ', null, '114120850', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242595, 'NOCAD', '2016-08-26 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('0549806', null, 'BC', '2005-01-17 14:57:58', '2009-01-17 00:00:00', null, null, null, null, 'KKHTNIHS', 'ALLXVWJB', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0549806', 6074785, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0549806', 'CO', 6074785, 0, null, 'EJCKCRFCVJHMXZKETCES', 'SXSETUWJS OCCQHQYQCZSRKUY', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0549806', 'RG', 9242595, null, 7535791, 7535790, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0549806', 'RC', 9242595, null, 7535791, 7535790, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0549806', 'RG', 6074785, 9242595, 2494022, 2494021, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0549806', 'RC', 6074785, 9242595, 2494024, 2494023, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494021, 'BC', 'CA', 'BW28Y7', '  VLQKYCIOVAPTMMFPHYLBMOP', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494022, 'BC', 'CA', 'Z1B2LR', 'OG  QEJIQHPYX ODAQQOQFURI', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494023, 'BC', 'CA', 'JWHN0P', 'ECOIYPAURBESEHGL YISSGCWB', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494024, 'BC', 'CA', 'HHT6TN', 'UQ AUGV CGP Z ONPDFHULHYW', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535790, 'BC', 'CA', 'LMYOZ2', 'UYQYAGAROWJRIYFTKIBTOFDHQ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535791, 'BC', 'CA', 'P4LRQC', 'YBK XDGFS IBJZYZDXMDLWWMG', 'MGA COLJYDQYHJRLMQEZIX VB', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_7233338": {
            "corp_num":'7233338', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":2, "party_addr_ct":2, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2559124, 4671453, null, '7233338', 'INC', 7237318, null, null, null, null, null, null, 'Rudy', 'E.', 'Brian', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2559125, 4671455, 4671456, '7233338', 'DIR', 7237318, 7926270, null, null, null, null, null, 'Griffiths', null, 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2874884, 5643096, 5643096, '7233338', 'OFF', 7926259, 9104380, 0, null, null, '2007-10-19 11:41:25', null, 'Griffiths', 'A.', 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2874892, 5643120, 5643119, '7233338', 'DIR', 7926270, null, 2559125, null, null, null, null, 'Griffiths', null, 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3451936, 7352471, 7352471, '7233338', 'OFF', 9104380, 9104388, 0, null, null, '2007-10-19 11:41:25', null, 'Griffiths', 'A.', 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3451937, 7352473, 7352473, '7233338', 'OFF', 9104388, null, 0, null, null, '2007-10-19 11:41:25', null, 'Griffiths', 'A.', 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105538816, 103490415, null, 'FM1902222', 'FBO', 104880184, null, null, null, null, '2006-08-16 00:00:00', null, null, null, null, '0765995PXPDGX WZMDTGLH HF O', '7233338', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105552151, 103503750, null, 'FM8009805', 'FBO', 104893496, null, null, null, null, '2007-02-14 00:00:00', null, null, null, null, '0765995 BIQPW AEGXPTRUN FTU', '7233338', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7237318, '7233338', 'FILE', '2006-08-14 13:40:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7926259, '7233338', 'FILE', '2007-10-19 11:41:25', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7926270, '7233338', 'FILE', '2007-10-19 11:43:10', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242244, '7233338', 'FILE', '2015-07-28 14:46:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9104380, '7233338', 'FILE', '2009-11-24 08:40:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9104388, '7233338', 'FILE', '2009-11-24 08:42:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104880184, 'FM1902222', 'CONVFMREGI', '2006-08-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104893496, 'FM8009805', 'CONVFMREGI', '2007-02-14 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7237318, 'ICORP', '2006-08-14 13:40:33', null, null, null, null, 'N', null, null, 'F ', null, null, 'NR5531789', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7926259, 'ANNBC', '2007-10-19 11:41:25', null, null, '2007-08-14 00:00:00', null, 'N', null, null, 'F ', null, '109893842', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7926270, 'NOCDR', '2007-10-19 11:43:10', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9104380, 'ANNBC', '2009-11-24 08:40:23', null, null, '2008-08-14 00:00:00', null, 'N', null, null, 'F ', null, '112859228', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9104388, 'ANNBC', '2009-11-24 08:42:28', null, null, '2009-08-14 00:00:00', null, 'N', null, null, 'F ', null, '115939381', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242244, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104880184, 'FRREG', '2006-08-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104893496, 'FRREG', '2007-02-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('7233338', null, 'BC', '2006-08-14 13:40:33', '2009-08-14 00:00:00', null, null, null, null, 'ZQKGJUOI', 'YEGRPLMP', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1902222', null, 'SP', '2006-08-16 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1095915, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM8009805', null, 'SP', '2007-02-14 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1114375, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('7233338', 7237318, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1902222', 104880184, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM8009805', 104893496, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('7233338', 'CO', 7237318, 0, null, 'ABLYANLOHPWYOKCSHFQL', 'IGHKFVAACAXKBCBYFHK YTGCU', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1902222', 'CO', 104880184, 0, null, 'ZWAZYBRKUOVQQLLHLVLK', 'XU C SXWWQERPDQDSAR ITKTX', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM8009805', 'CO', 104893496, 0, null, 'XRWLQOFOVPMPHTRWILQF', 'QDHMRBKVYAHNHOUCM KH DOEQ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7233338', 'RG', 7237318, 9242244, 4671463, 4671462, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7233338', 'RC', 7237318, 9242244, 4671465, 4671464, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7233338', 'RG', 9242244, null, 7535378, 7535378, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7233338', 'RC', 9242244, null, 7535378, 7535378, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM1902222', 'FO', 104880184, null, 103155280, 103155280, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM8009805', 'FO', 104893496, null, 103180754, 103180754, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671462, 'BC', 'CA', '09LHL3', 'ADOSEIFDWGKOJXEUXPDLL XEZ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671463, 'BC', 'CA', 'KTZ5WW', 'KRWAAFAODVIGGQ QFBTGIQPJZ', 'LANMKECYPHJKLUWICMCVDKQHL', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671464, 'BC', 'CA', '6SPMCA', 'VPKKFCFBYUQBLDGPYUCOOFKTV', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671465, 'BC', 'CA', 'WP56UL', 'ONQLJHGTFVHJOVGUBHZHPSEAO', 'QMNDW UNSB GXSEDXBGJWWHJC', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535378, 'BC', 'CA', 'EVPQY2', ' ISBQVCJXMASWVZLHBXKDRYXO', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103155280, 'BC', 'CA', 'Z5F6RY', null, null, null, 'DELTA', 'BAS', 'TYKNHXYJWO FLDWKHCUTOHHKXM HSGFWNESMEWKO', 'KUWYMMBLFDRPGRETUEWY', null, null, null, '537', null, 'IBGIJBYKBZDSZME', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103180754, 'BC', 'CA', '8SZP1H', null, null, null, 'DELTA', 'BAS', 'BRZBQJRLYJHHWEJYOUZWAWVD GMF DRZWPPSVMDI', 'F YHDDRCWGQGGTXUUKUL', null, null, null, '595', null, 'MZBYSHFCANIKJTM', 'ST', null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_7078358": {
            "corp_num":'7078358', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":2, "party_addr_ct":2, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3058561, 6215114, null, '7078358', 'INC', 8302204, null, null, null, null, null, null, 'Rudy', 'E.', 'Brian', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3058562, 6215116, 6215117, '7078358', 'DIR', 8302204, null, null, null, null, null, null, 'Wolf', null, 'Oliver', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3058563, 6215118, 6215119, '7078358', 'DIR', 8302204, null, null, null, null, null, null, 'Livingstone', null, 'Robert', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3422392, 7264415, 7264415, '7078358', 'OFF', 9038795, null, 0, null, null, '2009-10-14 10:46:35', null, 'Livingstone', null, 'Robert', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3422393, 7264416, 7264416, '7078358', 'OFF', 9038795, null, 0, null, null, '2009-10-14 10:46:35', null, 'Wolf', null, 'Oliver', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604136, 103555735, null, 'FM5850476', 'FBO', 104943462, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071PHYNZVCNLUIDAEXCTYLO', '7078358', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604099, 103555698, null, 'FM1974279', 'FBO', 104943427, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071SBIJDJUGUWPAIITPDLDG', '7078358', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242377, '7078358', 'FILE', '2015-07-28 14:46:36', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8302204, '7078358', 'FILE', '2008-06-06 10:49:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9038795, '7078358', 'FILE', '2009-10-14 10:46:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943427, 'FM1974279', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943462, 'FM5850476', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8302204, 'ICORP', '2008-06-06 10:49:31', null, null, null, null, 'N', null, null, 'F ', null, null, 'NR6563475', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9038795, 'ANNBC', '2009-10-14 10:46:35', null, null, '2009-06-06 00:00:00', null, 'N', null, null, 'F ', null, '115378101', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242377, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104943427, 'FRREG', '2008-12-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104943462, 'FRREG', '2008-12-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('7078358', null, 'BC', '2008-06-06 10:49:31', '2009-06-06 00:00:00', null, null, null, null, 'MAAHDOIC', 'WRCPWOFB', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1974279', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186186, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM5850476', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186243, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('7078358', 8302204, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1974279', 104943427, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM5850476', 104943462, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('7078358', 'CO', 8302204, 0, null, 'DZKUITEZXJEYLDFZTTMH', 'SFMAUKJFASJSJFFGJLZ OFJJH', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1974279', 'CO', 104943427, 0, null, 'PJLXJXVQCJXJAXPSSWUR', 'QFDIGDWAK UXKNKHNFLMFGZZZ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM5850476', 'CO', 104943462, 0, null, 'WZQQROTTFCJVDQGHEMKB', 'IBSBZVHYHSXOAYF JXFQLUUWA', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7078358', 'RG', 8302204, 9242377, 6215121, 6215120, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7078358', 'RC', 8302204, 9242377, 6215123, 6215122, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7078358', 'RG', 9242377, null, 7535511, 7535511, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7078358', 'RC', 9242377, null, 7535511, 7535511, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM1974279', 'FO', 104943427, null, 103280174, 103280174, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM5850476', 'FO', 104943462, null, 103280246, 103280246, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215120, 'BC', 'CA', 'AEB3VS', 'MVBHZZYBQXXZ BHIPKAKRXIIA', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215121, 'BC', 'CA', 'QFSFQ1', 'FTJGREJZYRAFYCJMTMTMJAOYK', 'F PCHKHJRE FPWGKPYISDZIVX', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215122, 'BC', 'CA', 'NKUG9K', 'PLDVEYNCAGBVLJQZJASXGOEDX', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215123, 'BC', 'CA', 'SIHRSR', 'GRAQFOQPHPEFWBQRVFPEWJMCM', 'SYTBXLXCRZSEHQVBHA JPLCZV', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535511, 'BC', 'CA', 'GBWCON', 'LIKTJIUZAOIZYAJXNWBYATBPO', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280174, null, 'CA', 'CZ7ZKD', 'BMPKWHSYFPTSGGLMPGMWSENOQ', null, null, 'DELTA', 'FOR', 'TULTLXOTXQMCPHJLPZZRU  WRULYWLOTQP IEKRP', 'HZYKEHBSLVBXQMDUQKNG', null, null, null, '283', null, 'HPSLUSQXSODGPNO', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280246, null, 'CA', 'F17N3Y', 'PRDBZFZOV RQUPC NGNAYWIDZ', null, null, 'DELTA', 'FOR', 'JQS  DT  BDHSWKCM APOMJAFZNVWCSQ KSSMJOU', 'VYNRQYXDHTHJAORBXLOG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_A4405946": {
            "corp_num":'A4405946', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":1, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510880, 7535989, 7535988, 'A4405946', 'ATT', 9242694, null, 3027731, null, null, null, null, null, null, null, 'BC0121625BESZMXMOJDDSZBIKQCMC', 'BC7347296', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245253, 215620, 215620, 'A4405946', 'ATT', 545718, 8241976, null, null, null, null, null, 'GIFFORD ', null, 'MARTIN N.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245254, 215621, 215621, 'A4405946', 'DIR', 545718, null, null, null, null, null, null, 'BERBIGIER', null, 'CLAUDE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245255, 215622, 215622, 'A4405946', 'DIR', 545718, null, null, null, null, null, null, 'FREUND', null, 'EDOUARD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245256, 215623, 215623, 'A4405946', 'OFF', 545718, null, null, null, null, null, null, 'GELFAND', null, 'BRAHM M.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245257, 215624, 215624, 'A4405946', 'DIR', 545718, null, null, null, null, null, null, 'KALAYDJIAN', null, 'FRANCOIS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245258, 215625, 215625, 'A4405946', 'DIR', 545718, null, null, null, null, null, null, 'PICARD', null, 'GEORGES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245259, 215625, 215625, 'A4405946', 'OFF', 545718, null, null, null, null, null, null, 'PICARD', null, 'GEORGES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3027731, 6122711, 6122710, 'A4405946', 'ATT', 8241969, 9242694, null, null, null, null, null, null, null, null, 'HCYSJOKJSCSQWTFHXACJ', null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6285155, 'A4405946', 'FILE', '2005-05-11 09:49:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7136415, 'A4405946', 'FILE', '2006-06-07 11:08:39', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7600204, 'A4405946', 'FILE', '2007-04-03 13:42:19', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242694, 'A4405946', 'FILE', '2017-04-04 16:19:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545718, 'A4405946', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545719, 'A4405946', 'FILE', '2003-08-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545720, 'A4405946', 'FILE', '2002-08-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545721, 'A4405946', 'FILE', '2002-04-25 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545722, 'A4405946', 'FILE', '2001-02-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5657325, 'A4405946', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5669443, 'A4405946', 'FILE', '2004-04-06 10:47:50', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8241969, 'A4405946', 'FILE', '2008-04-29 14:38:40', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8241976, 'A4405946', 'FILE', '2008-04-29 14:39:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8220338, 'A4405946', 'FILE', '2008-04-16 11:33:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8738911, 'A4405946', 'FILE', '2009-03-20 12:26:41', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (545719, 'CONVL', '2003-08-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (545720, 'CONVL', '2002-08-13 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (545721, 'CONVL', '2002-04-25 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (545722, 'CONVL', '2001-02-20 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5669443, 'ANNXP', '2004-04-06 10:47:50', null, null, '2004-02-20 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6285155, 'ANNXP', '2005-05-11 09:49:32', null, null, '2005-02-20 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7136415, 'ANNXP', '2006-06-07 11:08:39', null, null, '2006-02-20 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7600204, 'ANNXP', '2007-04-03 13:42:19', null, null, '2007-02-20 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8220338, 'ANNXP', '2008-04-16 11:33:44', null, null, '2008-02-20 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8241969, 'NOAPA', '2008-04-29 14:38:40', null, null, null, null, 'N', null, null, 'P ', 8241969, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8241976, 'NORVA', '2008-04-30 00:01:00', null, null, null, null, 'N', null, null, 'P ', 8241976, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8738911, 'ANNXP', '2009-03-20 12:26:41', null, null, '2009-02-20 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242694, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('A4405946', null, 'A', '2001-02-20 00:00:00', '2009-02-20 00:00:00', null, null, null, null, 'KHUJNOIS', 'RZQOLOSF', 'UPJTAMPJJVZO@MZDHRQGX.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A4405946', 545718, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4405946', 5669443, 7600204, null, 'QC', 'COR', '1992-09-25 00:00:00', null, '2961-8923', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4405946', 545718, 5669443, null, 'QC', 'COR', '1992-09-25 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4405946', 7600204, null, null, 'QC', 'COR', '1992-09-25 00:00:00', null, '2961-8923', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A4405946', 'CO', 545718, 0, null, 'ALUADQVOGMYGOMAPQELP', 'GPRBZ NQSYQCVFLHEQYTA IFO', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A4405946', 'NO', 5657325, 0, null, 'EPEZZJBRUZEFTVSXIGBQ', 'TNGCEYXBNGPXVZVPANBVWIBNA', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4405946', 'HD', 545718, null, 215619, 215619, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215619, 'QC', 'CA', 'OF7TXV', 'RHSNFIBXBXFOGXSYOEQREVAB ', 'FKFLCTWZHHEHJVHIFLKIUWNBZ', null, 'MONTREAL', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_C6020509": {
            "corp_num":'C6020509', "corp_typ_cd":'CUL', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":1, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361183, 103465149, null, 'FM9129945', 'FBO', 111258287, 111258289, 108361179, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156LTZNXUUJYJFXRVXBKLAP', 'C6020509', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510631, 7534072, 7534073, 'C6020509', 'DIR', 9236428, null, null, null, null, null, null, 'test', null, 'test', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361175, 103465149, null, 'FM9129945', 'FBO', 111258283, 111258285, 105513550, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156RQRSVLAPGHSIIFWMFJUS', 'C6020509', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361179, 103465149, null, 'FM9129945', 'FBO', 111258285, null, 108361175, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156XJJCGNFEWJSSONWXNDBX', 'C6020509', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236428, 'C6020509', 'FILE', '2012-02-17 15:29:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236430, 'C6020509', 'FILE', '2012-02-17 16:04:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236431, 'C6020509', 'FILE', '2012-02-17 16:06:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236429, 'C6020509', 'FILE', '2012-02-17 15:41:16', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258288, 'C6020509', 'ADFIRM', '2012-02-17 16:06:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258283, 'FM9129945', 'FILE', '2012-02-17 15:29:21', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258285, 'FM9129945', 'FILE', '2012-02-17 15:41:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258289, 'FM9129945', 'ADFIRM', '2012-02-17 16:06:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258287, 'FM9129945', 'FILE', '2012-02-17 16:04:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104854695, 'FM9129945', 'CONVFMREGI', '2005-09-26 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9236428, 'CONTU', '2012-02-17 15:29:14', '2012-02-17 00:00:00', null, null, null, 'N', '2012-02-17 00:00:00', null, 'F ', null, null, 'NR4165324', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9236429, 'NOALA', '2012-02-17 16:00:00', null, null, null, null, 'N', null, null, 'F ', 9236429, null, 'NR4626787', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9236430, 'NOALB', '2012-02-17 16:15:00', null, null, null, null, 'N', null, 9236431, 'F ', 9236430, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9236431, 'NWITH', '2012-02-17 16:06:12', null, null, null, null, 'N', '2012-02-17 00:00:00', null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104854695, 'FRREG', '2005-09-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (111258283, 'FRCHG', '2012-02-17 15:29:21', null, null, null, null, 'N', null, null, 'F ', 9236428, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (111258285, 'FRCHG', '2012-02-17 16:00:00', null, null, null, null, 'N', null, null, 'F ', 9236429, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (111258287, 'FRCHG', '2012-02-17 16:15:00', null, null, null, null, 'N', null, 9236431, 'F ', 9236430, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('C6020509', null, 'CUL', '2012-02-17 15:29:14', null, null, null, null, null, 'XTLMRFES', 'OURWNGTE', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9129945', null, 'SP', '2005-09-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-11-30 00:00:00', 1060316, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C6020509', 9236428, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9129945', 104854695, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C6020509', 9236428, null, null, 'NS', 'COR', '2001-02-28 00:00:00', null, '1234567', 'A0036611', 'ABC RECOVERY CANADA CORPORATION', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6020509', 'CO', 9236429, 1, 9236430, 'DRWJJBOOZKGSJHQFZAJJ', 'YEFUSBCKP RVGBFPCMMZAZSSF', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6020509', 'CO', 9236428, 0, 9236429, 'EQRGMKZDLYQOUGLIDOML', 'AHIKZAQRYWUSEZNNOQWUEQZ D', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6020509', 'NB', 9236430, 1, 9236431, 'SAHLPIOWBTNTXEIHCUCP', 'JTXOYCKRCIXPL  XCJJAW KXK', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6020509', 'CO', 9236431, 1, null, 'HQYRIYAHRKWURWBVMMGW', 'GROET VQHWRYEHORQVKSNBRUE', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9129945', 'CO', 104854695, 0, null, 'PZEDPIDOOYBQIJSSTPBY', 'TWDVNCMRUUM TQXGLKBSMNMID', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6020509', 'RG', 9236428, null, 7534075, 7534074, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6020509', 'RC', 9236428, null, 7534077, 7534076, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9129945', 'FO', 104854695, null, 103107494, 103107493, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534074, 'BC', 'CA', 'X1DHD9', 'L  VPHHAWTA VDU LSFTNQETD', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534075, 'BC', 'CA', 'K7J940', 'OJMFWIASIKDFMDHVCPAOVQLOD', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534076, 'BC', 'CA', 'SJHZNS', 'HNTKWJRK TRZP CSLXLSORURN', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534077, 'BC', 'CA', 'Z3A7JQ', 'WPLZBBGD HEPGFRZULOCJMWAH', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107493, 'BC', 'CA', 'F1EFW9', null, null, null, 'VANCOUVER', 'BAS', 'SHDUGPJMITMIFGBEWOHJLJEAJCGQNLFQTUZKOIXV', 'JF DTMXGGFLSLWEUEDMX', null, '889', null, '427', null, 'WRUSHDHYGUARFWI', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107494, 'BC', 'CA', 'R765HO', null, null, null, 'VANCOUVER', 'BAS', 'WNDQHWYBFN HDVZWCQCNETJHPBD IEELPEDLDQFY', 'IJXCNIYKO ENTNMTADQL', null, '781', null, '882', null, 'MJEMUYSAHVTZNIC', 'ST', 'N', null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_5081379": {
            "corp_num":'5081379', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1666017, 1528019, 1528019, '5081379', 'OFF', 5375035, 7331454, null, null, null, null, null, 'VILLANUEVA', null, 'MARILYN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1666018, 1528020, 1528020, '5081379', 'DIR', 5375035, null, null, null, null, null, null, 'VILLANUEVA', null, 'NELSON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1666019, 1528020, 1528020, '5081379', 'OFF', 5375035, 7331454, null, null, null, null, null, 'VILLANUEVA', null, 'NELSON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2604453, 4812797, 4812797, '5081379', 'OFF', 7331454, 7950926, 1666017, 'C', null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2604454, 4812798, 4812798, '5081379', 'OFF', 7331454, 7950926, 1666019, 'C', null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2886664, 5680379, 5680379, '5081379', 'OFF', 7950926, 8493310, 1666019, null, null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2886665, 5680380, 5680380, '5081379', 'OFF', 7950926, 8493310, 1666017, null, null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3154265, 6498061, 6498061, '5081379', 'OFF', 8493310, 9133058, 1666017, null, null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3154266, 6498062, 6498062, '5081379', 'OFF', 8493310, 9133058, 1666019, null, null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3464685, 7391250, 7391250, '5081379', 'OFF', 9133058, null, 1666019, null, null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3464686, 7391251, 7391251, '5081379', 'OFF', 9133058, null, 1666017, null, null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6562760, '5081379', 'FILE', '2005-09-16 08:22:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7134443, '5081379', 'FILE', '2006-06-06 11:30:27', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7331454, '5081379', 'FILE', '2006-10-18 10:47:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7950926, '5081379', 'FILE', '2007-11-02 14:32:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242017, '5081379', 'FILE', '2015-07-28 14:46:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375035, '5081379', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375036, '5081379', 'FILE', '2004-01-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375037, '5081379', 'FILE', '2003-09-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375038, '5081379', 'FILE', '2003-01-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375039, '5081379', 'FILE', '2001-11-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375040, '5081379', 'FILE', '2000-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5843351, '5081379', 'ADCORP', '2004-08-13 12:41:51', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5844360, '5081379', 'FILE', '2004-08-14 18:30:06', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5933282, '5081379', 'FILE', '2004-10-15 11:35:53', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8493310, '5081379', 'FILE', '2008-10-15 13:18:53', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9133058, '5081379', 'FILE', '2009-12-10 08:43:38', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5375036, 'CONVL', '2004-01-23 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5375037, 'CONVL', '2003-09-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5375038, 'CONVL', '2003-01-20 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5375039, 'CONVL', '2001-11-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5375040, 'CONVL', '2000-08-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5844360, 'TRANS', '2004-08-14 18:30:06', null, null, null, null, 'N', null, null, 'F ', 5844360, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5933282, 'ANNBC', '2004-10-15 11:35:53', null, null, '2004-08-28 00:00:00', null, 'N', null, null, 'F ', null, '101294817', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6562760, 'ANNBC', '2005-09-16 08:22:07', null, null, '2005-08-28 00:00:00', null, 'N', null, null, 'F ', null, '104180591', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7134443, 'NOCAD', '2006-06-07 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7331454, 'ANNBC', '2006-10-18 10:47:07', null, null, '2006-08-28 00:00:00', null, 'N', null, null, 'F ', null, '107055311', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7950926, 'ANNBC', '2007-11-02 14:32:28', null, null, '2007-08-28 00:00:00', null, 'N', null, null, 'F ', null, '109993717', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8493310, 'ANNBC', '2008-10-15 13:18:53', null, null, '2008-08-28 00:00:00', null, 'N', null, null, 'F ', null, '112963400', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9133058, 'ANNBC', '2009-12-10 08:43:38', null, null, '2009-08-28 00:00:00', null, 'N', null, null, 'F ', null, '116047580', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242017, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('5081379', null, 'BC', '2000-08-28 00:00:00', '2009-08-28 00:00:00', '2004-08-14 18:30:06', null, null, null, 'IMQUPJPD', 'MQLGANEB', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('5081379', 5375035, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('5081379', 'CO', 5375035, 0, null, 'CMMVJVFAHWNUFBAAZMYS', 'ZHEEDKUKEWSDWQDLRUFLUVCGO', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RG', 7134443, 9242017, 4515811, 4515810, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RC', 7134443, 9242017, 4515809, 4515808, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RG', 9242017, null, 7535151, 7535151, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RC', 9242017, null, 7535151, 7535151, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RG', 5375035, 5844360, 1528018, 1528018, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RC', 5375035, 5844360, 1528018, 1528018, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RC', 5844360, 7134443, 2055281, 2055280, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5081379', 'RG', 5844360, 7134443, 2055283, 2055282, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1528018, 'BC', 'CA', '081RGI', 'LHUYCIDHCGIUISPZERGHGYKEO', 'ARIELJFCYU ALXI LVZZKCAIS', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055280, 'BC', 'CA', '9M18G7', 'JFSAGJQYDCVOYF FMTWIAYHFD', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055281, 'BC', 'CA', 'MZKEX9', 'LFLXIFFEPRCVMUVNIJFKITJJP', ' LZWBIBXUTDWJUZAWQFYBWNSG', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055282, 'BC', 'CA', 'WDSMKR', 'NJVLFKOITZG VPGEZYTGQBTNR', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055283, 'BC', 'CA', 'LBCXSI', 'EZEXDYGVCHPKPHBCUBNTUHCRZ', 'KSMSFDUIKAGE EAVYSKRACOWR', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515808, 'BC', 'CA', 'VVIO59', 'UEPWCXCKELGUQ UHHQLXMWYRX', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515809, 'BC', 'CA', 'BA0M4M', 'IZPV BLSZPRDFEPOVQAMFDDWH', 'QXKDZCORCJLEUGTVZHPMARNKC', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515810, 'BC', 'CA', 'GDPJ0J', 'AUKMACVOZPURWCLPMKHOZEJAO', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515811, 'BC', 'CA', 'FOFJQ6', 'UVZEGZYLYZID WZVNQDTFXHIZ', 'TLZWSWM SIYCOZXHZPAMZLBUR', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535151, 'BC', 'CA', '7754SX', 'YYHUBOIRGQFLRIIGFLYVNYSPT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM0004365": {
            "corp_num":'FM0004365', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105778013, null, null, 'FM0004365', 'FBO', 104961111, null, null, null, null, '2009-08-12 00:00:00', null, null, null, null, 'A0053427VFAFYQOU HTGFCOTXZQU', 'A9673056', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104961111, 'FM0004365', 'CONVFMREGI', '2009-08-12 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104961111, 'FRREG', '2009-08-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM0004365', null, 'SP', '2009-08-12 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2009-08-12 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM0004365', 104961111, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM0004365', 'CO', 104961111, 0, null, 'WTHHJBXJSQZNZCFNYLSL', 'RNPEQABTOMMEQSUOTGHAHTEJI', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
    "corp_LLC3768758": {
            "corp_num":'LLC3768758', "corp_typ_cd":'LLC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2564426, 4687887, 4687888, 'LLC3768758', 'ATT', 7248293, 7940088, null, null, null, null, null, 'RISK', 'H.', 'DONALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2617713, 4854180, 4854179, 'LLC3768758', 'DIR', 7356685, null, null, null, null, '2006-11-06 00:00:00', null, 'PARISH', null, 'RHONDA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2881356, 5663684, 5663683, 'LLC3768758', 'ATT', 7940086, 9242767, null, null, null, null, null, null, null, null, 'AZHQPXEU OFTWKFVOVWU', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510953, 7536135, 7536134, 'LLC3768758', 'ATT', 9242767, null, 2881356, null, null, null, null, null, null, null, 'BC0121625BUMWPP VYNYQJO CYXJA', 'BC5305307', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7248293, 'LLC3768758', 'FILE', '2006-08-21 16:08:50', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7282058, 'LLC3768758', 'ADMIN', '2006-09-12 15:12:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7356685, 'LLC3768758', 'FILE', '2006-11-06 09:05:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7356692, 'LLC3768758', 'ADMIN', '2006-11-06 09:08:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7357584, 'LLC3768758', 'ADCORP', '2006-11-06 12:53:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7904628, 'LLC3768758', 'FILE', '2007-10-05 13:06:26', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7940086, 'LLC3768758', 'FILE', '2007-10-29 09:37:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7940088, 'LLC3768758', 'FILE', '2007-10-29 09:38:15', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242767, 'LLC3768758', 'FILE', '2017-04-04 16:19:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8468425, 'LLC3768758', 'FILE', '2008-09-29 14:13:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9022269, 'LLC3768758', 'FILE', '2009-10-01 16:31:51', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7248293, 'REGLL', '2006-08-21 16:08:50', null, null, null, null, 'N', null, null, 'P ', 7248293, null, 'NR8489910', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7356685, 'CO_DI', '2006-11-06 09:05:48', null, null, null, null, 'N', null, null, 'F ', 7356685, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7904628, 'ANNXP', '2007-10-05 13:06:26', null, null, '2007-08-21 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7940086, 'NOAPA', '2007-10-29 09:37:23', null, null, null, null, 'N', null, null, 'P ', 7940086, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7940088, 'NORVA', '2007-10-30 00:01:00', null, null, null, null, 'N', null, null, 'P ', 7940088, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8468425, 'ANNXP', '2008-09-29 14:13:32', null, null, '2008-08-21 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9022269, 'ANNXP', '2009-10-01 16:31:51', null, null, '2009-08-21 00:00:00', null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242767, 'NOCAA', '2017-04-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('LLC3768758', null, 'LLC', '2006-08-21 16:08:50', '2009-08-21 00:00:00', null, null, null, null, 'TYJUZFGD', 'QUSRERRV', 'VYLYBFJUTFUJ@QNXNEWWI.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('LLC3768758', 7248293, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('LLC3768758', 7248293, null, null, 'OT', 'LLC', '2006-06-28 00:00:00', 'US, DE', '2465132', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('LLC3768758', 'CO', 7248293, 0, null, 'LSMRGZSPCGFHGMPWQLCX', 'VNWPUCL F IPJPNEVCFZXHDA ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('LLC3768758', 'HD', 7248293, null, 4687886, 4687885, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4687885, 'SC', 'US', 'AWKTT4', 'AVRMUWJRNGNLMEAGVRQNVKYG ', null, null, 'SPARTANBURG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4687886, 'SC', 'US', 'JXO86L', 'NWLFOUWEBJPF RCJVXNBEVFOL', null, null, 'SPARTANBURG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_4441905": {
            "corp_num":'4441905', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3090638, 6312333, null, '4441905', 'INC', 8367008, null, null, null, null, null, null, null, null, null, 'QFDHMTQTSAH RZKWKYEQ', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3090639, 6312335, 6312336, '4441905', 'DIR', 8367008, null, null, null, null, null, null, 'Ellis', null, 'Pete', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242633, '4441905', 'FILE', '2016-08-25 15:25:02', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8367008, '4441905', 'FILE', '2008-07-18 11:35:50', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8367008, 'ICORP', '2008-07-18 11:35:50', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242633, 'NOCAD', '2016-08-26 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('4441905', null, 'BC', '2008-07-18 11:35:50', null, null, null, null, null, 'COJUZOLL', 'HJGNHDJQ', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('4441905', 8367008, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4441905', 'NB', 8367008, 0, null, 'WJYXJXOLHGPEGTIWSNLP', 'QWGMXQQJE QGJHMBUAXWMRIPK', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4441905', 'RG', 8367008, 9242633, 6312338, 6312337, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4441905', 'RC', 8367008, 9242633, 6312340, 6312339, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4441905', 'RG', 9242633, null, 7535867, 7535866, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4441905', 'RC', 9242633, null, 7535867, 7535866, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312337, 'BC', 'CA', 'NEEEPX', 'QFMCBAQIDRYSTLJFCYQUNMSYM', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312338, 'BC', 'CA', 'C9H35Z', 'ODDLRURIYEJCRSSIUGPA IVGO', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312339, 'BC', 'CA', '4O8HXF', 'FMHMIXSLRKVRVGTAAJWGAZOBW', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312340, 'BC', 'CA', 'ZC9K9Z', 'BCGUYYYC DJMCANDLUULXDIVR', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535866, 'BC', 'CA', 'D7QMRH', 'X RJOJFCCJXQB MWZOWMHXWEN', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535867, 'BC', 'CA', 'M6IPL7', 'KNUGU VKCZUTZXRBRLCPYUBQM', 'LXMULTSCX NBWSCDGQSJPRTLN', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM5250608": {
            "corp_num":'FM5250608', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682494, null, null, 'FM5250608', 'FBO', 105301927, null, null, null, null, '2001-05-09 14:29:44', null, null, null, null, 'A0031179LPVRFAPMODN MKMJSPVU', 'A8980227', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721465, 'FM5250608', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301927, 'FM5250608', 'CONVFMACP', '2001-05-09 14:29:44', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104721465, 'FRREG', '2000-06-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105301927, 'FRMEM', '2001-05-09 14:29:44', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM5250608', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM5250608', 104721465, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM5250608', 'CO', 104721465, 0, null, 'BJEXYFOOXWQVDPLQZPZP', '  ZHRTDYOWZFTNNGXSRTX AFO', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
    "corp_2201720": {
            "corp_num":'2201720', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105935322, null, null, 'FM3035075', 'FBO', 105148056, null, null, null, null, '1992-11-19 00:00:00', null, null, null, null, '0384698P REILGZZSKOQLWRXYFR', '2201720', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994837, 891658, 891658, '2201720', 'DIR', 3420140, null, null, null, null, null, null, 'KWAN', null, 'JAMES C.K.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994838, 891658, 891658, '2201720', 'OFF', 3420140, null, null, null, null, null, null, 'KWAN', null, 'JAMES C.K.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994839, 891659, 891659, '2201720', 'DIR', 3420140, null, null, null, null, null, null, 'KWAN', null, 'YVONNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994840, 891659, 891659, '2201720', 'OFF', 3420140, null, null, null, null, null, null, 'KWAN', null, 'YVONNE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420140, '2201720', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420141, '2201720', 'FILE', '2003-08-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420142, '2201720', 'FILE', '2003-05-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420143, '2201720', 'FILE', '2002-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420144, '2201720', 'FILE', '2001-04-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420145, '2201720', 'FILE', '2000-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420146, '2201720', 'FILE', '1999-07-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420147, '2201720', 'FILE', '1998-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420148, '2201720', 'FILE', '1997-04-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420149, '2201720', 'FILE', '1996-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420150, '2201720', 'FILE', '1996-01-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420151, '2201720', 'FILE', '1995-06-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420152, '2201720', 'FILE', '1995-06-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420153, '2201720', 'FILE', '1994-08-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420154, '2201720', 'FILE', '1994-07-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420155, '2201720', 'FILE', '1994-06-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420156, '2201720', 'FILE', '1993-09-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420157, '2201720', 'FILE', '1993-08-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420158, '2201720', 'FILE', '1992-09-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420159, '2201720', 'FILE', '1991-09-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420160, '2201720', 'FILE', '1991-07-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420161, '2201720', 'FILE', '1991-01-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420162, '2201720', 'FILE', '1990-06-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420163, '2201720', 'FILE', '1990-06-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420164, '2201720', 'FILE', '1990-03-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420165, '2201720', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6292549, '2201720', 'FILE', '2005-05-13 12:26:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6630308, '2201720', 'FILE', '2005-10-18 12:28:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6630310, '2201720', 'FILE', '2005-10-18 12:29:49', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7301104, '2201720', 'FILE', '2006-09-26 14:32:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7728004, '2201720', 'FILE', '2007-06-20 18:10:55', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9241844, '2201720', 'FILE', '2015-07-28 14:46:08', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5661793, '2201720', 'ADCORP', '2004-03-31 12:39:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5703773, '2201720', 'FILE', '2004-05-03 16:21:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8220941, '2201720', 'FILE', '2008-04-16 14:28:57', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8820401, '2201720', 'ADCORP', '2009-05-11 15:19:05', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8820407, '2201720', 'FILE', '2009-05-11 15:20:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105148056, 'FM3035075', 'CONVFMREGI', '1992-11-19 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420141, 'CONVL', '2003-08-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420142, 'CONVL', '2003-05-05 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420143, 'CONVL', '2002-05-27 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420144, 'CONVL', '2001-04-09 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420145, 'CONVL', '2000-04-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420146, 'CONVL', '1999-07-06 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420147, 'CONVL', '1998-04-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420148, 'CONVL', '1997-04-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420149, 'CONVL', '1996-04-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420150, 'CONVL', '1996-01-10 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420151, 'CONVL', '1995-06-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420152, 'CONVL', '1995-06-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420153, 'CONVL', '1994-08-30 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420154, 'CONVL', '1994-07-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420155, 'CONVL', '1994-06-09 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420156, 'CONVL', '1993-09-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420157, 'CONVL', '1993-08-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420158, 'CONVL', '1992-09-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420159, 'CONVL', '1991-09-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420160, 'CONVL', '1991-07-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420161, 'CONVL', '1991-01-23 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420162, 'CONVL', '1990-06-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420163, 'CONVL', '1990-06-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (3420164, 'CONVL', '1990-03-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5703773, 'ANNBC', '2004-05-03 16:21:48', null, null, '2004-03-28 00:00:00', null, 'N', null, null, 'F ', null, '26634697', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6292549, 'ANNBC', '2005-05-13 12:26:32', null, null, '2005-03-28 00:00:00', null, 'N', null, null, 'F ', null, '102947835', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6630308, 'TRANS', '2005-10-18 12:28:32', null, null, null, null, 'N', null, null, 'F ', 6630308, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6630310, 'NOALA', '2005-10-18 12:29:49', null, null, null, null, 'N', null, null, 'F ', 6630310, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7301104, 'ANNBC', '2006-09-26 14:32:03', null, null, '2006-03-28 00:00:00', null, 'N', null, null, 'F ', null, '105854202', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7728004, 'ANNBC', '2007-06-20 18:10:55', null, null, '2007-03-28 00:00:00', null, 'N', null, null, 'F ', null, '108802588', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8220941, 'ANNBC', '2008-04-16 14:28:57', null, null, '2008-03-28 00:00:00', null, 'N', null, null, 'F ', null, '111726584', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8820407, 'ANNBC', '2009-05-11 15:20:59', null, null, '2009-03-28 00:00:00', null, 'N', null, null, 'F ', null, '114762057', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9241844, 'NOCAD', '2015-07-29 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105148056, 'FRREG', '1992-11-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('2201720', null, 'BC', '1990-03-28 00:00:00', '2009-03-28 00:00:00', '2005-10-18 12:28:32', null, null, null, 'UKITSTRS', 'SRRVXYFC', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM3035075', null, 'SP', '1992-11-19 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('2201720', 3420140, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM3035075', 105148056, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('2201720', 'CO', 3420140, 0, 3420165, 'EUQECTCDDIYTSGMYIHBH', ' FGFF KYRZZIVFHQMHZOVJKUV', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('2201720', 'CO', 3420165, 0, null, 'RMHFCCTGCMYAQNSIIBON', 'YAKCOGRLSRVLQTMRRUDHGPUKJ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM3035075', 'CO', 105148056, 0, null, 'MYZYALBWZYGTRSKYBZVX', 'IAAWS OAEBNCOTHZEGJOXYUPX', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2201720', 'RG', 9241844, null, 7534978, 7534978, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2201720', 'RC', 9241844, null, 7534978, 7534978, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2201720', 'RG', 3420140, 6630308, 891657, 891657, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2201720', 'RC', 3420140, 6630308, 891657, 891657, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2201720', 'RC', 6630308, 9241844, 3471382, 3471381, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('2201720', 'RG', 6630308, 9241844, 3471384, 3471383, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (891657, 'BC', 'CA', '9NJ5GP', 'LFGTRQKCYDAYVLZMWYA LCF Q', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471381, 'BC', 'CA', 'IWL1QU', 'YCCMVPRHWLXMTVWJIGWVUGO Z', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471382, 'BC', 'CA', 'H56PKY', ' LXSCLYTMKZDEF XTQYYOBXKA', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471383, 'BC', 'CA', 'AZNJ23', 'KZABIWYSQNIZMGEKLDFXSBPMO', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471384, 'BC', 'CA', 'C6WK4D', 'UATKSVHVRFNMNIMOPDFQEJOTN', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534978, 'BC', 'CA', '31YRGU', 'PZVGTADKUROSVGVJQHEETQSNH', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_C6618176": {
            "corp_num":'C6618176', "corp_typ_cd":'C', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1659494, 1521768, 1521768, 'C6618176', 'DIR', 5362328, 5846843, null, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1659495, 1521768, 1521768, 'C6618176', 'OFF', 5362328, 5847471, null, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1926503, 2059264, 2059263, 'C6618176', 'DIR', 5846843, 6808452, 1659494, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1926786, 2060313, 2060313, 'C6618176', 'OFF', 5847471, 7269975, 0, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2351409, 3803504, 3803503, 'C6618176', 'DIR', 6808452, null, 1926503, 'C', null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2574350, 4718920, 4718920, 'C6618176', 'OFF', 7269975, 7869962, 1926786, 'C', null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2849441, 5564637, 5564637, 'C6618176', 'OFF', 7869962, 8402386, 1926786, null, null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3109313, 6366333, 6366333, 'C6618176', 'OFF', 8402386, 8991394, 1926786, null, null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3399039, 7195999, 7195999, 'C6618176', 'OFF', 8991394, null, 1926786, null, null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6808494, 'C6618176', 'FILE', '2006-01-11 16:37:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6808452, 'C6618176', 'FILE', '2006-01-11 16:29:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6808434, 'C6618176', 'FILE', '2006-01-11 16:26:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7269975, 'C6618176', 'FILE', '2006-09-06 08:52:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7869962, 'C6618176', 'FILE', '2007-09-17 11:11:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242666, 'C6618176', 'FILE', '2016-08-25 15:25:05', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362328, 'C6618176', 'CONVCIN', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362329, 'C6618176', 'FILE', '2003-07-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362330, 'C6618176', 'FILE', '2002-07-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362331, 'C6618176', 'FILE', '2001-08-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362332, 'C6618176', 'FILE', '2000-07-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5847471, 'C6618176', 'FILE', '2004-08-17 14:00:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5846855, 'C6618176', 'FILE', '2004-08-17 11:11:18', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5846833, 'C6618176', 'ADCORP', '2004-08-17 11:03:42', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5846843, 'C6618176', 'FILE', '2004-08-17 11:07:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8402386, 'C6618176', 'FILE', '2008-08-13 14:25:43', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8991394, 'C6618176', 'FILE', '2009-09-11 11:39:54', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5362329, 'CONVL', '2003-07-21 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5362330, 'CONVL', '2002-07-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5362331, 'CONVL', '2001-08-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5362332, 'CONVL', '2000-07-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5846843, 'NOCDR', '2004-08-17 11:07:33', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5846855, 'NOCDR', '2004-08-17 11:11:18', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5847471, 'ANNBC', '2004-08-17 14:00:29', null, null, '2004-07-17 00:00:00', null, 'N', null, null, 'F ', null, '101026060', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6808434, 'ANNBC', '2006-01-11 16:26:14', null, null, '2005-07-17 00:00:00', null, 'N', null, null, 'F ', null, '103888921', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6808452, 'TRANS', '2006-01-11 16:29:48', null, null, null, null, 'N', null, null, 'F ', 6808452, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6808494, 'NOALA', '2006-01-11 16:37:35', null, null, null, null, 'N', null, null, 'F ', 6808494, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7269975, 'ANNBC', '2006-09-06 08:52:14', null, null, '2006-07-17 00:00:00', null, 'N', null, null, 'F ', null, '106752082', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7869962, 'ANNBC', '2007-09-17 11:11:29', null, null, '2007-07-17 00:00:00', null, 'N', null, null, 'F ', null, '109693606', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8402386, 'ANNBC', '2008-08-13 14:25:43', null, null, '2008-07-17 00:00:00', null, 'N', null, null, 'F ', null, '112651690', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8991394, 'ANNBC', '2009-09-11 11:39:54', null, null, '2009-07-17 00:00:00', null, 'N', null, null, 'F ', null, '115724213', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242666, 'NOCAD', '2016-08-26 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('C6618176', null, 'C', '2000-07-17 00:00:00', '2009-07-17 00:00:00', '2006-01-11 16:29:48', null, null, null, 'CJPOHZKR', 'RGSRLQCL', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C6618176', 5362328, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C6618176', 5362328, null, null, 'OT', 'COR', '1990-06-25 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6618176', 'CO', 5362328, 0, null, 'TEQHJZXZGGRODSOEIKAJ', 'KE PKROAOKRV XGZEBF CVROO', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6618176', 'RG', 9242666, null, 7535933, 7535932, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6618176', 'RC', 9242666, null, 7535933, 7535932, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6618176', 'RG', 5362328, 6808452, 1521767, 1521767, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6618176', 'RC', 5362328, 6808452, 1521767, 1521767, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6618176', 'RC', 6808452, 9242666, 3803506, 3803505, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6618176', 'RG', 6808452, 9242666, 3803508, 3803507, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1521767, 'BC', 'CA', '45RSNY', 'LJBKCAYPBQ SHLZYMQELTQKJX', 'EHQHB EMHMINUUWZLWFPXHMAE', 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803505, 'BC', 'CA', 'T1B3EH', 'YLDCHRNEDGY P GEIVCZYIWSS', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803506, 'BC', 'CA', 'VJLDIW', 'YRBYFCQEJYVVRASFIZOHFGDKE', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803507, 'BC', 'CA', 'RHQXBX', 'JYMGNXRIBCMGBCMVEBFTCJ XM', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803508, 'BC', 'CA', 'QMUU51', 'JTDJJNMOSHZFKUJZDVG WXONX', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535932, 'BC', 'CA', 'X1W5QZ', 'FYYQLUADLEQBDWDRBCFUVQEDV', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535933, 'BC', 'CA', 'EO4XVN', 'ISJAVLNPDSLEQQQXVWNDGKLUJ', 'HUYDELZXBLWAKQFHJZEEXBJGO', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_4783263": {
            "corp_num":'4783263', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179508, 1065552, 1065552, '4783263', 'DIR', 4029955, 5780844, null, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179509, 1065552, 1065552, '4783263', 'OFF', 4029955, 5781539, null, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179511, 1065553, 1065553, '4783263', 'OFF', 4029955, 5781539, null, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179512, 1065554, 1065554, '4783263', 'OFF', 4029955, 5781539, null, null, null, null, null, 'SUHNER', null, 'LAURA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179513, 1065555, 1065555, '4783263', 'DIR', 4029955, 5664415, null, null, null, null, '2003-09-07 00:00:00', 'TAYLOR', null, 'JON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1845013, 1743892, 1743891, '4783263', 'DIR', 5664415, 6270088, null, null, null, '2003-09-07 00:00:00', '2004-09-01 00:00:00', 'KRAMER, JR.', 'D.', 'GEORGE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1896759, 1941440, 1941439, '4783263', 'DIR', 5780844, 8086210, 1179510, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1896760, 1941442, 1941441, '4783263', 'DIR', 5780844, 8086210, 1179508, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179510, 1065553, 1065553, '4783263', 'DIR', 4029955, 5780844, null, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1897055, 1942775, 1942775, '4783263', 'OFF', 5781539, 6316602, 0, null, null, null, null, 'SUHNER', null, 'LAURA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1897056, 1942776, 1942776, '4783263', 'OFF', 5781539, 6316602, 0, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1897057, 1942777, 1942777, '4783263', 'OFF', 5781539, 6316602, 0, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2134346, 2887244, 2887243, '4783263', 'DIR', 6270088, 8086210, null, null, null, '2004-09-01 00:00:00', '2007-02-09 00:00:00', 'Molgat', null, 'Bob', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2155220, 2974593, 2974592, '4783263', 'OFF', 6316602, 7352151, 0, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2155221, 2974595, 2974594, '4783263', 'OFF', 6316602, 7352151, 1897056, 'C', null, null, null, 'SCOTT', 'C.', 'JOHN ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2155222, 2974597, 2974596, '4783263', 'OFF', 6316602, 7352151, 0, null, null, null, null, 'SUHNER', null, 'LAURA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2614999, 4845389, 4845389, '4783263', 'OFF', 7352151, 7879272, 2155221, 'C', null, null, null, 'Scott', 'C.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2615000, 4845390, 4845390, '4783263', 'OFF', 7352151, 7879272, 2155222, 'C', null, null, null, 'Suhner', null, 'Laura', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2615001, 4845391, 4845391, '4783263', 'OFF', 7352151, 7879272, 2155220, 'C', null, null, null, 'Nishimura', null, 'Don', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2853508, 5577055, 5577055, '4783263', 'OFF', 7879272, 8899110, 2155221, null, null, null, null, 'Scott', 'C.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2853509, 5577056, 5577056, '4783263', 'OFF', 7879272, 8899110, 2155220, null, null, null, null, 'Nishimura', null, 'Don', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2853510, 5577057, 5577057, '4783263', 'OFF', 7879272, 8899110, 2155222, null, null, null, null, 'Suhner', null, 'Laura', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2948557, 5882782, 5882781, '4783263', 'DIR', 8086210, null, 1896759, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2948558, 5882784, 5882783, '4783263', 'DIR', 8086210, null, 1896760, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3352675, 7060605, 7060605, '4783263', 'OFF', 8899110, null, 2155222, null, null, null, null, 'Suhner', null, 'Laura', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3352676, 7060606, 7060606, '4783263', 'OFF', 8899110, null, 2155221, null, null, null, null, 'Scott', 'C.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3352677, 7060607, 7060607, '4783263', 'OFF', 8899110, null, 2155220, null, null, null, null, 'Nishimura', null, 'Don', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6316602, '4783263', 'FILE', '2005-05-26 14:26:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6270088, '4783263', 'FILE', '2005-05-03 15:22:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7352151, '4783263', 'FILE', '2006-11-01 12:06:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7879272, '4783263', 'FILE', '2007-09-21 10:51:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242546, '4783263', 'FILE', '2016-08-25 15:24:54', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029971, '4783263', 'FILE', '1995-03-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029972, '4783263', 'FILE', '1994-07-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029973, '4783263', 'FILE', '1993-09-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029974, '4783263', 'FILE', '1993-07-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029975, '4783263', 'FILE', '1993-05-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029976, '4783263', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029955, '4783263', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029956, '4783263', 'FILE', '2004-03-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029957, '4783263', 'FILE', '2003-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029958, '4783263', 'FILE', '2002-05-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029959, '4783263', 'FILE', '2002-03-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029960, '4783263', 'FILE', '2001-10-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029961, '4783263', 'FILE', '2001-10-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029962, '4783263', 'FILE', '2001-02-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029963, '4783263', 'FILE', '2000-05-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029964, '4783263', 'FILE', '1999-07-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029965, '4783263', 'FILE', '1998-07-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029966, '4783263', 'FILE', '1997-06-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029967, '4783263', 'FILE', '1996-08-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029968, '4783263', 'FILE', '1996-08-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029969, '4783263', 'FILE', '1995-09-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029970, '4783263', 'FILE', '1995-07-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5664415, '4783263', 'FILE', '2004-04-01 15:35:30', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5664353, '4783263', 'ADCORP', '2004-04-01 15:22:38', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5780844, '4783263', 'FILE', '2004-06-29 11:07:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5781539, '4783263', 'FILE', '2004-06-29 14:44:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8086210, '4783263', 'FILE', '2008-01-23 16:03:08', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8316658, '4783263', 'FILE', '2008-06-16 14:36:36', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8899110, '4783263', 'FILE', '2009-07-06 12:50:39', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029956, 'CONVL', '2004-03-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029957, 'CONVL', '2003-07-02 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029958, 'CONVL', '2002-05-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029959, 'CONVL', '2002-03-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029960, 'CONVL', '2001-10-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029961, 'CONVL', '2001-10-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029962, 'CONVL', '2001-02-28 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029963, 'CONVL', '2000-05-18 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029964, 'CONVL', '1999-07-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029965, 'CONVL', '1998-07-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029966, 'CONVL', '1997-06-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029967, 'CONVL', '1996-08-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029968, 'CONVL', '1996-08-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029969, 'CONVL', '1995-09-27 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029970, 'CONVL', '1995-07-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029971, 'CONVL', '1995-03-03 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029972, 'CONVL', '1994-07-29 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029973, 'CONVL', '1993-09-20 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029974, 'CONVL', '1993-07-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (4029975, 'CONVL', '1993-05-04 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5664415, 'NOCDR', '2004-04-01 15:35:30', '2003-09-07 00:00:00', null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5780844, 'TRANS', '2004-06-29 11:07:52', null, null, null, null, 'N', null, null, 'F ', 5780844, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5781539, 'ANNBC', '2004-06-29 14:44:07', null, null, '2004-05-04 00:00:00', null, 'N', null, null, 'F ', null, '100427418', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6270088, 'NOCDR', '2005-05-03 15:22:34', '2004-09-01 00:00:00', null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6316602, 'ANNBC', '2005-05-26 14:26:17', null, null, '2005-05-04 00:00:00', null, 'N', null, null, 'F ', null, '103238689', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7352151, 'ANNBC', '2006-11-01 12:06:59', null, null, '2006-05-04 00:00:00', null, 'N', null, null, 'F ', null, '106158116', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7879272, 'ANNBC', '2007-09-21 10:51:22', null, null, '2007-05-04 00:00:00', null, 'N', null, null, 'F ', null, '109104299', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8086210, 'NOCDR', '2008-01-23 16:03:08', '2007-02-09 00:00:00', null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8316658, 'ANNBC', '2008-06-16 14:36:36', null, null, '2008-05-04 00:00:00', null, 'N', null, null, 'F ', null, '112039011', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8899110, 'ANNBC', '2009-07-06 12:50:39', null, null, '2009-05-04 00:00:00', null, 'N', null, null, 'F ', null, '115088718', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242546, 'NOCAD', '2016-08-26 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('4783263', null, 'BC', '1993-05-04 00:00:00', '2009-05-04 00:00:00', '2004-06-29 11:07:52', null, null, null, 'HGVGLPDH', 'AHURHZWH', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('4783263', 4029955, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4783263', 'CO', 4029955, 0, 4029976, 'HRDMUZUSPZILXCAMKOGY', 'QLTHBBGSVKKEFAJLFKYFWKFVS', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('4783263', 'CO', 4029976, 0, null, 'ZKYSRMBMGSFOSPOIVDYK', 'L PSXW OUEKWKQVFDHLGPLYWF', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4783263', 'RG', 9242546, null, 7535693, 7535692, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4783263', 'RC', 9242546, null, 7535693, 7535692, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4783263', 'RG', 4029955, 5780844, 1065551, 1065551, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4783263', 'RC', 4029955, 5780844, 1065551, 1065551, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4783263', 'RC', 5780844, 9242546, 1941444, 1941443, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('4783263', 'RG', 5780844, 9242546, 1941446, 1941445, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1065551, 'BC', 'CA', '9OQ368', 'A SQSHQXICWWEADHPRSMKUTHT', 'HHCFFZOCFLGHHPHVCTMTGTZCD', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941443, 'BC', 'CA', 'XQDIKF', 'WYLMLYXXTASXFVJXOXZAUZFFF', ' LXEMRTZPOXPOFCHZMBYVACEM', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941444, 'BC', 'CA', 'PN3FI3', 'H D BGNUZR A SVTDMBAAHIUV', 'YYPYZ ONMTYWQF HCWLJYAB P', 'P.O. BOX 48600', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941445, 'BC', 'CA', '9X4JWH', 'UMONSPQAIBLGBQBCYSMHBSGTA', 'XFUXVOFSJPZBVPPYXUPSEWPAY', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941446, 'BC', 'CA', 'MWPAGK', 'JZZCVQKCR GTTVFBMMF UTMDO', 'TH AQGNEIJGT TCZUWJBZPYQU', 'P.O. BOX 48600', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535692, 'BC', 'CA', '276CY4', 'GSUFZGPJTUJADCOTKKJWSUEH ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535693, 'BC', 'CA', 'YR9RQZ', 'VCJTPNZPQCBUXYXYDHYABNKOO', 'XCTRLG JEACDY WPTYOOQHFDD', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_FM5457780": {
            "corp_num":'FM5457780', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105935322, null, null, 'FM5457780', 'FBO', 105148056, null, null, null, null, '1992-11-19 00:00:00', null, null, null, null, '0384698KRNBOTIIOEBOLKXUKPQK', '1274433', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105148056, 'FM5457780', 'CONVFMREGI', '1992-11-19 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105148056, 'FRREG', '1992-11-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM5457780', null, 'SP', '1992-11-19 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM5457780', 105148056, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM5457780', 'CO', 105148056, 0, null, 'TFVYMLGQYXUCMSTADLNY', 'OHWLLZFXVYODVYDMUAXALQIRA', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
    "corp_FM0643134": {
            "corp_num":'FM0643134', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361182, 104982591, null, 'FM0643134', 'FCP', 111258287, 111258289, 108361178, null, null, null, null, null, null, null, 'YGOJYDUITBHDKXDN IBW', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361183, 103465149, null, 'FM0643134', 'FBO', 111258287, 111258289, 108361179, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156JCSIXLMFUQFOLIQNWXVP', 'C0289649', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361174, 104982583, null, 'FM0643134', 'FCP', 111258283, 111258285, 105319638, null, null, null, null, null, null, null, 'ZFUYLDZRJTYYZSILNEVK', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361175, 103465149, null, 'FM0643134', 'FBO', 111258283, 111258285, 105513550, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156EYNX UXESSNAJWHZUJFI', 'C0289649', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105513550, 103465149, null, 'FM0643134', 'FBO', 104854695, 111258283, null, null, null, '2005-09-26 00:00:00', null, null, null, null, 'A0036611O RMQGPEGOFIMQCVGHVS', 'A2383953', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361178, 104982587, null, 'FM0643134', 'FCP', 111258285, null, 108361174, null, null, null, null, null, null, null, 'UBYXXLENKPVXZVJTDBGS', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361179, 103465149, null, 'FM0643134', 'FBO', 111258285, null, 108361175, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156NQXXFLBFXSXKFFHKKZZV', 'C0289649', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105319638, 103107492, null, 'FM0643134', 'FCP', 104854695, 111258283, null, null, null, null, null, 'RAMIREZ', null, 'BEVERLY', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258283, 'FM0643134', 'FILE', '2012-02-17 15:29:21', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258285, 'FM0643134', 'FILE', '2012-02-17 15:41:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258289, 'FM0643134', 'ADFIRM', '2012-02-17 16:06:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258287, 'FM0643134', 'FILE', '2012-02-17 16:04:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104854695, 'FM0643134', 'CONVFMREGI', '2005-09-26 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104854695, 'FRREG', '2005-09-26 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (111258283, 'FRCHG', '2012-02-17 15:29:21', null, null, null, null, 'N', null, null, 'F ', 9236428, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (111258285, 'FRCHG', '2012-02-17 16:00:00', null, null, null, null, 'N', null, null, 'F ', 9236429, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (111258287, 'FRCHG', '2012-02-17 16:15:00', null, null, null, null, 'N', null, 9236431, 'F ', 9236430, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM0643134', null, 'SP', '2005-09-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-11-30 00:00:00', 1060316, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM0643134', 104854695, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM0643134', 'CO', 104854695, 0, null, 'KRKEBCIRNMRFPLAZCSYB', 'D PRZYFYBCOVKEYUMKNT WPWK', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM0643134', 'FO', 104854695, null, 103107494, 103107493, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107493, 'BC', 'CA', '3R2P1O', null, null, null, 'VANCOUVER', 'BAS', 'SBEZ VCWUCYUSRRRTJAYZLILIMUIFJNEGOYBXFON', 'GB LIBSHSOUQFKSIXZKK', null, '383', null, '003', null, 'RGXOYDBBEITIOEX', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107494, 'BC', 'CA', '2NP17N', null, null, null, 'VANCOUVER', 'BAS', 'BPLCELTZMQDVDXQWAJCQPCGYMJI KABQRSA MICF', 'SRXULMDKTMUQHGTGFJIG', null, '922', null, '166', null, 'JVLGEKZGZRXXYTH', 'ST', 'N', null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_6763577": {
            "corp_num":'6763577', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495427, 431310, 431310, '6763577', 'LIQ', 1631095, null, null, null, null, '1991-01-29 00:00:00', null, null, null, null, 'CWYJBHDQHFUSVPTVLOTM', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495428, 431311, 431311, '6763577', 'DIR', 1631095, null, null, null, null, null, null, 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495429, 431311, 431311, '6763577', 'OFF', 1631095, null, null, null, null, null, null, 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6005579, null, null, '6763577', 'DIR', 1631095, 1631095, null, null, null, null, '1988-01-29 00:00:00', 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631095, '6763577', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631096, '6763577', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631097, '6763577', 'FILE', '1991-01-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631098, '6763577', 'FILE', '1990-12-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631099, '6763577', 'FILE', '1990-12-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631100, '6763577', 'FILE', '1989-07-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631101, '6763577', 'FILE', '1989-04-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631102, '6763577', 'FILE', '1987-10-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631103, '6763577', 'FILE', '1985-01-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631104, '6763577', 'FILE', '1983-10-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631105, '6763577', 'FILE', '1982-08-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631106, '6763577', 'FILE', '1981-09-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631107, '6763577', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631108, '6763577', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631109, '6763577', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
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
                    ('6763577', null, 'BC', '1979-07-31 00:00:00', '1990-07-31 00:00:00', null, '237858994', '439190809948484', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6763577', 1631109, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6763577', 1631108, 1631109, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6763577', 1631107, 1631108, 'HDF', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('6763577', 'CO', 1631095, 0, null, 'DVIZKGZYJLZVITJJUTGC', 'BPQNZI HDSVPHUHNQBZCSZDCF', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6763577', 'RG', 1631095, null, 431309, 431309, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6763577', 'RC', 1631095, null, 431309, 431309, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (431309, 'BC', 'CA', 'WDW0V6', 'CFUDWNTZPGVWKXGFRHCCZBZLC', 'BFYT DGNPANQOKUOSYOKBM XP', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
}
