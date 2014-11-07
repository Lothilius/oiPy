__author__ = 'Lothilius'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from Pyoi import *
from authentication import mysql_engine_prod, mysql_engine_test
import numpy as np
import random
import sys


like_start = current_time.strftime('%Y-%m-%d %H:%M:%S')
user_id = 13


def start_up_engine(environment):
    Base = declarative_base()

    if environment == 'prod':
        db = mysql_engine_prod()
    else:
        db = mysql_engine_test()

    Session = sessionmaker()
    Session.configure(bind=db)

    session = Session()

    return session

def filter_current(event_list, session):
    """ Search for events in list already in the oiDB.
        Once found remove the duplicate events and return scrubbed event list.
    """
    current_events = []

    for i, e_id in session.query(Like.id, Like.event_id).order_by(desc(Like.id)).limit(500):
        current_events.append(e_id)
    # print current_events

    event_list = np.array(event_list)
    #print event_list[::, 0]

    compare = np.intersect1d(event_list, current_events)

    duplicates = []
    for each in compare:
        for i, item in enumerate(event_list):
            if each == item[0]:
                duplicates.append(i)

    print "Number of duplicates found: ", len(duplicates)

    # for i in duplicates:
    new_import_list = np.delete(event_list, duplicates, axis=0)
    # new_import_list = event_list

    return new_import_list


def main():
    environment = raw_input("Which environment is this? (prod/test): ")

    events_list = []
    session = start_up_engine(environment)

    for i in session.query(Event.id).order_by(desc(Event.id)).limit(100):
            events_list.append(i)

    events_list = filter_current(events_list, session)

    print 'Number of like records added: ', len(events_list[::, 0])
    for event_id in events_list:
        start_like = Like(user_id, event_id[0], like_start, like_count=0)
        session.add(start_like)
        like_count = random.randint(1, 7)
        likes = Likecount(event_id[0], like_count)
        session.add(likes)
        print event_id[0]

    session.commit()



main()
