import psycopg2
import json

keys = open('db/keys.json')
auth = json.load(keys)
keys.close()

conn = psycopg2.connect(host=auth['host'], 
    port=auth['port'], 
    dbname=auth['dbname'],
    user=auth['user'], 
    password=auth['password'])

cur = conn.cursor()

if conn.status == psycopg2.extensions.STATUS_READY:
    print("Connection is ready!")
else:
    print("Connection is not ready!")

cur.execute("DROP TABLE submissions")
conn.commit()

cur.execute("CREATE TABLE submissions (id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL);")
conn.commit()

cur.execute("DROP TABLE submissions")
conn.commit()