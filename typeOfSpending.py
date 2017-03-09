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
    culture = 'культура'
    defense = 'защита'
    economy = 'экономика'
    education = 'образование'
    environmental_protection = 'защита окружающей среды'
    # federal_issue = 'общегосударственные вопросы'
    health = 'здравоохранение'
    household = 'жкх'
    safety = 'безопасность'
    social_policy = 'социальная политика'
    sport = 'спорт'

train_fieldOfSpending = []

with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
            if ('\ufeff' in request):
                request = request[1:]
        if ('S-culture' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.culture.name))
        elif ('S-national_defence' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.defense.name))
        elif ('S-national_economy' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.economy.name))
        elif ('S-education' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.defense.name))
        elif ('S-environment' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.environmental_protection.name))
        elif ('S-health' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.health.name))
        elif ('S-housing_utilities' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.household.name))
        elif ('S-national_security' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.safety.name))
        elif ('S-social_policy' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.social_policy.name))
        elif ('S-pe_and_sports' in row.split('\t')[-1]):
            train_fieldOfSpending.append((request.strip(), FieldOfRequest.sport.name))



test_fieldOfSpending = []
with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
            if ('\ufeff' in request):
                request = request[1:]
        if ('S-culture' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.culture.name))
        elif ('S-national_defence' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.defense.name))
        elif ('S-national_economy' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.economy.name))
        elif ('S-education' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.defense.name))
        elif ('S-environment' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.environmental_protection.name))
        elif ('S-health' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.health.name))
        elif ('S-housing_utilities' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.household.name))
        elif ('S-national_security' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.safety.name))
        elif ('S-social_policy' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.social_policy.name))
        elif ('S-pe_and_sports' in row.split('\t')[-1]):
            test_fieldOfSpending.append((request.strip(), FieldOfRequest.sport.name))

cl_fieldOfRequest = NaiveBayesClassifier(train_fieldOfSpending)


print("Точность результата:  " + repr(cl_fieldOfRequest.accuracy(test_fieldOfSpending)))
cl_fieldOfRequest.show_informative_features(20)