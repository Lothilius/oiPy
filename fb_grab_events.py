__author__ = 'Lothilius'

import json
import authentication as oath
import re
from datetime import datetime
import urllib2
import numpy as np

url = 'https://graph.facebook.com/v2.2/100004568139047/events/not_replied?fields=id&limit=200'
response = oath.twitterreq(url)
message = json.load(response)

import_list = []
description = []

def get_how(description, website=''):
    """ Search event description for ticket website, cost of event, or place to purchase

    :param description: Event description as string
    :return: string
    """
    the_how = re.search('(?<=\$)\d+', description)

    if website != '' and the_how is not None:
        the_how = the_how.group(0) + "\n" + website
    elif website != '' and the_how is None:
        the_how = website
    else:
        try:
            the_how = u'$' + the_how.group(0)
        except AttributeError:
            the_how = u'tba'


    return the_how

def change_datetime_format(the_datetime):
    """Change the format of the datetime value to a true python datetime value."""

    year = int(the_datetime[:4])
    month = int(the_datetime[5:7])
    day = int(the_datetime[8:10])
    try:
        hour = int(the_datetime[11:13])
        minutes = int(the_datetime[14:16])
        seconds = int(the_datetime[17:19])
    except ValueError:
        hour = 9
        minutes = 0
        seconds = 0
    the_datetime = datetime(year, month, day, hour, minutes, seconds)

    return the_datetime

def unicode_friendly(item):
    """Search string for mulitple unicodes and replace with a corresponding character
        so that latin-1 codec will handle the character with out error
    """
    item = item.replace(u'\u2019', '\'')
    item = item.replace(u'\u201c', '\"')
    item = item.replace(u'\u201d', '\"')
    item = item.replace(u'\u2026', '...')
    item = item.replace(u'\u2013', '-')
    item = item.replace(u'\xf1o', 'n')
    item = item.replace(u'\xe1n', 'o')
    item = item.replace(u'\xe9', 'e')
    item = item.replace(u'\xe7', 'c')
    item = item.replace(u'\xe8', 'e')
    item = item.replace(u'\xed', 'i')
    item = item.replace(u'\xe1', 'a')
    item = item.replace(u'\xbd', '1/2')
    item = item.replace(u'\xfc', 'u')
    item = item.replace(u'\xf3', 'o')
    item = item.replace(u'\u2014', '-')
    item = item.replace(u'\u2605', '')
    item = item.replace(u'\u25ba', '->')
    item = item.replace(u'\u279c', '->')
    item = item.replace(u'\u2666', '')
    item = item.replace(u'\u2018', '\'')

    return item

def main():
    # print message['data']
    try:
        # Get main set of data
        statuses = message['data']
        full_descriptions = []

        # Retreeve details for each event
        for each in statuses:
            # Get event data
            url = 'https://graph.facebook.com/v2.2/' + str(each['id']) + '?fields=id,name,description,venue,' \
                                                                         'ticket_uri,start_time,cover,attending_count'
            event_request = oath.twitterreq(url)
            event_request = json.load(event_request)


            each['start_time'] = change_datetime_format(each['start_time'])

            if datetime.date(datetime.now()) < datetime.date(each['start_time']):
                # Check for ticket url
                try:
                    url_ticket = event_request['ticket_uri']
                except KeyError:
                    url_ticket = ''

                # Check for description
                try:
                    description = unicode_friendly(event_request['description'])
                except KeyError:
                    description = event_request['name'] + '\n' + url_ticket


                # Get venue name from the venue id
                try:
                    venue_id = event_request['venue']['id']
                    url = 'https://graph.facebook.com/v2.1/' + str(venue_id)
                    venue_request = oath.twitterreq(url)
                    venue_request = json.load(venue_request)
                    venu_name = venue_request['name']
                except KeyError:
                    try:
                        venue_id = u'1'
                        venu_name = venue_request['name']
                    except KeyError:
                        venue_id = u'1'
                        venu_name = u'Undisclosed'

                # Check for cover image urllib2.quote(.encode("utf8"))
                try:
                    cover_link = urllib2.quote(event_request['cover']['source'])
                except KeyError:
                    cover_link = u'http://oi915.com/public/images/events/oi915_fillerpic.png'

                full_descriptions.append([each['id'], event_request['name'], description, venue_id,
                                    venu_name, str(each['start_time']), u'http://www.facebook.com/events/' + str(each['id']),
                                    u'Facebook', cover_link,
                                    get_how(description, url_ticket), u'2', event_request['attending_count']])

        # for each in full_descriptions:
        #     print each[2]

        return full_descriptions

        # for i, each in enumerate(statuses):
        #     import_list.append([each['id'], each['name'], each['start_time'], each['location']])
        # import_list = np.array(import_list)
    except KeyError:
        print KeyError
        print message['events']['data']


if __name__ == '__main__':
    main()
