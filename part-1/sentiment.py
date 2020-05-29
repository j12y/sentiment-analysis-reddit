#!/usr/bin/env python

"""
This sample demonstrates querying Reddit and
doing a sentiment analysis and compiling the
results.  It does this for all of the comments
on a post given by url on the commandline.
"""

import os
import praw
import argparse
from nltk.sentiment.vader import SentimentIntensityAnalyzer

reddit = praw.Reddit(
        client_id = os.environ['REDDIT_CLIENT_ID'],
        client_secret = os.environ['REDDIT_CLIENT_SECRET'],
        user_agent = os.environ['REDDIT_USER_AGENT'],
        )

parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--threshold', default=.8, type=float)
args = parser.parse_args()

submission = reddit.submission(url=args.url)
print('{} - by {}'.format(submission.title, submission.author))
submission.comments.replace_more(limit=None)
print('{} comments'.format(submission.num_comments))

analyzer = SentimentIntensityAnalyzer()
comments = {'pos': {'count': 0, 'results': []},
        'neu': {'count': 0, 'results': []},
        'neg': {'count': 0, 'results': []}}
for comment in submission.comments.list():
    score = analyzer.polarity_scores(comment.body)

    if score['compound'] > args.threshold:
        comments['pos']['count'] += 1
        comments['pos']['results'].append(comment.body)
        print("positive: {}".format(score))
    elif score['compound'] <= (args.threshold * -1):
        comments['neg']['count'] += 1
        comments['neg']['results'].append(comment.body)
        print("negative: {}".format(score))
    else:
        comments['neu']['count'] += 1
        comments['neu']['results'].append(comment.body)
        print("neutral: {}".format(score))

print('pos: {} neg: {} neu: {}'.format(comments['pos']['count'], comments['neg']['count'], comments['neu']['count']))

for pos in comments['pos']['results']:
    print(pos)
    print('---')


