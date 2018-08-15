#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from bcreg.config import config

system_type = 'BC_REG'


# custom encoder to convert wierd data types to strings
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (list, dict, str, int, float, bool, type(None))):
            return JSONEncoder.default(self, o)        
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        if isinstance(o, set):
            return list(o)
        if isinstance(o, map):
            return list(o)
        return json.JSONEncoder.default(self, o)


# interface to BC Registries database
# data is returned as dictionaries, using the sql column name as identifier
class BCRegistriesBaseline:
    def __init__(self):
        try:
            params = config(section='bc_registries')
            self.conn = psycopg2.connect(**params)
        except (Exception) as error:
            print(error)
            self.conn = None
            raise

    def __del__(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        # todo
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # todo
        pass

    
    # get max event number from bc registries event log
    def get_max_event(self):
        cur = None
        try:
            # create a cursor
            cur = self.conn.cursor()
            cur.execute("""SELECT max(event_id) FROM bc_registries.event""")
            row = cur.fetchone()
            cur.close()
            cur = None
            return row[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # return a specific set of corporations, based on an event range
    def get_specific_corps(self, corp_filter):
        sql = """SELECT distinct(corp_num) from bc_registries.event
                where corp_num in ({})
                order by corp_num;"""
        cur = None
        try:
            cur = self.conn.cursor()
            placeholders= ', '.join(['%s']*len(corp_filter))  # "%s, %s, %s, ... %s"
            sql = sql.format(placeholders)
            cur.execute(sql, tuple(corp_filter))
            row = cur.fetchone()
            corps = []
            while row is not None:
                # print(row)
                corps.append({'CORP_NUM':row[0],})
                row = cur.fetchone()
            cur.close()
            cur = None
            return corps
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # return unprocessed corporations, based on an event range
    def get_unprocessed_corps(self, last_event_id, max_event_id):
        cur = None
        try:
            cur = self.conn.cursor()
            cur.execute("""SELECT distinct(corp_num) from bc_registries.event
                            where event_id > %s and event_id <= %s
                            and corp_num in
                            (SELECT corp_num from bc_registries.corporation
                             where corp_typ_cd in ('A','LLC','BC','C','CUL','ULC'))
                            order by corp_num;""", (last_event_id, max_event_id,))
            row = cur.fetchone()
            corps = []
            while row is not None:
                # print(row)
                corps.append({'CORP_NUM':row[0],})
                row = cur.fetchone()
            cur.close()
            cur = None
            return corps
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    #return the (unprocessed) event range for each provided corporation
    def get_unprocessed_corp_events(self, last_event_id, max_event_id, corps, max=None):
        cur = None
        try:
            for i,corp in enumerate(corps): 
                # create a cursor
                # print(corp['CORP_NUM'])
                cur = self.conn.cursor()
                cur.execute("""SELECT max(event_id) from bc_registries.event
                                where corp_num = %s and event_id > %s and event_id <= %s""", 
                                (corp['CORP_NUM'], last_event_id, max_event_id,))
                row = cur.fetchone()
                corp['PREV_EVENT_ID'] = last_event_id
                corp['LAST_EVENT_ID'] = row[0]
                cur.close()
                cur = None
                if max and i >= max:
                    break
            return corps
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise
        finally:
            if cur is not None:
                cur.close()

    # find a specific event, 
    # return None if not found
    def get_event(self, corp_num, event_id):
        sql = """SELECT event_id, corp_num, event_typ_cd, event_timestmp
                    FROM bc_registries.event
                    WHERE corp_num = %s and event_id = %s"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (corp_num, event_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(event) > 0:
                return event[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_filing_event(self, corp_num, event_id):
        sql_filing = """SELECT * from bc_registries.filing 
                        WHERE event_id = %s"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_filing, (event_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            filing_event = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(filing_event) > 0:
                return filing_event[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_office(self, corp_num):
        sql_office = """SELECT * from bc_registries.office
                        WHERE corp_num = %s and office_typ_cd in ('RG','HD','FO') and end_event_id is null"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_office, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            offices = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None

            for office in offices:
                office['delivery_addr'] = self.get_address(office['delivery_addr_id'])
                if 'mailing_addr_id' in office and office['mailing_addr_id'] != office['delivery_addr_id']:
                    office['mailing_addr'] = self.get_address(office['mailing_addr_id'])
                office['start_event'] = self.get_event(corp_num, office['start_event_id'])
                office['start_filing_event'] = self.get_filing_event(corp_num, office['start_event_id'])

            return offices
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_address(self, address_id):
        sql_addr = """SELECT addr_id, province, country_typ_cd, postal_cd, addr_line_1, addr_line_2, addr_line_3, city, address_format_type,
                         address_desc, address_desc_short, unit_no, unit_type, province_state_name
                  FROM bc_registries.address
                  WHERE addr_id = %s"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_addr, (address_id,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            addresses = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(addresses) >  0:
                address = addresses[0]
                if 'addr_line_1' in address and address['addr_line_1'] is not None:
                    address['local_addr'] = self.addr_line(address['addr_line_1'], ', ') + \
                                                self.addr_line(address['addr_line_2'], ', ') + \
                                                self.addr_line(address['addr_line_3'], ', ') + \
                                                self.addr_line(address['city'], ', ') + \
                                                self.addr_line(address['province'], ', ') + \
                                                self.addr_line(address['postal_cd'], ', ') + \
                                                self.addr_line(address['country_typ_cd'], '')
                elif 'address_desc' in address and address['address_desc'] is not None:
                    address['local_addr'] = address['address_desc']
                else:
                    address['local_addr'] = ""
                return address
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_names(self, corp_num, name_typ_cds, event_id):
        sql_name = """SELECT corp_num, corp_name_typ_cd, start_event_id, end_event_id, corp_name_seq_num, srch_nme, corp_nme, dd_corp_num
                  FROM bc_registries.corp_name
                  WHERE corp_num = %s AND end_event_id is null 
                    AND corp_name_typ_cd in ({}) """

        cur = None
        try:
            names = []
            cur = self.conn.cursor()
            placeholders= ', '.join(['%s']*len(name_typ_cds))  # "%s, %s, %s, ... %s"
            sql_name = sql_name.format(placeholders)
            cur.execute(sql_name, (corp_num,) + tuple(name_typ_cds))
            row = cur.fetchone()
            while row is not None:
                corp_name = {}
                corp_name['corp_num'] = row[0]
                corp_name['corp_name_typ_cd'] = row[1]
                corp_name['start_event_id'] = row[2]
                corp_name['start_event'] = self.get_event(row[0], row[2])
                corp_name['start_filing_event'] = self.get_filing_event(row[0], row[2])
                corp_name['end_event_id'] = row[3]
                corp_name['corp_name_seq_num'] = row[4]
                corp_name['srch_nme'] = row[5]
                corp_name['corp_nme'] = row[6]
                corp_name['dd_corp_num'] = row[7]
                names.append(corp_name)
                row = cur.fetchone()
            cur.close()
            cur = None
            return names
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cur is not None:
                cur.close()

    def get_corp_active_date(self, corp):
        sql_state = """SELECT state.corp_num corp_num, state.start_event_id start_event_id, state.end_event_id end_event_id, 
                        state.state_typ_cd state_typ_cd, state.dd_corp_num dd_corp_num, 
                        op_state.op_state_typ_cd op_state_typ_cd, op_state.short_desc short_desc, op_state.full_desc full_desc
                        FROM bc_registries.corp_state state, bc_registries.corp_op_state op_state
                        WHERE corp_num = %s and op_state.state_typ_cd = state.state_typ_cd"""
        cursor = None
        try:
            #print('Read event and filing history to determine date')
            cursor = self.conn.cursor()
            cursor.execute(sql_state, (corp['corp_num'],))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            corp_states = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            for corp_state in corp_states:
                #print('     ' + corp_state['corp_num'] + ' ' + corp_state['state_typ_cd'] + ' ' + corp_state['op_state_typ_cd'] + ' ' + str(corp_state['start_event_id']))
                corp_state['start_event'] = self.get_event(corp_state['corp_num'], corp_state['start_event_id'])
                corp_state['start_filing_event'] = self.get_filing_event(corp_state['corp_num'], corp_state['start_event_id'])
                if 'effective_dt' in corp_state['start_filing_event']:
                    corp_state['effective_date'] = corp_state['start_filing_event']['effective_dt']
                else:
                    corp_state['effective_date'] = corp_state['start_event']['event_timestmp']
                #print('     ' + corp_state['corp_num'] + ' ' + corp_state['state_typ_cd'] + ' ' + corp_state['op_state_typ_cd'] + ' ' + str(corp_state['start_event_id']) + ' ' + str(corp_state['effective_date']))
            sorted_corp_states = sorted(corp_states, key=lambda k: k['effective_date'], reverse=True)
            active_date = None
            for corp_state in sorted_corp_states:
                if corp_state['op_state_typ_cd'] == 'ACT':
                    if 'effective_dt' in corp_state['start_filing_event']:
                        active_date = corp_state['start_filing_event']['effective_dt']
                    else:
                        active_date = corp_state['start_event']['event_timestmp']
                else:
                    return active_date
                #print('    --> ' + corp['corp_num'] + ' ' + str(active_date))
            return active_date

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_corp_state_date(self, corp):
        corp_state = corp['corp_state']
        if corp_state is None:
            return corp['recognition_dts']
        else:
            if corp_state['op_state_typ_cd'] == 'HIS':
                # for historical corps pull the effective date from the filing or event
                #print('  ' + corp['corp_num'] + ' Get corp historical date')
                if 'effective_dt' in corp_state['start_filing_event']:
                    return corp_state['start_filing_event']['effective_dt']
                else:
                    return corp_state['start_event']['event_timestmp']
            else:
                # for active corps find the date of activation
                #print('  ' + corp['corp_num'] + ' Get corp active date')
                if corp_state['state_typ_cd'] == 'ACT':
                    if 'effective_dt' in corp_state['start_filing_event']:
                        return corp_state['start_filing_event']['effective_dt']
                    else:
                        return corp_state['start_event']['event_timestmp']
                else:
                    # some other "active" status, when was corp previously activated?
                    return self.get_corp_active_date(corp)


    def get_corp_state(self, corp_num):
        sql_state = """SELECT state.corp_num corp_num, state.start_event_id start_event_id, state.end_event_id end_event_id, 
                        state.state_typ_cd state_typ_cd, state.dd_corp_num dd_corp_num, 
                        op_state.op_state_typ_cd op_state_typ_cd, op_state.short_desc short_desc, op_state.full_desc full_desc
                        FROM bc_registries.corp_state state, bc_registries.corp_op_state op_state
                        WHERE corp_num = %s and end_event_id is null and op_state.state_typ_cd = state.state_typ_cd"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_state, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            corp_state = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(corp_state) > 0:
                return corp_state[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_jurisdicton(self, corp_num):
        sql_juris = """SELECT corp_num, start_event_id, end_event_id, j.can_jur_typ_cd can_jur_typ_cd,
                                home_recogn_dt, othr_juris_desc, home_juris_num, home_company_nme,
                                short_desc, full_desc
                        FROM bc_registries.jurisdiction j, bc_registries.jurisdiction_type jt
                        WHERE j.corp_num = %s and j.end_event_id is null
                          AND j.can_jur_typ_cd = jt.can_jur_typ_cd"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_juris, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            jurisdiction = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(jurisdiction) > 0:
                return jurisdiction[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_corp_type(self, corp_typ_cd):
        sql_type = """SELECT corp_typ_cd, colin_ind, corp_class, short_desc, full_desc
                        FROM bc_registries.corp_type
                        WHERE corp_typ_cd = %s"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_type, (corp_typ_cd,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            corp_type = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(corp_type) > 0:
                return corp_type[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def get_tilma_involveds(self, corp_num):
        sql_tilma = """SELECT * from bc_registries.tilma_involved
                        WHERE corp_num = %s and end_event_id is null and involved_ind = 'Y'"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_tilma, (corp_num,))
            desc = cursor.description
            column_names = [col[0] for col in desc]
            tilma_type = [dict(zip(column_names, row))  
                for row in cursor]
            cursor.close()
            cursor = None
            if len(tilma_type) > 0:
                return tilma_type[0]
            return {}
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cursor is not None:
                cursor.close()

    def addr_line(self, addr_element, delimiter):
        if addr_element is not None:
            return addr_element + delimiter
        return ''

    def get_basic_corp_info(self, corp_num, event_id):
        sql_corp = """SELECT corp_num, corp_typ_cd, recognition_dts, last_ar_filed_dt, bn_9, bn_15, admin_email, last_ledger_dt
                 FROM bc_registries.corporation
                 WHERE corp_num = %s"""

        cur = None
        try:
            corp = {}

            # assume there is just one corp record
            cur = self.conn.cursor()
            cur.execute(sql_corp, (corp_num,))
            row = cur.fetchone()
            corp['corp_num'] = row[0]
            corp['jurisdiction'] = self.get_jurisdicton(row[0])
            corp['corp_typ_cd'] = row[1]
            corp['corp_type'] = self.get_corp_type(row[1])
            corp['recognition_dts'] = row[2]
            corp['last_ar_filed_dt'] = row[3]
            corp['bn_9'] = row[4]
            corp['bn_15'] = row[5]
            corp['admin_email'] = row[6]
            corp['last_ledger_dt'] = row[7]
            cur.close()
            cur = None
     
            # get corp names
            corp['org_names'] = self.get_names(corp_num, ['CO','NB'], event_id)
            corp['org_name_assumed'] = self.get_names(corp_num, ['AS'], event_id)
            corp['org_name_trans'] = self.get_names(corp_num, ['TR', 'NO'], event_id)
            corp['office'] = self.get_office(corp_num)

            # other corp attributes
            corp['corp_state'] = self.get_corp_state(corp_num)
            #print(corp['corp_num'] + ' corp_state = ' + corp['corp_state']['state_typ_cd'] + ' ' + corp['corp_state']['op_state_typ_cd'])
            if corp['corp_state'] is not None: 
                corp['corp_state']['start_event'] = self.get_event(corp['corp_num'], corp['corp_state']['start_event_id'])
                corp['corp_state']['start_filing_event'] = self.get_filing_event(corp['corp_num'], corp['corp_state']['start_event_id'])
            corp['corp_state_dt'] = self.get_corp_state_date(corp)
            #print('--> ' + corp['corp_num'] + ' corp_state_dt = ' + str(corp['corp_state_dt']))
            corp['tilma_involved'] = self.get_tilma_involveds(corp_num)

            return corp
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cur is not None:
                cur.close()

    def get_bc_reg_corp_info(self, corp_num, event_id):
        sql_party = """SELECT corp_num, corp_party_id, mailing_addr_id, delivery_addr_id, party_typ_cd, start_event_id, end_event_id, cessation_dt,
                         last_nme, middle_nme, first_nme, business_nme, bus_company_num, email_address, corp_party_seq_num, office_notification_dt,
                         phone, reason_typ_cd
                  FROM bc_registries.corp_party
                  WHERE bus_company_num = %s AND party_typ_cd = 'FBO' AND end_event_id is null"""

        cur = None
        try:
            corp = self.get_basic_corp_info(corp_num, event_id)

            # get parties
            corp['parties'] = []
            cur = self.conn.cursor()
            cur.execute(sql_party, (corp_num,))
            row = cur.fetchone()
            while row is not None:
                corp_party = {}
                corp_party['corp_num'] = row[0]
                corp_party['corp_party_id'] = row[1]
                corp_party['mailing_addr_id'] = row[2]
                corp_party['mailing_addr'] = self.get_address(row[2])
                corp_party['delivery_addr_id'] = row[3]
                corp_party['delivery_addr'] = self.get_address(row[3])
                corp_party['party_typ_cd'] = row[4]
                corp_party['start_event_id'] = row[5]
                corp_party['start_event'] = self.get_event(row[0], row[5])
                corp_party['start_filing_event'] = self.get_filing_event(row[0], row[5])
                corp_party['end_event_id'] = row[6]
                corp_party['cessation_dt'] = row[7]
                corp_party['last_nme'] = row[8]
                corp_party['middle_nme'] = row[9]
                corp_party['first_nme'] = row[10]
                corp_party['business_nme'] = row[11]
                corp_party['bus_company_num'] = row[12]
                corp_party['email_address'] = row[13]
                corp_party['corp_party_seq_num'] = row[14]
                corp_party['office_notification_dt'] = row[15]
                corp_party['phone'] = row[16]
                corp_party['reason_typ_cd'] = row[17]
                # note we need to pull corporate info for DBA companies
                #corp_party['dba_names'] = self.get_names(corp_party['corp_num'], ['CO','NB'], event_id)
                corp_party['corp_info'] = self.get_basic_corp_info(corp_party['corp_num'], event_id)

                #corp_party['office'] = self.get_office(corp_party['corp_num'])
                corp['parties'].append(corp_party)
                row = cur.fetchone()
            cur.close()
            cur = None

            return corp
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise 
        finally:
            if cur is not None:
                cur.close()

    # convert object to JSON, converting data types (decimal, date) to string
    def to_json(self, data):
        ret = json.dumps(data, cls=CustomJsonEncoder, default=str)
        return ret

