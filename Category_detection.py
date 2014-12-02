__author__ = 'Lothilius'

from sqlalchemy.orm import sessionmaker
from Pyoi import *
from authentication import mysql_engine_prod
import numpy as np
from Word_Solver import Wordlist
import string
import re

Base = declarative_base()

db = mysql_engine_prod()

Session = sessionmaker()
Session.configure(bind=db)

session = Session()


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


events_list = np.array([[0, 0, 0, 0, 0, 0, 0]])
for e_id, fb_id, category, subcat, venue_id, name, description, how in session.query(Event.id, Event.fb_eventid,
                                                                               Event.category_id, Event.subcat_id,
                                                                               Event.venue_id, Event.event_name,
                                                                               Event.event_desc, Event.how).all():
    events_list = np.append(events_list, [[category, fb_id, subcat, venue_id, name, description, how]], axis=0)

events_list = np.delete(events_list, 0, axis=0)

wordList = Wordlist.BinaryTreeWordList()

word_string = events_list[:, 4:6].flatten()

word_string = ' '.join(word_string)
clean_description = sanitize(word_string)

word_array = clean_description.split()
word_array = list(set(word_array))
word_array.sort()

print word_array

for word in word_array:
    wordList.addWord(word, lambda x: len(x) in [4, 13])
print "The Wordlist contains ", len(wordList), " words."

# for word in word_array:
#     if wordList.findWord(word):
#         print "Found ", word
#     else:
#         pass