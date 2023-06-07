-- 'created':postGot['created'],
-- 'id':postGot['id'],
-- 'num_comments':postGot['num_comments'],
-- 'score':postGot['score'],
-- 'title':postGot['title'],
-- 'url':postGot['url'],
-- 'selftext':postGot['selftext'],
-- 'over_18':postGot['over_18'],
-- 'author':str(postGot['author']),
-- 'subreddit':str(postGot['subreddit']),
-- 'permalink':postGot['permalink']

CREATE TABLE submisisons (
    created TIMESTAMP WITHOUT TIME ZONE,
    id VARCHAR(32) NOT NULL, 
    num_comments VARCHAR(32) NOT NULL, 
    score INT, 
    title VARCHAR(300) NOT NULL,
    url VARCHAR(500),
    selftext VARCHAR(40000),
    over_18 BOOLEAN,
    author VARCHAR(50) NOT NULL,
    subreddit VARCHAR(100) NOT NULL,
    permalink VARCHAR(500) NOT NULL
);
