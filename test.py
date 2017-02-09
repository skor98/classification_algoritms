# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from enum import Enum
from csv import reader as csv_reader
from nltk.stem.snowball import RussianStemmer
import pickle as p

stem = RussianStemmer(ignore_stopwords=True)

test_fieldOfRequest = []
with open('test.txt', 'r+') as sp_file:
    request = ''
    for row in sp_file:
        for word in row.split('#')[0].split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        test_fieldOfRequest.append((request, row.split('#')[1].strip()))

print(5)