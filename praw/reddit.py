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
    subredditPosts = reddit.subreddit(sub).top(limit=1000)
    # for i in range(1000):

    # Print the title of the top post
    for post in subredditPosts:
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

        pprint.pprint((obj))

        getCommentsOnSubmission(post)

def getCommentsOnSubmission(submission):
    submission.comments.replace_more(limit=None)
    print('found {} comments!'.format( len(submission.comments.list()) ))
    # for comment in submission.comments.list():
    #     print("found some comments: ",len(comment.body))

reddit = connect()
getSubmissionsFromSubreddit('njtech')