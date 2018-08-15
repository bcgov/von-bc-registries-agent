
import sqlite3
import time
from bcreg.bcregistries import BCRegistries


def test_connect_sqlite3():
	# connect to an in-mem database and create a cursor
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')
    
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    
    # Save (commit) the changes
    conn.commit()

    # Do this instead
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print(c.fetchone())

    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
	             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
	             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
	            ]
    c.executemany('INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (?,?,?,?,?)', purchases)

    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def test_load_bcreg_table():
    # connect to an in-mem database and create a cursor
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    with BCRegistries() as bc_registries:
        desc = bc_registries.get_bcreg_table_struct('party_type')
        #print('party_type:', desc)
        create_table = bc_registries.create_table_sql('party_type', desc)
        #print('party_type:', create_table)
        c.execute(create_table)

        desc = bc_registries.get_bcreg_table_struct('corporation', "corp_num = '0641655'")
        #print('corporation:', desc)
        create_table = bc_registries.create_table_sql('corporation', desc)
        #print('corporation:', create_table)
        c.execute(create_table)

        desc = bc_registries.get_bcreg_table_struct('jurisdiction', "corp_num = 'REG0000185'")
        #print('jurisdiction:', desc)
        create_table = bc_registries.create_table_sql('jurisdiction', desc)
        #print('jurisdiction:', create_table)
        c.execute(create_table)

        desc = bc_registries.get_bcreg_table_struct('event', "corp_num = '0641655'")
        #print('event:', desc)
        create_table = bc_registries.create_table_sql('event', desc)
        #print('event:', create_table)
        c.execute(create_table)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def test_cache_bcreg_table():
    with BCRegistries(True) as bc_registries:
        rows = bc_registries.get_bcreg_table('party_type', '', '', True)
        c_rows = bc_registries.get_cache_sql('SELECT * FROM party_type')
        assert len(rows) == len(c_rows)
        assert rows == c_rows
        
        rows = bc_registries.get_bcreg_table('corporation', "corp_num = '0641655'", '', True)
        c_rows = bc_registries.get_cache_sql('SELECT * FROM corporation')
        assert len(rows) == len(c_rows)
        assert rows == c_rows
        
        rows = bc_registries.get_bcreg_table('event', "corp_num = '0641655'", '', True)
        c_rows = bc_registries.get_cache_sql('SELECT * FROM event')
        assert len(rows) == len(c_rows)
        assert rows == c_rows
        
        rows = bc_registries.get_bcreg_table('jurisdiction', "corp_num = 'REG0000185'", '', True)
        c_rows = bc_registries.get_cache_sql('SELECT * FROM jurisdiction')
        assert len(rows) == len(c_rows)
        assert rows == c_rows
        
def test_cache_bcreg_clients():
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
                    ]
    with BCRegistries(True) as bc_registries:
        start_time = time.perf_counter()
        bc_registries.cache_bcreg_corps(specific_corps)
        caching_time = time.perf_counter() - start_time
        print(caching_time)

