# -*- coding: utf-8 -*-
"""
events plugin for Pelican
=========================

This plugin looks for and parses an "events" directory and generates
blog posts with a user-defined event date. (typically in the future)
It also generates an ICalendar v2.0 calendar file.
https://en.wikipedia.org/wiki/ICalendar


Author: Federico Ceratto <federico.ceratto@gmail.com>
Released under AGPLv3+ license, see LICENSE
"""

from datetime import datetime, timedelta
from pelican import signals, utils, contents
import icalendar
from icalendar import vDatetime
import re
import logging
import os.path
import pytz

log = logging.getLogger(__name__)

TIME_MULTIPLIERS = {
    'w': 'weeks',
    'd': 'days',
    'h': 'hours',
    'm': 'minutes',
    's': 'seconds'
}

events = []


def parse_tstamp(ev, field_name):
    """Parse a timestamp string in format "YYYY-MM-DD HH:MM"

    :returns: datetime
    """
    try:
        return datetime.strptime(ev[field_name], '%Y-%m-%d %H:%M')
    except Exception as e:
        log.error("Unable to parse the '%s' field in the event named '%s': %s" \
            % (field_name, ev['title'], e))
        raise


def parse_timedelta(ev):
    """Parse a timedelta string in format [<num><multiplier> ]*
    e.g. 2h 30m

    :returns: timedelta
    """

    chunks = ev['event-duration'].split()
    tdargs = {}
    for c in chunks:
        try:
            m = TIME_MULTIPLIERS[c[-1]]
            val = int(c[:-1])
            tdargs[m] = val
        except KeyError:
            log.error("""Unknown time multiplier '%s' value in the \
'event-duration' field in the '%s' event. Supported multipliers \
are: '%s'.""" % (c, ev['title'], ' '.join(TIME_MULTIPLIERS)))
            raise RuntimeError("Unknown time multiplier '%s'" % c)
        except ValueError:
            log.error("""Unable to parse '%s' value in the 'event-duration' \
field in the '%s' event.""" % (c, ev['title']))
            raise ValueError("Unable to parse '%s'" % c)


    return timedelta(**tdargs)


def parse_article(article):
    """Collect articles metadata to be used for building the event calendar

    :returns: None
    """
    global events

    if type(article) is not contents.Article:
        return

    if not 'event-start' in article.metadata:
        return

    dtstart = parse_tstamp(article.metadata, 'event-start')

    if 'event-end' in article.metadata:
        dtend = parse_tstamp(article.metadata, 'event-end')

    elif 'event-duration' in article.metadata:
        dtdelta = parse_timedelta(article.metadata)
        dtend = dtstart + dtdelta

    else:
        msg = "Either 'event-end' or 'event-duration' must be" + \
            " specified in the event named '%s'" % article.metadata['title']
        log.error(msg)
        raise ValueError(msg)

    events.append((dtstart, dtend, article))


def generate_ical_file(generator):
    """Generate an iCalendar file
    """
    global events

    ics_fname = generator.settings['PLUGIN_EVENTS']['ics_fname']
    if not ics_fname:
        return

    ics_fname = os.path.join(generator.settings['OUTPUT_PATH'], ics_fname)
    log.debug("Generating calendar at %s with %d events" % (ics_fname, len(events)))

    tz = generator.settings.get('TIMEZONE', 'UTC')
    tz = pytz.timezone(tz)

    ical = icalendar.Calendar()
    ical.add('prodid', '-//My calendar product//mxm.dk//')
    ical.add('version', '2.0')

    for e in events:
        dtstart, dtend, article = e
        
        title = re.sub("&nbsp;", " ", article.metadata['title'])

        ie = icalendar.Event(
            summary=title,
            dtstart=vDatetime(dtstart).to_ical(),
            dtend=vDatetime(dtend).to_ical(),
            dtstamp=vDatetime(article.metadata['date']).to_ical(),
            uid=title,
        )

        if 'event-location' in article.metadata:
            ie.add('location', article.metadata['event-location'])

        if 'event-origanizer' in article.metadata:
            ie.add('organizer', article.metadata['event-organizer'])

        if 'event-url' in article.metadata:
            ie.add('description', article.metadata['event-url'])

        ical.add_component(ie)

    with open(ics_fname, 'wb') as f:
        f.write(ical.to_ical())



def generate_events_list(generator):
    """Populate the event_list variable to be used in jinja templates"""
    global events
    generator.context['events_list'] = sorted(events, reverse=True)
    events = []

def register():
    signals.content_object_init.connect(parse_article)
    signals.article_generator_finalized.connect(generate_ical_file)
    signals.article_generator_finalized.connect(generate_events_list)


