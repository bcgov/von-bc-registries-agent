
sample_test_dates_corps = {
    "corp_1529559": {
            "corp_num":'1529559', "corp_typ_cd":'BC', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2168418, 3029182, 3029181, '1529559', 'OFF', 6348533, 8860651, 0, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (2519656, 4549036, 4549035, '1529559', 'DIR', 7154307, 8858230, 1710901, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3873946, 8616325, 8616325, '1529559', 'OFF', 9892259, 10503517, 3653793, 'C', null, null, null, 'Chow', 'Q.', 'Norman', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3873952, 8616348, 8616347, '1529559', 'DIR', 9892269, 12357515, 3653790, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (4750537, 11171642, 11171642, '1529559', 'OFF', 11765900, 12357503, 3653793, null, null, null, null, 'Chow', 'Q.', 'Norman', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5046860, 12025170, 12025169, '1529559', 'DIR', 12357515, 14382365, 3873952, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5046850, 12025141, 12025141, '1529559', 'OFF', 12357503, 14391356, 3653793, null, null, null, null, 'Chow', 'Q.', 'Norman', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1710901, 1571748, 1571748, '1529559', 'DIR', 5456003, 7154307, null, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1710902, 1571748, 1571748, '1529559', 'OFF', 5456003, 5772934, null, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (1893046, 1926757, 1926756, '1529559', 'OFF', 5772934, 6348533, 0, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3333020, 7001697, 7001696, '1529559', 'OFF', 8860651, 9483708, 0, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3332040, 6998680, 6998679, '1529559', 'DIR', 8858230, 9483706, 2519656, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3653790, 7958984, 7958983, '1529559', 'DIR', 9483706, 9892269, 3332040, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (3653793, 7958995, 7958994, '1529559', 'OFF', 9483708, 9892259, 0, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (4158060, 9450552, 9450552, '1529559', 'OFF', 10503517, 11173898, 3653793, null, null, null, null, 'Chow', 'Q.', 'Norman', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (4461595, 10330723, 10330723, '1529559', 'OFF', 11173898, 11765900, 3653793, null, null, null, null, 'Chow', 'Q.', 'Norman', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8850548, 15129774, 15129773, '1529559', 'DIR', 14382365, null, 5046860, null, null, null, null, 'CHOW', null, 'NORMAN Q.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8854231, 15140731, 15140730, '1529559', 'OFF', 14391356, null, 3653793, null, null, null, null, 'Chow', 'Q.', 'Norman', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5456003, '1529559', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5456004, '1529559', 'FILE', '2003-08-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5456005, '1529559', 'FILE', '2003-06-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5456006, '1529559', 'FILE', '2002-06-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5456007, '1529559', 'FILE', '2001-06-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5732605, '1529559', 'FILE', '2004-05-27 11:37:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5726080, '1529559', 'ADCORP', '2004-05-20 15:05:24', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (5772934, '1529559', 'FILE', '2004-06-23 11:46:11', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8305721, '1529559', 'FILE', '2008-06-09 16:41:33', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8413924, '1529559', 'FILE', '2008-08-21 10:07:56', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8858230, '1529559', 'FILE', '2009-06-08 08:39:38', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (8860651, '1529559', 'FILE', '2009-06-09 08:28:03', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9295088, '1529559', 'FILE', '2010-03-31 16:08:04', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9483706, '1529559', 'FILE', '2010-08-28 16:03:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9483708, '1529559', 'FILE', '2010-08-28 16:07:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (10503517, '1529559', 'FILE', '2012-06-21 11:19:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (11173898, '1529559', 'FILE', '2013-07-08 14:24:26', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (11765900, '1529559', 'FILE', '2014-06-25 14:16:48', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12093563, '1529559', 'ADCORP', '2015-01-13 15:35:19', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (14277508, '1529559', 'ADCORP', '2018-04-19 10:34:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (14308710, '1529559', 'ADCORP', '2018-05-03 15:59:09', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (14310154, '1529559', 'FILE', '2018-05-04 12:28:05', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (14382365, '1529559', 'FILE', '2018-06-11 12:54:46', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (14391356, '1529559', 'FILE', '2018-06-14 08:40:07', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6348533, '1529559', 'FILE', '2005-06-09 18:00:50', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7154313, '1529559', 'FILE', '2006-06-19 14:49:51', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7154307, '1529559', 'FILE', '2006-06-19 14:47:25', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (7712598, '1529559', 'FILE', '2007-06-13 08:35:36', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9892251, '1529559', 'ADCORP', '2011-06-17 09:33:19', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9892259, '1529559', 'FILE', '2011-06-17 09:35:34', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9892269, '1529559', 'FILE', '2011-06-17 09:40:09', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (9892274, '1529559', 'FILE', '2011-06-17 09:41:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12207764, '1529559', 'FILE', '2015-03-17 15:18:35', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12207777, '1529559', 'ADCORP', '2015-03-17 15:20:49', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12357515, '1529559', 'FILE', '2015-06-09 11:33:28', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12357503, '1529559', 'FILE', '2015-06-09 11:30:52', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13008522, '1529559', 'FILE', '2016-06-10 11:06:04', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13690599, '1529559', 'FILE', '2017-06-16 13:23:55', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5456004, 'CONVL', '2003-08-11 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5456005, 'CONVL', '2003-06-12 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5456006, 'CONVL', '2002-06-19 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5456007, 'CONVL', '2001-06-07 00:00:00', null, null, null, null, null, null, null, 'P ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5732605, 'TRANS', '2004-05-27 11:37:34', null, null, null, null, 'N', null, null, 'F ', 5732605, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (5772934, 'ANNBC', '2004-06-23 11:46:11', null, null, '2004-06-07 00:00:00', null, 'N', null, null, 'F ', null, '100706290', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (6348533, 'ANNBC', '2005-06-09 18:00:50', null, null, '2005-06-07 00:00:00', null, 'N', null, null, 'F ', null, '103545950', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7154307, 'NOCDR', '2006-06-19 14:47:25', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7154313, 'ANNBC', '2006-06-19 14:49:51', null, null, '2006-06-07 00:00:00', null, 'N', null, null, 'F ', null, '106433790', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (7712598, 'ANNBC', '2007-06-13 08:35:36', null, null, '2007-06-07 00:00:00', null, 'N', null, null, 'F ', null, '109376608', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8305721, 'ANNBC', '2008-06-09 16:41:33', null, null, '2008-06-07 00:00:00', null, 'N', null, null, 'F ', null, '112321765', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8413924, 'NOCAD', '2008-08-22 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8858230, 'NOCDR', '2009-06-08 08:39:38', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (8860651, 'ANNBC', '2009-06-09 08:28:03', null, null, '2009-06-07 00:00:00', null, 'N', null, null, 'F ', null, '115383234', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9295088, 'NOCAD', '2010-04-01 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9483706, 'NOCDR', '2010-08-28 16:03:48', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9483708, 'ANNBC', '2010-08-28 16:07:44', null, null, '2010-06-07 00:00:00', null, 'N', null, null, 'F ', null, '118504448', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9892259, 'ANNBC', '2011-06-17 09:35:34', null, null, '2011-06-07 00:00:00', null, 'N', null, null, 'F ', null, '121812820', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9892269, 'NOCDR', '2011-06-17 09:40:09', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (9892274, 'NOCAD', '2011-06-18 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (10503517, 'ANNBC', '2012-06-21 11:19:48', null, null, '2012-06-07 00:00:00', null, 'N', null, null, 'F ', null, '125429340', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (11173898, 'ANNBC', '2013-07-08 14:24:26', null, null, '2013-06-07 00:00:00', null, 'N', null, null, 'F ', null, '129034088', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (11765900, 'ANNBC', '2014-06-25 14:16:48', null, null, '2014-06-07 00:00:00', null, 'N', null, null, 'F ', null, '132681545', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (12207764, 'NOCAD', '2015-03-18 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (12357503, 'ANNBC', '2015-06-09 11:30:52', null, null, '2015-06-07 00:00:00', null, 'N', null, null, 'F ', null, '136453719', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (12357515, 'NOCDR', '2015-06-09 11:33:28', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13008522, 'ANNBC', '2016-06-10 11:06:04', null, null, '2016-06-07 00:00:00', null, 'N', null, null, 'F ', null, '140311960', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13690599, 'ANNBC', '2017-06-16 13:23:55', null, null, '2017-06-07 00:00:00', null, 'N', null, null, 'F ', null, '144189834', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (14310154, 'NOCAD', '2018-05-05 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (14382365, 'NOCDR', '2018-06-11 12:54:46', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (14391356, 'ANNBC', '2018-06-14 08:40:07', null, null, '2018-06-07 00:00:00', null, 'N', null, null, 'F ', null, '148253297', null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('1529559', null, 'BC', '2001-06-07 00:00:00', '2018-06-07 00:00:00', '2004-05-27 11:37:34', '352957361', '920838811165081', null, 'OWAJFMVT', 'PDYTHDSN', 'NBIDQHJFFDCO@NVYITKCM.com', 'N', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('1529559', 5456003, null, 'ACT', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('1529559', 'NB', 5456003, 0, null, 'GMGTDYDDQQGHLFBCGZEF', 'TMTWFPMLSDBTEUHX  VHLPXZU', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 5456003, 5732605, 1571747, 1571747, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 5456003, 5732605, 1571747, 1571747, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 5732605, 8413924, 1857154, 1857153, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 5732605, 8413924, 1857156, 1857155, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 8413924, 9295088, 6382157, 6382156, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 8413924, 9295088, 6382155, 6382154, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 14310154, null, 15016565, 15016564, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 14310154, null, 15016563, 15016562, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 9295088, 9892274, 7642314, 7642313, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 9295088, 9892274, 7642312, 7642311, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 9892274, 12207764, 8616355, 8616354, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 9892274, 12207764, 8616353, 8616352, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RG', 12207764, 14310154, 11805851, 11805850, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('1529559', 'RC', 12207764, 14310154, 11805849, 11805848, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1571747, 'BC', 'CA', '2JPRA1', 'W VQBDBVZJICW OCXLSC FRMB', 'YCLMOLVTZXSWPYUZEOMYZM XV', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1857153, 'BC', 'CA', 'Z3CIFS', 'BZHCGCKAMDLCEKMUFRSMAODSO', 'JHAHYQRAFMOJUZKFSUGIFKMBO', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1857154, 'BC', 'CA', '4M03BO', 'ILFLFLJMHWOJHTXZFFK  PNFH', 'QBIFQRZJJGRFM ATLDBCRGAXQ', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1857155, 'BC', 'CA', 'SS5276', 'RDLVWNQKMJTASAHQERTDURUEF', 'HSA YWZJBVHZFTDOHJPTWRINH', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (1857156, 'BC', 'CA', 'R4TFVM', 'IMFIOIWQOJNGWAUSZBGCHK LG', 'EPKYKAVFJNENJMNYQABBQ XVM', null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6382154, 'BC', 'CA', 'M8B6R4', ' QYQCTRATPOIMFWQMIGORRVON', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6382155, 'BC', 'CA', '863EUQ', 'NBAVX BGLHNNXADYGYUDRHCHU', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6382156, 'BC', 'CA', 'PQVO5A', 'PYQBV VUBNPNMY DGLJKMYWQP', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (6382157, 'BC', 'CA', 'MKVEGP', 'YUULKAIBYQKLRSENXHXQEWZKL', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7642311, 'BC', 'CA', 'AU6IVJ', 'NJXFQFNJYXRHOVYWWTPH FEPZ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7642312, 'BC', 'CA', 'T7H0BY', 'R DILVGKHS  RVFAVYMAII CB', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7642313, 'BC', 'CA', 'YFVYWS', 'GICCPQMGDKGKDNVSBFETDXTRE', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (7642314, 'BC', 'CA', 'A8RMXN', 'KB OYIFFPCSCYRXX DIVGYN V', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (8616352, 'BC', 'CA', 'ERJ75U', 'LIPCYNVSESPNGFCQZVMAYDAGQ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (8616353, 'BC', 'CA', 'PM8XAB', 'BQHTRS EZIANWRSVOMDFGXXPZ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (8616354, 'BC', 'CA', 'UPRLYJ', 'DVSMK RULYYKBHGZCAZARVNHB', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (8616355, 'BC', 'CA', '80UZU8', 'TPUEURZVUADPQLODDDWPBEXUT', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (11805848, 'BC', 'CA', 'NK71XC', 'KBVZXUEEXEQEMUJGOLYUPNDMT', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (11805849, 'BC', 'CA', 'UZKEWG', ' VJIMMRDTZPUFRUM DXKARQMN', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (11805850, 'BC', 'CA', 'F1QMVM', 'IQNBKWKRRHCQWSXMFVVEPRXHF', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (11805851, 'BC', 'CA', '69UUIE', 'PWAQSRGJKVLSPSDEGNZXOZJGY', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (15016562, 'BC', 'CA', 'A1OJP5', 'KKIETPBUJ E JXOPIVXAWIXRM', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (15016563, 'BC', 'CA', 'YHTDSD', 'ZTFFLTGZKFAYUIFOZHZKJ MQ ', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (15016564, 'BC', 'CA', '5ES32I', 'NCQSZINUNJIC YBCSEHSXMUYN', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (15016565, 'BC', 'CA', 'EA37CG', 'KTAQEPPF BJCE NP LNOJZYVH', null, null, 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_3692600": {
            "corp_num":'3692600', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (381551, 333495, 333495, '3692600', 'LIQ', 1054033, null, null, null, null, '1987-12-23 00:00:00', null, null, null, null, 'VQJCWFUFI TWEYUNMDMX', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (381552, 333496, 333496, '3692600', 'DIR', 1054033, null, null, null, null, null, null, 'COUVELIER', null, 'DEBRA', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (381553, 333497, 333497, '3692600', 'OFF', 1054033, null, null, null, null, null, null, 'COUVELIER', null, 'MELVILLE B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830099, null, null, '3692600', 'DIR', 1054033, 1054033, null, null, null, null, '1987-12-31 00:00:00', 'COUVELIER', null, 'RODNEY STEVEN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830100, null, null, '3692600', 'DIR', 1054033, 1054033, null, null, null, null, '1983-04-07 00:00:00', 'COUVELIER', null, 'MILDRED ANN', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830101, null, null, '3692600', 'DIR', 1054033, 1054033, null, null, null, null, '1989-10-20 00:00:00', 'COUVELIER', null, 'MELVILLE B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5830102, null, null, '3692600', 'DIR', 1054033, 1054033, null, null, null, null, '1989-10-20 00:00:00', 'COUVELIER', null, 'DEBRA', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054033, '3692600', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054034, '3692600', 'FILE', '1990-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054035, '3692600', 'FILE', '1990-11-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054036, '3692600', 'FILE', '1988-01-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054037, '3692600', 'FILE', '1987-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054038, '3692600', 'FILE', '1987-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054039, '3692600', 'FILE', '1987-02-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054040, '3692600', 'FILE', '1987-02-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054041, '3692600', 'FILE', '1986-01-03 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054042, '3692600', 'FILE', '1985-01-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054043, '3692600', 'FILE', '1983-12-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054044, '3692600', 'FILE', '1983-12-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054045, '3692600', 'FILE', '1983-04-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054046, '3692600', 'FILE', '1982-01-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054047, '3692600', 'FILE', '1981-06-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054048, '3692600', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054049, '3692600', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1054050, '3692600', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
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
                    ('3692600', null, 'BC', '1973-11-30 00:00:00', '1986-11-30 00:00:00', null, '523758105', '747594983923840', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3692600', 1054050, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3692600', 1054049, 1054050, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3692600', 1054048, 1054049, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('3692600', 'CO', 1054033, 0, null, 'NHRCQVGZADNBUQHBIUMU', ' SVSZWSKCGFCIGSXLRWMYOOXS', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3692600', 'RG', 1054033, null, 333494, 333494, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3692600', 'RC', 1054033, null, 333494, 333494, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (333494, 'BC', 'CA', 'BEK2WS', 'BPQOEJGCCUJINCMSJAKVGXFPF', 'MJIOLMRILU AT VZI JPXMZLK', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_8585951": {
            "corp_num":'8585951', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495427, 431310, 431310, '8585951', 'LIQ', 1631095, null, null, null, null, '1991-01-29 00:00:00', null, null, null, null, 'XM YTDCHAXAICKK GIJE', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495428, 431311, 431311, '8585951', 'DIR', 1631095, null, null, null, null, null, null, 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (495429, 431311, 431311, '8585951', 'OFF', 1631095, null, null, null, null, null, null, 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6005579, null, null, '8585951', 'DIR', 1631095, 1631095, null, null, null, null, '1988-01-29 00:00:00', 'VARLEY', null, 'DOUGLAS W.', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631095, '8585951', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631096, '8585951', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631097, '8585951', 'FILE', '1991-01-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631098, '8585951', 'FILE', '1990-12-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631099, '8585951', 'FILE', '1990-12-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631100, '8585951', 'FILE', '1989-07-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631101, '8585951', 'FILE', '1989-04-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631102, '8585951', 'FILE', '1987-10-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631103, '8585951', 'FILE', '1985-01-15 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631104, '8585951', 'FILE', '1983-10-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631105, '8585951', 'FILE', '1982-08-17 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631106, '8585951', 'FILE', '1981-09-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631107, '8585951', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631108, '8585951', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1631109, '8585951', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
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
                    ('8585951', null, 'BC', '1979-07-31 00:00:00', '1990-07-31 00:00:00', null, '077477581', '475195051870304', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8585951', 1631109, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8585951', 1631108, 1631109, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('8585951', 1631107, 1631108, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('8585951', 'CO', 1631095, 0, null, 'YXELYQNRZQRLMFZJVBND', 'AZHGWDBCGIBFSHOSISD ZOAJO', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8585951', 'RG', 1631095, null, 431309, 431309, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('8585951', 'RC', 1631095, null, 431309, 431309, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (431309, 'BC', 'CA', '8C4GIK', 'LQVE K DYYGHMWU STNLJHHXU', 'RATZJEGAZQVMAFYUSCEDVDFRD', 'VANCOUVER', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_3305431": {
            "corp_num":'3305431', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91069, 79291, 79291, '3305431', 'LIQ', 253983, null, null, null, null, '1987-03-10 00:00:00', null, null, null, null, 'EVMXRIHZYAQ GIMHETYX', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91070, 79292, 79292, '3305431', 'DIR', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'JULIETTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91071, 79292, 79292, '3305431', 'OFF', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'JULIETTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91072, 79293, 79293, '3305431', 'DIR', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'LESLIE ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (91073, 79293, 79293, '3305431', 'OFF', 253983, null, null, null, null, null, null, 'JANUSSON', null, 'LESLIE ROBERT', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683604, null, null, '3305431', 'DIR', 253983, 253983, null, null, null, null, '1985-05-08 00:00:00', 'JANUSSON', null, 'BERGON B.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683605, null, null, '3305431', 'DIR', 253983, 253983, null, null, null, null, '1983-10-28 00:00:00', 'JANUSSON', null, 'AMY E.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683606, null, null, '3305431', 'DIR', 253983, 253983, null, null, null, null, '1987-12-21 00:00:00', 'JANUSSON', null, 'JULIETTE', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5683607, null, null, '3305431', 'DIR', 253983, 253983, null, null, null, null, '1987-12-21 00:00:00', 'JANUSSON', null, 'LESLIE ROBERT', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253983, '3305431', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253984, '3305431', 'FILE', '1988-01-05 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253985, '3305431', 'FILE', '1987-09-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253986, '3305431', 'FILE', '1987-06-22 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253987, '3305431', 'FILE', '1987-03-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253988, '3305431', 'FILE', '1987-03-12 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253989, '3305431', 'FILE', '1987-03-04 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253990, '3305431', 'FILE', '1986-05-27 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253991, '3305431', 'FILE', '1985-07-09 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253992, '3305431', 'FILE', '1985-05-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253993, '3305431', 'FILE', '1985-05-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253994, '3305431', 'FILE', '1983-10-26 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253995, '3305431', 'FILE', '1983-01-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253996, '3305431', 'FILE', '1982-09-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253997, '3305431', 'FILE', '1981-08-11 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253998, '3305431', 'FILE', '1980-07-14 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (253999, '3305431', 'CONVDSO', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (254000, '3305431', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (254001, '3305431', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
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
                    ('3305431', null, 'BC', '1953-05-13 00:00:00', '1986-05-13 00:00:00', null, '573939057', '795766487966757', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3305431', 254001, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3305431', 254000, 254001, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('3305431', 253999, 254000, 'HDO', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('3305431', 'CO', 253983, 0, null, 'RKMBQQFKDKELJDWEFVQR', 'YRZSNCSCRJYOADDQPBILFXNLT', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3305431', 'RG', 253983, null, 79290, 79290, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('3305431', 'RC', 253983, null, 79290, 79290, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (79290, 'BC', 'CA', null, 'PIRRBBRRUFMWUYSAWEBFOZWPH', 'CRSJXA  QPDAMZCGBAXZTLQYA', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_C3793011": {
            "corp_num":'C3793011', "corp_typ_cd":'CUL', "state_typ_cd":'HAM', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5567530, 13559822, 13559823, 'C3793011', 'DIR', 13366519, null, null, null, null, null, null, 'Shelby', 'S.', 'Thomas', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5567531, 13559824, 13559825, 'C3793011', 'DIR', 13366519, null, null, null, null, null, null, 'Loeffler', 'A.', 'Christopher', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5567532, 13559826, 13559827, 'C3793011', 'DIR', 13366519, 13366556, null, null, null, null, '2016-12-30 09:40:29', 'Claggett', 'H.', 'David', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5567533, 13559834, null, 'C3793011', 'PAS', 13366519, null, null, null, null, '2016-12-30 09:40:29', null, 'NICKEL', 'A.', 'WILLIAM', null, null, null, 3, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5567534, 13559835, null, 'C3793011', 'PAS', 13366519, null, null, null, null, '2016-12-30 09:40:29', null, 'MCKEAGUE', 'J.', 'DAVID', null, null, null, 4, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5567535, 13559836, null, 'C3793011', 'PAS', 13366519, null, null, null, null, '2016-12-30 09:40:29', null, 'JONES', 'M.', 'LINDSAY', null, null, null, 5, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13366519, 'C3793011', 'FILE', '2016-12-30 09:40:29', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13366556, 'C3793011', 'FILE', '2016-12-30 09:48:32', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13366519, 'CONTU', '2016-12-30 09:40:29', '2016-12-30 00:00:00', null, null, null, 'N', '2016-12-30 00:00:00', null, 'P ', null, null, 'NR8669246', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13366556, 'NOCDR', '2016-12-30 09:48:32', '2016-12-30 00:00:00', null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('C3793011', null, 'CUL', '2016-12-30 09:40:29', null, null, '737867366', '271873671805903', null, 'ZSJNKWQS', 'UVAHMMUT', 'PBXHUBBHXZCR@VRYNKZPM.com', 'N', 'Y', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C3793011', 13366519, 13366802, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C3793011', 13366802, null, 'HAM', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C3793011', 13366519, null, null, 'AB', 'COR', '2013-02-21 00:00:00', null, '2017316262', null, 'Kiewit Engineering Canada ULC', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C3793011', 'CO', 13366519, 0, null, 'TKXYCIPUBRXWXQDMMPSR', 'SCIWCMGXWEBVYAWCYPLKVOCCH', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C3793011', 'SN', 13366519, 1, null, 'OACKRLUMDNLDETEDNLIG', 'SFEVTTFQUKMXDFWSARNU PBHM', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C3793011', 'RG', 13366519, null, 13559829, 13559828, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C3793011', 'RC', 13366519, null, 13559831, 13559830, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C3793011', 'SH', 13366519, null, 13559832, 13559833, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13559828, 'BC', 'CA', 'DHXRP1', 'YHDVNAN AIDREV GRGDFCCIPI', 'KCOZVZZVFTWSGXGEFOFJEYZNJ', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13559829, 'BC', 'CA', 'T87M0S', 'IZBP RHSVGTEUHASZDBGXJDS ', 'PYONXWRMZRPTUSIFTBMJWBPFI', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13559830, 'BC', 'CA', '8R7CZC', 'SUWSTXUQYNAKVHQWOFIIWYXA ', 'CYP HLZBQUBXZAIPFHBSMUTCU', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13559831, 'BC', 'CA', 'O2OG78', 'CJJUJASLWFQVPGMGPXH IQRNI', 'ZMIESNFAJSOGLRBAKDCSFNPLY', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13559832, 'BC', 'CA', 'IF24DD', 'PTSVHGVZGYTVRHAWFEFWH BYB', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13559833, 'SK', 'CA', 'RNH8XI', 'GVSXJNFVJUAOMDIHHLSJXTPS ', null, null, 'SASKATOON', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_6885343": {
            "corp_num":'6885343', "corp_typ_cd":'BC', "state_typ_cd":'LIQ', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":0, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (506019, 440484, 440484, '6885343', 'LIQ', 1678556, null, null, null, null, '2000-05-24 00:00:00', null, null, null, null, 'OUOISXUKWCKXKFPJUNHA', null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (506020, 440485, 440485, '6885343', 'DIR', 1678556, null, null, null, null, null, null, 'CARSON', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (506021, 440485, 440485, '6885343', 'OFF', 1678556, null, null, null, null, null, null, 'CARSON', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021588, null, null, '6885343', 'DIR', 1678556, 1678556, null, null, null, null, '1985-05-03 00:00:00', 'PETERS', null, 'FREDERICK A.', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021589, null, null, '6885343', 'DIR', 1678556, 1678556, null, null, null, null, '2000-02-08 00:00:00', 'JEFFERD', null, 'RAYMOND', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021590, null, null, '6885343', 'DIR', 1678556, 1678556, null, null, null, null, '1994-08-22 00:00:00', 'BOYCE', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (6021591, null, null, '6885343', 'DIR', 1678556, 1678556, null, null, null, null, '1985-05-03 00:00:00', 'BOYCE', null, 'WILLIAM PETER', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678556, '6885343', 'CONVICORP', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678557, '6885343', 'FILE', '2000-07-24 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678558, '6885343', 'FILE', '2000-03-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678559, '6885343', 'FILE', '2000-02-08 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678560, '6885343', 'FILE', '1999-08-23 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678561, '6885343', 'FILE', '1999-07-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678562, '6885343', 'FILE', '1999-07-30 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678563, '6885343', 'FILE', '1998-07-02 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678564, '6885343', 'FILE', '1997-07-07 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678565, '6885343', 'FILE', '1996-12-16 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678566, '6885343', 'FILE', '1996-02-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678567, '6885343', 'FILE', '1995-02-28 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678568, '6885343', 'FILE', '1994-08-19 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678569, '6885343', 'FILE', '1993-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678570, '6885343', 'FILE', '1991-12-06 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678571, '6885343', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678572, '6885343', 'FILE', '1991-03-01 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678573, '6885343', 'FILE', '1988-12-29 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678574, '6885343', 'FILE', '1988-01-21 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678575, '6885343', 'FILE', '1987-01-20 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678576, '6885343', 'FILE', '1985-12-31 00:00:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678577, '6885343', 'CONVDSF', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678578, '6885343', 'CONVRSTR', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (1678579, '6885343', 'CONVILIQ', '2004-03-26 20:36:00', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6637862, '6885343', 'ADMIN', '2005-10-21 10:15:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (6637857, '6885343', 'ADCORP', '2005-10-21 10:14:01', null)""",
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
                    ('6885343', null, 'BC', '1979-11-23 00:00:00', '1999-11-23 00:00:00', null, '157629775', '823400881860941', null, null, null, null, 'Y', 'N', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6885343', 1678579, null, 'LIQ', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6885343', 1678578, 1678579, 'ACT', null)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('6885343', 1678577, 1678578, 'HDF', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('6885343', 'CO', 1678556, 0, null, 'YNJXNRJCOMMDQULENGQU', 'WUPIFATV VTCHTORPTAMYBKFA', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6885343', 'RG', 1678556, null, 440483, 440483, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('6885343', 'RC', 1678556, null, 440483, 440483, null, null)""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (440483, 'BC', 'CA', 'YFSQI2', 'L VBWZTCQPZOHJGEJGVVWJOLM', 'BQXUEN DWENEHR UNUZCEHLDU', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_C2920969": {
            "corp_num":'C2920969', "corp_typ_cd":'CUL', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8590710, 14367108, 14367109, 'C2920969', 'DIR', 13890605, null, null, null, null, null, null, 'McDonald', null, 'Greg', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8590711, 14367116, null, 'C2920969', 'PAS', 13890605, null, null, null, null, '2017-10-02 10:11:26', null, 'RICHARDSON', 'B.', 'DOUGLAS', null, null, null, 1, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8599978, 14393963, null, 'C2920969', 'TAP', 13908789, null, null, null, null, '2017-10-11 11:41:44', null, 'Sur', 'Y.', 'Frank', 'QLBCQKBPVRBMHKIAWQKY', null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13895769, 'C2920969', 'SYST', '2017-10-03 15:18:13', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13890605, 'C2920969', 'FILE', '2017-10-02 10:11:26', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13891064, 'C2920969', 'FILE', '2017-10-02 11:45:44', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13908789, 'C2920969', 'SYST', '2017-10-11 11:41:44', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13890605, 'CONTI', '2017-10-02 10:11:26', '2017-10-02 00:00:00', null, null, null, 'N', '2017-10-02 00:00:00', null, 'F ', null, null, 'NR2307125', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13891064, 'NOALU', '2017-10-02 11:45:44', null, null, null, null, 'N', null, null, 'F ', 13891064, null, 'NR3853523', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13895769, 'CHGPN', '2017-10-03 15:18:13', null, null, null, null, 'N', null, null, 'F ', 13895769, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13908789, 'NWPTA', '2017-10-11 11:41:44', null, null, null, null, 'N', null, null, 'F ', 13908789, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('C2920969', null, 'CUL', '2017-10-02 10:11:26', null, null, '228619311', '642706915630680', null, 'MBOOYHFV', 'VIZIBVSL', 'MUXFFRWSHMIJ@UARJQECG.com', 'N', 'Y', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C2920969', 13890605, null, 'ACT', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C2920969', 13890605, null, null, 'AB', 'COR', '2014-02-14 00:00:00', null, '2018026316', 'A0100442', 'UNITED SUPPLIERS CANADA INC.', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C2920969', 'SN', 13895769, 1, null, 'TIVNULFZDFLXTDJMJEXG', 'WREOIXSJYLVOCXJMBEFZXAUXB', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C2920969', 'CO', 13890605, 0, 13891064, 'BHWOHECRXNZCEOWUVEDO', 'GGKKVPQRQXAALVUWEGZOIJQQQ', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C2920969', 'SN', 13890605, 1, 13895769, 'XKNFUCKHNKLLLXELEERQ', 'QDD  ZQRM VHQFMJJVIVKKKMN', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C2920969', 'CO', 13891064, 1, null, 'ZVMAHKFCMRIDGMBSCJWM', 'QSLMKYLBSKLEPYYMPNQNXONAX', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C2920969', 'AN', 13908789, 1, null, 'DZUUIJZDCTGORQHESRJI', 'USATFBWZZTRGNYSSTMGIWIDYX', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C2920969', 'RG', 13890605, null, 14367111, 14367110, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C2920969', 'RC', 13890605, null, 14367113, 14367112, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C2920969', 'SH', 13890605, null, 14367114, 14367115, null, 'Van-Corp-Regco@gowlingwlg.com')""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C2920969', 'TH', 13908789, null, 14393962, null, null, 'van-corp-regco@gowlingwlg.com')""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14367110, 'BC', 'CA', 'VOFQG0', 'MB YOGGW BQ VBDYDTEOWOSSE', 'ABTFLVOTTOCXLSXXPPMZLBHTF', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14367111, 'BC', 'CA', 'G8S6B6', 'MGKDAZQFZOPOVEMONHAPKRXEJ', 'FMVZ VWTLNZKRTLBZMIMAPZGK', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14367112, 'BC', 'CA', '7PTLB1', 'NTMMQBEHNBGRGOBDVQZAJDCOV', 'KZMGEUMRQCZB DUYVANXLTKTL', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14367113, 'BC', 'CA', 'BI8V31', 'MAZLYLTTMBNFFIHIESJOKSCAC', 'NBSYMFXOXNQCQDEIVOCEZONEG', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14367114, 'BC', 'CA', '2GQA0Y', 'AVQCAHXFFXUAZUPFRKTVZKZGS', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14367115, 'BC', 'CA', '1TGABM', 'CYUTZYHPITDSIHEDQGBGVUFZL', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (14393962, 'BC', 'CA', 'BHKSZQ', 'HGPMN YDVJZYEIIFHBKSLBQIU', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
    "corp_C8831865": {
            "corp_num":'C8831865', "corp_typ_cd":'C', "state_typ_cd":'ACT', "party_ct":0, "party_addr_ct":0, "name_ct":1, "name_assumed_ct":0, "name_trans_ct":0, "tilma_ct":0, "juisdiction_ct":1, 
             "sqls": [
                    """create table if not exists corp_party (corp_party_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, corp_num text, party_typ_cd text, start_event_id numeric, end_event_id numeric, prev_party_id numeric, corr_typ_cd text, last_report_dt timestamp, appointment_dt timestamp, cessation_dt timestamp, last_nme text, middle_nme text, first_nme text, business_nme text, bus_company_num text, email_address text, corp_party_seq_num numeric, office_notification_dt timestamp, phone text, reason_typ_cd text)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5080515, 12123550, 12123551, 'C8831865', 'DIR', 12425024, 13992757, null, null, null, null, null, 'Fisher', null, 'Keenan', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5080516, 12123552, 12123553, 'C8831865', 'DIR', 12425024, 13992757, null, null, null, null, null, 'Fisher', null, 'Kenneth', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5080517, 12123560, null, 'C8831865', 'PAS', 12425024, null, null, null, null, '2015-07-16 16:41:57', null, 'BERNAKEVITCH', 'L.', 'WAYNE', null, null, null, 2, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5080518, 12123561, null, 'C8831865', 'PAS', 12425024, null, null, null, null, '2015-07-16 16:41:57', null, 'CARLSON', 'W.', 'DARREN', null, null, null, 3, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8569728, 14305827, 14305827, 'C8831865', 'OFF', 13851296, null, 0, null, null, '2016-09-30 08:20:49', null, 'Fisher', null, 'Kenneth', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8569729, 14305828, 14305828, 'C8831865', 'OFF', 13851296, null, 0, null, null, '2016-09-30 08:20:49', null, 'Fisher', null, 'Keenan', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8645558, 14527100, 14527099, 'C8831865', 'DIR', 13992757, null, null, null, null, '2017-10-01 00:00:00', null, 'Anderson', null, 'Cory', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8645559, 14527102, 14527101, 'C8831865', 'DIR', 13992757, null, 5080516, null, null, null, null, 'Fisher', null, 'Kenneth', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (8645560, 14527104, 14527103, 'C8831865', 'DIR', 13992757, null, 5080515, null, null, null, null, 'Fisher', null, 'Keenan', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5482894, 13311152, 13311152, 'C8831865', 'OFF', 13204811, 13851296, 0, null, null, '2016-09-30 08:20:49', null, 'Fisher', null, 'Kenneth', null, null, null, null, null, null, null)""",
                    """insert into corp_party (corp_party_id, mailing_addr_id, delivery_addr_id, corp_num, party_typ_cd, start_event_id, end_event_id, prev_party_id, corr_typ_cd, last_report_dt, appointment_dt, cessation_dt, last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt, phone, reason_typ_cd)
                    values
                    (5482895, 13311153, 13311153, 'C8831865', 'OFF', 13204811, 13851296, 0, null, null, '2016-09-30 08:20:49', null, 'Fisher', null, 'Keenan', null, null, null, null, null, null, null)""",
                    """create table if not exists event (event_id numeric, corp_num text, event_typ_cd text, event_timestmp timestamp, trigger_dts timestamp)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13851296, 'C8831865', 'FILE', '2017-09-11 13:17:08', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13992757, 'C8831865', 'FILE', '2017-11-24 13:50:02', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12425738, 'C8831865', 'SYST', '2015-07-17 10:42:49', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12425024, 'C8831865', 'FILE', '2015-07-16 16:41:57', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12514456, 'C8831865', 'ADCORP', '2015-09-08 12:23:01', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12514464, 'C8831865', 'FILE', '2015-09-08 12:26:13', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (12558660, 'C8831865', 'ADCORP', '2015-10-02 16:04:11', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13204811, 'C8831865', 'FILE', '2016-09-30 08:20:49', null)""",
                    """insert into event (event_id, corp_num, event_typ_cd, event_timestmp, trigger_dts)
                    values
                    (13251336, 'C8831865', 'SYST', '2016-10-26 11:14:35', null)""",
                    """create table if not exists filing (event_id numeric, filing_typ_cd text, effective_dt timestamp, change_dt timestamp, registration_dt timestamp, period_end_dt timestamp, accession_num text, arrangement_ind text, auth_sign_dt timestamp, withdrawn_event_id numeric, ods_typ_cd text, dd_event_id numeric, access_cd text, nr_num text, court_appr_ind text, court_order_num text, agm_date timestamp, new_corp_num text)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (12425024, 'CONTI', '2015-07-16 16:41:57', '2015-07-16 00:00:00', null, null, null, 'N', '2015-07-16 00:00:00', null, 'F ', null, null, 'NR3170023', null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (12425738, 'TILHO', '2015-07-17 10:42:49', null, null, null, null, 'N', null, null, 'F ', 12425738, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (12514464, 'NOCAD', '2015-09-09 00:01:00', null, null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13204811, 'ANNBC', '2016-09-30 08:20:49', null, null, '2016-07-16 00:00:00', null, 'N', null, null, 'F ', null, '140723917', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13251336, 'TILHO', '2016-10-26 11:14:35', null, null, null, null, 'N', null, null, 'F ', 13251336, null, null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13851296, 'ANNBC', '2017-09-11 13:17:08', null, null, '2017-07-16 00:00:00', null, 'N', null, null, 'F ', null, '144621042', null, null, null, null, null)""",
                    """insert into filing (event_id, filing_typ_cd, effective_dt, change_dt, registration_dt, period_end_dt, accession_num, arrangement_ind, auth_sign_dt, withdrawn_event_id, ods_typ_cd, dd_event_id, access_cd, nr_num, court_appr_ind, court_order_num, agm_date, new_corp_num)
                    values
                    (13992757, 'NOCDR', '2017-11-24 13:50:02', '2017-10-01 00:00:00', null, null, null, 'N', null, null, 'F ', null, null, null, null, null, null, null)""",
                    """create table if not exists corporation (corp_num text, corp_frozen_typ_cd text, corp_typ_cd text, recognition_dts timestamp, last_ar_filed_dt timestamp, transition_dt timestamp, bn_9 text, bn_15 text, accession_num text, corp_password text, prompt_question text, admin_email text, send_ar_ind text, tilma_involved_ind text, tilma_cessation_dt timestamp, firm_last_image_date timestamp, os_session integer, last_agm_date timestamp, firm_lp_xp_termination_date timestamp, last_ledger_dt timestamp, ar_reminder_option text, ar_reminder_date text, temp_password text, temp_password_expiry_date timestamp)""",
                    """insert into corporation (corp_num, corp_frozen_typ_cd, corp_typ_cd, recognition_dts, last_ar_filed_dt, transition_dt, bn_9, bn_15, accession_num, corp_password, prompt_question, admin_email, send_ar_ind, tilma_involved_ind, tilma_cessation_dt, firm_last_image_date, os_session, last_agm_date, firm_lp_xp_termination_date, last_ledger_dt, ar_reminder_option, ar_reminder_date, temp_password, temp_password_expiry_date)
                    values
                    ('C8831865', null, 'C', '2015-07-16 16:41:57', '2017-07-16 00:00:00', null, '975013385', '740483982118592', null, 'RUBGECDH', 'GUYINJSE', 'SWJAQETFNJBW@GCPUQDGJ.com', 'N', 'Y', null, null, null, null, null, null, null, null, null, null)""",
                    """create table if not exists conv_event (event_id numeric, effective_dt timestamp, report_corp_ind text, prev_bc_ind text, activity_user_id text, activity_dt timestamp, activity_tm timestamp, annual_file_dt timestamp, corp_cre_typ_cd text, accession_num text, dd_event_id numeric, remarks text)""",
                    """create table if not exists corp_state (corp_num text, start_event_id numeric, end_event_id numeric, state_typ_cd text, dd_corp_num text)""",
                    """insert into corp_state (corp_num, start_event_id, end_event_id, state_typ_cd, dd_corp_num)
                    values
                    ('C8831865', 12425024, null, 'ACT', null)""",
                    """create table if not exists jurisdiction (corp_num text, start_event_id numeric, end_event_id numeric, dd_corp_num text, can_jur_typ_cd text, xpro_typ_cd text, home_recogn_dt timestamp, othr_juris_desc text, home_juris_num text, bc_xpro_num text, home_company_nme text, other_juris_party_id text)""",
                    """insert into jurisdiction (corp_num, start_event_id, end_event_id, dd_corp_num, can_jur_typ_cd, xpro_typ_cd, home_recogn_dt, othr_juris_desc, home_juris_num, bc_xpro_num, home_company_nme, other_juris_party_id)
                    values
                    ('C8831865', 12425024, null, null, 'AB', 'COR', '2013-06-03 00:00:00', null, '2017524386', null, 'TG Real Estate (SK) Limited', null)""",
                    """create table if not exists corp_name (corp_num text, corp_name_typ_cd text, start_event_id numeric, corp_name_seq_num numeric, end_event_id numeric, srch_nme text, corp_nme text, dd_corp_num text)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C8831865', 'CO', 12425024, 0, null, 'QUPZNKWOTSXBOOHVWHSQ', 'ZIXEUW DJKOKQXLOZPHLDNJWX', null)""",
                    """insert into corp_name (corp_num, corp_name_typ_cd, start_event_id, corp_name_seq_num, end_event_id, srch_nme, corp_nme, dd_corp_num)
                    values
                    ('C8831865', 'SN', 12425024, 1, null, 'FSVLVHOBPJTSIXLXHTBI', 'EIAOOVUFCLKUPXMQTZ H YNYT', null)""",
                    """create table if not exists office (corp_num text, office_typ_cd text, start_event_id numeric, end_event_id numeric, mailing_addr_id numeric, delivery_addr_id numeric, dd_corp_num text, email_address text)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'SH', 12425738, 13251336, 12124527, 12124528, null, 'corprecords@fmc-law.com')""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'RG', 12425024, 12514464, 12123555, 12123554, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'RC', 12425024, 12514464, 12123557, 12123556, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'SH', 12425024, 12425738, 12123558, 12123559, null, 'corprecords@fmc-law.com')""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'RG', 12514464, null, 12255170, 12255169, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'RC', 12514464, null, 12255168, 12255167, null, null)""",
                    """insert into office (corp_num, office_typ_cd, start_event_id, end_event_id, mailing_addr_id, delivery_addr_id, dd_corp_num, email_address)
                    values
                    ('C8831865', 'SH', 13251336, null, 13382364, 13382365, null, 'corporateserviceskelowna@farris.com')""",
                    """create table if not exists address (addr_id numeric, province text, country_typ_cd text, postal_cd text, addr_line_1 text, addr_line_2 text, addr_line_3 text, city text, address_format_type text, address_desc text, address_desc_short text, delivery_instructions text, unit_no text, unit_type text, civic_no text, civic_no_suffix text, street_name text, street_type text, street_direction text, lock_box_no text, installation_type text, installation_name text, installation_qualifier text, route_service_type text, route_service_no text, province_state_name text)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12123554, 'BC', 'CA', '19HVKW', 'VKUZMQBYXQDYLMQW P USNARD', 'INSYSPA YZ RIHMXBHZKDHSTM', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12123555, 'BC', 'CA', 'L2RJDJ', 'XZMGBPQNFITFUQZROREQ ZX L', 'NB WMOOZTGEALN QNFBCCHRSJ', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12123556, 'BC', 'CA', 'S1Q12S', 'OZCLZPLNEWNRXGRVOLWCMSENN', 'LEVIKTXYB OTSEIJALDVXSJLW', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12123557, 'BC', 'CA', 'B98E00', 'QKOHXY XEUCGVUAKVINRKYJYL', 'DTNLTATNQWXEKORJMHNHHGPRG', null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12123558, 'BC', 'CA', 'GFYEKF', 'ZSLRJOQSOEXLKCNLUBNRBH HJ', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12123559, 'BC', 'CA', 'M41OAN', 'MEBHMBPDFUHPMZQJKFQVKLMUB', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12124527, 'BC', 'CA', '0EIKS9', 'DYBLZXG TSXOWHY UCSUJHOSG', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12124528, 'BC', 'CA', 'PVHH59', 'YDPEXBUQAVCJVBHRVUBTBGCIA', null, null, 'Vancouver', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12255167, 'BC', 'CA', 'PDJZTB', 'CKXBPYDKCHUTSXCKHQSKYFICZ', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12255168, 'BC', 'CA', 'PWUGN0', ' GTFMDSDDGQUPHWLTAILFIXWV', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12255169, 'BC', 'CA', 'O2YNFG', 'AHHDYANWMDN LAEVFHRP WMMY', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (12255170, 'BC', 'CA', 'LDM9R9', 'HHKYPDSNZKBHYPOLKHHDFXGVG', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13382364, 'BC', 'CA', 'LV4289', 'OFYSEQQT BOMZHNPXM KJIXIC', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                    """insert into address (addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type, address_desc, address_desc_short, delivery_instructions, unit_no, unit_type, civic_no, civic_no_suffix, street_name, street_type, street_direction, lock_box_no, installation_type, installation_name, installation_qualifier, route_service_type, route_service_no, province_state_name)
                    values
                    (13382365, 'BC', 'CA', '8J81WO', 'TMNPYYIRBFWRYCUNONRGPLGDN', null, null, 'Kelowna', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null)""",
                   ]
             },
}
