__author__ = 'Lothilius'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from Pyoi import *
from authentication import mysql_engine_prod
import fb_grab_events
import numpy as np
import urllib2

Base = declarative_base()

db = mysql_engine_prod()

Session = sessionmaker()
Session.configure(bind=db)

session = Session()

events_list = np.array([[0, 0, 0, 0, 0, 0, 0]])
for e_id, fb_id, category, subcat, venue_id, name, description, how in session.query(Event.id, Event.fb_eventid,
                                                                               Event.category_id, Event.subcat_id,
                                                                               Event.venue_id, Event.event_name,
                                                                               Event.event_desc, Event.how).all():
    events_list = np.append(events_list, [[fb_id, category, subcat, venue_id, name, description, how]], axis=0)

events_list = np.delete(events_list, 0, axis=0)

print events_list[::, 1]