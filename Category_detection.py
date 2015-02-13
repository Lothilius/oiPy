__author__ = 'Lothilius'

from sqlalchemy.orm import sessionmaker
from Pyoi import *
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from authentication import mysql_engine_prod
import numpy as np
from Word_Solver import Wordlist
import string
import re
import urllib
import urllib2

np.set_printoptions(threshold=np.nan)

Base = declarative_base()

db = mysql_engine_prod()

Session = sessionmaker()
Session.configure(bind=db)

session = Session()


def notify_martin(message='Hey its ready'):
    number = 9152178558
    prov = 203
    url = 'http://www.onlinetextmessage.com/send.php'
    values = {'code' : '',
              'number' : number,
              'from' : '',
              'remember' : 'n',
              'subject' : '.\n',
              'carrier' : prov,
              'quicktext' : '',
              'message' : message,
              's' : 'Send Message'}
    data = urllib.urlencode(values)  ##text sender
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()

    print 'Message sent.'

def sanitize(long_string):
    """ Sanatize string of html markup. Then using regex any non-alphanumeric characters
        are removed except those useful for numbers, emails, and web sites. The words
        accepted are also 4 characters or larger. Any thing not acceptable is replaced with a
        space.
    """
    # Remove html markups like \n \r \t
    long_string = long_string.translate(string.maketrans("\n\t\r", "   "))

    # Use Regex to limit the string to only useful information by selecting not useful items
    regex_pattern = ur'([^a-zA-Z0-9]+|(?<!\.)\b[a-zA-Z0-9]{1,3}\b(?=[^.]))(([^\.-@]?|[^-\.@]?)[^a-zA-Z0-9]+)+'
    pattern = re.compile(regex_pattern, re.UNICODE)
    # Replace selected items from regex with a space
    clean_description = pattern.sub(' ', long_string)

    # Use Regex to remove facebook event URLs from string
    regex_pattern = ur'(www.)?facebook.com\/events\/(\d)*'
    pattern = re.compile(regex_pattern, re.UNICODE)
    # Replace selected items from regex with a space
    clean_description = pattern.sub(' ', clean_description)

    # Use Regex to remove generic Ticket URLs from string
    regex_pattern = ur'(www.)?(ticket)(\w*|\.)\.?\D{2,3}\/?[a-zA-Z0-9]*\.?[a-zA-Z0-9]*\??[a-zA-Z0-9]*=?'
    pattern = re.compile(regex_pattern, re.UNICODE)
    # Replace selected items from regex with a space
    clean_description = pattern.sub(' ', clean_description)


    return clean_description

def convert_to_binary(fb_id_list):
    """Change the fb ids column in to a minary list.
        If an id is present represent the value as 1.
        If none represent as 0.
    """

    final_list = []
    for item in fb_id_list:
        if item == None:
            final_list.append(0)
        else:
            final_list.append(1)

    return final_list

def split_categories(the_array):
    single_category = []
    for each in the_array:
        cat = each.split(",")[0]
        single_category.append(cat)

    return single_category



def build_bulk(events_strings, word_array):
    bulk_array = [[0]*len(word_array)]
    for item in events_strings:
        bulk_row = [[0]*len(word_array)]
        for each in item:
            match_index = np.searchsorted(word_array, each)
            if each == word_array[match_index]:
                bulk_row[0][match_index] = bulk_row[0][match_index] + 1
        bulk_array = np.append(bulk_array, bulk_row, axis=0)

    return bulk_array


def create_string_arrays(the_array):
    word_string = the_array.flatten()
    word_string = ' '.join(word_string)
    clean_description = sanitize(word_string)

    word_array = clean_description.split()
    word_array = np.array(list(set(word_array)))
    word_array.sort()

    return word_array

def build_event_array(events_list):
    events_strings = []
    for each in events_list:
        events_row = create_string_arrays(each)
        events_strings.append(events_row)

    return events_strings


events_list = np.array([[0, 0, 0, 0, 0, 0, 0]])
for e_id, fb_id, category, subcat, venue_id, name, description, how in session.query(Event.id, Event.fb_eventid,
                                                                               Event.category_id, Event.subcat_id,
                                                                               Event.venue_id, Event.event_name,
                                                                               Event.event_desc, Event.how).all():
    events_list = np.append(events_list, [[category, fb_id, subcat, venue_id, name, description, how]], axis=0)

events_list = np.delete(events_list, 0, axis=0)

training_category = split_categories(events_list[:, 0])

# Assemble fb id and fb binary columns
fb_id_ = np.vstack(events_list[:, 1])
fb_id_binary = convert_to_binary(events_list[:, 1])
fb_id_binary = np.vstack(fb_id_binary)

# Convert venue column to 2d
venue_id_binary = np.vstack(events_list[:, 3])

training_array = np.concatenate((fb_id_, fb_id_binary), axis=1)
training_array = np.concatenate((training_array, venue_id_binary), axis=1)

# Create the word count matrix.
word_array = create_string_arrays(events_list[:, 4:6])
events_strings = build_event_array(events_list[:, 4:6])
word_count = build_bulk(events_strings, word_array)
word_count = np.delete(word_count, 0, axis=0)

training_array = np.concatenate((training_array, word_count), axis=1)

print np.shape(training_array)

# Create final training data set and test data set
training_array = training_array[:-100]
test_dataset = training_array[-100:]

print training_category

# Create random forest
cfr = RandomForestClassifier(n_estimators=500, n_jobs=-1)
the_forest = cfr.fit(training_array[2000:2100, 1:], training_category[2000:2100])

predictions = the_forest.predict(test_dataset[:, 1:])
predictions = np.vstack(predictions)

test_fb_id = np.vstack(test_dataset[:, 0])

print np.concatenate((test_fb_id, predictions), axis=1)


notify_martin()

# for word in word_array[:1090]:
#     wordList.addWord(word, lambda x: len(x) > 2)
# print "The Wordlist contains ", len(wordList), " words."

# for word in word_array:
#     if wordList.findWord(word):
#         print "Found ", word
#     else:
#         pass