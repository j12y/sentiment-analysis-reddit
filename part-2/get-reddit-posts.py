#!/usr/bin/env python

import os
import praw

# Initialize the client library with your credentials
reddit = praw.Reddit(
   client_id = os.environ['REDDIT_CLIENT_ID'],
   client_secret = os.environ['REDDIT_CLIENT_SECRET'],
   user_agent = "script:sentiment-analysis:v0.0.1 (by {})".format(os.environ['REDDIT_USERNAME'])
)

# Query for a subreddit by name
sub = reddit.subreddit('learnpython')

# Can query for top posts for a time period, the top 20 posts, or the
# 10 most controversial posts of the past month
# top_posts_of_the_day = sub.top('day')
# hot_posts = sub.hot(limit=20)
controversial_posts = sub.controversial('month', limit=10)
posts = controversial_posts

# Can also search for use of a keyword
# nltk_posts = sub.search(‘nltk’)

# Sample of some of the more interesting data about a 
# submission that could make for interesting analysis
for submission in posts:
    print("TITLE: {}".format(submission.title))
    print("AUTHOR: {}".format(submission.author))
    print("CREATED: {}".format(submission.created))
    print("COMMENTS: {}".format(submission.num_comments))
    print("UPS: {}".format(submission.ups))
    print("DOWNS: {}".format(submission.downs))
    print("URL: {}".format(submission.url))
