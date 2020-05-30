#!/usr/bin/env python

import os
import praw

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

reddit = praw.Reddit(
    client_id = os.environ['REDDIT_CLIENT_ID'],
    client_secret = os.environ['REDDIT_CLIENT_SECRET'],
    user_agent = "script:sentiment-analysis:v0.0.1 (by {})".format(os.environ['REDDIT_USERNAME'])
    )

# Instead of getting submissions by querying a subreddit, this time
# we go directly to a url for the post.
post = "https://www.reddit.com/r/learnpython/comments/fwhcas/whats_the_difference_between_and_is_not"
submission = reddit.submission(url=post)
submission.comments.replace_more(limit=None)

# We can get the comments which the API returns as a generator, but
# we can turn it into a list.
comments = submission.comments.list()


analyzer = SentimentIntensityAnalyzer()
results = {}
for comment in comments:
    score = analyzer.polarity_scores(comment.body)
    results[comment.id] = {
        'score': score,
        'ups': comment.ups,
        'downs': comment.downs,
        'created': comment.created,
        'text': comment.body
    }

    if comment.author:
        results[comment.id]['author'] = comment.author.name
    else:
        results[comment.id]['author'] = 'deleted'

# Store results in a file for annotation
filename = submission.id + '.json'
with open(filename, 'w') as file:
    json.dump(results, file, indent=4)
