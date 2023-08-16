import os
import psycopg2

#DB=password
#DB_USERNAME=postgress
#DB_NAME=sr_db
#DB_SERVER=postgres

class PreCheckDB():
    def __init__(self, conn=None):
        self.conn = conn
    def check(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                    host="10.117.203.153",
                    port="9004",
                    database="sr_db",
                    #user=os.environ['DB_USERNAME'],
                    #password=os.environ['DB_PASSWORD']
                    user = os.getenv('DB_USERNAME'),
                    password = os.getenv('DB_PASSWORD')
                    #user="postgres",
                    #password="password"
                    )

        # Open a cursor to perform database operations
        cur = self.conn.cursor()

        # Check if the table is existed
        # https://www.programcreek.com/python/?CodeExample=check%20table%20exists
        cur.execute("SELECT COUNT(*) FROM pg_class WHERE relname='srtable';")
        ret = bool(cur.fetchone()[0])
        #print(ret)
        if ret :
            print('The Table is existed')
        else:
            print('The Table is not existed, and will create one')
            # Execute a command: this creates a new table
            print('Creating the table')
            cur.execute('DROP TABLE IF EXISTS srtable;')
            cur.execute('CREATE TABLE srtable (id serial PRIMARY KEY,'
                                         'sr text NOT NULL, '
                                         'owner varchar (150) NOT NULL,'
                                         'pr integer DEFAULT 999999,'
                                         'comment text,'
                                         'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                         )
            # Insert data into the table
            print('Inserting data...')
            cur.execute('INSERT INTO srtable (sr, owner, comment)'
                    'VALUES (%s, %s, %s)',
                    ('23452847208',
                     'Dan HU',
                     '虚机恢复快照提示文件被锁定')
                    )
            cur.execute('INSERT INTO srtable (sr, owner, pr, comment)'
                    'VALUES (%s, %s, %s, %s)',
                    ('23453280308',
                     'Chang WANG',
                     '222222',
                     'SST-PP Issue')
                    )
            self.conn.commit()
            print('The table has been created')

            cur.close()
            self.conn.close()