#!/usr/bin/env python

"""
This sample demonstrates querying Reddit and printing out
various details about each post in a specific subreddit.
"""


import os
import praw

reddit = praw.Reddit(
        client_id = os.environ['REDDIT_CLIENT_ID'],
        client_secret = os.environ['REDDIT_CLIENT_SECRET'],
        user_agent = os.environ['REDDIT_USER_AGENT'],
        )

for submission in reddit.subreddit('learnpython').top('day', limit=1):
    print("TITLE: {}".format(submission.title))
    print("AUTHOR: {}".format(submission.author))
    print("CREATED: {}".format(submission.created))
    print("URL: {}".format(submission.url))
    print("COMMENTS: {}".format(submission.num_comments))
    print("CATEGORY: {}".format(submission.category))
    print("UPS: {}".format(submission.ups))
    print("DOWNS: {}".format(submission.downs))
    print("LIKES: {}".format(submission.likes))
    print("VIEWS: {}".format(submission.view_count))


