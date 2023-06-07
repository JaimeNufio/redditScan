-- 'created':comment.created,
-- 'id':comment.id,
-- 'parent_id':comment.parent_id,
-- 'depth':comment.depth,
-- 'score':comment.score,
-- 'total_awards_received':comment.total_awards_received,
-- 'body':comment.body,
-- 'body_html':comment.body_html,
-- 'author':replaceNone(str(comment.author)),
-- 'subreddit':str(comment.subreddit),
-- 'permalink':comment.permalink,
-- 'is_submitter':comment.is_submitter

CREATE TABLE comments (
    created TIMESTAMP WITHOUT TIME ZONE,
    id VARCHAR(32) NOT NULL, 
    parent_id VARCHAR(32), 
    depth INT, 
    score INT, 
    total_awards_received INT, 
    body VARCHAR(40000),
    body_html VARCHAR(80000),
    author VARCHAR(50) NOT NULL,
    subreddit VARCHAR(100) NOT NULL,
    permalink VARCHAR(500) NOT NULL,
    is_submitter BOOLEAN
);
