import praw,json,pprint


def connect():
    keys = open('keys.json')
    auth = json.load(keys)
    keys.close()


    # Create the Reddit instance
    reddit = praw.Reddit(
        client_id=auth['client_id'],
        client_secret=auth['client_secret'],
        user_agent=auth['user_agent']
    )

    return reddit

def getSubPosts(reddit):
    # Get the top post in a subreddit
    subreddit = reddit.subreddit('njtech')
    top_post = subreddit.top(limit=1)

    # Print the title of the top post
    for post in top_post:
        # pprint.pprint(vars(post)['created','id','num_comments','score','title','url'])
        postGot = vars(post)
        obj = {
            'created':postGot['created'],
            'id':postGot['id'],
            'num_comments':postGot['num_comments'],
            'score':postGot['score'],
            'title':postGot['title'],
            'url':postGot['url']
        }

        print(obj)


reddit = connect()
getSubPosts(reddit)