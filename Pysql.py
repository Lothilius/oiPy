__author__ = 'martin'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from sqlalchemy import update
from sqlalchemy import connectors as conn
from Pyoi import *
from authentication import mysql_engine_prod, mysql_engine_test
import fb_grab_events
import numpy as np
from sqlalchemy.orm.exc import MultipleResultsFound
import sys

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

def get_oiVenue_id(event_info, session):
    """Get the venue id from the oi915 database"""
    fb_venue_name = event_info[4]
    event_info = np.delete(event_info, 3)
    oi_venue_id = []

    for i, name in session.query(Venue.id, Venue.name).filter(Venue.name.like('%' + fb_venue_name + '%')):
        oi_venue_id.append(i)

    if not oi_venue_id:
        oi_venue_id = u'379'
    else:
        oi_venue_id = unicode(oi_venue_id[0])

    event_info = np.insert(event_info, 3, oi_venue_id)
    # print event_info, '\n'

    return event_info

def filter_current(event_list, session):
    """ Search for events in list already in the oiDB.
        Once found remove the duplicate events and return scrubbed event list.
    """
    current_events = []

    for i, fb_id in session.query(Event.id, Event.fb_eventid).order_by(desc(Event.id)).limit(500):
        current_events.append(fb_id)
    # print current_events

    event_list = np.array(event_list)
    #print event_list[::, 0]

    compare = np.intersect1d(event_list[::, 0], current_events)

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

def post_id_string(fb_event_ids, session):
    """ Post the string of event fb ids to User once the events have been posted."""
    post_to_user = ',' + fb_event_ids

    try:
        results = session.query(FrontUser.id, FrontUser.fb_eventid_uploaded).filter(FrontUser.id=='6').one()
        id, past_posts = results
        post_to_user = past_posts + post_to_user
        stmt = update(FrontUser).where(FrontUser.id == 6).values({"fb_eventid_uploaded": post_to_user})
        session.execute(stmt)
    except MultipleResultsFound, e:
        print e


def main():
    # Grab events from Facebook and place in to a list
    events_import = fb_grab_events.main()

    # Start db session for designated environment
    environment = raw_input("Which environment is this? (prod/test): ")
    session = start_up_engine(environment)

    print len(events_import)
    events_import = filter_current(events_import, session)

    print "Events array shape: ", events_import.shape

    event_upload_count = 0

    for each in events_import:
        event_ready = get_oiVenue_id(each, session)
        if event_ready[3] == u'379':
            pass
        else:
            try:
                # TODO also update event like count
                new_event = Event(event_ready)
                session.add(new_event)
                post_id_string(event_ready[0], session)
                event_upload_count += 1
                print event_ready[0]
            except UnicodeEncodeError as detail:
                print sys.exc_info()[0], detail, ' ', event_ready[0]
                session.close()
                session = start_up_engine(environment)
                pass

    print event_upload_count, "Facebook event ids have been posted to user."

    # for each in events_import:
    #print events_import, '\n'

    # session.commit()

    # for each in events_import:
    #     print each, '\n'

main()