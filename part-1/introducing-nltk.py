#!/bin/env python

import nltk

# Download corpus
nltk.download('punkt')

# Tokenize Example
sentence = "A long time ago in a galaxy far, far away..."
tokens = nltk.word_tokenize(sentence)
print(tokens)
