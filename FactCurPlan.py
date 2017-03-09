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
    actual = 'фактические'
    current = 'текущие'
    planned = 'плановые'


train_fieldOfRequest = []

with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
            if ('\ufeff' in request):
                request = request[1:]
        if ('Fact' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.actual.name))
        elif ('Current' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.current.name))
        elif ('Planned' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.planned.name))
        else:
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.actual.name))



test_fieldOfRequest = []
with open('test.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
            if ('\ufeff' in request):
                request = request[1:]
        if ('Fact' in row.split('\t')[-1]):
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.actual.name))
        elif ('Current' in row.split('\t')[-1]):
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.current.name))
        elif ('Planned' in row.split('\t')[-1]):
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.planned.name))
        else:
            test_fieldOfRequest.append((request.strip(), FieldOfRequest.actual.name))

cl_fieldOfRequest = NaiveBayesClassifier(train_fieldOfRequest)


print("Точность результата:  " + repr(cl_fieldOfRequest.accuracy(test_fieldOfRequest)))
cl_fieldOfRequest.show_informative_features(20)