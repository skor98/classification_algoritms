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

    all_revenue = 'все'
    tax_revenue = 'налоговые'
    non_tax_revenue = 'неналоговые'

    actual = 'фактические'
    current = 'текущие'
    planned = 'плановые'

    culture = 'культура'
    defense = 'защита'
    economy = 'экономика'
    education = 'образование'
    environmental_protection = 'защита окружающей среды'
    #federal_issue = 'общегосударственные вопросы'
    health = 'здравоохранение'
    household = 'жкх'
    safety = 'безопасность'
    social_policy = 'социальная политика'
    sport = 'спорт'

    year_2007 = '2007'
    year_2008 = '2008'
    year_2009 = '2009'
    year_2010 = '2010'
    year_2011 = '2011'
    year_2012 = '2012'
    year_2013 = '2013'
    year_2014 = '2014'
    year_2015 = '2015'
    year_2016 = '2016'
    year_2017 = '2017'


def prepare_the_string(string):
    prepared_string = '{}' \
        .format(TextBlob(str(string)
                         .replace('\'', '')
                         .replace('[', '')
                         .replace(']', '')
                         ))
    prepared_string = stem.stem(prepared_string)
    #print(prepared_string)
    return prepared_string

train_fieldOfRequest = []
train_tax = []
train_type = []
train_fieldOfSpending = []
train_year = []

#________________________________Field of request___________________________________________________

with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        if ('S ' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.spending.name))
        elif ('D ' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.deficit.name))
        elif ('R ' in row.split('\t')[-1]):
            train_fieldOfRequest.append((request.strip(), FieldOfRequest.revenue.name))


#__________Actual or Current or Planned (for all fields of request)__________________________________
'''
with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        if ('Planned' in row.split('\t')[-1]):
            train_type.append((request.strip(), FieldOfRequest.planned.name))
        elif ('Fact' in row.split('\t')[-1]):
            train_type.append((request.strip(), FieldOfRequest.actual.name))
        elif ('Current' in row.split('\t')[-1]):
            train_type.append((request.strip(), FieldOfRequest.current.name))
'''
#_____________________Field of spendings (for spendings only)________________________________________
'''
with open('DIR/train3.txt', 'r', encoding='utf-8') as sp_file:
    for row in sp_file:
        request = ''
        for word in (row.split('\t')[0]).split(' '):
            word = stem.stem(word)
            request += (word + ' ')
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
'''

#__________________________Years_____________________________________________





cl_fieldOfRequest = NaiveBayesClassifier(train_fieldOfRequest)


test_fieldOfRequest = []
with open('test.txt', 'r+') as sp_file:
    for row in sp_file:
        request = ''
        for word in row.split('#')[0].split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        test_fieldOfRequest.append((request, row.split('#')[1].strip()))
'''
test_fieldOfSpending = []
with open('train3.txt', 'r+') as sp_file:
    for row in sp_file:
        request = ''
        for word in row.split('#')[0].split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        test_fieldOfSpending.append((request, row.split('#')[1].strip()))
'''


with open('test.txt', 'r+') as sp_file:
    for row in sp_file:
        request = ''
        for word in row.split('#')[0].split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        print(row.split('#')[0].strip())
        prob_dist = cl_fieldOfRequest.prob_classify(request)
        #print("Класс: " + cl_fieldOfRequest.classify(request))
        print("Я считаю, что это:  " + prob_dist.max())
        print("Вероятность revenue:  " + repr(prob_dist.prob("revenue")))
        print("Вероятность spending:  " + repr(prob_dist.prob("spending")))
        print("Вероятность deficit:  " + repr(prob_dist.prob("deficit")))
        print("\n")

#print("Точность результата:  " + repr(cl_fieldOfRequest.accuracy(test_fieldOfRequest)))
#cl_fieldOfRequest.show_informative_features(45)
'''

with open('train3.txt', 'r+') as sp_file:
    for row in sp_file:
        request = ''
        for word in row.split('#')[0].split(' '):
            word = stem.stem(word)
            request += (word + ' ')
        print(row.split('#')[0].strip())
        prob_dist = cl_fieldOfSpending.prob_classify(request)
        #print("Класс: " + cl_fieldOfRequest.classify(request))
        print("Я считаю, что это:  " + prob_dist.max())
        print("Вероятность culture:  " + repr(prob_dist.prob("culture")))
        print("Вероятность defense:  " + repr(prob_dist.prob("defense")))
        print("Вероятность economy:  " + repr(prob_dist.prob("economy")))
        print("Вероятность education:  " + repr(prob_dist.prob("education")))
        print("Вероятность environmental_protection:  " + repr(prob_dist.prob("environmental_protection")))
        print("Вероятность health:  " + repr(prob_dist.prob("health")))
        print("Вероятность household:  " + repr(prob_dist.prob("household")))
        print("Вероятность safety:  " + repr(prob_dist.prob("safety")))
        print("Вероятность social_policy:  " + repr(prob_dist.prob("social_policy")))
        print("Вероятность sport:  " + repr(prob_dist.prob("sport")))
        print("\n")

print("Точность результата:  " + repr(cl_fieldOfSpending.accuracy(test_fieldOfSpending)))
#print("Точность результата:  " + repr(cl_fieldOfRequest.accuracy(test_fieldOfRequest)))
#cl_fieldOfRequest.show_informative_features(45)

'''
'''
if (cl_fieldOfRequest.classify(request) == 'spending'):
    print(cl_fieldOfRequest.classify(request), cl_fieldOfSpending.classify(request), cl_type.classify(request), cl_year.classify(request))
elif (cl_fieldOfRequest.classify(request) == 'revenue'):
    print(cl_fieldOfRequest.classify(request), cl_tax.classify(request), cl_type.classify(request), cl_year.classify(request))
elif (cl_fieldOfRequest.classify(request) == 'deficit'):
    print(cl_fieldOfRequest.classify(request), cl_type.classify(request), cl_year.classify(request))
'''

