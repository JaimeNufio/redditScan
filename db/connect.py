import psycopg2
import collections
from pprint import pprint

class connectionManager: 

    conn = None
    cur = None

    def connect(self,auth):

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

    def execute (self,command):
        print("Executing:", command)
        self.cur.execute(command)
        self.conn.commit()

    def createTable(self,table):
        try:
            with open('db/tables/{}.sql'.format(table),'r') as f:
                # self.execute('{}'.format(table))
                self.execute(f.read())
        except Exception as e:
            print("Error:",e)

    def insertMany(self,objs,table):

        batch = []
        for obj in objs:
            ordered_dict = collections.OrderedDict.fromkeys(obj, None)
            ordered_dict.update(obj.items())
            batch.append(ordered_dict)
        

        pprint(batch)


    def __init__(self,auth):
        self.connect(auth)
