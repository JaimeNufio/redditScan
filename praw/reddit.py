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

def getSubmissionsFromSubreddit(sub):
    # Get the top post in a subreddit
    subreddit = reddit.subreddit(sub)
    top_post = subreddit.top(limit=10)

    # Print the title of the top post
    for post in top_post:
        postGot = vars(post)
        obj = {
            'created':postGot['created'],
            'id':postGot['id'],
            'num_comments':postGot['num_comments'],
            'score':postGot['score'],
            'title':postGot['title'],
            'url':postGot['url'],
            'selftext':postGot['selftext'],
            'over_18':postGot['over_18'],
            'author':str(postGot['author']),
            'subreddit':str(postGot['subreddit']),
            'permalink':postGot['permalink']
        }

        pprint.pprint(vars(post))

def getCommentsOnSubmission():
    pass

reddit = connect()
getSubmissionsFromSubreddit('njtech')