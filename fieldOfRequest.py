# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from enum import Enum
from csv import reader as csv_reader
from nltk.stem.snowball import RussianStemmer
import pickle as p
import nltk

stem = RussianStemmer(ignore_stopwords=True)

class FieldOfRequest(Enum):
    spending = 'доходы'
    revenue = 'расходы'
    deficit = 'дефицит'

train_fieldOfRequest = []

with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
            if ('\ufeff' in request):
                request = request[1:]
        if ('S ' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.spending.name))
        elif ('D' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.deficit.name))
        elif ('R' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.revenue.name))

test_fieldOfRequest = []
with open('test.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
            if ('\ufeff' in request):
                request = request[1:]
        if ('S ' in row.split('\t')[-1]):
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.spending.name))
        elif ('D' in row.split('\t')[-1]):
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.deficit.name))
        elif ('R' in row.split('\t')[-1]):
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.revenue.name))


cl_fieldOfRequest = NaiveBayesClassifier(train_fieldOfRequest)


print("Точность результата:  " + repr(cl_fieldOfRequest.accuracy(test_fieldOfRequest)))
cl_fieldOfRequest.show_informative_features(20)