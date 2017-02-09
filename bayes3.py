# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from enum import Enum
from csv import reader as csv_reader
from nltk.stem.snowball import RussianStemmer
import pickle as p

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
    federal_issue = 'общегосударственные вопросы'
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

with open('DIR/fieldOfRequest/request_container_spendings.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfRequest.append((string_to_append, FieldOfRequest.spending.name))

with open('DIR/fieldOfRequest/request_container_revenues.txt', 'r+') as re_file:
    reader = csv_reader(re_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfRequest.append((string_to_append, FieldOfRequest.revenue.name))

with open('DIR/fieldOfRequest/request_container_deficit.txt', 'r+') as de_file:
    reader = csv_reader(de_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfRequest.append((string_to_append, FieldOfRequest.deficit.name))


#______________________Tax or Non-tax (for revenue only)____________________________________________

with open('DIR/tax/tax.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_tax.append((string_to_append, FieldOfRequest.tax_revenue.name))

with open('DIR/tax/non_tax.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_tax.append((string_to_append, FieldOfRequest.non_tax_revenue.name))

with open('DIR/tax/all.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_tax.append((string_to_append, FieldOfRequest.all_revenue.name))


#__________Actual or Current or Planned (for all fields of request)__________________________________

with open('DIR/type/actual.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_type.append((string_to_append, FieldOfRequest.actual.name))

with open('DIR/type/current.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_type.append((string_to_append, FieldOfRequest.current.name))

with open('DIR/type/planned.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_type.append((string_to_append, FieldOfRequest.planned.name))


#_____________________Field of spendings (for spendings only)________________________________________

with open('DIR/fieldOfSpending/culture.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.culture.name))

with open('DIR/fieldOfSpending/defense.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.defense.name))

with open('DIR/fieldOfSpending/economy.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.economy.name))

with open('DIR/fieldOfSpending/education.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.education.name))

with open('DIR/fieldOfSpending/environmental_protection.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.environmental_protection.name))

with open('DIR/fieldOfSpending/federal_issue.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.federal_issue.name))

with open('DIR/fieldOfSpending/health.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.health.name))

with open('DIR/fieldOfSpending/household.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.household.name))

with open('DIR/fieldOfSpending/safety.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.safety.name))

with open('DIR/fieldOfSpending/social_policy.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.social_policy.name))

with open('DIR/fieldOfSpending/sport.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_fieldOfSpending.append((string_to_append, FieldOfRequest.sport.name))

#__________________________Years_____________________________________________

with open('DIR/year/2007.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2007.name))
with open('DIR/year/2008.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2008.name))
with open('DIR/year/2009.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2009.name))
with open('DIR/year/2010.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2010.name))
with open('DIR/year/2011.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2011.name))
with open('DIR/year/2012.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2012.name))
with open('DIR/year/2013.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2013.name))
with open('DIR/year/2014.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2014.name))
with open('DIR/year/2015.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2015.name))
with open('DIR/year/2016.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2016.name))
with open('DIR/year/2017.txt', 'r+') as sp_file:
    reader = csv_reader(sp_file)
    for row in reader:
        string_to_append = prepare_the_string(row)
        train_year.append((string_to_append, FieldOfRequest.year_2017.name))

test = [
    ('сколько денег заработала Чечня в 2011 году', FieldOfRequest.revenue.name),
    ('сколько денег потрачено на экономику в этом году', FieldOfRequest.spending.name),
    ('сколько мы подняли на налогах год назад', FieldOfRequest.revenue.name),
    ('сколько Россия потратит на образование', FieldOfRequest.spending.name),
    ('дефицит Москвы в этом году', FieldOfRequest.deficit.name),
    ('дефицит федерального бюджета 2013', FieldOfRequest.deficit.name),
    ('тверская область расходы на спорт в 2016 году', FieldOfRequest.spending.name)
]

cl_fieldOfRequest = NaiveBayesClassifier(train_fieldOfRequest)
cl_tax = NaiveBayesClassifier(train_tax)
cl_type = NaiveBayesClassifier(train_type)
cl_fieldOfSpending = NaiveBayesClassifier(train_fieldOfSpending)
cl_year = NaiveBayesClassifier(train_year)


request = 'фактические расходы москвы на жкх в 17 году'

#print(cl_fieldOfRequest.accuracy(test))

#print(cl_fieldOfRequest.classify(request))

#'''
if (cl_fieldOfRequest.classify(request) == 'spending'):
    print(cl_fieldOfRequest.classify(request), cl_fieldOfSpending.classify(request), cl_type.classify(request), cl_year.classify(request))
elif (cl_fieldOfRequest.classify(request) == 'revenue'):
    print(cl_fieldOfRequest.classify(request), cl_tax.classify(request), cl_type.classify(request), cl_year.classify(request))
elif (cl_fieldOfRequest.classify(request) == 'deficit'):
    print(cl_fieldOfRequest.classify(request), cl_type.classify(request), cl_year.classify(request))
#'''

