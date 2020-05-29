#!/usr/bin/env python

"""
This sample demonstrates querying comments from
a Reddit post and printing the results.
"""

import os
import praw
import argparse

reddit = praw.Reddit(
        client_id = os.environ['REDDIT_CLIENT_ID'],
        client_secret = os.environ['REDDIT_CLIENT_SECRET'],
        user_agent = os.environ['REDDIT_USER_AGENT'],
        )

parser = argparse.ArgumentParser()
parser.add_argument('url')
args = parser.parse_args()

submission = reddit.submission(url=args.url)
print('{} - by {}'.format(submission.title, submission.author))

submission.comments.replace_more(limit=None)
comments = submission.comments.list()
print('{} comments'.format(len(comments)))
for comment in comments:
    print(comment.body)

