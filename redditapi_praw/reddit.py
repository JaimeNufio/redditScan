import praw,pprint

class redditManager:

    reddit = None

    replaceNone = lambda x: 'deleted' if x is None or x == 'None' or not x else x

    def connect(self,auth):

        # Create the Reddit instance
        self.reddit = praw.Reddit(
            client_id=auth['client_id'],
            client_secret=auth['client_secret'],
            user_agent=auth['user_agent']
        )


    def getSubmissionsFromSubreddit(self,sub,insertFunc):
        # Get the top post in a subreddit
        subredditPosts = self.reddit.subreddit(sub).new(limit=1000)
        # for i in range(1000):

        # Print the title of the top post
        for post in subredditPosts:
            obj = {
                'created':int(post.created),
                'id':post.id,
                'num_comments':post.num_comments,
                'score':post.score,
                'title':post.title,
                'url':post.url,
                'selftext':post.selftext,
                'over_18':post.over_18,
                'author':self.__class__.replaceNone(str(post.author)),
                'subreddit':str(post.subreddit),
                'permalink':post.permalink
            }

            # pprint.pprint((obj))
            # print("Post \"{}\" by /u/{} in /r/{}".format(obj['title'],obj['author'],obj['subreddit']))
            
            insertFunc([obj],'submissions')
            self.getCommentsOnSubmission(post,insertFunc)
        

    def getCommentsOnSubmission(self,submission,insertFunc):

        submission.comments.replace_more(limit=None)
        print('found {} comments!'.format( len(submission.comments.list()) ))

        batch = []

        for comment in submission.comments.list():
            obj = {
                'created':int(comment.created),
                'id':comment.id,
                'parent_id':comment.parent_id,
                'depth':comment.depth,
                'score':comment.score,
                'total_awards_received':comment.total_awards_received,
                'body':comment.body,
                'body_html':comment.body_html,
                'author':self.__class__.replaceNone(str(comment.author)),
                'subreddit':str(comment.subreddit),
                'permalink':comment.permalink,
                'is_submitter':comment.is_submitter
            }

            batch.append(obj)

        insertFunc(batch,'comments')

    def __init__(self,auth):
        self.connect(auth)

# https://stackoverflow.com/questions/758945/whats-the-fastest-way-to-do-a-bulk-insert-into-postgres