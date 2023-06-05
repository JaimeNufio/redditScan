import connect

dbConnection = connect
db = dbConnection.connectionManager()
# print(manager)

# db.createTable('comments')
db.createTable('submissions')

# db.execute("DROP TABLE if exists test")

# db.execute("CREATE TABLE test (id serial PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL);")

# cur.execute("DROP TABLE test")
# conn.commit()