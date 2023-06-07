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
