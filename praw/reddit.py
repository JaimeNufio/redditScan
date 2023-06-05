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


replaceNone = lambda x: 'deleted' if x is None or x == 'None' or not x else x

def getSubmissionsFromSubreddit(sub):
    # Get the top post in a subreddit
    subredditPosts = reddit.subreddit(sub).top(limit=1000)
    # for i in range(1000):

    # Print the title of the top post
    for post in subredditPosts:
        obj = {
            'created':post.created,
            'id':post.id,
            'num_comments':post.num_comments,
            'score':post.score,
            'title':post.title,
            'url':post.url,
            'selftext':post.selftext,
            'over_18':post.over_18,
            'author':replaceNone(str(post.author)),
            'subreddit':str(post.subreddit),
            'permalink':post.permalink
        }

        # pprint.pprint((obj))
        print("Post \"{}\" by /u/{} in /r/{}".format(obj['title'],obj['author'],obj['subreddit']))

        getCommentsOnSubmission(post)

def getCommentsOnSubmission(submission):
    submission.comments.replace_more(limit=None)
    print('found {} comments!'.format( len(submission.comments.list()) ))
    for comment in submission.comments.list():
        # print("found some comments: ",len(comment.body))

        obj = {
            'created':comment.created,
            'id':comment.id,
            'parent_id':comment.parent_id,
            'depth':comment.depth,
            'score':comment.score,
            'total_awards_received':comment.total_awards_received,
            'body':comment.body,
            'body_html':comment.body_html,
            'author':replaceNone(str(comment.author)),
            'subreddit':str(comment.subreddit),
            'permalink':comment.permalink,
            'is_submitter':comment.is_submitter
        }


        pprint.pprint(obj)

reddit = connect()
getSubmissionsFromSubreddit('njtech')

# https://stackoverflow.com/questions/758945/whats-the-fastest-way-to-do-a-bulk-insert-into-postgres