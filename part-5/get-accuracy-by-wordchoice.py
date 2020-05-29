#!/usr/bin/env python

import random
from nltk.corpus import movie_reviews

import nltk.classify
from nltk import NaiveBayesClassifier

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# return a list of tuple pairs
#   a string of the raw review before tokenization
#   a string label of a pre-classified sentiment ('pos' or 'neg')
def get_labeled_dataset():
    dataset = []
    for label in movie_reviews.categories():
        for review in movie_reviews.fileids(label):
            dataset.append((movie_reviews.raw(review), label))

    random.shuffle(dataset)
    return dataset

def get_features(text):
    features = {}

    # Feature #1 - verbosity
    features['verbosity'] = len(text)

    # Feature #2 and #3 - lexical word choice
    scores = analyzer.polarity_scores(text)
    features['vader(pos)'] = scores['pos']
    features['vader(neg)'] = scores['neg']

    return features

def evaluate_model(dataset, train_percentage=0.9):
    feature_set = [(get_features(i), label) for (i, label) in dataset]
    count = int(len(feature_set) * train_percentage)
    train_set, test_set = feature_set[:count], feature_set[count:]
    classifier = NaiveBayesClassifier.train(train_set)
    return nltk.classify.accuracy(classifier, test_set)

analyzer = SentimentIntensityAnalyzer()

dataset = get_labeled_dataset()
print(evaluate_model(dataset))
