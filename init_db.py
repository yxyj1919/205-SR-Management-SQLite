import os
import psycopg2

conn = psycopg2.connect(
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
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS srtable;')
cur.execute('CREATE TABLE srtable (id serial PRIMARY KEY,'
                                 'sr text NOT NULL, '
                                 'owner varchar (150) NOT NULL,'
                                 'pr integer DEFAULT 999999,'
                                 'comment text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

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

conn.commit()

cur.close()
conn.close()