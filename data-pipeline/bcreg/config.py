#!/usr/bin/python
from configparser import ConfigParser
import os 
 
def config(filename='database.ini', section='postgresql'):
    db = {}
    if section == 'bc_registries':
        db['host'] = os.environ.get('BC_REG_DB_HOST', 'localhost')
        db['port'] = os.environ.get('BC_REG_DB_PORT', '5454')
        db['database'] = os.environ.get('BC_REG_DB_DATABASE', 'BC_REGISTRIES')
        db['user'] = os.environ.get('BC_REG_DB_USER', '')
        db['password'] = os.environ.get('BC_REG_DB_PASSWORD', '')
    elif section == 'bc_reg_lear':
        db['host'] = os.environ.get('LEAR_DB_HOST', 'localhost')
        db['port'] = os.environ.get('LEAR_DB_PORT', '5455')
        db['database'] = os.environ.get('LEAR_DB_DATABASE', 'lear')
        db['user'] = os.environ.get('LEAR_DB_USER', '')
        db['password'] = os.environ.get('LEAR_DB_PASSWORD', '')
    elif section == 'event_processor':
        db['host'] = os.environ.get('EVENT_PROC_DB_HOST', 'localhost')
        db['port'] = os.environ.get('EVENT_PROC_DB_PORT', '5444')
        db['database'] = os.environ.get('EVENT_PROC_DB_DATABASE', 'bc_reg_db')
        db['user'] = os.environ.get('EVENT_PROC_DB_USER', 'bc_reg_db')
        db['password'] = os.environ.get('EVENT_PROC_DB_PASSWORD', '')
    elif section == 'org_book':
        db['host'] = os.environ.get('ORGBOOK_DB_HOST', 'localhost')
        db['port'] = os.environ.get('ORGBOOK_DB_PORT', '5432')
        db['database'] = os.environ.get('ORGBOOK_DB_DATABASE', 'THE_ORG_BOOK')
        db['user'] = os.environ.get('ORGBOOK_DB_USER', 'DB_USER')
        db['password'] = os.environ.get('ORGBOOK_DB_PASSWORD', 'DB_PASSWORD')
    else:
        raise Exception('Section {0} not a valid database'.format(section))
 
    return db

