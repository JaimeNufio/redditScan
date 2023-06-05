import psycopg2
import json

class connectionManager: 

    conn = None
    cur = None

    def createConnection(self):

        keys = open('keys.json')
        auth = json.load(keys)
        keys.close()

        self.conn = psycopg2.connect(host=auth['host'], 
            port=auth['port'], 
            dbname=auth['dbname'],
            user=auth['user'], 
            password=auth['password'])

        self.cur = self.conn.cursor()

        if self.conn.status == psycopg2.extensions.STATUS_READY:
            print("Connection is ready!")
        else:
            print("Connection is not ready!")
            return

    def __str__(self):
        return 'test'

    def execute (self,command):
        print("Executing:", command)
        self.cur.execute(command)
        self.conn.commit()

    def createTable(self,table):
        try:
            with open('tables/{}.sql'.format(table),'r') as f:
                self.execute('drop table if exists {}'.format(table))
                self.execute(f.read())
        except Exception as e:
            print("Error:",e)

    def __init__(self):
        self.createConnection()
