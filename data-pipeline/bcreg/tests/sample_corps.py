
sample_test_corps = {
'corp_5464412': {
            "corp_num":'5464412', "corp_typ_cd":'ULC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3379538, 7138912, null, '5464412', 'INC', 8952972, null, null, null, null, null, null, null, null, null, 'K UJDTDBUUXGIXVPLZCB', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3379539, 7138914, 7138915, '5464412', 'DIR', 8952972, null, null, null, null, null, null, 'Bourgeois', null, 'Robert', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242653, '5464412', 'FILE', '2016-08-25 15:25:04', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8952972, '5464412', 'FILE', '2009-08-13 10:35:36', null)""",
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
                    ('5464412', null, 'ULC', '2009-08-13 10:35:36', null, null, null, null, null, 'QLIYDXNI', 'PBRIZFLL', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('5464412', 8952972, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('5464412', 'NB', 8952972, 0, null, 'BQMYJFQFVBJYPFFLITWW', 'YXHGBLREBDN MLMZ ZARFHBND', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5464412', 'RG', 8952972, 9242653, 7138917, 7138916, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5464412', 'RC', 8952972, 9242653, 7138919, 7138918, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5464412', 'RG', 9242653, null, 7535907, 7535906, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('5464412', 'RC', 9242653, null, 7535907, 7535906, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138912, 'BC', 'CA', 'MDNFMA', 'L I XOUOTTCG  AJNWTOGGTZ ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138914, 'ON', 'CA', '3BPY35', 'KWMCVDDYIPS TAQUQEBOPLEFR', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138915, 'ON', 'CA', 'N00UBC', 'JXOQ RYVQIYUENVIDHYXSKAAU', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138916, 'BC', 'CA', '4024ZK', 'HKKXMYF DJGFFYBOEGBJRPMUC', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138917, 'BC', 'CA', 'C6WQMY', 'TCJAWVJHRJKBYRUVFXXOQQSIJ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138918, 'BC', 'CA', 'QOEWGN', 'XSGLF PBBSLAYBTSW WENNEQH', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7138919, 'BC', 'CA', '3GP7XP', 'YPTTJIDEISGGXMEMYKXBFIPTI', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535906, 'BC', 'CA', '66FZMR', 'HKVPDBS JI WPOIPJILKQEAKQ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535907, 'BC', 'CA', '42ZZ0R', 'ASJPYHJDBOQDVKNXY JTVCDRC', 'LCJA OINZOQ  SQZUDHWSBZYL', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_A7330600': {
            "corp_num":'A7330600', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":3, "party_addr_ct":1, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682494, null, null, 'FM6157989', 'FBO', 105301927, null, null, null, null, '2001-05-09 14:29:44', null, null, null, null, 'A0031179LXNZRGDVDGURHOUBNM P', 'A7330600', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682496, null, null, 'FM8210420', 'FBO', 105301928, null, null, null, null, '2001-05-09 14:36:16', null, null, null, null, 'A0031179LUCAKWAKYCSCWYSWDCMI', 'A7330600', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510862, 7535953, 7535952, 'A7330600', 'ATT', 9242676, null, 96730, null, null, null, null, null, null, null, 'BC0121625SSXNDBTOYOBCBTOMQAYB', 'BC4478671', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96730, 84222, 84222, 'A7330600', 'ATT', 265264, 9242676, null, null, null, null, null, 'FERBER', null, 'JOHN P.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96731, 84223, 84223, 'A7330600', 'OFF', 265264, null, null, null, null, null, null, 'FLAHERTY', null, 'TIMOTHY J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96732, 84224, 84224, 'A7330600', 'DIR', 265264, null, null, null, null, null, null, 'KELLY', null, 'KEVIN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96733, 84224, 84224, 'A7330600', 'OFF', 265264, null, null, null, null, null, null, 'KELLY', null, 'KEVIN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96734, 84225, 84225, 'A7330600', 'DIR', 265264, null, null, null, null, null, null, 'MORIN', null, 'JEAN PAUL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96735, 84226, 84226, 'A7330600', 'OFF', 265264, null, null, null, null, null, null, 'RASPER', null, 'WOLFGANG', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96736, 84227, 84227, 'A7330600', 'DIR', 265264, null, null, null, null, null, null, 'ROXBURGH', null, 'LORIE-ANN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96737, 84228, 84228, 'A7330600', 'OFF', 265264, null, null, null, null, null, null, 'SCHUPP', null, 'PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (96738, 84229, 84229, 'A7330600', 'OFF', 265264, null, null, null, null, null, null, 'STRANG', null, 'ALLEN L.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105587336, 103538935, null, 'FM1730937', 'FBO', 104927429, null, null, null, null, '2008-04-25 00:00:00', null, null, null, null, 'A0031179WPTYMGNYQIQVIYRENT U', 'A7330600', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6351769, 'A7330600', 'FILE', '2005-06-13 11:13:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7098741, 'A7330600', 'FILE', '2006-05-15 10:30:06', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7567036, 'A7330600', 'ADCORP', '2007-03-13 10:54:46', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7636083, 'A7330600', 'FILE', '2007-04-26 09:38:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242676, 'A7330600', 'FILE', '2017-04-04 16:19:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265264, 'A7330600', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265265, 'A7330600', 'FILE', '2003-09-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265266, 'A7330600', 'FILE', '2003-09-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265267, 'A7330600', 'FILE', '2002-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265268, 'A7330600', 'FILE', '2001-06-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265269, 'A7330600', 'FILE', '2001-04-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265270, 'A7330600', 'FILE', '2001-04-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265271, 'A7330600', 'FILE', '2000-06-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265272, 'A7330600', 'FILE', '1999-06-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265273, 'A7330600', 'FILE', '1999-06-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265274, 'A7330600', 'FILE', '1998-12-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265275, 'A7330600', 'FILE', '1998-10-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265276, 'A7330600', 'FILE', '1998-07-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265277, 'A7330600', 'FILE', '1998-05-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265278, 'A7330600', 'FILE', '1997-07-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265279, 'A7330600', 'FILE', '1996-07-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265280, 'A7330600', 'FILE', '1995-10-25 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265281, 'A7330600', 'FILE', '1995-06-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265282, 'A7330600', 'FILE', '1995-06-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265283, 'A7330600', 'FILE', '1994-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265284, 'A7330600', 'FILE', '1994-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265285, 'A7330600', 'FILE', '1993-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265286, 'A7330600', 'FILE', '1993-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265287, 'A7330600', 'FILE', '1993-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265288, 'A7330600', 'FILE', '1992-09-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265289, 'A7330600', 'FILE', '1992-09-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265290, 'A7330600', 'FILE', '1992-05-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265291, 'A7330600', 'FILE', '1991-06-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265292, 'A7330600', 'FILE', '1991-04-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265293, 'A7330600', 'FILE', '1990-04-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (265294, 'A7330600', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5695631, 'A7330600', 'FILE', '2004-04-27 11:08:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8299235, 'A7330600', 'FILE', '2008-06-04 16:00:45', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8778281, 'A7330600', 'FILE', '2009-04-16 12:15:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721465, 'FM6157989', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301927, 'FM6157989', 'CONVFMACP', '2001-05-09 14:29:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721467, 'FM8210420', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301928, 'FM8210420', 'CONVFMACP', '2001-05-09 14:36:16', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104927429, 'FM1730937', 'CONVFMREGI', '2008-04-25 00:00:00', null)""",
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
                    ('A7330600', null, 'A', '1990-04-03 00:00:00', '2009-04-03 00:00:00', null, null, null, null, 'LJDDMBYA', 'QCFRDJNE', 'GVRNWQORZRLJ@HXECNJYN.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM6157989', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM8210420', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1730937', null, 'SP', '2008-04-25 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1163592, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A7330600', 265264, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM6157989', 104721465, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM8210420', 104721467, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1730937', 104927429, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A7330600', 265264, 5695631, null, 'FD', 'COR', '1989-11-21 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A7330600', 5695631, null, null, 'FD', 'COR', '1989-11-21 00:00:00', null, '254278-1', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A7330600', 'CO', 265264, 0, 265294, 'CTJKJOHIIRZIEYCRMMZS', 'YMBVMM SAXIXHEUSOWVKXSNWP', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A7330600', 'CO', 265294, 0, null, 'WOHDLSTJATWHSPKFBPMO', 'LGCRZNI NWH QWXMDWSVYVDMJ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM6157989', 'CO', 104721465, 0, null, 'KFTKZCTWYOSSPJSRDCCJ', 'WPOUMDDAKUPSEGK EBVLP UFY', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM8210420', 'CO', 104721467, 0, null, 'JFCQUHGCUIIURWFWYFUD', 'KE EHYLIZBPDXIZVCKYQYLHQF', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1730937', 'CO', 104927429, 0, null, 'UQJNFZFPOZTEASIQPLLS', 'FWCWALDQHPIGZBTCXWOLILNDW', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A7330600', 'HD', 265264, null, 84221, 84221, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM1730937', 'FO', 104927429, null, 103248012, 103248011, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84221, 'QC', 'CA', 'Y50AX1', 'XU TSEJYWCZKVLKXXSXPOPVEK', null, null, 'VILLE SAINT-LAURENT', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84222, null, null, 'DB6MG6', 'ZMTYVSFXCILTDGRZKBBFPPS M', 'RAFRZIOKKGXLPECVZLWJ TVNE', 'VANCOUVER BC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84223, null, null, null, 'BKMTQDETBMWSCUOQUCNBYBOEP', 'OJVWQAAIRQYWMYCCUNOHUUBPW', 'USA 48326', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84224, null, null, null, 'MARRUVMDTIUOCZTLKXAPHWZXK', 'L VQCUOPWRQSPTIONZRRBGLNK', 'USA 48326', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84225, null, null, 'H5Y80V', 'H UOXBOEYGPDWXCJLKGJIMYHU', 'KLJBDAYFLEPJMBFDSDBNOYTSJ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84226, null, null, null, 'OHEFIGFOLCNKX FPIYOCXEJCN', 'UVBSLXINESUCFZNEIPYPBZET ', 'USA 48326', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84227, null, null, 'GK0MY1', 'YQIGHYJZ LIIJHUIGGMSZ GHP', 'VT JSMCERSSBNWA NOHSZKQVW', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84228, null, null, null, 'KBVPYA JW TZGJEABAZQWZTDD', 'UQKUYFXWIJAOPWR YRGWHAUHH', 'USA 48326', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (84229, null, null, null, 'MGUZIZXSSTXYWT AKITMAXJXV', 'KAXTEHKEIMXMOXMMT YJRTEDA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535952, 'BC', 'CA', 'N120YE', 'SJPSRBMALCAEMJFVMWH TOAZD', null, null, 'Vancouver', 'FOR', 'USQDPTYFQJMAPBKVKZQJGYWVQLSDNIWEIINOAOAD', ' EDPNLOKVDSBIEZWLDHZ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535953, 'BC', 'CA', 'YLG6A0', 'JBHTWMYTGOPMPGJPFKFDCKDMH', 'GTFHEBRSICRRXXPRTQNWROQAS', null, 'Vancouver', 'FOR', 'FZJLIAINMNKKUAHHPXVOGXTWZXFKJELZYEVGNTGY', 'EVVMJWFBY AHAFEVIVPV', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248011, 'BC', 'CA', '0QMHP9', null, null, null, 'VANCOUVER', 'BAS', 'AB OQSILPGDRJLJDHWTNTTDIGRKHOA EGGVXJNUJ', 'UQR WRXDXKZJATYZRCMA', null, '629', null, '495', null, 'SWWRSXJSWHNLEJZ', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248012, 'ON', 'CA', 'JLAVMT', null, null, null, 'MARKHAM', 'BAS', 'JEGLXGXJQVZWJOIAGPFWUBXOMLUEAFIQTVZDAF A', 'TAEROGLYBHBAYPSVUSCX', null, '232', null, '464', null, 'IPWNSUSFXXNJDXP', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103538935, 'QC', 'CA', 'HBYL3B', 'LCBWMOGLIAUDXRDZGSQVZMGNX', null, null, 'SAINT-LAURENT', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM7980803': {
            "corp_num":'FM7980803', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105351824, 103180753, null, 'FM7980803', 'FCP', 104893496, null, null, null, null, null, null, 'LAWYERS', null, 'SYNERGY BUSINESS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105552151, 103503750, null, 'FM7980803', 'FBO', 104893496, null, null, null, null, '2007-02-14 00:00:00', null, null, null, null, '0765995PTFA BDPLBQIWGHHLLVK', '7869795', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104893496, 'FM7980803', 'CONVFMREGI', '2007-02-14 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104893496, 'FRREG', '2007-02-14 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM7980803', null, 'SP', '2007-02-14 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1114375, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM7980803', 104893496, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM7980803', 'CO', 104893496, 0, null, 'FKKNDDBONERFWCNHXFOQ', 'MLJHDIQICWYAXPUYZCZPQNBOQ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM7980803', 'FO', 104893496, null, 103180754, 103180754, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103180753, 'BC', 'CA', 'OJTCPY', null, null, null, 'VANCOUVER', 'BAS', 'NIBHWGTOSQJVJVURJGPDIAPKKGABZCOMNZDHNYXM', 'NH TIXTJCQWICLKINIPG', null, '653', null, '918', null, 'UYLNIEUFFBVBPBA', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103180754, 'BC', 'CA', '7ZMQD8', null, null, null, 'DELTA', 'BAS', 'ZLXKRPEHRMJZSOIJOZKIAKZFWUBE IN MFTQR ZY', 'GHMZQNBHS DPTIUROPIR', null, null, null, '741', null, 'DXOLBNPRJTGSBZV', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103503750, 'BC', 'CA', 'JWTGN6', 'QNUGKS YUTUZCAJRMOPTHIGJJ', null, null, 'VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_LP0737103': {
            "corp_num":'LP0737103', "corp_typ_cd":'LP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105772250, null, null, 'LP0737103', 'FBO', 104900882, null, null, null, null, '2007-05-15 00:00:00', null, null, null, null, '0790280SZZFTK BNDCFAKSFMRZE', '5282560', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104900882, 'LP0737103', 'CONVFMREGI', '2007-05-15 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104900882, 'LPREG', '2007-05-15 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('LP0737103', null, 'LP', '2007-05-15 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-05-15 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('LP0737103', 104900882, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('LP0737103', 'CO', 104900882, 0, null, 'ILCLYQJLHBQTJDWODVGD', 'XJHRO YYPDUBEBOW TXCZRBDR', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
'corp_8539182': {
            "corp_num":'8539182', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2747922, 5258703, null, '8539182', 'INC', 7651354, null, null, null, null, null, null, null, null, null, 'IAIXNRXXNUZUOHQXUQTU', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2747923, 5258705, 5258706, '8539182', 'DIR', 7651354, null, null, null, null, null, null, 'O''NEILL', 'C.', 'JOHN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2747924, 5258707, 5258708, '8539182', 'DIR', 7651354, null, null, null, null, null, null, 'O''NEILL', 'F.', 'ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105772250, null, null, 'LP1658610', 'FBO', 104900882, null, null, null, null, '2007-05-15 00:00:00', null, null, null, null, '0790280SAVQQKXDKVZQKBYYZWHP', '8539182', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3342812, 7030460, 7030460, '8539182', 'OFF', 8879933, null, 0, null, null, '2009-06-22 12:05:23', null, 'O''NEILL', null, 'ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3342813, 7030461, 7030461, '8539182', 'OFF', 8879933, null, 0, null, null, '2009-06-22 12:05:23', null, 'O''NEILL', null, 'JOHN', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7651354, '8539182', 'FILE', '2007-05-04 15:52:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242296, '8539182', 'FILE', '2015-07-28 14:46:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8879949, '8539182', 'FILE', '2009-06-22 12:07:54', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8879933, '8539182', 'FILE', '2009-06-22 12:05:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104900882, 'LP1658610', 'CONVFMREGI', '2007-05-15 00:00:00', null)""",
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
                    ('8539182', null, 'BC', '2007-05-04 15:52:52', '2009-05-04 00:00:00', null, null, null, null, 'FFELUCBY', 'FIJPJWMR', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('LP1658610', null, 'LP', '2007-05-15 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-05-15 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8539182', 7651354, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('LP1658610', 104900882, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('8539182', 'CO', 7651354, 0, null, 'IKQGJEWTZOHRNSRLPRZT', 'YJYROABNLYBRCYTRLEGPXKYLW', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('LP1658610', 'CO', 104900882, 0, null, 'TEYSJJIGTTCPEZATJANM', 'MF DLSBEFHAGWRKUPHERCINCT', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8539182', 'RG', 7651354, 9242296, 5258710, 5258709, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8539182', 'RC', 7651354, 9242296, 5258712, 5258711, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8539182', 'RG', 9242296, null, 7535430, 7535430, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8539182', 'RC', 9242296, null, 7535430, 7535430, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258703, 'BC', 'CA', '9OTY2I', 'JYMPTMWHOTYXLQYLXJPJSWDEA', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258705, 'BC', 'CA', '313DVK', ' MXXD XPN PZEHCXSSINQOVAF', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258706, 'BC', 'CA', 'J420TQ', 'JTFSBCWHZNBFBHLHWYLLCKKMU', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258707, 'BC', 'CA', 'Q6VTU7', 'XYGRZVZGFFMNTFBD FYXAJDTO', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258708, 'BC', 'CA', 'G5CF17', 'KUANVWEMSAFSISRKQHEVUYXHA', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258709, 'BC', 'CA', 'LT1FN1', 'QEVMJKNCFKCZFGAVIVGOE OKE', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258710, 'BC', 'CA', 'NIKYD0', 'RXZFMVSUQHSWJUBWTSOYZO NR', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258711, 'BC', 'CA', 'YSD01O', 'FZHVNSGUBSHMTVEAEEELFADTD', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5258712, 'BC', 'CA', '4CDAVF', 'FNOTVAPCEVNUOTBETAMARESXW', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7030460, 'BC', 'CA', 'E6AGEI', 'PASYGHTUGMZQHZQEXHTGTUFEG', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7030461, 'BC', 'CA', 'QO9SBV', 'NOI BYVHYYLVQYDD H AGKXCC', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535430, 'BC', 'CA', '583392', 'UCDBJSOEQRZDHBIBDSEJAAXOZ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM9737693': {
            "corp_num":'FM9737693', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105340674, 103155279, null, 'FM9737693', 'FCP', 104880184, null, null, null, null, null, null, 'LAWYERS', null, 'SYNERGY BUSINESS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105538816, 103490415, null, 'FM9737693', 'FBO', 104880184, null, null, null, null, '2006-08-16 00:00:00', null, null, null, null, '0765995PJULGTEDTCQZ KITKSRW', '5717946', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104880184, 'FM9737693', 'CONVFMREGI', '2006-08-16 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104880184, 'FRREG', '2006-08-16 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9737693', null, 'SP', '2006-08-16 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1095915, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9737693', 104880184, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9737693', 'CO', 104880184, 0, null, 'RXSGIJYELRXPTJHGFZED', 'VWMYENFYKU LACSODFGHDOKIR', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9737693', 'FO', 104880184, null, 103155280, 103155280, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103155279, 'BC', 'CA', 'Q1SFBM', null, null, null, 'VANCOUVER', 'BAS', 'XDIXUVTGGGIXLMCBNTLPBVNEIEAUTFRQJKHTWNII', 'UOPGZPKNGVMLOLNMLFJS', null, '008', null, '485', null, 'TMZSQXPOOYSGTBB', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103155280, 'BC', 'CA', 'C9Y17N', null, null, null, 'DELTA', 'BAS', ' TDJPMWXTRXDJMOFMVTVCJLOWFKTODLPHBLHRUPJ', 'NDIOEKFFPKSRJH HPOMG', null, null, null, '709', null, 'XLBHKNHASGOTRTT', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103490415, 'BC', 'CA', '0YCSVW', 'CELBICTZMHCZHZPWOQBGWEBVX', null, null, 'VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM4265857': {
            "corp_num":'FM4265857', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105381285, 103248010, null, 'FM4265857', 'FCP', 104927429, null, null, null, null, null, null, 'THOMSON LLP', null, 'MILLER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105587336, 103538935, null, 'FM4265857', 'FBO', 104927429, null, null, null, null, '2008-04-25 00:00:00', null, null, null, null, 'A0031179LAUTZSECPYVJRNWPXDWT', 'A1221449', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104927429, 'FM4265857', 'CONVFMREGI', '2008-04-25 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104927429, 'FRREG', '2008-04-25 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM4265857', null, 'SP', '2008-04-25 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1163592, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM4265857', 104927429, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM4265857', 'CO', 104927429, 0, null, 'LXSWHLQIDNRFBGPLQSJE', 'RFUWAQXPUNYKRHYCZJXY BCYH', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM4265857', 'FO', 104927429, null, 103248012, 103248011, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248010, 'BC', 'CA', '8VYQFC', null, null, null, 'VANCOUVER', 'BAS', 'QBZLODYSLANJKTGFJMOS DNMXOAVQKTOZFGTYIXV', 'CRAKUMLWOKNT KC BNAO', null, '953', null, '399', null, 'JXBQGWGUEYJETUP', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248011, 'BC', 'CA', 'H6RSST', null, null, null, 'VANCOUVER', 'BAS', 'CAIL FQKGQFFXTUVWXIMISYDVAXUDOLVHFNNQEKV', 'CXWXIDOYMTOVFZUYLPDX', null, '308', null, '824', null, 'XLSXWEFZQTLCAJT', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103248012, 'ON', 'CA', 'YBNW05', null, null, null, 'MARKHAM', 'BAS', 'LEFAPVIIOAXAWPUGUVHJFKBJSPFHUJBUSYICAFGM', 'XBJPV DDTXFNNZORSYVG', null, '136', null, '816', null, 'SYNJWFUJAFCDFTI', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103538935, 'QC', 'CA', '5L7KRP', 'JIJOXNJIQYUUGDKVXBZYMONEL', null, null, 'SAINT-LAURENT', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_A4138183': {
            "corp_num":'A4138183', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1922541, 2043487, 2043486, 'A4138183', 'ATT', 5837836, 9242706, 269581, null, null, null, null, null, null, null, 'ARAGBGXGYZNCIABJKZDJ', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510892, 7536013, 7536012, 'A4138183', 'ATT', 9242706, null, 1922541, null, null, null, null, null, null, null, 'BC0121625IRFNQYSCILBYWVUSNYEA', 'BC7429609', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269581, 237083, 237083, 'A4138183', 'ATT', 580103, 5837836, null, null, null, null, null, 'HEENAN BLAIKIE CORPORATE', null, 'SERVICES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269582, 237084, 237084, 'A4138183', 'DIR', 580103, null, null, null, null, null, null, 'KEARNS', null, 'JOHN R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269583, 237084, 237084, 'A4138183', 'OFF', 580103, null, null, null, null, null, null, 'KEARNS', null, 'JOHN R.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269584, 237085, 237085, 'A4138183', 'OFF', 580103, null, null, null, null, null, null, 'LEWIS', null, 'PETER A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (269585, 237086, 237086, 'A4138183', 'OFF', 580103, null, null, null, null, null, null, 'MATEAR', null, 'CAROLE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6576516, 'A4138183', 'FILE', '2005-09-22 15:01:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7254645, 'A4138183', 'FILE', '2006-08-24 10:34:27', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7896643, 'A4138183', 'FILE', '2007-10-02 10:42:47', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242706, 'A4138183', 'FILE', '2017-04-04 16:19:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580103, 'A4138183', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580104, 'A4138183', 'FILE', '2003-09-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580105, 'A4138183', 'FILE', '2003-05-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580106, 'A4138183', 'FILE', '2002-11-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (580107, 'A4138183', 'FILE', '2002-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5837836, 'A4138183', 'FILE', '2004-08-10 14:33:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5836508, 'A4138183', 'FILE', '2004-08-09 16:56:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8410817, 'A4138183', 'FILE', '2008-08-19 15:39:18', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8413272, 'A4138183', 'FILE', '2008-08-20 15:21:11', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8980486, 'A4138183', 'FILE', '2009-09-02 14:49:33', null)""",
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
                    ('A4138183', null, 'A', '2002-07-02 00:00:00', '2009-07-02 00:00:00', null, null, null, null, 'SCYPESPN', 'RPENAJAW', 'YCXOLRIDCCYW@TBTQHUTB.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A4138183', 580103, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4138183', 5836508, null, null, 'FD', 'COR', '1998-07-21 00:00:00', null, '351401-3', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4138183', 580103, 5836508, null, 'FD', 'COR', '1998-07-21 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A4138183', 'CO', 580103, 0, null, 'VNRYUDOSQCKESWDVWUEA', 'TSHJFWQOBJJAUDYSDVEMGBUOE', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4138183', 'HD', 8413272, null, 6381045, 6381044, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4138183', 'HD', 580103, 8413272, 237082, 237082, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (237082, null, null, 'QN96AA', 'FECHBCSFPKWMAZKQUY SOPJZA', 'BRGEBJUOTTPQTD AFVYFLAKLJ', 'TORONTO ON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (237083, null, null, '3GXX3U', 'OGGKHLP APFYGYDVOKDWZJHNA', ' DRQVYUCIJEUYRLROCVYKDMHP', 'VANCOUVER BC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (237084, null, null, 'PT8AZI', 'ZT DLXJLAOMYIOPVFDBSOEMAJ', 'ITVRFBWYRQLZAAJUSVVYWXWDT', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (237085, null, null, 'ACJ55V', 'ZRMCIDKASLSVXODPINFULZYCA', 'ADEKNW JYTYIITBWJXWBGOFLM', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (237086, null, null, '0HB4B4', 'LWTWZWAERKQMJNMAGKNUUBLDE', 'ZTQVUR QBSN PDZDASORDZOPO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2043486, 'BC', 'CA', 'L3N39I', 'FRHJECCBICPUSBSJACDJRPNRS', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2043487, 'BC', 'CA', 'KXB1VH', 'AJLUM WBTQFWBNUUEGBDQRXA ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6381044, 'ON', 'CA', 'CB17LG', 'URPCYP V QXKPOCVILMYXBGBX', null, null, 'TORONTO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6381045, 'ON', 'CA', '886912', 'IZTOMZJSKYOSOQALJRBADKJYB', null, null, 'TORONTO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7536012, 'BC', 'CA', '7ZWCA9', 'MBTDPQIEPN FGRIMWSMLABXTW', null, null, 'Vancouver', 'FOR', 'CICQVXUGHUPPPJBLCLALGIGBWYXIRDYLDZEW AWG', 'PAGSVOZCBGCMZCSYQOGM', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7536013, 'BC', 'CA', 'U9LWZD', 'FRAVXC LVPXWPCYLXDSSAOQON', 'ISAXIQT SPV XRXFVOHZCQ LK', null, 'Vancouver', 'FOR', 'DHMJJXYTLEYYXSH ZERTPAFMMVIVSYDXZTYUMRTE', 'PRPJFGYNBIZTFEE FLPX', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM9935965': {
            "corp_num":'FM9935965', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105395407, 103280173, null, 'FM9935965', 'FCP', 104943427, null, null, null, null, null, null, 'BUSINESS LAWYERS', null, 'SYNERGY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604099, 103555698, null, 'FM9935965', 'FBO', 104943427, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071DZKXTCQGJXKWHCLTMQDA', '1935208', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943427, 'FM9935965', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104943427, 'FRREG', '2008-12-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9935965', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186186, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9935965', 104943427, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9935965', 'CO', 104943427, 0, null, 'WVUTIRIYNNAGMCGPENQO', 'HAISLDDZEEKMVCFYWNAJCPGJV', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9935965', 'FO', 104943427, null, 103280174, 103280174, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280173, null, 'CA', 'E85Y55', 'KSIYVWGVAPDRXVYVTHBVFZOTE', null, null, 'VANCOUVER', 'FOR', 'AORLXDJCBQGTTDLWXGVBJSQYJLMXCNCCEIKNAXEB', 'WHFNOMHSBPHTZPXWMRQZ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280174, null, 'CA', 'KY6PUV', 'EDNGYZVGRWXA UKC GLDVANVZ', null, null, 'DELTA', 'FOR', 'DBEHQNEKPBWCHHNQIZTVSSJMLMDUZU TNAUPQTHL', 'RUBIVVAWHBUBLZCJMMYD', null, null, null, '119', null, 'WBKTOVNDOKEJQQD', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103555698, 'BC', 'CA', 'H8L89O', 'QYSYMU PIYXRUJBECVOZQHSTL', null, null, 'DELTA', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_9143683': {
            "corp_num":'9143683', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":2, "party_addr_ct":1, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1669259, 1531135, 1531135, '9143683', 'DIR', 5381349, 5921183, null, null, null, null, null, 'GILLESPIE', null, 'GEOFFREY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1669260, 1531135, 1531135, '9143683', 'OFF', 5381349, null, null, null, null, null, null, 'GILLESPIE', null, 'GEOFFREY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1961692, 2196611, 2196610, '9143683', 'DIR', 5921183, null, 1669259, null, null, null, null, 'GILLESPIE', null, 'GEOFFREY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105641127, 103592726, null, 'FM7821785', 'FBO', 104977770, null, null, null, null, '2010-03-22 00:00:00', null, null, null, null, '0614205CSBPFDRNDVJEDHYTDVRJ', '9143683', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105755067, null, null, 'FM1687454', 'FBO', 104799510, null, null, null, null, '2003-09-17 00:00:00', null, null, null, null, '0614205SUXBIAVPZPSZVONFUJKO', '9143683', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6355428, '9143683', 'ADCORP', '2005-06-14 09:18:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6355556, '9143683', 'FILE', '2005-06-14 09:40:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6466334, '9143683', 'FILE', '2005-08-02 14:18:38', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6466631, '9143683', 'ADCORP', '2005-08-02 15:04:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6596448, '9143683', 'FILE', '2005-10-03 12:58:21', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7302429, '9143683', 'FILE', '2006-09-27 12:02:40', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7879279, '9143683', 'FILE', '2007-09-21 10:52:54', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242019, '9143683', 'FILE', '2015-07-28 14:46:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381350, '9143683', 'FILE', '2003-09-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381351, '9143683', 'FILE', '2002-11-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381352, '9143683', 'FILE', '2001-11-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381353, '9143683', 'FILE', '2000-09-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5381349, '9143683', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5693022, '9143683', 'ADCORP', '2004-04-24 10:10:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5915165, '9143683', 'FILE', '2004-10-04 09:36:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5921183, '9143683', 'FILE', '2004-10-06 15:43:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5921193, '9143683', 'FILE', '2004-10-06 15:44:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8734851, '9143683', 'FILE', '2009-03-18 11:14:27', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9054719, '9143683', 'FILE', '2009-10-23 11:28:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104799510, 'FM1687454', 'CONVFMREGI', '2003-09-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104977770, 'FM7821785', 'CONVFMREGI', '2010-03-22 00:00:00', null)""",
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
                    ('9143683', null, 'BC', '2000-09-15 00:00:00', '2009-09-15 00:00:00', '2004-10-06 15:43:00', null, null, null, 'DPYAMWBY', 'ROVJHXLF', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1687454', null, 'SP', '2003-09-17 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2003-09-17 00:00:00', null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM7821785', null, 'SP', '2010-03-22 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1240790, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('9143683', 5381349, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1687454', 104799510, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM7821785', 104977770, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('9143683', 'CO', 5381349, 0, null, 'EMDKUEMLRHZREJSSNHVW', 'DTULHWZUYGJPZAOIJFVLXXGNG', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1687454', 'CO', 104799510, 0, null, 'UKBXMBSRXWVJHXKXUFWX', 'CV XCWFDRAPTOSFYFHB CMBRV', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM7821785', 'CO', 104977770, 0, null, 'SJDAVSVUHYBXEUEBNHVO', 'CBFGSJWFKHCVMWRZZZZOYWJDI', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RG', 9242019, null, 7535153, 7535153, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RC', 9242019, null, 7535153, 7535153, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RG', 5381349, 5921183, 1531134, 1531134, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RC', 5381349, 5921183, 1531134, 1531134, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RC', 5921183, 6466334, 2196613, 2196612, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RG', 5921183, 6466334, 2196615, 2196614, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RG', 6466334, 9242019, 3208074, 3208073, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9143683', 'RC', 6466334, 9242019, 3208072, 3208071, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM7821785', 'FO', 104977770, null, 103346956, 103346956, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1531134, 'BC', 'CA', 'USO1FE', ' OZBPVLSFLIYIPHTLQBGUHLCU', 'P UCQYPINDBQZC IUBRBMBQZE', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1531135, null, null, 'FEGUV7', 'LYFFUKXMFBGUIVPEOLWDJNECM', 'F AMLVEQEBIUWT VSKBJPEXVH', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196610, 'BC', 'CA', 'GSYQNX', 'WKCGGUQOBNWJETGDBLGDI FTH', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196611, 'BC', 'CA', 'E7258D', 'EBVPPVESYVBWAIWSQUYDAKOXT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196612, 'BC', 'CA', 'QFSGCK', 'DWTTETYOPARHQMRZOGNTENVGI', ' UTE EVJPEHXVTYHWWCJBX QU', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196613, 'BC', 'CA', 'TVNTUB', 'U KG U JUZEXEWRZBQFDZAUVY', 'AHPTSJFPNNLBLGQLOEROSLXUU', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196614, 'BC', 'CA', 'XC93SP', 'SAILHRGTZ PUD DTPBAMFL SQ', 'MCJNTCAZHINETNOFZUPXVQMKE', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2196615, 'BC', 'CA', 'N82F1V', 'LKVANKTNOZTLSKNJLAXCKWLIP', 'PNLMVICYQFW HNVNXEBWMJIUA', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208071, 'BC', 'CA', 'JQPUWE', 'D RLBHQESPZJZPWXSEDNBOTCI', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208072, 'BC', 'CA', 'PMHCU5', 'QMYKNETSGAUOLA VOSWOCYSNZ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208073, 'BC', 'CA', 'T9RZ4U', 'L CBKHVEOEJSKVGWSKAZDWSPF', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3208074, 'BC', 'CA', '9X9TGO', 'MURPJBRETEHYBIBOP CAONLUF', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535153, 'BC', 'CA', 'R3XZTT', 'JHDRDXQZTIPPMETUBXCCDYMII', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103346956, 'BC', 'CA', 'EKH4QJ', null, null, null, 'WEST VANCOUVER', 'BAS', 'ZKHTHPD ULFPDWMXKFTFG DULOITZTDYXWMDPDOM', 'POPOMBMCSPFBQSEOFBMR', null, null, null, '186', null, 'YDHYOMGDHCBIQUK', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103592726, 'BC', 'CA', 'AOTZUH', 'YDAN AFNDJVBIYGUQIFGSYUAL', null, null, 'WEST VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_A8503135': {
            "corp_num":'A8503135', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":1, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105778013, null, null, 'FM2134347', 'FBO', 104961111, null, null, null, null, '2009-08-12 00:00:00', null, null, null, null, 'A0053427VKRTJOQPJAZEJSZMVR G', 'A8503135', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510879, 7535987, 7535986, 'A8503135', 'ATT', 9242693, null, 241959, null, null, null, null, null, null, null, 'BC0121625BEV SWDGMCIDAE CYWYQ', 'BC0612290', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241959, 212679, 212679, 'A8503135', 'ATT', 540651, 9242693, null, null, null, null, null, null, null, null, 'IFPWPUHJ KMKDOOEMFFM', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241960, 212680, 212680, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'BEATON', null, 'ELIZABETH', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241961, 212681, 212681, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'CARTER', null, 'KIM', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241962, 212682, 212682, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'CLARK', null, 'GREG', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241963, 212683, 212683, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'CORTESE', null, 'ROBERTO', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241964, 212684, 212684, 'A8503135', 'DIR', 540651, null, null, null, null, null, null, 'DOWDING', null, 'JANICE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241965, 212684, 212684, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'DOWDING', null, 'JANICE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241966, 212685, 212685, 'A8503135', 'DIR', 540651, null, null, null, null, null, null, 'MANNING', null, 'GERALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241967, 212685, 212685, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'MANNING', null, 'GERALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241968, 212686, 212686, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'RAHILL', null, 'DONNACHA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241969, 212687, 212687, 'A8503135', 'DIR', 540651, null, null, null, null, null, null, 'SCHELLENS', null, 'KAREL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241970, 212687, 212687, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'SCHELLENS', null, 'KAREL', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241971, 212688, 212688, 'A8503135', 'DIR', 540651, null, null, null, null, null, null, 'SHANNON', null, 'LORRIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241972, 212688, 212688, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'SHANNON', null, 'LORRIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241973, 212689, 212689, 'A8503135', 'DIR', 540651, null, null, null, null, null, null, 'SLAATS', null, 'RONALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (241974, 212689, 212689, 'A8503135', 'OFF', 540651, null, null, null, null, null, null, 'SLAATS', null, 'RONALD', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6131779, 'A8503135', 'FILE', '2005-02-17 12:52:19', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6781060, 'A8503135', 'FILE', '2005-12-29 11:26:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7463049, 'A8503135', 'FILE', '2007-01-15 11:47:02', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7657304, 'A8503135', 'ADCORP', '2007-05-09 13:45:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242693, 'A8503135', 'FILE', '2017-04-04 16:19:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540651, 'A8503135', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540652, 'A8503135', 'FILE', '2003-02-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540653, 'A8503135', 'FILE', '2002-04-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (540654, 'A8503135', 'FILE', '2000-12-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5657305, 'A8503135', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5688948, 'A8503135', 'FILE', '2004-04-21 16:13:39', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8066579, 'A8503135', 'FILE', '2008-01-11 15:16:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8727866, 'A8503135', 'FILE', '2009-03-13 14:33:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9189992, 'A8503135', 'FILE', '2010-01-19 11:58:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104961111, 'FM2134347', 'CONVFMREGI', '2009-08-12 00:00:00', null)""",
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
                    ('A8503135', null, 'A', '2000-12-13 00:00:00', '2009-12-13 00:00:00', null, null, null, null, 'BOXSAPWZ', 'JWSAZQOK', 'BQFHCFSBTEEA@HWHAKENO.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM2134347', null, 'SP', '2009-08-12 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2009-08-12 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A8503135', 540651, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM2134347', 104961111, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A8503135', 540651, 6131779, null, 'FD', 'COR', '2000-07-31 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A8503135', 6131779, null, null, 'FD', 'COR', '2000-07-31 00:00:00', null, '378756-7', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A8503135', 'CO', 540651, 0, null, 'WLGTXMZSBHRCUQAUWSUB', 'FYFJBO HOAFDKBNVSKNWFOPJS', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A8503135', 'NO', 5657305, 0, null, 'AQTAKLNVTIHJTGRDESIW', 'YLJNEDCSPWVDZZY NOQDOPEYH', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM2134347', 'CO', 104961111, 0, null, 'XDHNYOCQFHUKMCATBQTD', 'CKLIIDWITMITIBYVSROBBRANY', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A8503135', 'HD', 540651, null, 212678, 212678, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212678, 'ON', 'CA', '57L73X', 'DYTVXJORZV DWKLWUM MUQGDX', null, null, 'OAKVILLE', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212679, 'BC', 'CA', 'TME43I', 'QQOGCJSXPSVVFZ SQORPGIBYL', 'TTT RMZJTXXPBBZSLGILNCSCP', '595 BURRARD STREET,', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212680, null, null, 'X6CMPI', 'LKXDMIEZCVTFPFWYGCPWFSAO ', 'GGIOVQKZYGVGDMV DKILYUIQJ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212681, null, null, 'UJPO3Y', 'QJMOIDOGOACPAXKYOMVOLQRBS', 'YSCFHCVUNMTSKSXUDHCFUZNDH', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212682, null, null, 'G4UHYF', 'I XUSHQJJYTMMALVIRBIFZKJY', 'FTLTRXSUGEEDFWKIFNFCYKIUL', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212683, null, null, 'C3VEV3', 'IXGNUICKORCZDZBZAUHHDJHLN', 'VPHXBDLADMLADYMXICMLILNLG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212684, null, null, 'GRCLA9', 'XAPWCPGM ASIUPKIMQEXSXJDI', 'KGLEQC VJMCH RDY GDXDWKOI', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212685, null, null, '99W8TT', 'OUEDBTCZMTDRNQUOR EHCCPCD', 'NDWVBY ZCFCYDPSBZRDBYXFRK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212686, null, null, 'V7RN15', 'GNPO NSJAWQLAJXPDJRVDDXTQ', 'WFIWOTRLBJBZNDCDEMMEGF ER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212687, null, null, null, 'IZIMSHNWI SMWZNBSDNKJWEYM', 'UCZZTDNBOUTAEPLROLOPDMHBT', 'EINHOVEN THE NETHERLANDS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212688, null, null, '5203SE', 'GGKITPNMDQUTBSXPUYVXPIWUV', ' BFARUCMWOVIQUWFKCQHOTLKT', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (212689, null, null, null, 'E DKHAJVIWDEGPKZSASBPMYWT', '  WDUQSMWXPQOQPQPTLXXWNAL', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535986, 'BC', 'CA', 'AM7KF8', 'QYWYHPTWJKLKULIJNCHEMZFE ', null, null, 'Vancouver', 'FOR', 'DRJRUYOXIPWQCADMFZBTTBPDPDOAEELCMVOGARQZ', 'MEGQIJHRRERAKXYTEYZQ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535987, 'BC', 'CA', '6KAIP8', 'WTUSNXCZIFRPCQMQELTFLYIOG', 'FZLYKQYZEDITDYOL KOQG URI', null, 'Vancouver', 'FOR', 'YDMSJJNZDUPMBPEZWROKFNMNTYSSBHVIMDAXEQAV', 'IDJLRWQEXBSLCWQHQEVP', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM4575576': {
            "corp_num":'FM4575576', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105395439, 103280245, null, 'FM4575576', 'FCP', 104943462, null, null, null, null, null, null, 'BUSINESS LAWYERS', null, 'SYNERGY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604136, 103555735, null, 'FM4575576', 'FBO', 104943462, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071CZGCOUXWHHGEMTOTLYED', '8305663', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943462, 'FM4575576', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104943462, 'FRREG', '2008-12-08 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM4575576', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186243, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM4575576', 104943462, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM4575576', 'CO', 104943462, 0, null, 'HJRPULEIIOSALBXNQJRC', ' PLDYAWYJAFDPEDDVBQBINDAD', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM4575576', 'FO', 104943462, null, 103280246, 103280246, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280245, null, 'CA', 'S14CNW', 'GIEX JOQAKZIKGQKAKUQBPZGM', null, null, 'VANCOUVER', 'FOR', 'QPKVE GZTJ EZEHDINTMBDVBTW QUREIHHZEVBUL', 'URVYLIFGBKRQMLPJDPHP', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280246, null, 'CA', '91LE35', 'RBPJEPVSWTAGCPMNPFJBPBKNU', null, null, 'DELTA', 'FOR', 'LNPQVXLMDVOH SWRW GLSDMPZJFALHFWBTWXMZEY', 'DXBCMAJQVCTK MMABDGM', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103555735, 'BC', 'CA', 'IIGEIJ', 'TUDUAFHDENTPFN RHTGKMKFVQ', null, null, 'DELTA', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_C6706515': {
            "corp_num":'C6706515', "corp_typ_cd":'C', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1337715, 1214404, 1214404, 'C6706515', 'DIR', 4524285, 6608265, null, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1337716, 1214404, 1214404, 'C6706515', 'OFF', 4524285, 6597413, null, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2261922, 3419756, 3419756, 'C6706515', 'OFF', 6597413, 7189315, 0, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2266047, 3437285, 3437284, 'C6706515', 'DIR', 6608265, 7189306, 1337715, 'C', null, null, null, 'MOHR', 'PHILLIP', 'BRUCE ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2536266, 4600111, 4600110, 'C6706515', 'DIR', 7189306, null, 2266047, null, null, null, null, 'MOHR', 'PHILLIP', 'BRUCE ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2536274, 4600135, 4600135, 'C6706515', 'OFF', 7189315, null, 0, null, null, null, null, 'MOHR', null, 'BRUCE PHILLIP', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6608265, 'C6706515', 'FILE', '2005-10-07 10:12:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6597413, 'C6706515', 'FILE', '2005-10-03 16:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6597431, 'C6706515', 'FILE', '2005-10-03 16:41:37', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7189306, 'C6706515', 'FILE', '2006-07-11 15:05:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7189315, 'C6706515', 'FILE', '2006-07-11 15:07:41', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7361673, 'C6706515', 'ADCORP', '2006-11-07 14:23:09', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7869174, 'C6706515', 'FILE', '2007-09-15 08:00:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242527, 'C6706515', 'FILE', '2015-07-28 14:46:42', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524285, 'C6706515', 'CONVCIN', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524286, 'C6706515', 'FILE', '2003-08-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524287, 'C6706515', 'FILE', '2002-09-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524288, 'C6706515', 'FILE', '2001-07-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524289, 'C6706515', 'FILE', '2000-08-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524290, 'C6706515', 'FILE', '1999-09-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524291, 'C6706515', 'FILE', '1998-07-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524292, 'C6706515', 'FILE', '1997-07-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524293, 'C6706515', 'FILE', '1997-07-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524294, 'C6706515', 'FILE', '1996-09-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524295, 'C6706515', 'FILE', '1996-07-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524296, 'C6706515', 'FILE', '1996-05-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524297, 'C6706515', 'FILE', '1995-06-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4524298, 'C6706515', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5837762, 'C6706515', 'ADCORP', '2004-08-10 14:14:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5837768, 'C6706515', 'FILE', '2004-08-10 14:15:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8366741, 'C6706515', 'FILE', '2008-07-18 10:22:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8970759, 'C6706515', 'FILE', '2009-08-26 11:35:26', null)""",
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
                    ('C6706515', null, 'C', '1995-06-26 00:00:00', '2009-06-26 00:00:00', '2005-10-07 10:12:20', null, null, null, 'RWLEAYND', 'RVWJHAGK', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C6706515', 4524285, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C6706515', 4524285, null, null, 'AB', 'COR', '1989-07-20 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6706515', 'CO', 4524285, 0, 4524298, 'BJZQIGVFKJYKQLXCDVAW', 'JURENLCIMACEFMRCM TQMWNMZ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C6706515', 'CO', 4524298, 0, null, 'OZLGMOUONYYDIHXLXWAF', 'W N ISLZIUFWUGTVFQTHWKIDC', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6706515', 'RG', 9242527, null, 7535661, 7535661, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6706515', 'RC', 9242527, null, 7535661, 7535661, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6706515', 'RG', 4524285, 6597431, 1214403, 1214403, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6706515', 'RC', 4524285, 6597431, 1214403, 1214403, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6706515', 'RG', 6597431, 9242527, 3419781, 3419780, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C6706515', 'RC', 6597431, 9242527, 3419779, 3419778, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1214403, 'BC', 'CA', 'VCOX8R', ' PPCDRHBJJV QPVMFGBWY RAZ', 'GWYESRB ZQRDSTTLZXGITESIQ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1214404, null, null, 'DV5BW0', 'RHTYAFHAIOICVTWDSLPNNALAO', 'QJRVYTLXOPBYB VEBYIYDWAFQ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419756, 'BC', 'CA', 'RQBCXV', 'ZNNNIUDZUWKELUMCJPVKBFBJH', null, null, 'WHISTLER ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419778, 'BC', 'CA', 'MW2NDG', 'BQVMY WGISUDLU NJQHLRHBSR', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419779, 'BC', 'CA', 'F3RZVI', 'NEKWXBNQTVJFILLXRDYCJLOIE', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419780, 'BC', 'CA', 'KCXELQ', 'COZWOKPR VAUXWKSNTMCXNDAP', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3419781, 'BC', 'CA', 'ZMPOC8', 'JTXGWGQUVUIQTYMMMNQLFLZES', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3437284, 'BC', 'CA', '89UXCF', 'UMHOSJLQAJUUKZKIDYJU IUPG', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3437285, 'BC', 'CA', 'RO70Z2', 'IGZJNCAPJJ GS WJKWZTULPHH', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4600110, 'BC', 'CA', 'MG1XHW', 'SUWHWNZJN  FICJZMWSPZIKWP', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4600111, 'BC', 'CA', 'GIY79N', 'ODCDXYFYMYABCIUPNMEUJNAYQ', null, null, 'WHISTLER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4600135, 'BC', 'CA', 'N3UOT2', 'UHNPYVNILJDCGQOLJLWNCSQP ', null, null, 'WHISTLER ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535661, 'BC', 'CA', '9K1GHS', 'GVFJSHIEIKTOORSZSHLSUCLJY', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_A4031472': {
            "corp_num":'A4031472', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":1, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510945, 7536119, 7536118, 'A4031472', 'ATT', 9242759, null, 3396139, null, null, null, null, null, null, null, 'BC0121625IYNJTJXONIKDXQILJLAA', 'BC3107709', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3396139, 7187950, 7187951, 'A4031472', 'ATT', 8985982, 9242759, null, null, null, null, null, null, null, null, 'SSPO JN EUPZA E LPKK', null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242759, 'A4031472', 'FILE', '2017-04-04 16:19:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8985982, 'A4031472', 'FILE', '2009-09-08 12:28:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9005775, 'A4031472', 'FILE', '2009-09-22 13:15:35', null)""",
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
                    ('A4031472', null, 'A', '2009-09-08 12:28:58', null, null, null, null, null, 'ENNUSHKO', 'TVLGPXSE', 'ZVKQDXTDHSGO@QUIOFIPQ.com', null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A4031472', 8985982, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A4031472', 8985982, null, null, 'ON', 'COR', '2008-02-28 00:00:00', null, '1761802', null, 'HOLIDAY FILMS INC.', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A4031472', 'AS', 8985982, 0, null, 'NYCLAUUPIISAQDFRFIFW', 'B JAERAHXGNTSLVGYDMGFGKNP', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A4031472', 'CO', 8985982, 0, null, 'PNYPGQNKQWCRHIXIKNMX', 'LXJNIJSRI Q RWPYZQSCUUUAC', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4031472', 'HD', 9005775, null, 7217652, 7217651, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A4031472', 'HD', 8985982, 9005775, 7187949, 7187948, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7187948, 'ON', 'CA', '5059DR', 'N W XCEKNUSPBNXQRGHKFQJRR', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7187949, 'ON', 'CA', 'PSZBBT', 'VONNVVXR VIHHALEPMXHZDENQ', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7187950, 'BC', 'CA', '28RIFC', 'TEGZQCDYZQSLHLKKTPFFINPDK', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7187951, 'BC', 'CA', 'XTTRCC', 'HUYQHUGYDIIGWXCNWFOAJG UH', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7217651, 'ON', 'CA', 'F2VCDS', 'XSXYDJONUVJ DAFLJAIKRHTUA', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7217652, 'ON', 'CA', 'XESP09', 'OMHZHYIWDTGUDQCJMDRUFNMVP', null, null, 'Toronto', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7536118, 'BC', 'CA', '0QHW26', 'FKSISDYHQNFD FEFZJQFYWWFD', null, null, 'Vancouver', 'FOR', ' WKAERACDDKWSNJMQHGPQPGVDIVNMJMR AIDTYOX', 'VUA BEDSLGUPADYOMFJX', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7536119, 'BC', 'CA', 'A5T9A8', 'YVHCYFKCEKTLXCNCRDJUAXHPP', 'GATOPIYMFBBTLEZLRSTOXPJOF', null, 'Vancouver', 'FOR', 'XCCLM BBN WUEEUOJ VFIFBRRERLZHLAHGUYN QX', 'PUZUQ FBFGQLZTPEKYSA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM1437726': {
            "corp_num":'FM1437726', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105641127, 103592726, null, 'FM1437726', 'FBO', 104977770, null, null, null, null, '2010-03-22 00:00:00', null, null, null, null, '0614205EUTNWXDOSZHC HTLUWAO', '0915518', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105426618, 103346955, null, 'FM1437726', 'FCP', 104977770, null, null, null, null, null, null, 'GEOFFREY', null, 'GILLESPIE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104977770, 'FM1437726', 'CONVFMREGI', '2010-03-22 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104977770, 'FRREG', '2010-03-22 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1437726', null, 'SP', '2010-03-22 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1240790, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1437726', 104977770, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1437726', 'CO', 104977770, 0, null, 'MLKORQLETYTFCLJLOSPJ', 'QNZUBZPVHVHMAXLTJSHGJIQ U', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM1437726', 'FO', 104977770, null, 103346956, 103346956, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103346955, 'BC', 'CA', 'PK3D1K', null, null, null, 'WEST VANCOUVER', 'BAS', 'JRLJQ QUALUDKIZH CKTYCLJMOSQQVZSYKMDGDEA', 'KEBUTLMJSPRCFBTX YL ', null, null, null, '718', null, 'GCAJKVTQYSMERJE', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103346956, 'BC', 'CA', 'FZTYPY', null, null, null, 'WEST VANCOUVER', 'BAS', 'ZTVZSXQVFFXXPYMIOMBVOQTFBKXALHOEHFSTQVLI', 'GIVOAOWUNB  MUZCBFRS', null, null, null, '331', null, 'SVNBLUVLPLNEUEM', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103592726, 'BC', 'CA', 'IFSXS7', 'IJZM MHZB RNCDQQBWRPBASGK', null, null, 'WEST VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_0031643': {
            "corp_num":'0031643', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2390060, 3982722, 3982721, '0031643', 'DIR', 6889406, null, 177654, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2390051, 3982665, 3982665, '0031643', 'OFF', 6889381, null, 0, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177652, 155618, 155618, '0031643', 'DIR', 424281, null, null, null, null, null, null, 'FARRELL', null, 'RICKY WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177653, 155618, 155618, '0031643', 'OFF', 424281, null, null, null, null, null, null, 'FARRELL', null, 'RICKY WAYNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177654, 155619, 155619, '0031643', 'DIR', 424281, 6889406, null, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (177655, 155619, 155619, '0031643', 'OFF', 424281, 6889381, null, null, null, null, null, 'YUCHYM', null, 'PENNY GAYLENE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6210660, '0031643', 'FILE', '2005-04-04 11:31:45', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6210656, '0031643', 'ADCORP', '2005-04-04 11:31:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6889381, '0031643', 'FILE', '2006-02-15 16:07:11', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6889406, '0031643', 'FILE', '2006-02-15 16:10:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7506338, '0031643', 'FILE', '2007-02-07 15:12:25', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9241789, '0031643', 'FILE', '2015-07-28 14:46:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424281, '0031643', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424282, '0031643', 'FILE', '2003-04-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424283, '0031643', 'FILE', '2003-04-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424284, '0031643', 'FILE', '2001-03-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424285, '0031643', 'FILE', '2001-01-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424286, '0031643', 'FILE', '1999-03-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424287, '0031643', 'FILE', '1998-05-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424288, '0031643', 'FILE', '1998-02-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424289, '0031643', 'FILE', '1997-02-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424290, '0031643', 'FILE', '1996-05-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424291, '0031643', 'FILE', '1996-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424292, '0031643', 'FILE', '1996-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424293, '0031643', 'FILE', '1996-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424294, '0031643', 'FILE', '1993-02-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424295, '0031643', 'FILE', '1992-04-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424296, '0031643', 'FILE', '1991-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424297, '0031643', 'FILE', '1991-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424298, '0031643', 'FILE', '1991-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424299, '0031643', 'FILE', '1988-02-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424300, '0031643', 'FILE', '1987-04-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424301, '0031643', 'FILE', '1986-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424302, '0031643', 'FILE', '1985-02-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424303, '0031643', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424304, '0031643', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424305, '0031643', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424306, '0031643', 'FILE', '1984-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (424307, '0031643', 'FILE', '1980-07-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5706124, '0031643', 'FILE', '2004-05-05 11:35:43', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8122051, '0031643', 'FILE', '2008-02-14 11:57:16', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8875342, '0031643', 'FILE', '2009-06-18 11:20:27', null)""",
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
                    ('0031643', null, 'BC', '1959-01-23 00:00:00', '2009-01-23 00:00:00', '2006-02-15 16:10:48', null, null, null, 'JWOOZMAQ', 'HWXBZCKD', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0031643', 424281, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0031643', 'CO', 424281, 0, null, 'SDDXOWPXSXNTSMHZXHAM', 'VWTYCDFSUOSUWOF POIQVHLED', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0031643', 'RG', 9241789, null, 7534923, 7534923, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0031643', 'RC', 9241789, null, 7534923, 7534923, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0031643', 'RG', 424281, 6889406, 155617, 155617, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0031643', 'RC', 424281, 6889406, 155617, 155617, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0031643', 'RC', 6889406, 9241789, 3982724, 3982723, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0031643', 'RG', 6889406, 9241789, 3982726, 3982725, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (155617, 'BC', 'CA', 'FTTSY2', 'YPZBLLCUPNNUXQVKSILSRQWQO', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (155618, null, null, 'W8XKKR', 'TJXXDEZKCGYYHSML RMEWEIWV', 'VDUOHV AFLFRI WTXYWRVGTEN', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (155619, null, null, 'QYZNWM', 'LJHOGJZUZZYILZOIQSHRZCRVO', 'PVGHFD XRDFTYFH JASCJLMYG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982665, 'BC', 'CA', 'QZOGOX', 'AUOMYABSJLIMUFXCOVGTWLBSU', null, null, 'CRANBROOK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982721, 'BC', 'CA', 'WYLE3N', ' TNKHGGSFPASMKXPH GJGQ AQ', null, null, 'CRANBROOK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982722, 'BC', 'CA', 'QHG06P', 'DCDXZPYUFLHDZPQEXGMJZDKFB', null, null, 'CRANBROOK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982723, 'BC', 'CA', 'IW8FKI', 'HFLECYQLAGFHKEKBIOZUJAFTK', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982724, 'BC', 'CA', 'X4TUSK', 'URDDYJXFCFTMEFS  MPBYUMPN', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982725, 'BC', 'CA', '9U1T0R', 'UFFT UJDU UJH GBGKMLUUSXB', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3982726, 'BC', 'CA', 'S6ZQKU', 'QS DXCSQHEWTDGLMHDWCUOHC ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534923, 'BC', 'CA', 'ODPA3G', 'CFSYY FGDIZYJVVBMTXHOMGQW', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_8004306': {
            "corp_num":'8004306', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511446, 7537108, null, '8004306', 'INC', 9242902, null, null, null, null, null, null, 'Phillips', null, 'Tashia', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511447, 7537110, 7537111, '8004306', 'DIR', 9242902, null, null, null, null, null, null, 'Yearwood', 'V', 'Jen', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242902, '8004306', 'FILE', '2018-07-24 13:47:53', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242902, 'ICORP', '2018-07-24 13:47:53', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('8004306', null, 'BC', '2018-07-24 13:47:53', null, null, null, null, null, 'HYHJDSOZ', 'FAAJYHZI', 'EFUMCTWWCGZA@YZUTBLIC.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8004306', 9242902, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('8004306', 'NB', 9242902, 0, null, 'XWCXQRJHLIHBQDHASIFA', 'UMHNWWYQ XFIB EMEENWKMOGA', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8004306', 'RG', 9242902, null, 7537113, 7537112, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8004306', 'RC', 9242902, null, 7537115, 7537114, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537108, 'BC', 'CA', 'VLASTD', 'OVWXYAVQQ IZUKKJJVIJTKCRJ', null, null, 'Sidney', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537110, 'SK', 'CA', 'SPCI4R', 'KSCYVFDLGIPUKN KUO AKMLAB', null, null, 'Moose Jaw', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537111, 'SK', 'CA', 'ZEJ8B1', 'XAQSLCQJQYDDMQGMOKCDBJWDA', null, null, 'Moose Jaw', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537112, 'BC', 'CA', 'F7L4JF', 'YWBNJOOIOVNRYKYSSXAQBQRWJ', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537113, 'BC', 'CA', 'GA3H78', 'GOCBYLBQISESMVD RYAFKYLPD', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537114, 'BC', 'CA', 'V2H8QW', 'UAQBMLMLVJ ZEBPNZRIHUBJC ', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537115, 'BC', 'CA', 'BZ3XQL', 'FWJYYRAJKOQHPHYAR UJOYWRH', null, null, 'Osoyoos', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_3394994': {
            "corp_num":'3394994', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":1, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511442, 7537095, null, '3394994', 'INC', 9242901, null, null, null, null, null, null, null, null, null, 'XWCSMM NBSTLDOKGOYTW', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511443, 7537097, 7537098, '3394994', 'DIR', 9242901, null, null, null, null, null, null, 'Nobu', null, 'Aiki', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511444, 7537099, 7537100, '3394994', 'DIR', 9242901, null, null, null, null, null, null, 'Ubright', 'K.', 'Adrienne', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3511445, 7537101, 7537102, '3394994', 'DIR', 9242901, null, null, null, null, null, null, 'Johannsen', null, 'Gary', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242901, '3394994', 'FILE', '2018-07-24 13:39:06', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9242901, 'ICORP', '2018-07-24 13:39:06', null, null, null, null, 'N', null, null, 'F ', null, null, 'NR5634946', null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('3394994', null, 'BC', '2018-07-24 13:39:06', null, null, null, null, null, 'XXYAZODZ', 'UWPKZEFI', 'NCZEYSAKFHYD@TQIMRMMH.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3394994', 9242901, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('3394994', 'CO', 9242901, 0, null, 'ZQWNUYPUGIKTTBRPXLZH', 'LFOZMECZU WWNNNERLPNILVIZ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('3394994', 'TR', 9242901, 1, null, 'PTIGUAXHIANUFHRMVSBY', 'IO ZKATAELMFQ XBWSOMIDHVE', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3394994', 'RG', 9242901, null, 7537104, 7537103, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3394994', 'RC', 9242901, null, 7537106, 7537105, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537095, 'BC', 'CA', 'Z3JXGH', 'WVUNCADRXTC HQLVRPD U H A', 'JBPJHHK PJMJOACSNWZGOTOFV', null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537097, 'BC', 'CA', 'LTE6QW', 'MXBTYQFZVEHBQNNGMUMYKHQLI', null, null, 'Whistler', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537098, 'BC', 'CA', 'MX58SL', 'KY FWZCMSMSJOHYAJZJOAXJDR', null, null, 'Whistler', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537099, 'BC', 'CA', 'XERTU2', 'DOEDLTYUAFPLHZDSWCCUQPMHZ', null, null, 'Whistler', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537100, 'BC', 'CA', 'O176OP', 'DIGLDMLCYGZBMX TSVVNNRYCG', null, null, 'Whistler', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537101, 'BC', 'CA', 'F3LPXG', 'TOHOFXUDUSDBZSGUZONLSXYRW', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537102, 'BC', 'CA', 'PRY6H5', 'HJWGAYEZPSILQC ZDUQEFBTTS', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537103, 'BC', 'CA', 'E905HV', 'XBFVPIIMCVMNRRRBFKWUNXVLV', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537104, 'BC', 'CA', 'X3TJ86', 'MEBOYRSEMAVEZBJZBTSCVPNBZ', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537105, 'BC', 'CA', 'NNTS41', 'EQDHSMWB AIUKEMWQTNDH JMI', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7537106, 'BC', 'CA', 'BPYO1F', 'ALJXZRIMQACO HMXZNGMACBNO', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM6895313': {
            "corp_num":'FM6895313', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682496, null, null, 'FM6895313', 'FBO', 105301928, null, null, null, null, '2001-05-09 14:36:16', null, null, null, null, 'A0031179DTTPVPZPYUPPZBRRDZMO', 'A7542403', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721467, 'FM6895313', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301928, 'FM6895313', 'CONVFMACP', '2001-05-09 14:36:16', null)""",
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
                    ('FM6895313', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM6895313', 104721467, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM6895313', 'CO', 104721467, 0, null, 'LGRWPVZUTISQZQEXTTFB', 'DOVAIDVCIWJVORZFVBYUOIUVU', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
'corp_FM0708722': {
            "corp_num":'FM0708722', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105755067, null, null, 'FM0708722', 'FBO', 104799510, null, null, null, null, '2003-09-17 00:00:00', null, null, null, null, '0614205HUROSB QXAHKDKQVTOAN', '1839629', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104799510, 'FM0708722', 'CONVFMREGI', '2003-09-17 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104799510, 'FRREG', '2003-09-17 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM0708722', null, 'SP', '2003-09-17 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2003-09-17 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM0708722', 104799510, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM0708722', 'CO', 104799510, 0, null, 'DEKRLFPBKYRLURJVNTRN', 'VUBYEHJRZRYHPENYUBMMPGJFL', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
'corp_A8373673': {
            "corp_num":'A8373673', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510870, 7535969, 7535968, 'A8373673', 'ATT', 9242684, null, 148741, null, null, null, null, null, null, null, 'BC0121625OHOBMKDCFJEPJU YJN G', 'BC0605157', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148741, 130138, 130138, 'A8373673', 'ATT', 364974, 9242684, null, null, null, null, null, 'GIFFORD ', null, 'MARTIN N.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148742, 130139, 130139, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'BEALE', null, 'MARK S.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148743, 130140, 130140, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'BEATTIE', null, 'IAN J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148744, 130141, 130141, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'BRAY', null, 'TIMOTHY J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148745, 130142, 130142, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'BROWN', null, 'KEITH C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148746, 130143, 130143, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'COVINGTON', null, 'HOWARD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148747, 130144, 130144, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'KIRK', null, 'ANNA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148748, 130145, 130145, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'LEWIS', null, 'RICHARD D.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148749, 130146, 130146, 'A8373673', 'OFF', 364974, null, null, null, null, null, null, 'NEW STAR ASSET', null, 'MANAGEMENT LTD.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148750, 130147, 130147, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'RUVIGNY', null, 'RUPERT F. J.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148751, 130148, 130148, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'SANDERS', null, 'CHRISTIE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148752, 130149, 130149, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'SANDERS', null, 'MICHELLE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (148753, 130150, 130150, 'A8373673', 'DIR', 364974, null, null, null, null, null, null, 'WEEKES', null, 'DEBORAH J.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6450564, 'A8373673', 'FILE', '2005-07-26 08:35:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6472092, 'A8373673', 'FILE', '2005-08-05 10:18:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7251378, 'A8373673', 'FILE', '2006-08-22 10:31:55', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7785800, 'A8373673', 'FILE', '2007-07-25 08:53:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7789158, 'A8373673', 'ADCORP', '2007-07-26 14:39:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242684, 'A8373673', 'FILE', '2017-04-04 16:19:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364974, 'A8373673', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364975, 'A8373673', 'FILE', '2003-08-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364976, 'A8373673', 'FILE', '2002-08-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364977, 'A8373673', 'FILE', '2002-08-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364978, 'A8373673', 'FILE', '2002-02-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364979, 'A8373673', 'FILE', '2002-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364980, 'A8373673', 'FILE', '2002-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364981, 'A8373673', 'FILE', '2001-11-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364982, 'A8373673', 'FILE', '2001-11-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364983, 'A8373673', 'FILE', '2001-11-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364984, 'A8373673', 'FILE', '2000-07-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364985, 'A8373673', 'FILE', '1999-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364986, 'A8373673', 'FILE', '1999-08-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364987, 'A8373673', 'FILE', '1999-08-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364988, 'A8373673', 'FILE', '1999-08-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364989, 'A8373673', 'FILE', '1998-11-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364990, 'A8373673', 'FILE', '1998-08-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364991, 'A8373673', 'FILE', '1998-03-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364992, 'A8373673', 'FILE', '1998-03-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364993, 'A8373673', 'FILE', '1997-12-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364994, 'A8373673', 'FILE', '1997-11-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364995, 'A8373673', 'FILE', '1997-11-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364996, 'A8373673', 'FILE', '1994-05-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364997, 'A8373673', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364998, 'A8373673', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (364999, 'A8373673', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5796928, 'A8373673', 'FILE', '2004-07-12 08:41:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8343436, 'A8373673', 'FILE', '2008-07-03 10:43:14', null)""",
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
                    ('A8373673', null, 'A', '1994-05-17 00:00:00', '2008-05-17 00:00:00', null, null, null, null, 'RJGJGMET', 'ARVENBPO', 'EEGTHCSIOGHY@YVQFNNDY.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A8373673', 364974, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A8373673', 364974, 5796928, null, 'OT', 'COR', '1985-01-23 00:00:00', 'ENGLAND', null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A8373673', 5796928, 6450564, null, 'OT', 'COR', '1985-01-23 00:00:00', 'ENGLAND', '1880176', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A8373673', 6450564, null, null, 'OT', 'COR', '1985-01-23 00:00:00', 'GB', '1880176', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A8373673', 'CO', 364974, 0, 364997, 'PQCZXWFFDWTLQYLCXNLU', 'LTZHRWYV  BVASUR YVLEERIP', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A8373673', 'CO', 364997, 0, 364998, 'XDHFFAGRUVRNJCOXDCLQ', 'RDCYAFOECRBROCUJPZDAMODHV', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A8373673', 'CO', 364998, 0, 364999, 'STOFKNTOLHBUYYKOXEVT', 'DBRHMTBOKQBQWJYGVRWCODGXC', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A8373673', 'CO', 364999, 0, null, 'LQEDMZFYJZGCWJYHNUPK', 'MCXGRFIUSWXRHRIWR KFQEFID', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A8373673', 'HD', 364974, 6450564, 130137, 130137, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A8373673', 'HD', 6450564, null, 3185044, 3185043, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130137, null, null, null, 'P HXRMBPWVAAHTEMGGTYENGVU', 'EIFSJHYZUUTMIRLARGGOJTQEZ', 'WC1B 4HP', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130138, null, null, 'Q6AEBE', 'RAEWIMYJZBYIOEQEUKM QRK R', 'DWYKZEQRWGCWYAXBP WKKMSDN', 'VANCOUVER BC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130139, null, null, null, 'SQOMLLFHUBMQAZYFOHAEDJNAT', 'OYGHHFK F QWAY NUNSKLHCCR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130140, null, null, null, 'FXJPVEFMXAHGFTEFBLKBVEBWS', ' WQZDNCOJBIKWWPRFPVCCVZFM', 'SOUTH BUCKS UK SL2 3EN', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130141, null, null, null, ' KLZYUUMBZMSYYHRFRZCGTESP', 'IRWQIMQKYRVZGKWBKYSBZHHEV', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130142, null, null, null, 'SWGD LTDHQCTCGYOGTXQHPBFI', 'UK JWIEEEALGGYLUIFKDBENHT', 'UK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130143, null, null, null, 'XXSBLGOFTTHSKRRCF CIRYWWJ', 'IQURBGCTGOTXQ MCCGVSJICCS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130144, null, null, null, 'LOUCBKZZYELOLBPA PFBRFDVV', 'ZTQJRCJWVNYHKWSICXTHATTVS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130145, null, null, null, 'NUQRNKFUEIMNQBCFKIOAJOTZ ', 'TXDUMBCQUXHLPAIYCYIMXTWDK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130146, null, null, null, 'QXDNUTCJQHBABGGNFRQGNNPKR', 'LHVYQIMYYMCSZVXBISFMHTJKR', 'SW1X 7NE', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130147, null, null, null, 'FYPL XMJUWHUQFDEUUU AXWHA', 'QQLNXJPMQTXRISKNL HQMW DA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130148, null, null, null, 'RTRBHGSFIACQ ZHYTJULPYLGS', 'YAZJLDGNKEV VCDGLYNMYIWDZ', 'HERTFORDSHIRE  UK HP1', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130149, null, null, null, 'WQZMZGLFYDQW WRM EHBSQLHY', 'RBGKELTYSEDTARFDTLHHUBZXM', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (130150, null, null, null, 'ARCVPUXJQWFKZILQCDHNAHQDC', 'VILLEY MLYGNUGHT RBYYWVGH', 'HORDON ON THE HILL ESSEX UK ESSEX UK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3185043, null, 'GB', 'WLV77X', 'HDLZHAILLLYDIJPZRBTBVYFXE', null, null, 'LONDON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3185044, null, 'GB', 'ICKZYJ', 'XMXYIXJGGLCTLEGIKDGSLKD Q', null, null, 'LONDON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535968, 'BC', 'CA', 'VBJ1M1', 'DYZOAYSZKNYNOLYB BVSD XZZ', null, null, 'Vancouver', 'FOR', 'NDSWLBM JRDGTPUJQBEQAWHIDUXTQPPCYNDMFLBZ', 'ALAFDCBJDPOBCMVPLISA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535969, 'BC', 'CA', 'NJ66W8', 'DPGFAZNOMGVQZEUSZUNDURHFG', 'HYSDRWKZTHOBPOQSKTGETBWFV', null, 'Vancouver', 'FOR', 'KNRJSMXRDOGRJVXNQPIVMKYUGJHHIAKZRTXMXQYZ', 'TWWPKUBK TWWLXVKBZZC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_8451586': {
            "corp_num":'8451586', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037327, 2494013, null, '8451586', 'INC', 6074785, null, null, null, null, null, null, null, null, null, 'CNDZVUXXWCIVOIEAQU R', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037328, 2494015, 2494016, '8451586', 'DIR', 6074785, 8431719, null, null, null, null, null, 'TINGLEY', 'H.', 'CALEB', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037329, 2494017, 2494018, '8451586', 'DIR', 6074785, 7163282, null, null, null, null, null, 'HUQ', 'E.', 'MOHAMMED', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2037330, 2494019, 2494020, '8451586', 'DIR', 6074785, 8431719, null, null, null, null, null, 'TSE', 'Y.', 'GARY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2524514, 4564167, 4564166, '8451586', 'DIR', 7163282, 8431719, 2037329, 'C', null, null, null, 'HUQ', 'E.', 'MUHAMMED', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539790, 4611323, 4611323, '8451586', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539791, 4611324, 4611324, '8451586', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539792, 4611325, 4611325, '8451586', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2539793, 4611326, 4611326, '8451586', 'OFF', 7195364, 7617777, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732684, 5211601, 5211601, '8451586', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732685, 5211602, 5211602, '8451586', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732686, 5211603, 5211603, '8451586', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2732687, 5211604, 5211604, '8451586', 'OFF', 7617777, 8431717, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123758, 6408221, 6408221, '8451586', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123759, 6408222, 6408222, '8451586', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123760, 6408223, 6408223, '8451586', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123761, 6408224, 6408224, '8451586', 'OFF', 8431717, 8782837, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123763, 6408228, 6408227, '8451586', 'DIR', 8431719, null, 2037330, null, null, null, null, 'TSE', 'Y.', 'GARY', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123764, 6408230, 6408229, '8451586', 'DIR', 8431719, null, 2524514, null, null, null, null, 'HUQ', 'E.', 'MUHAMMED', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3123765, 6408232, 6408231, '8451586', 'DIR', 8431719, null, 2037328, null, null, null, null, 'TINGLEY', 'H.', 'CALEB', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288226, 6882402, 6882402, '8451586', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'E.', 'Howard', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288227, 6882403, 6882403, '8451586', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Tse', 'Y.', 'Gary', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288228, 6882404, 6882404, '8451586', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Huq', 'E.', 'Muhammed', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3288229, 6882405, 6882405, '8451586', 'OFF', 8782837, null, 0, null, null, '2006-07-17 08:39:28', null, 'Pechet', 'T.', 'Jason', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6074785, '8451586', 'FILE', '2005-01-17 14:57:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7163282, '8451586', 'FILE', '2006-06-26 09:55:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7195364, '8451586', 'FILE', '2006-07-17 08:39:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7617777, '8451586', 'FILE', '2007-04-16 11:58:57', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242595, '8451586', 'FILE', '2016-08-25 15:24:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8431717, '8451586', 'FILE', '2008-09-03 12:36:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8431719, '8451586', 'FILE', '2008-09-03 12:37:09', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8782837, '8451586', 'FILE', '2009-04-20 14:34:23', null)""",
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
                    ('8451586', null, 'BC', '2005-01-17 14:57:58', '2009-01-17 00:00:00', null, null, null, null, 'FZAQXBCD', 'XCXSIPBL', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8451586', 6074785, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('8451586', 'CO', 6074785, 0, null, 'RIQATNGRWDHRASCBHTIZ', 'PWHIFFMQFDOJPBRYTMXORJBKD', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8451586', 'RG', 9242595, null, 7535791, 7535790, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8451586', 'RC', 9242595, null, 7535791, 7535790, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8451586', 'RG', 6074785, 9242595, 2494022, 2494021, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8451586', 'RC', 6074785, 9242595, 2494024, 2494023, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494013, 'BC', 'CA', 'VC2PB5', 'PSZXJUFIADGETAMMKZQRZLJPL', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494015, 'BC', 'CA', 'ALWI6U', 'FWKOA ARBOA ADDNGFSRSARPZ', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494016, 'BC', 'CA', 'RI4650', 'TUCZVAEQDKBGBJGTANA OVZRZ', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494017, 'BC', 'CA', '18TWFB', 'FSYVYSLSYJZVRAYFSUCCTFFRI', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494018, 'BC', 'CA', 'XJ24XI', 'HISERXTZBSAWGRTNIOQ UZJK ', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494019, 'BC', 'CA', '41SVHI', 'KQOCZLXMQL UEATUBVGRMIRAT', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494020, 'BC', 'CA', '6ARQKS', 'WDNGZNYNQORZPOCQLSPOF YYF', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494021, 'BC', 'CA', 'JXQ4KU', 'OSOQBMDDPRLPCRPFDGQYNGPWG', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494022, 'BC', 'CA', '4QOUV6', 'SPVT DVOEDMYGCXMLQEWXSAYO', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494023, 'BC', 'CA', 'X67AA8', 'FGAZRFYQBPQOZGEAYIULERXRE', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2494024, 'BC', 'CA', 'DKC26Y', 'XKOAVEMXYFYCPSANDAOXEVACZ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4564166, 'BC', 'CA', 'LTOU4M', 'PJG UXRQY YEOXYTLWTGXPTAA', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4564167, 'BC', 'CA', 'SKAZLU', 'QSIYDWBKKSVWAURD DNOPF LU', null, null, 'RICHMOND', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4611323, 'BC', 'CA', 'TMYJ5D', 'SWADWORYOJLHFDDLPTVASCWEA', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4611324, 'BC', 'CA', '4T035H', 'TKQZZAT KIXHEIPWZZIBTSMRL', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4611325, 'BC', 'CA', '9LOU13', 'ODTCDEOYVJAXTWJIRKYBEROHC', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4611326, 'BC', 'CA', 'ELEIHU', 'IZFDXHVKIYMQ WWAIROYLLARY', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5211601, 'BC', 'CA', 'HA6QUF', 'GBHSGFXHENWKLTXOLWSE HYIQ', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5211602, 'BC', 'CA', '68XCRU', 'HQ IPBCEIYAHFAUPURGWUCBMK', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5211603, 'BC', 'CA', 'MRWIAU', 'AIMFTLNYZLXXGCTLWT PSMCFQ', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5211604, 'BC', 'CA', 'NNA7ZT', 'LXFEUWBYLKHMMGZGYWLK TBAE', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408221, 'AB', 'CA', 'PWCGJ3', 'OKXTCBFMVKKCHPQYPEWMELBGM', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408222, 'AB', 'CA', 'V9PBSC', 'DJWFYFPYKGSPNQQWVZ ZOBZGK', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408223, 'AB', 'CA', 'C0EP8N', 'HKCJAKVNCX JVOPV GWGPSKDH', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408224, 'AB', 'CA', 'HPOK8Y', 'UENMEJZJYFNTUVIDES T D SZ', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408227, 'AB', 'CA', '8S7INX', 'IAIWWJLMJTAIGNEESCJRXXGTU', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408228, 'AB', 'CA', 'FCZ1SC', ' QWJIOS HUTIODHBLT  LVUEI', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408229, 'AB', 'CA', 'GQR68O', 'VSX MMQYQTHU BSNDGRTIMZUK', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408230, 'AB', 'CA', 'ZTNEL8', 'KLCWTHIBB  DHXPV FLYDLULT', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408231, 'AB', 'CA', 'F9AQAT', 'RDLJCYDTDDXNMNGXGKUUHXHKR', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6408232, 'AB', 'CA', 'ZAUXNV', 'NWSIRDYDABWYCPMW  OQTNOFE', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6882402, 'AB', 'CA', 'BJ59DH', 'EBUTJF BADM XBF RBAPH LFX', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6882403, 'AB', 'CA', 'IT59PQ', 'XAXJZSW LPIVLXUEUFXHEDFRI', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6882404, 'AB', 'CA', '5KVHS5', 'ZUSWONQZKYUKVUXFMQJWABNHY', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6882405, 'AB', 'CA', '73KYLT', 'OPVKQSRLXHSFSY K CRICDBTU', null, null, 'Edmonton', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535790, 'BC', 'CA', 'MI5BAR', 'VOSRCJVRIZDNYBQZKXLONXGPA', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535791, 'BC', 'CA', 'EJS59G', 'VDDJRKRXFYKQZTHBXHEWFKHUJ', 'ZMRQSWAXIHKTMYQTFSZK JCXK', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_7633478': {
            "corp_num":'7633478', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":2, "party_addr_ct":2, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2559124, 4671453, null, '7633478', 'INC', 7237318, null, null, null, null, null, null, 'Rudy', 'E.', 'Brian', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2559125, 4671455, 4671456, '7633478', 'DIR', 7237318, 7926270, null, null, null, null, null, 'Griffiths', null, 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2874884, 5643096, 5643096, '7633478', 'OFF', 7926259, 9104380, 0, null, null, '2007-10-19 11:41:25', null, 'Griffiths', 'A.', 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2874892, 5643120, 5643119, '7633478', 'DIR', 7926270, null, 2559125, null, null, null, null, 'Griffiths', null, 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3451936, 7352471, 7352471, '7633478', 'OFF', 9104380, 9104388, 0, null, null, '2007-10-19 11:41:25', null, 'Griffiths', 'A.', 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3451937, 7352473, 7352473, '7633478', 'OFF', 9104388, null, 0, null, null, '2007-10-19 11:41:25', null, 'Griffiths', 'A.', 'Jerome', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105538816, 103490415, null, 'FM9425722', 'FBO', 104880184, null, null, null, null, '2006-08-16 00:00:00', null, null, null, null, '0765995QUCLUJBQGKFIMW Y RQV', '7633478', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105552151, 103503750, null, 'FM2030203', 'FBO', 104893496, null, null, null, null, '2007-02-14 00:00:00', null, null, null, null, '0765995EOSMVNNTJV  UONQGG U', '7633478', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7237318, '7633478', 'FILE', '2006-08-14 13:40:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7926259, '7633478', 'FILE', '2007-10-19 11:41:25', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7926270, '7633478', 'FILE', '2007-10-19 11:43:10', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242244, '7633478', 'FILE', '2015-07-28 14:46:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9104380, '7633478', 'FILE', '2009-11-24 08:40:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9104388, '7633478', 'FILE', '2009-11-24 08:42:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104880184, 'FM9425722', 'CONVFMREGI', '2006-08-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104893496, 'FM2030203', 'CONVFMREGI', '2007-02-14 00:00:00', null)""",
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
                    ('7633478', null, 'BC', '2006-08-14 13:40:33', '2009-08-14 00:00:00', null, null, null, null, 'DFYHGEBG', 'VNEHHPPQ', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9425722', null, 'SP', '2006-08-16 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1095915, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM2030203', null, 'SP', '2007-02-14 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1114375, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('7633478', 7237318, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9425722', 104880184, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM2030203', 104893496, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('7633478', 'CO', 7237318, 0, null, 'LPZBSFJOUFFPMRGQXOUP', 'NZXJAQLKDFLGNHQFH CBEDEQH', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9425722', 'CO', 104880184, 0, null, 'FVGHQDCUJIUHHLDVAZMJ', 'LRYYJNOJO YRSIVSAPEEDTVGQ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM2030203', 'CO', 104893496, 0, null, 'WAAWCAJCPCGPOYBRINDB', 'CLCB FDEFA SV IUPWRPSHAHR', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7633478', 'RG', 7237318, 9242244, 4671463, 4671462, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7633478', 'RC', 7237318, 9242244, 4671465, 4671464, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7633478', 'RG', 9242244, null, 7535378, 7535378, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('7633478', 'RC', 9242244, null, 7535378, 7535378, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9425722', 'FO', 104880184, null, 103155280, 103155280, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM2030203', 'FO', 104893496, null, 103180754, 103180754, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671453, 'BC', 'CA', '08WVR1', 'THIQJRFJDOZHLONHVEXEYIW S', 'UAPA CXAGLEBWFVEHYBFHACEF', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671455, 'BC', 'CA', 'HJ88HV', 'B BHYHHTGPFASQIKK  PZNZIJ', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671456, 'BC', 'CA', 'MNRAR4', 'SSFDORKXYKBIAEPEBJNRP PWC', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671462, 'BC', 'CA', 'NP7341', 'HZXDITLIPMCGMULVCFVBBC OK', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671463, 'BC', 'CA', 'Q04E8A', 'VN EZPCXBBXCQZE G ORCPTMS', 'XKZVZDYGAHVOUINZFCRNEXLRA', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671464, 'BC', 'CA', 'G18I2V', ' YXAPOJOGRKGIQEKBHMGFFYS ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4671465, 'BC', 'CA', 'AL7D1Q', 'DYZOCBAIFUABUTPANOEUCHDSW', 'VVKBWHUFORNOGWDMZLUR JQGG', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5643096, 'BC', 'CA', '1CA3HF', 'JNOKDAKOMCKIRQMRUHDJWCRZX', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5643119, 'BC', 'CA', '4H59L8', 'QCRRXBHUKEVNWIEZKNQNMWFJR', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5643120, 'BC', 'CA', '5A2C1P', 'TOYYDTHGEGLDPPNZNHOTFXNNW', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7352471, 'BC', 'CA', 'H91A8V', 'EOM ORRZSUAPNCBMLJAQYZAMS', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7352473, 'BC', 'CA', 'EEQWZV', 'ZPHHIKSWXZBBUFNM ADNOSPRY', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535378, 'BC', 'CA', 'KURA0I', 'FZICBIOKWUQOJJYAVRSNZ FV ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103155280, 'BC', 'CA', 'O6W7V4', null, null, null, 'DELTA', 'BAS', 'JGJGVNOZIPHHOOEIUJMEORCLBZHSWJOURFREXQVI', 'BAJPQEBHPLZICZBFUIXA', null, null, null, '403', null, 'FFHLJPZVIUUQTBP', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103180754, 'BC', 'CA', 'AX08NY', null, null, null, 'DELTA', 'BAS', 'UBLLVTXVTJVDRODOBDOSPZAUWEKAZCEQDFNRXNHF', 'TPAEZNALEUVF YAPPBUR', null, null, null, '101', null, 'RVXVDUSQYENVDPC', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103490415, 'BC', 'CA', '1Q8QI9', 'HXYJBSMODCLVFZGKPRZPORKIE', null, null, 'VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103503750, 'BC', 'CA', 'TJNGVA', 'HIRS XPYOCVKLU QRLZAQQAGW', null, null, 'VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_8793129': {
            "corp_num":'8793129', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":2, "party_addr_ct":2, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3058561, 6215114, null, '8793129', 'INC', 8302204, null, null, null, null, null, null, 'Rudy', 'E.', 'Brian', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3058562, 6215116, 6215117, '8793129', 'DIR', 8302204, null, null, null, null, null, null, 'Wolf', null, 'Oliver', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3058563, 6215118, 6215119, '8793129', 'DIR', 8302204, null, null, null, null, null, null, 'Livingstone', null, 'Robert', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3422392, 7264415, 7264415, '8793129', 'OFF', 9038795, null, 0, null, null, '2009-10-14 10:46:35', null, 'Livingstone', null, 'Robert', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3422393, 7264416, 7264416, '8793129', 'OFF', 9038795, null, 0, null, null, '2009-10-14 10:46:35', null, 'Wolf', null, 'Oliver', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604136, 103555735, null, 'FM9959091', 'FBO', 104943462, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071JIJOHFBZHFAUOYSACRK ', '8793129', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105604099, 103555698, null, 'FM8398011', 'FBO', 104943427, null, null, null, null, '2008-12-08 00:00:00', null, null, null, null, '0827071QFSRFYZNZOBTPRBHQBCM', '8793129', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242377, '8793129', 'FILE', '2015-07-28 14:46:36', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8302204, '8793129', 'FILE', '2008-06-06 10:49:31', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9038795, '8793129', 'FILE', '2009-10-14 10:46:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943427, 'FM8398011', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104943462, 'FM9959091', 'CONVFMREGI', '2008-12-08 00:00:00', null)""",
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
                    ('8793129', null, 'BC', '2008-06-06 10:49:31', '2009-06-06 00:00:00', null, null, null, null, 'QRHUUQRJ', 'NRMICDLP', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM8398011', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186186, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM9959091', null, 'SP', '2008-12-08 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, 1186243, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8793129', 8302204, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM8398011', 104943427, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM9959091', 104943462, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('8793129', 'CO', 8302204, 0, null, 'XIGLTQCTPRALZFMIJORY', 'DAQHZZEXYJJPPUPSKQEUCDTNS', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM8398011', 'CO', 104943427, 0, null, 'QJOFXMJYVSWDAFSWXTHE', 'RAZGXQLSVBVCDPNQPCCCPVHXC', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM9959091', 'CO', 104943462, 0, null, 'WGQGOZOGVDQQBADRWEFT', 'RMPUIUURPHGDDOPA MDOJRTFE', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8793129', 'RG', 8302204, 9242377, 6215121, 6215120, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8793129', 'RC', 8302204, 9242377, 6215123, 6215122, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8793129', 'RG', 9242377, null, 7535511, 7535511, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8793129', 'RC', 9242377, null, 7535511, 7535511, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM8398011', 'FO', 104943427, null, 103280174, 103280174, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM9959091', 'FO', 104943462, null, 103280246, 103280246, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215114, 'BC', 'CA', 'HAEVDK', 'LUN CUICVGHUPWZILIFRSXTBK', 'FMBPZQJREY VXOVZDAZDGNYDX', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215116, 'BC', 'CA', 'HBU9FO', 'UMBWQLHFBYSOVVQOVEDPYSZHB', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215117, 'BC', 'CA', 'DU2EKD', 'FWFZHJJDA IIWXAW EHLPEUWD', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215118, 'BC', 'CA', '10O14G', 'YSBVWCDPPPAJYPKNBVJGXUYMO', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215119, 'BC', 'CA', 'OC2186', 'ITNQTZAWZDLVVIPYFANTHREGJ', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215120, 'BC', 'CA', '8GVX0P', 'CBZGCJWCLHZBGWDZHFWVYG A ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215121, 'BC', 'CA', '9MTT3Q', ' FWXKPUNPVVOFBVLIQXHFHQRT', 'KUHS PCCUZHBOZHVROEMTIYIP', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215122, 'BC', 'CA', 'CLSAXZ', 'DNDAPCYXXHBFPWBQUONDSLZDL', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6215123, 'BC', 'CA', '899QUV', 'LGE RRWHPYFWSFBWOOSGKLWAR', 'IZA WRIUFKHGYVGFTFWIGBZIT', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7264415, 'BC', 'CA', 'PECKXK', 'MJMBRM GJSSOVLYRMYMAITDYO', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7264416, 'BC', 'CA', 'W6422G', 'PAHQ XMNMWTYRCFOEGY TXG  ', null, null, 'Delta', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535511, 'BC', 'CA', '24ABPR', 'WVAFDZOKUPJBRKLGSRLZCVSVT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280174, null, 'CA', 'YT6RIT', 'NWDSGUWR QUCAFNJSYHBCOHHP', null, null, 'DELTA', 'FOR', 'PJFHSRVNRRDCGBBVYZDJYEBUMUNGVGHMZKNIJMGT', ' FJESQEZOYSSYRVBOXCU', null, null, null, '009', null, 'BUNFSMZAIWRHGKK', 'ST', null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103280246, null, 'CA', 'COH4CL', 'KJAOIENOBYAJPIYJKOJSGEATV', null, null, 'DELTA', 'FOR', 'NRTEQURKBXAFGTCAMPAFYEAFQCVELQKTUOAKTDMG', 'VBODIDVLYROZLKVPOUQR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103555698, 'BC', 'CA', 'R9XXU1', 'JUKCZWGMIEPNOPTKQRZTFBFWY', null, null, 'DELTA', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103555735, 'BC', 'CA', '7WP5M5', ' KVJLL NQPSWYLOKWAJQIONEN', null, null, 'DELTA', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_A6497538': {
            "corp_num":'A6497538', "corp_typ_cd":'A', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":1, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510880, 7535989, 7535988, 'A6497538', 'ATT', 9242694, null, 3027731, null, null, null, null, null, null, null, 'BC0121625 MMRKIKCKGJAGYXRFZH ', 'BC5550559', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245253, 215620, 215620, 'A6497538', 'ATT', 545718, 8241976, null, null, null, null, null, 'GIFFORD ', null, 'MARTIN N.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245254, 215621, 215621, 'A6497538', 'DIR', 545718, null, null, null, null, null, null, 'BERBIGIER', null, 'CLAUDE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245255, 215622, 215622, 'A6497538', 'DIR', 545718, null, null, null, null, null, null, 'FREUND', null, 'EDOUARD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245256, 215623, 215623, 'A6497538', 'OFF', 545718, null, null, null, null, null, null, 'GELFAND', null, 'BRAHM M.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245257, 215624, 215624, 'A6497538', 'DIR', 545718, null, null, null, null, null, null, 'KALAYDJIAN', null, 'FRANCOIS', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245258, 215625, 215625, 'A6497538', 'DIR', 545718, null, null, null, null, null, null, 'PICARD', null, 'GEORGES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (245259, 215625, 215625, 'A6497538', 'OFF', 545718, null, null, null, null, null, null, 'PICARD', null, 'GEORGES', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3027731, 6122711, 6122710, 'A6497538', 'ATT', 8241969, 9242694, null, null, null, null, null, null, null, null, 'UBEPUOBRKDDRQCNLF LT', null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6285155, 'A6497538', 'FILE', '2005-05-11 09:49:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7136415, 'A6497538', 'FILE', '2006-06-07 11:08:39', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7600204, 'A6497538', 'FILE', '2007-04-03 13:42:19', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242694, 'A6497538', 'FILE', '2017-04-04 16:19:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545718, 'A6497538', 'CONVREGST', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545719, 'A6497538', 'FILE', '2003-08-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545720, 'A6497538', 'FILE', '2002-08-13 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545721, 'A6497538', 'FILE', '2002-04-25 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (545722, 'A6497538', 'FILE', '2001-02-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5657325, 'A6497538', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5669443, 'A6497538', 'FILE', '2004-04-06 10:47:50', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8241969, 'A6497538', 'FILE', '2008-04-29 14:38:40', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8241976, 'A6497538', 'FILE', '2008-04-29 14:39:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8220338, 'A6497538', 'FILE', '2008-04-16 11:33:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8738911, 'A6497538', 'FILE', '2009-03-20 12:26:41', null)""",
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
                    ('A6497538', null, 'A', '2001-02-20 00:00:00', '2009-02-20 00:00:00', null, null, null, null, 'WZTLMZGI', 'AACEDKHU', 'NQKLNDCROARO@VBCFLGYA.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('A6497538', 545718, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A6497538', 5669443, 7600204, null, 'QC', 'COR', '1992-09-25 00:00:00', null, '2961-8923', null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A6497538', 545718, 5669443, null, 'QC', 'COR', '1992-09-25 00:00:00', null, null, null, null, null)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('A6497538', 7600204, null, null, 'QC', 'COR', '1992-09-25 00:00:00', null, '2961-8923', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A6497538', 'CO', 545718, 0, null, 'SCTMQKLANFHEXVZACYFW', 'TNXFP TBVTPC ZJQYXRMFIXHB', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('A6497538', 'NO', 5657325, 0, null, 'BEPQKCFCHUZNIRFVEYXV', 'W ALOEDUDXLEIWIH HDIGMAPZ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('A6497538', 'HD', 545718, null, 215619, 215619, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215619, 'QC', 'CA', 'KHQICY', 'FSDRY SXEOYZMTWAJGSEGKQPQ', 'FNWBCUSHTZELGNKOCYL PSBAV', null, 'MONTREAL', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215620, 'BC', 'CA', 'EO8KXJ', 'HNWS BTGVSJNVTUPSGKWPWXTR', 'H CYUIGTHFXS TMSXORZ PWDB', 'ROBSON COURT, 1000-840 HOWE ST.', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215621, null, null, null, 'WBXSJA XEZIKVRXFMDCAFXVNK', 'SOVMWIZGKJPCFCWANBYAVYEJW', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215622, null, null, null, 'JWALQDWZEGVDNXBZPLNXQVPSE', 'YMABKQJEHZWNFQYXOT ZENTRE', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215623, null, null, 'A6LYKE', 'ZGTVAHPKUJCULZXDERRCFNSCE', 'ZHSJR DOQLRXZGIPQYLABWAPF', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215624, null, null, null, 'XHJTDROI EVCF QPXFVKSJJQV', ' TUPNSBBTWVIJXDLOQYFP ZE ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (215625, null, null, null, 'IAIAEZOZMWJHPIIJXBRGKTATI', 'TKMZGLCDGQR OJHILASOEJFMT', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6122710, 'BC', 'CA', '1IND6G', 'ITPXDTBMIWCRDAZQWBVUMKIEI', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6122711, 'BC', 'CA', 'X3SCJG', 'WEV CUXV S  FXDXBBKRAQUHL', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535988, 'BC', 'CA', '57FXWN', 'OAJWBTFGYPAEFPMTAVSVMVL X', null, null, 'Vancouver', 'FOR', 'GYGKUNAXUKADIDNJSBIJLLUDXFCGWPVVUGKYLFCM', 'GHURMIMUOZZJWWZOJSOT', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535989, 'BC', 'CA', 'W7F25G', 'OAUXNOKQGGJAWRRNSDYWGQ FL', 'YHLCUOYNRLTQWJCFVTKXEXUEI', null, 'Vancouver', 'FOR', 'YZVFHDK OLAOF CEWFOQ XYJOXDRJUFF ALJXNQF', 'SNTGFZKUDAQBDVOXHYCS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_C1208664': {
            "corp_num":'C1208664', "corp_typ_cd":'CUL', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":1, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361183, 103465149, null, 'FM0538567', 'FBO', 111258287, 111258289, 108361179, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156LZDFXZTFTNVBERE VI C', 'C1208664', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510631, 7534072, 7534073, 'C1208664', 'DIR', 9236428, null, null, null, null, null, null, 'test', null, 'test', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361175, 103465149, null, 'FM0538567', 'FBO', 111258283, 111258285, 105513550, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156JGYUEWFLN AHIVSSFUHO', 'C1208664', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361179, 103465149, null, 'FM0538567', 'FBO', 111258285, null, 108361175, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156ILONAOXMEADYBRFWSERY', 'C1208664', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236428, 'C1208664', 'FILE', '2012-02-17 15:29:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236430, 'C1208664', 'FILE', '2012-02-17 16:04:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236431, 'C1208664', 'FILE', '2012-02-17 16:06:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9236429, 'C1208664', 'FILE', '2012-02-17 15:41:16', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258288, 'C1208664', 'ADFIRM', '2012-02-17 16:06:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258283, 'FM0538567', 'FILE', '2012-02-17 15:29:21', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258285, 'FM0538567', 'FILE', '2012-02-17 15:41:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258289, 'FM0538567', 'ADFIRM', '2012-02-17 16:06:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258287, 'FM0538567', 'FILE', '2012-02-17 16:04:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104854695, 'FM0538567', 'CONVFMREGI', '2005-09-26 00:00:00', null)""",
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
                    ('C1208664', null, 'CUL', '2012-02-17 15:29:14', null, null, null, null, null, 'SUWBJVAQ', 'CIZXAEEL', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM0538567', null, 'SP', '2005-09-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-11-30 00:00:00', 1060316, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C1208664', 9236428, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM0538567', 104854695, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C1208664', 9236428, null, null, 'NS', 'COR', '2001-02-28 00:00:00', null, '1234567', 'A0036611', 'ABC RECOVERY CANADA CORPORATION', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C1208664', 'CO', 9236429, 1, 9236430, 'YXZGAZUHEKSPGPZOZOMJ', 'XI LEJWXOTQKULSOZYZLGCXO ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C1208664', 'CO', 9236428, 0, 9236429, 'NXJWMSNRSULPVLRELXMT', 'CVATJBEJ UUZOONXEYRBVMZIF', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C1208664', 'NB', 9236430, 1, 9236431, 'LVURGUOLJCQZZYVSDPHI', 'XWQE XKFIWRJPPQERZBKHMJWQ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C1208664', 'CO', 9236431, 1, null, 'GHNYPSIAGWWHMTEVBLKE', 'QGIITJJXJBNOXEAIXEQTRXNQY', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM0538567', 'CO', 104854695, 0, null, 'MGFMEHPARRXKWJEGAOEU', 'PBFWDWUCNMOWYDWIMRHIRILPS', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C1208664', 'RG', 9236428, null, 7534075, 7534074, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C1208664', 'RC', 9236428, null, 7534077, 7534076, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM0538567', 'FO', 104854695, null, 103107494, 103107493, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534072, 'BC', 'CA', '26J42U', 'OUNICFNPAZMUVZ J DBVTQYTM', null, null, 'test', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534073, 'BC', 'CA', 'ZRML91', 'LRBUQNFFJSPBUNSMRFIKJWKYK', null, null, 'test', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534074, 'BC', 'CA', 'FTWOKK', 'Q DTWAFVGXBZVRJRBTMIKOAHI', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534075, 'BC', 'CA', 'SNZK4H', 'AVMOXUOKUOIJK IGLVYRNYVKG', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534076, 'BC', 'CA', 'VFECP9', 'DZXGAQJNHNUDGCLBWJAHIEKT ', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534077, 'BC', 'CA', 'FQGOYV', 'HFVUBHMHVWUWUDGHQZNIHVBM ', null, null, 'testcity', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107493, 'BC', 'CA', 'J5UR6X', null, null, null, 'VANCOUVER', 'BAS', 'JHWMFNDPUEXZYVFTZ TBFUXEGBRVZMFSBEISUQGE', 'HADLFJSXI FOPQGACURX', null, '332', null, '792', null, 'LOPGKXNKEIATDWT', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107494, 'BC', 'CA', 'AI70K7', null, null, null, 'VANCOUVER', 'BAS', 'LYZZVFXEZKWPOOSUVFDGUFPEJXBKUPYZAPDSUFGG', 'JSJLNUYRBJWBVDUTPUUA', null, '571', null, '518', null, 'UKRVIIRQCRWQHSH', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103465149, 'BC', 'CA', 'SJBC26', 'WY ZILKBDCXRPSOHFXPUIYZDL', null, null, 'VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_1277500': {
            "corp_num":'1277500', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1666017, 1528019, 1528019, '1277500', 'OFF', 5375035, 7331454, null, null, null, null, null, 'VILLANUEVA', null, 'MARILYN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1666018, 1528020, 1528020, '1277500', 'DIR', 5375035, null, null, null, null, null, null, 'VILLANUEVA', null, 'NELSON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1666019, 1528020, 1528020, '1277500', 'OFF', 5375035, 7331454, null, null, null, null, null, 'VILLANUEVA', null, 'NELSON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2604453, 4812797, 4812797, '1277500', 'OFF', 7331454, 7950926, 1666017, 'C', null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2604454, 4812798, 4812798, '1277500', 'OFF', 7331454, 7950926, 1666019, 'C', null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2886664, 5680379, 5680379, '1277500', 'OFF', 7950926, 8493310, 1666019, null, null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2886665, 5680380, 5680380, '1277500', 'OFF', 7950926, 8493310, 1666017, null, null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3154265, 6498061, 6498061, '1277500', 'OFF', 8493310, 9133058, 1666017, null, null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3154266, 6498062, 6498062, '1277500', 'OFF', 8493310, 9133058, 1666019, null, null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3464685, 7391250, 7391250, '1277500', 'OFF', 9133058, null, 1666019, null, null, null, null, 'Villanueva', null, 'Nelson', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3464686, 7391251, 7391251, '1277500', 'OFF', 9133058, null, 1666017, null, null, null, null, 'Villanueva', null, 'Marilyn', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6562760, '1277500', 'FILE', '2005-09-16 08:22:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7134443, '1277500', 'FILE', '2006-06-06 11:30:27', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7331454, '1277500', 'FILE', '2006-10-18 10:47:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7950926, '1277500', 'FILE', '2007-11-02 14:32:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242017, '1277500', 'FILE', '2015-07-28 14:46:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375035, '1277500', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375036, '1277500', 'FILE', '2004-01-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375037, '1277500', 'FILE', '2003-09-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375038, '1277500', 'FILE', '2003-01-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375039, '1277500', 'FILE', '2001-11-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5375040, '1277500', 'FILE', '2000-08-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5843351, '1277500', 'ADCORP', '2004-08-13 12:41:51', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5844360, '1277500', 'FILE', '2004-08-14 18:30:06', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5933282, '1277500', 'FILE', '2004-10-15 11:35:53', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8493310, '1277500', 'FILE', '2008-10-15 13:18:53', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9133058, '1277500', 'FILE', '2009-12-10 08:43:38', null)""",
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
                    ('1277500', null, 'BC', '2000-08-28 00:00:00', '2009-08-28 00:00:00', '2004-08-14 18:30:06', null, null, null, 'TQETPWAY', 'VMAKWDII', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1277500', 5375035, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('1277500', 'CO', 5375035, 0, null, 'QTKMLZHXNWFJADJKKCCA', 'XCXBRANU  CKTYRDNTL JGXUT', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RG', 7134443, 9242017, 4515811, 4515810, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RC', 7134443, 9242017, 4515809, 4515808, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RG', 9242017, null, 7535151, 7535151, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RC', 9242017, null, 7535151, 7535151, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RG', 5375035, 5844360, 1528018, 1528018, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RC', 5375035, 5844360, 1528018, 1528018, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RC', 5844360, 7134443, 2055281, 2055280, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1277500', 'RG', 5844360, 7134443, 2055283, 2055282, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1528018, 'BC', 'CA', 'IURBMU', 'ARRSBDAHLEXEKXYLXNMJWLPYI', 'POTPLVCEIOZEUHNJSTLBFNMAB', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1528019, null, null, 'SEEKFT', 'KNOGMZINENA XANNGM JGGBFZ', 'RXFPIHGMHKFMQKN UMALFQOAA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1528020, null, null, 'R5I7NU', 'CIBSKOFYBFZUOMZKHBORGCMFY', 'M QMVZLHSBUDVLKKYWYNL OJD', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055280, 'BC', 'CA', 'GFF9S9', 'WKYDKWCEHOGAHFC  ERUYZVTF', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055281, 'BC', 'CA', 'XH1J03', 'TXHCNUQMZBIZJHUBBRHUASWKN', 'LQLQDZRGHZZLWEHYMGB RCMNS', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055282, 'BC', 'CA', 'NB0NY5', 'TATTBTOGNZCXNDHMTOIWJDGAP', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2055283, 'BC', 'CA', 'ZOPK14', 'WJALKOYVJW TNNRWYWHHZMFPK', 'OZGZUUIHGDKZFUCPYQOOAZDHV', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515808, 'BC', 'CA', '4FQRK0', 'VOMXRMZNWUW PJCAGWRCHHYCN', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515809, 'BC', 'CA', 'VQRTLM', 'SSLWVZRULRALHFSRQMKWPSXOW', 'R IYMPRSRIXUXKEIFYJUFWPJT', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515810, 'BC', 'CA', 'A0ZL98', 'GJ DRJQBVTWNKZNYNSWRXPVVK', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4515811, 'BC', 'CA', '2CME7U', 'EDSDRYGVRGLWNREULCZUTHAHX', 'RFUV  UAOPPFKAOOPDVQJFKZB', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4812797, 'BC', 'CA', 'QKH54S', 'GJLDFIEYTCOMTRRKUYFFNOPRI', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4812798, 'BC', 'CA', 'CBG7TU', 'ALILOSCMHEDBAMVNCKBPXGIIJ', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5680379, 'BC', 'CA', 'MR5L6K', 'JZZEG KYLMRQJKIHIAB GMTER', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5680380, 'BC', 'CA', '34O1GQ', ' BPRCXLAEJVTERAADUAUPOEAK', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6498061, 'BC', 'CA', 'Y6MB0J', 'WFGLAKVLFZHGOPGRDXSBQCEQS', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6498062, 'BC', 'CA', '9QCLYJ', 'OR KXQOCYXGXNTPJGFERSILNY', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7391250, 'BC', 'CA', '4XBJM2', 'QRBZCEFSJTZ XSATRLCQIISCP', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7391251, 'BC', 'CA', 'PX0WGC', 'OEPLOQTXNOYXFWTUHOOALCPNM', null, null, 'Richmond', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535151, 'BC', 'CA', 'XABLQ7', 'MJLPBGUQJ NNDPGRIVQJHCFEM', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM4280968': {
            "corp_num":'FM4280968', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105778013, null, null, 'FM4280968', 'FBO', 104961111, null, null, null, null, '2009-08-12 00:00:00', null, null, null, null, 'A0053427UCYNPQ QHOJKQLZNFSZH', 'A2652799', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104961111, 'FM4280968', 'CONVFMREGI', '2009-08-12 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (104961111, 'FRREG', '2009-08-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM4280968', null, 'SP', '2009-08-12 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2009-08-12 00:00:00', null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM4280968', 104961111, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM4280968', 'CO', 104961111, 0, null, 'GTCHWTLRYZXWPKIACCLG', 'UWJMN GMEMXPTSIVTBSUPEGBL', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
'corp_LLC8529009': {
            "corp_num":'LLC8529009', "corp_typ_cd":'LLC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2564426, 4687887, 4687888, 'LLC8529009', 'ATT', 7248293, 7940088, null, null, null, null, null, 'RISK', 'H.', 'DONALD', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2617713, 4854180, 4854179, 'LLC8529009', 'DIR', 7356685, null, null, null, null, '2006-11-06 00:00:00', null, 'PARISH', null, 'RHONDA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2881356, 5663684, 5663683, 'LLC8529009', 'ATT', 7940086, 9242767, null, null, null, null, null, null, null, null, 'DHHEFMFBTBWTECKNDJZD', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3510953, 7536135, 7536134, 'LLC8529009', 'ATT', 9242767, null, 2881356, null, null, null, null, null, null, null, 'BC0121625ERZUYOM DYKANIGZCF U', 'BC2044710', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7248293, 'LLC8529009', 'FILE', '2006-08-21 16:08:50', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7282058, 'LLC8529009', 'ADMIN', '2006-09-12 15:12:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7356685, 'LLC8529009', 'FILE', '2006-11-06 09:05:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7356692, 'LLC8529009', 'ADMIN', '2006-11-06 09:08:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7357584, 'LLC8529009', 'ADCORP', '2006-11-06 12:53:12', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7904628, 'LLC8529009', 'FILE', '2007-10-05 13:06:26', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7940086, 'LLC8529009', 'FILE', '2007-10-29 09:37:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7940088, 'LLC8529009', 'FILE', '2007-10-29 09:38:15', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242767, 'LLC8529009', 'FILE', '2017-04-04 16:19:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8468425, 'LLC8529009', 'FILE', '2008-09-29 14:13:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9022269, 'LLC8529009', 'FILE', '2009-10-01 16:31:51', null)""",
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
                    ('LLC8529009', null, 'LLC', '2006-08-21 16:08:50', '2009-08-21 00:00:00', null, null, null, null, 'FWZXIIEM', 'DYSPQGMV', 'SNHSYJVEURJS@ERMPPZVR.com', 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('LLC8529009', 7248293, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('LLC8529009', 7248293, null, null, 'OT', 'LLC', '2006-06-28 00:00:00', 'US, DE', '2465132', null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('LLC8529009', 'CO', 7248293, 0, null, 'YYYPXEFEFXRTGJXCZFTG', 'XKFNVLZBVAPBLVEPJZUZSOMY ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('LLC8529009', 'HD', 7248293, null, 4687886, 4687885, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4687885, 'SC', 'US', '2B5UEO', 'YOWIJMVRKRKAHHSYXTPYLVDRA', null, null, 'SPARTANBURG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4687886, 'SC', 'US', 'H05QDD', 'TYHHVHGLHTPTYMUDJKWWEQOVF', null, null, 'SPARTANBURG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4687887, 'BC', 'CA', 'VTR28X', 'IXZYVCHWBOYUXCCQ PPTRXFOH', 'UBXQQCGECUU JQQYUICTWCUHE', '1000 - 840 HOWE STREET', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4687888, 'BC', 'CA', 'XHEQFJ', 'MWCCQLCJTIQJGOKIWFCDKEWHH', 'QYMUOIFUGIQLGGEHUQQYQEBTH', '1000 - 840 HOWE STREET', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4854179, 'SC', 'US', 'VXXASM', 'HQFNUATMBYBKC QEPTOULGNAY', null, null, 'SPARTANBURG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4854180, 'SC', 'US', 'M3UZSX', 'FODFIUUMRABZJHLRYAYXMFXJ ', null, null, 'SPARTANBURG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5663683, 'BC', 'CA', 'OZVMAP', 'KXIMXZ OCNNINGXUNQRCYUXEX', 'PNFACMKJHZGMOBFXPMWXIOQXI', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5663684, 'BC', 'CA', 'TE4XZZ', 'ZRJNFNQ SJNIKGNEGRBLDQQFU', 'TF LEHPQOQEPUIXIUPNUNBTZG', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7536134, 'BC', 'CA', '2XCQL8', 'SNRTXWFIBDODVFYWIMDQU  BD', null, null, 'Vancouver', 'FOR', 'NNYCTWCCZHNENRXTIKIMRSUCBHTQGPYPLQIMXDSS', 'QFFKNPOUS FROLLRJ OC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7536135, 'BC', 'CA', '38ZEMF', 'ANSYUXURUDUYLSPMXIAWSMTNL', 'BXJKQHZXQMKUEYRBWZUFSATIO', null, 'Vancouver', 'FOR', 'APJAKGSKSCYHTQXFPFR UMRLNMOMXCKN WCFR BB', 'OFDKXXWXUDOFKF HNEQW', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_9897475': {
            "corp_num":'9897475', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3090638, 6312333, null, '9897475', 'INC', 8367008, null, null, null, null, null, null, null, null, null, 'EFRXAYTIVAUNODAT VHW', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3090639, 6312335, 6312336, '9897475', 'DIR', 8367008, null, null, null, null, null, null, 'Ellis', null, 'Pete', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242633, '9897475', 'FILE', '2016-08-25 15:25:02', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8367008, '9897475', 'FILE', '2008-07-18 11:35:50', null)""",
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
                    ('9897475', null, 'BC', '2008-07-18 11:35:50', null, null, null, null, null, 'AVBJLVXG', 'QIOUXPND', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('9897475', 8367008, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('9897475', 'NB', 8367008, 0, null, 'DVQZVRCYNAMQHXKVMAJO', 'AULHC SWDLHGHWDONDS VRASR', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9897475', 'RG', 8367008, 9242633, 6312338, 6312337, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9897475', 'RC', 8367008, 9242633, 6312340, 6312339, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9897475', 'RG', 9242633, null, 7535867, 7535866, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9897475', 'RC', 9242633, null, 7535867, 7535866, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312333, 'BC', 'CA', 'PRD9CI', 'HSGQDYAOLHPKSJCTGE JGDGRE', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312335, 'NY', 'US', 'N4LRU5', 'XNQCCOVGXCWCVMHICKNPEQNLQ', null, null, 'New York', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312336, 'NY', 'US', 'VY60E4', 'JJFMCSCUWVLELAZQXGUVM ULZ', null, null, 'New York', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312337, 'BC', 'CA', 'VGYGGK', 'AURYUOXNWYOXQNRZPLQPYZHES', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312338, 'BC', 'CA', 'DRVNKO', 'FEW VNFGCDPSHTKDGDCSX JGN', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312339, 'BC', 'CA', '0RAFM1', 'MIACYGMSDVYOEHYZMNBHBUIJN', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6312340, 'BC', 'CA', 'AV15SY', 'AORHLBHFXBTFDYWGOLYYNYVYT', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535866, 'BC', 'CA', 'MVCX28', 'UZPNBQEJNFKXBEGPRMWJKEPSC', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535867, 'BC', 'CA', 'TOMNDD', 'EXHMTTUOBLPYS UGXZPVQEPME', 'JOZEGAPLXHNJZL QJHNNQSCCZ', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM5949349': {
            "corp_num":'FM5949349', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105682494, null, null, 'FM5949349', 'FBO', 105301927, null, null, null, null, '2001-05-09 14:29:44', null, null, null, null, 'A0031179GPZQNJFLSRMOOMDGYUXO', 'A4095958', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104721465, 'FM5949349', 'CONVFMREGI', '2000-06-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105301927, 'FM5949349', 'CONVFMACP', '2001-05-09 14:29:44', null)""",
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
                    ('FM5949349', null, 'SP', '2000-06-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM5949349', 104721465, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM5949349', 'CO', 104721465, 0, null, 'CRVONBXSTYKEGZKPIVJB', 'SFLOQVPFPJCSOBLFUUTVWMVFU', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
'corp_9260984': {
            "corp_num":'9260984', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":1, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105935322, null, null, 'FM1480726', 'FBO', 105148056, null, null, null, null, '1992-11-19 00:00:00', null, null, null, null, '0384698WYHIRFZYICGEPXXTDOTC', '9260984', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994837, 891658, 891658, '9260984', 'DIR', 3420140, null, null, null, null, null, null, 'KWAN', null, 'JAMES C.K.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994838, 891658, 891658, '9260984', 'OFF', 3420140, null, null, null, null, null, null, 'KWAN', null, 'JAMES C.K.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994839, 891659, 891659, '9260984', 'DIR', 3420140, null, null, null, null, null, null, 'KWAN', null, 'YVONNE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (994840, 891659, 891659, '9260984', 'OFF', 3420140, null, null, null, null, null, null, 'KWAN', null, 'YVONNE', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420140, '9260984', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420141, '9260984', 'FILE', '2003-08-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420142, '9260984', 'FILE', '2003-05-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420143, '9260984', 'FILE', '2002-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420144, '9260984', 'FILE', '2001-04-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420145, '9260984', 'FILE', '2000-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420146, '9260984', 'FILE', '1999-07-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420147, '9260984', 'FILE', '1998-04-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420148, '9260984', 'FILE', '1997-04-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420149, '9260984', 'FILE', '1996-04-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420150, '9260984', 'FILE', '1996-01-10 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420151, '9260984', 'FILE', '1995-06-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420152, '9260984', 'FILE', '1995-06-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420153, '9260984', 'FILE', '1994-08-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420154, '9260984', 'FILE', '1994-07-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420155, '9260984', 'FILE', '1994-06-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420156, '9260984', 'FILE', '1993-09-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420157, '9260984', 'FILE', '1993-08-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420158, '9260984', 'FILE', '1992-09-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420159, '9260984', 'FILE', '1991-09-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420160, '9260984', 'FILE', '1991-07-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420161, '9260984', 'FILE', '1991-01-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420162, '9260984', 'FILE', '1990-06-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420163, '9260984', 'FILE', '1990-06-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420164, '9260984', 'FILE', '1990-03-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (3420165, '9260984', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6292549, '9260984', 'FILE', '2005-05-13 12:26:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6630308, '9260984', 'FILE', '2005-10-18 12:28:32', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6630310, '9260984', 'FILE', '2005-10-18 12:29:49', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7301104, '9260984', 'FILE', '2006-09-26 14:32:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7728004, '9260984', 'FILE', '2007-06-20 18:10:55', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9241844, '9260984', 'FILE', '2015-07-28 14:46:08', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5661793, '9260984', 'ADCORP', '2004-03-31 12:39:58', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5703773, '9260984', 'FILE', '2004-05-03 16:21:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8220941, '9260984', 'FILE', '2008-04-16 14:28:57', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8820401, '9260984', 'ADCORP', '2009-05-11 15:19:05', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8820407, '9260984', 'FILE', '2009-05-11 15:20:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105148056, 'FM1480726', 'CONVFMREGI', '1992-11-19 00:00:00', null)""",
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
                    ('9260984', null, 'BC', '1990-03-28 00:00:00', '2009-03-28 00:00:00', '2005-10-18 12:28:32', null, null, null, 'TBJXACLF', 'AERPTCDD', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM1480726', null, 'SP', '1992-11-19 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('9260984', 3420140, null, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM1480726', 105148056, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('9260984', 'CO', 3420140, 0, 3420165, 'JOIOPFRLAOEWUNGENMDD', 'INPWMYQNLHLRUTFW AGVRDH J', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('9260984', 'CO', 3420165, 0, null, 'WMPBPTBINQCMQHQZYQGW', 'YGXJLVINNOAMXNAYGIOCTMONV', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM1480726', 'CO', 105148056, 0, null, 'SLVTLKYUZJEPFJKENWST', 'OVNER Q KTDCARCCXJXGCW CW', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9260984', 'RG', 9241844, null, 7534978, 7534978, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9260984', 'RC', 9241844, null, 7534978, 7534978, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9260984', 'RG', 3420140, 6630308, 891657, 891657, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9260984', 'RC', 3420140, 6630308, 891657, 891657, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9260984', 'RC', 6630308, 9241844, 3471382, 3471381, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('9260984', 'RG', 6630308, 9241844, 3471384, 3471383, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (891657, 'BC', 'CA', 'FQLBEW', 'UGT JOXATCBZZELXCRWH BHYH', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (891658, null, null, '48JGZ2', 'INNNAYCYSHFMVPGMXVFEQDFE ', 'ZNGRQSMHCGMXZJKHEBTZSLUCD', 'FULL NAME: JAMES CHEE KEUNG', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (891659, null, null, '26N280', 'Y KNVOPEHODPATFPRCHYOZHZE', 'IJ JNLUM EVXCAOEWWXHECAZK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471381, 'BC', 'CA', 'HM8WNO', 'RNBXZTBMZSHGENLOSJSFNMXWU', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471382, 'BC', 'CA', 'P9T7R7', 'JWZGVWYCKFHCKUVQHYZL PHZT', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471383, 'BC', 'CA', '3GPDQS', 'HCQIRRVCPEMMIOESWFXMWXFIL', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3471384, 'BC', 'CA', '8O769I', 'QGAWAIAPPAPVAM ZUUXTWJWTI', null, null, 'BURNABY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7534978, 'BC', 'CA', '2C1K34', 'CLZLNG KVAIMZKZODCDRRJFGD', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_C5466117': {
            "corp_num":'C5466117', "corp_typ_cd":'C', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1659494, 1521768, 1521768, 'C5466117', 'DIR', 5362328, 5846843, null, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1659495, 1521768, 1521768, 'C5466117', 'OFF', 5362328, 5847471, null, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1926503, 2059264, 2059263, 'C5466117', 'DIR', 5846843, 6808452, 1659494, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1926786, 2060313, 2060313, 'C5466117', 'OFF', 5847471, 7269975, 0, null, null, null, null, 'LEGGE', null, 'JOHN A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2351409, 3803504, 3803503, 'C5466117', 'DIR', 6808452, null, 1926503, 'C', null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2574350, 4718920, 4718920, 'C5466117', 'OFF', 7269975, 7869962, 1926786, 'C', null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2849441, 5564637, 5564637, 'C5466117', 'OFF', 7869962, 8402386, 1926786, null, null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3109313, 6366333, 6366333, 'C5466117', 'OFF', 8402386, 8991394, 1926786, null, null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3399039, 7195999, 7195999, 'C5466117', 'OFF', 8991394, null, 1926786, null, null, null, null, 'Legge', 'A.', 'John', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6808494, 'C5466117', 'FILE', '2006-01-11 16:37:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6808452, 'C5466117', 'FILE', '2006-01-11 16:29:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6808434, 'C5466117', 'FILE', '2006-01-11 16:26:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7269975, 'C5466117', 'FILE', '2006-09-06 08:52:14', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7869962, 'C5466117', 'FILE', '2007-09-17 11:11:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242666, 'C5466117', 'FILE', '2016-08-25 15:25:05', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362328, 'C5466117', 'CONVCIN', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362329, 'C5466117', 'FILE', '2003-07-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362330, 'C5466117', 'FILE', '2002-07-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362331, 'C5466117', 'FILE', '2001-08-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5362332, 'C5466117', 'FILE', '2000-07-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5847471, 'C5466117', 'FILE', '2004-08-17 14:00:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5846855, 'C5466117', 'FILE', '2004-08-17 11:11:18', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5846833, 'C5466117', 'ADCORP', '2004-08-17 11:03:42', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5846843, 'C5466117', 'FILE', '2004-08-17 11:07:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8402386, 'C5466117', 'FILE', '2008-08-13 14:25:43', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8991394, 'C5466117', 'FILE', '2009-09-11 11:39:54', null)""",
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
                    ('C5466117', null, 'C', '2000-07-17 00:00:00', '2009-07-17 00:00:00', '2006-01-11 16:29:48', null, null, null, 'NOKPAHDM', 'NLNJIJBF', null, 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C5466117', 5362328, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C5466117', 5362328, null, null, 'OT', 'COR', '1990-06-25 00:00:00', null, null, null, null, null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C5466117', 'CO', 5362328, 0, null, 'NKXWJXMKAYEIAJMIBLXJ', 'HGU  HOI MATHIBXDIXTDHGQV', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C5466117', 'RG', 9242666, null, 7535933, 7535932, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C5466117', 'RC', 9242666, null, 7535933, 7535932, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C5466117', 'RG', 5362328, 6808452, 1521767, 1521767, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C5466117', 'RC', 5362328, 6808452, 1521767, 1521767, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C5466117', 'RC', 6808452, 9242666, 3803506, 3803505, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C5466117', 'RG', 6808452, 9242666, 3803508, 3803507, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1521767, 'BC', 'CA', 'HBK02I', 'YDM VLCQQOTGFGIHZGYHLETSQ', 'ZPD YQSBJWTRXIJUBHEOVKEWK', 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1521768, null, null, 'RRDA02', 'FNISXHYSOGJYMBMCNHWDZECET', 'AQTTKLKILBFOMMXCYXQYOAREO', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2059263, 'BC', 'CA', 'PAQMEK', 'VPULZXFARYTYXURPNGGENH LJ', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2059264, 'BC', 'CA', '6J69QS', 'FYIVJUAFUVUYDDVYQVUOAVYIO', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2060313, 'BC', 'CA', 'BMNFOV', ' PRWNUUVKCUEPLPGPZZILEEIZ', null, null, 'VANCOUVER, ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803503, 'BC', 'CA', 'T2I5F2', 'CRUJTAORMWTZOJ DJVGGZUIGY', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803504, 'BC', 'CA', 'CX8VDE', 'GJ GKAEKMOIMFKWROACLTDPLV', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803505, 'BC', 'CA', 'DLZ6RO', 'IPJVDZMLWNLXNEFDHLNFMCSLJ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803506, 'BC', 'CA', '3LJ58X', 'TMLMITNBZDTYJVHLXOUMDLOLN', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803507, 'BC', 'CA', 'CVGLZK', 'DNSKYWZRIZZSBJEXNHSMEETWO', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (3803508, 'BC', 'CA', '6XCSYB', 'LSOWXKBOYVLKKCYMYTSMGRY R', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4718920, 'BC', 'CA', 'TXZOBF', 'BATZVXIPQMRHDD KHALWYOBGM', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5564637, 'BC', 'CA', 'NRS5WI', 'ZHTCYIDQPYRRUGNTYWMPZBLXP', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6366333, 'BC', 'CA', 'SMBLAF', 'YYPLX PYLUQXQGUJNKSROXWSB', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7195999, 'BC', 'CA', 'HM8RQK', 'VXUSSHFOETFXZUXHRHHVZIKFL', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535932, 'BC', 'CA', 'A2S3FU', 'PEYSLJDOIBKMIDSRNPHXOSRRL', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535933, 'BC', 'CA', 'NDHTIC', 'YCVOH V QSIOLBEDTIZZHWJQI', ' YCVUNWMWGJKCZOCDFDSSXMSH', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_0562726': {
            "corp_num":'0562726', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179508, 1065552, 1065552, '0562726', 'DIR', 4029955, 5780844, null, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179509, 1065552, 1065552, '0562726', 'OFF', 4029955, 5781539, null, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179511, 1065553, 1065553, '0562726', 'OFF', 4029955, 5781539, null, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179512, 1065554, 1065554, '0562726', 'OFF', 4029955, 5781539, null, null, null, null, null, 'SUHNER', null, 'LAURA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179513, 1065555, 1065555, '0562726', 'DIR', 4029955, 5664415, null, null, null, null, '2003-09-07 00:00:00', 'TAYLOR', null, 'JON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1845013, 1743892, 1743891, '0562726', 'DIR', 5664415, 6270088, null, null, null, '2003-09-07 00:00:00', '2004-09-01 00:00:00', 'KRAMER, JR.', 'D.', 'GEORGE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1896759, 1941440, 1941439, '0562726', 'DIR', 5780844, 8086210, 1179510, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1896760, 1941442, 1941441, '0562726', 'DIR', 5780844, 8086210, 1179508, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1179510, 1065553, 1065553, '0562726', 'DIR', 4029955, 5780844, null, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1897055, 1942775, 1942775, '0562726', 'OFF', 5781539, 6316602, 0, null, null, null, null, 'SUHNER', null, 'LAURA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1897056, 1942776, 1942776, '0562726', 'OFF', 5781539, 6316602, 0, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1897057, 1942777, 1942777, '0562726', 'OFF', 5781539, 6316602, 0, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2134346, 2887244, 2887243, '0562726', 'DIR', 6270088, 8086210, null, null, null, '2004-09-01 00:00:00', '2007-02-09 00:00:00', 'Molgat', null, 'Bob', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2155220, 2974593, 2974592, '0562726', 'OFF', 6316602, 7352151, 0, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2155221, 2974595, 2974594, '0562726', 'OFF', 6316602, 7352151, 1897056, 'C', null, null, null, 'SCOTT', 'C.', 'JOHN ', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2155222, 2974597, 2974596, '0562726', 'OFF', 6316602, 7352151, 0, null, null, null, null, 'SUHNER', null, 'LAURA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2614999, 4845389, 4845389, '0562726', 'OFF', 7352151, 7879272, 2155221, 'C', null, null, null, 'Scott', 'C.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2615000, 4845390, 4845390, '0562726', 'OFF', 7352151, 7879272, 2155222, 'C', null, null, null, 'Suhner', null, 'Laura', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2615001, 4845391, 4845391, '0562726', 'OFF', 7352151, 7879272, 2155220, 'C', null, null, null, 'Nishimura', null, 'Don', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2853508, 5577055, 5577055, '0562726', 'OFF', 7879272, 8899110, 2155221, null, null, null, null, 'Scott', 'C.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2853509, 5577056, 5577056, '0562726', 'OFF', 7879272, 8899110, 2155220, null, null, null, null, 'Nishimura', null, 'Don', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2853510, 5577057, 5577057, '0562726', 'OFF', 7879272, 8899110, 2155222, null, null, null, null, 'Suhner', null, 'Laura', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2948557, 5882782, 5882781, '0562726', 'DIR', 8086210, null, 1896759, null, null, null, null, 'SCOTT', null, 'JOHN C.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2948558, 5882784, 5882783, '0562726', 'DIR', 8086210, null, 1896760, null, null, null, null, 'NISHIMURA', null, 'DON', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3352675, 7060605, 7060605, '0562726', 'OFF', 8899110, null, 2155222, null, null, null, null, 'Suhner', null, 'Laura', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3352676, 7060606, 7060606, '0562726', 'OFF', 8899110, null, 2155221, null, null, null, null, 'Scott', 'C.', 'John', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3352677, 7060607, 7060607, '0562726', 'OFF', 8899110, null, 2155220, null, null, null, null, 'Nishimura', null, 'Don', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6316602, '0562726', 'FILE', '2005-05-26 14:26:17', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6270088, '0562726', 'FILE', '2005-05-03 15:22:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7352151, '0562726', 'FILE', '2006-11-01 12:06:59', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7879272, '0562726', 'FILE', '2007-09-21 10:51:22', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9242546, '0562726', 'FILE', '2016-08-25 15:24:54', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029971, '0562726', 'FILE', '1995-03-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029972, '0562726', 'FILE', '1994-07-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029973, '0562726', 'FILE', '1993-09-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029974, '0562726', 'FILE', '1993-07-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029975, '0562726', 'FILE', '1993-05-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029976, '0562726', 'CONVNC', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029955, '0562726', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029956, '0562726', 'FILE', '2004-03-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029957, '0562726', 'FILE', '2003-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029958, '0562726', 'FILE', '2002-05-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029959, '0562726', 'FILE', '2002-03-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029960, '0562726', 'FILE', '2001-10-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029961, '0562726', 'FILE', '2001-10-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029962, '0562726', 'FILE', '2001-02-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029963, '0562726', 'FILE', '2000-05-18 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029964, '0562726', 'FILE', '1999-07-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029965, '0562726', 'FILE', '1998-07-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029966, '0562726', 'FILE', '1997-06-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029967, '0562726', 'FILE', '1996-08-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029968, '0562726', 'FILE', '1996-08-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029969, '0562726', 'FILE', '1995-09-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (4029970, '0562726', 'FILE', '1995-07-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5664415, '0562726', 'FILE', '2004-04-01 15:35:30', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5664353, '0562726', 'ADCORP', '2004-04-01 15:22:38', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5780844, '0562726', 'FILE', '2004-06-29 11:07:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5781539, '0562726', 'FILE', '2004-06-29 14:44:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8086210, '0562726', 'FILE', '2008-01-23 16:03:08', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8316658, '0562726', 'FILE', '2008-06-16 14:36:36', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8899110, '0562726', 'FILE', '2009-07-06 12:50:39', null)""",
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
                    ('0562726', null, 'BC', '1993-05-04 00:00:00', '2009-05-04 00:00:00', '2004-06-29 11:07:52', null, null, null, 'CBOVDIKL', 'CTZTLDQF', null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('0562726', 4029955, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0562726', 'CO', 4029955, 0, 4029976, 'WBISXISMQODMXVBHTIOV', 'NEOYUREWSLSHVJMPRWMBWFFKM', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('0562726', 'CO', 4029976, 0, null, 'SJJIHTUCOZNXHWHMNENF', 'PIYPSKRCGEZNXXXKPROCSLAME', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0562726', 'RG', 9242546, null, 7535693, 7535692, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0562726', 'RC', 9242546, null, 7535693, 7535692, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0562726', 'RG', 4029955, 5780844, 1065551, 1065551, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0562726', 'RC', 4029955, 5780844, 1065551, 1065551, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0562726', 'RC', 5780844, 9242546, 1941444, 1941443, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('0562726', 'RG', 5780844, 9242546, 1941446, 1941445, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1065551, 'BC', 'CA', '0CXLHL', 'QNFBTRFVTWJBZHOIWWSGTDFWD', 'JXQMOKTKJTDUZNGVQGCMHKDVP', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1065552, null, null, 'QAZJOQ', 'OYIZOGNQAZIBVMUKNPEQGHVXY', 'RYBPANBSLQXEPHGNJHAPZXMDT', 'VANCOUVER BC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1065553, null, null, 'BWIF80', ' CELKSSGPOFJCCHWLXYNZHLLA', 'GYNUCOYKYXFNGZGWCBRIMTIJA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1065554, null, null, 'IS513J', ' HDT LTH ZZGXQATOORL MJHO', 'Q IZHJECMYTQKDPJECNKGFMUY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1065555, null, null, 'RKXF5S', 'LIEYUEUESSQIMADDYCHZJAPPK', 'FINBRLVQARTKJAPTVIXKEHGRV', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1743891, 'WA', 'US', 'GRIC7W', 'J MBVVIYZSTQYI OOFIEUYMGT', null, null, 'MILL CREEK,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1743892, 'WA', 'US', 'SQ1F7N', 'RWTVQVZVLOUVULKLPR RPILHA', null, null, 'MILL CREEK,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941439, 'BC', 'CA', 'PPPER8', 'JCDXLFMNECGKFTJDLULQHHJQ ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941440, 'BC', 'CA', 'GXIGHU', 'QKBYAZOALFCDKBOEZZJNTZHJQ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941441, 'BC', 'CA', 'LWI95N', 'ZBEZLRUKDXVCJQKRPVYUXMBLS', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941442, 'BC', 'CA', '0NB6OS', 'QVKQQGNYMYORWDRWVZWFMM WT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941443, 'BC', 'CA', '9PA6JF', 'RCWXSZHUJQDEXVDJRCXPSOPVQ', 'XXBZFOSWHWKUQJOWBSHNDXSBH', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941444, 'BC', 'CA', 'XAWDCC', 'PFBENPZBSGTGIP N QWZVCL M', 'ZDDZOLBWZ EGEXWBSUZREQ FS', 'P.O. BOX 48600', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941445, 'BC', 'CA', '2UV1GX', 'TINBHSKDGXBCAOVPAMGPGBLFN', 'JYHRZHGPNVTGFNRQQ KEQDHWD', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1941446, 'BC', 'CA', 'DV8BO6', 'UPYDZHNMIDOR FNEKZDYBZCJW', 'PTJFTGIZMCQANKNQHBPGPJNTG', 'P.O. BOX 48600', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1942775, 'BC', 'CA', 'NMQX1J', 'NSJNCZYBECLEXFJFSEUUIXAEX', null, null, 'NEW WESTMINSTER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1942776, 'BC', 'CA', 'W3LM14', 'KGFBKZFSBWUXXBPECL ZWI WI', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1942777, 'BC', 'CA', 'F6A4M7', 'JFHKBLHTQ XHBV YPMPMVEOWR', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2887243, 'ON', 'CA', 'MKZLPJ', 'TSECDBRCZAMD R NNCIDFUGGG', null, null, 'Mississauga', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2887244, 'ON', 'CA', 'WDHB85', 'LGALNHGUEYHHEIQEZDGTUORSK', null, null, 'Mississauga', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2974592, 'BC', 'CA', 'PNBSXY', 'SUJVBLQCDGQNQYKDZXRQWVXVJ', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2974593, 'BC', 'CA', 'WCRC0E', 'P GT NILCPDCZTEGBZS TBSJW', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2974594, 'BC', 'CA', '4HNT9X', 'JRQJUTRKHIIWF ELKPHSOJDGM', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2974595, 'BC', 'CA', '7VGB95', 'N DTUOZRGNNTAPMAQA CHUEVF', null, null, 'VANCOUVER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2974596, 'BC', 'CA', 'LKXRWP', 'TRYY WLQJSMH JOADLSUZKXGJ', null, null, 'NEW WESTMINSTER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (2974597, 'BC', 'CA', 'QME37L', 'GRUSCDCCHH TMPHILHFHF WDE', null, null, 'NEW WESTMINSTER,', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4845389, 'BC', 'CA', 'EQ9T9I', 'PVRY UXTKOGJTOSQTGIEVV RR', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4845390, 'BC', 'CA', '9ZN2H2', 'MURNCRVAKGUUMVFRLIPOVUXDU', null, null, 'New Westminster', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (4845391, 'BC', 'CA', 'SPZLSC', 'MBDQGYSJODCEVLHPJVSANKOSW', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5577055, 'BC', 'CA', 'LWG5FC', 'E DQKOGQQTAFBFJKWWWGADUYI', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5577056, 'BC', 'CA', 'ZLLRRW', 'MJQOTNQOFAXWUETPUCTEOVZON', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5577057, 'BC', 'CA', 'JN3Z9O', 'FOCMTW GAZWVRBMXACCUGU B ', null, null, 'New Westminster', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5882781, 'BC', 'CA', 'FGUN3E', 'LZAOWXCDCWBAPZQFDHLKWXKB ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5882782, 'BC', 'CA', 'W63NPQ', 'VPFMYMAEWBFJCBCZJMSEZPAEY', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5882783, 'BC', 'CA', 'NOTCTA', 'EIIOYL FHTPOYVVPOEFLBGBWR', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (5882784, 'BC', 'CA', 'NZI6DD', 'CLFDIGIWYJEXJEIYHIXJSPUKJ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7060605, 'BC', 'CA', 'JL8UBR', 'RMNLDNUIOZYEPWTTUEWZBIEDW', null, null, 'New Westminster', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7060606, 'BC', 'CA', 'NU1Y1U', 'NLXGSXSLEZTXG SHQQMMU DAX', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7060607, 'BC', 'CA', '2VWBTL', 'OSOHFLZASZSLYDZNNZEYIDFPG', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535692, 'BC', 'CA', 'D34EM9', 'CDGLUGU LH  ZIYVHWRDHCUQP', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7535693, 'BC', 'CA', '3JEOW8', ' EJSVOALNJKUYYZCAZCYEVQRM', 'TFHATXMDHBXTRYWPHGOTXEBNT', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
'corp_FM8872572': {
            "corp_num":'FM8872572', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105935322, null, null, 'FM8872572', 'FBO', 105148056, null, null, null, null, '1992-11-19 00:00:00', null, null, null, null, '0384698XSVIEUCTIBFQHZXJYXGL', '2499856', null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (105148056, 'FM8872572', 'CONVFMREGI', '1992-11-19 00:00:00', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (105148056, 'FRREG', '1992-11-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('FM8872572', null, 'SP', '1992-11-19 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM8872572', 105148056, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM8872572', 'CO', 105148056, 0, null, 'IVMGZSTMSIVJDPVLDJCQ', 'ILWPZJTYTBODA AVU RYHAWHR', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                   ]
             },
'corp_FM2240721': {
            "corp_num":'FM2240721', "corp_typ_cd":'SP', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361182, 104982591, null, 'FM2240721', 'FCP', 111258287, 111258289, 108361178, null, null, null, null, null, null, null, 'HGHBZOROJVGEKMURPMCL', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361183, 103465149, null, 'FM2240721', 'FBO', 111258287, 111258289, 108361179, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156HOZEAVGTFQFJSOABLQTM', 'C4389029', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361174, 104982583, null, 'FM2240721', 'FCP', 111258283, 111258285, 105319638, null, null, null, null, null, null, null, 'DT FHGFMYFQJVCPWYPWR', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361175, 103465149, null, 'FM2240721', 'FBO', 111258283, 111258285, 105513550, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156WLIRLESMHCWRPTYBBHZR', 'C4389029', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105513550, 103465149, null, 'FM2240721', 'FBO', 104854695, 111258283, null, null, null, '2005-09-26 00:00:00', null, null, null, null, 'A0036611DM AFNQEOGLPANDLAAIU', 'A0532082', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361178, 104982587, null, 'FM2240721', 'FCP', 111258285, null, 108361174, null, null, null, null, null, null, null, 'MTNKHGEDUAPLWOOUDEHY', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (108361179, 103465149, null, 'FM2240721', 'FBO', 111258285, null, 108361175, null, null, '2005-09-26 00:00:00', null, null, null, null, 'C0874156HAEYDDOPCLBLVDAOOAYO', 'C4389029', null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (105319638, 103107492, null, 'FM2240721', 'FCP', 104854695, 111258283, null, null, null, null, null, 'RAMIREZ', null, 'BEVERLY', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258283, 'FM2240721', 'FILE', '2012-02-17 15:29:21', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258285, 'FM2240721', 'FILE', '2012-02-17 15:41:20', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258289, 'FM2240721', 'ADFIRM', '2012-02-17 16:06:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (111258287, 'FM2240721', 'FILE', '2012-02-17 16:04:23', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (104854695, 'FM2240721', 'CONVFMREGI', '2005-09-26 00:00:00', null)""",
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
                    ('FM2240721', null, 'SP', '2005-09-26 00:00:00', null, null, null, null, null, null, null, null, null, 'N', null, '2007-11-30 00:00:00', 1060316, null, null, null, null, null, null, null)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('FM2240721', 104854695, null, 'ACT', null)""",
                    """create table if not exists tilma_involved (tilma_involved_id text, corp_num text, start_event_id text, end_event_id text, tilma_jurisdiction text, nuans_number text, nuans_expiry_date timestamp, nr_number text, jurisdiction_num text, jurisdiction_reg_date timestamp, can_number text, jurisdiction_assumed_name text, assumed_nuans_number text, assumed_nuans_name text, assumed_nuans_expiration_date timestamp, involved_ind text, cessation_date timestamp)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('FM2240721', 'CO', 104854695, 0, null, 'PEBZZWNFKPTIYEODBKVQ', 'DAX LPBTSDYYQDQXXVFMYDTE ', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('FM2240721', 'FO', 104854695, null, 103107494, 103107493, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107492, 'BC', 'CA', 'YXXLNA', null, null, null, 'VANCOUVER', 'BAS', 'OILVDUSNXNYQIICIR CXDBIFYOYGIQCPIPOSCMTH', 'NHJLOPQGMAPYNMVVXBTW', null, '302', null, '513', null, 'AFOJYDOPRHUONPH', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107493, 'BC', 'CA', 'CXOZQI', null, null, null, 'VANCOUVER', 'BAS', 'VEZYQKSCJJ GXTXHTMWIKCPAFLMSQSEHSRXNKLRP', 'JZFACPLVJOKCXEIAJMSN', null, '625', null, '407', null, 'NBBKKFLMPTQPVTH', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103107494, 'BC', 'CA', 'SB90SA', null, null, null, 'VANCOUVER', 'BAS', 'LBW DUTVEVRLXFMYEYREWIFZJSR TCVIWZNWFOID', 'PIUYDGOQOWOGSSQMRX B', null, '665', null, '922', null, 'SRYUFMWLNZMKYVC', 'ST', 'N', null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (103465149, 'BC', 'CA', 'NCLQY9', 'BELEUAU TLQGMJGPDQVQZCDJK', null, null, 'VANCOUVER', 'FOR', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (104982583, 'BC', 'CA', 'ZTT776', 'BFVCEEUDSFVDBIPDDWXZIXPIY', null, null, 'testcity', 'FOR', 'GXVCQTIYPN ZTSRWJGLU NYRICCRXGZNVNINWTEP', 'R YQGQXYICLCXFV XJMP', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (104982587, 'BC', 'CA', 'KZJ95D', 'ZKSNCCYGSTALGBJQAEGV CRJG', null, null, 'testcity', 'FOR', 'KGZWMPXVCDCDJYNVYQZVGDUVWJQQLUPYAQ YSFSC', 'GHRSEWQIECOXCZMYXGGY', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (104982591, 'BC', 'CA', '5LQJDI', 'U NKOQPZXEUMMLNJMUTNMLMU ', null, null, 'testcity', 'FOR', 'XOYISP SWTCOXWMNIWNKXPSOMYDAKHNKPAYUFGFD', 'HTUMIGJEYFAQADQEJMBC', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
}
