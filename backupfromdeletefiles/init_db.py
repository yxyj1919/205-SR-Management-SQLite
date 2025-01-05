import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="9003",
    database="sr_db",
    # user=os.environ['DB_USERNAME'],
    # password=os.environ['DB_PASSWORD']
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD')
    # user="postgres",
    # password="password"
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
            ('100001',
             'User1',
             'DISK Issue')
            )

cur.execute('INSERT INTO srtable (sr, owner, pr, comment)'
            'VALUES (%s, %s, %s, %s)',
            ('100002',
             'User2',
             '200002',
             'FAN Issue')
            )

cur.execute('INSERT INTO srtable (sr, owner, pr, comment)'
            'VALUES (%s, %s, %s, %s)',
            ('100003',
             'User3',
             '200003',
             'Power Issue')
            )
conn.commit()

cur.close()
conn.close()