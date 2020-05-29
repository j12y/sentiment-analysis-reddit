#!/usr/bin/env python

import os
import praw
import nltk

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_comments_for_post(post):
    # Initialize the client library with your credentials
    reddit = praw.Reddit(
    client_id = os.environ['REDDIT_CLIENT_ID'],
    client_secret = os.environ['REDDIT_CLIENT_SECRET'],
    user_agent = "script:sentiment-analysis:v0.0.1 (by {})".format(os.environ['REDDIT_USERNAME'])
    )

    # Instead of getting submissions by querying a subreddit, this time
    # we go directly to a url for the post.
    submission = reddit.submission(url=post)
    submission.comments.replace_more(limit=None)

    # We can get the comments which the API returns as a generator, but
    # we can turn it into a list.
    comments = submission.comments.list()
    return comments



analyzer = SentimentIntensityAnalyzer()
post = "https://www.reddit.com/r/learnpython/comments/fwhcas/whats_the_difference_between_and_is_not"
comments = get_comments_for_post(post)
score = analyzer.polarity_scores(comments[116].body)
print(score)
