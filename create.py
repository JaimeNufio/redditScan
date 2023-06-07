import json
from db import connect
from redditapi_praw import reddit
from pprint import pprint

keys = open('keys.json')
auth = json.load(keys)
keys.close()

db = connect.connectionManager(auth['db'])
db.createTable('comments')
db.createTable('submissions')

r = reddit.redditManager(auth['reddit'])
r.getSubmissionsFromSubreddit('njtech',db.insertMany)
