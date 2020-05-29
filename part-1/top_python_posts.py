#!/usr/bin/env python

"""
This sample demonstrates querying for hot topics
instead.
"""

import os
import praw

reddit = praw.Reddit(
        client_id = os.environ['REDDIT_CLIENT_ID'],
        client_secret = os.environ['REDDIT_CLIENT_SECRET'],
        user_agent = os.environ['REDDIT_USER_AGENT'],
        )

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
    print(submission.url)


