#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Peter Bouda'
SITENAME = 'μbrew ZEOMA.'
SITESUBTITLE = 'Your Modular Game Console.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/dopetrope'

PLUGIN_PATHS = [ "plugins" ]
PLUGINS = [ "pelican-page-hierarchy", "events" ]

PLUGIN_EVENTS = {
    'ics_fname': 'ubrew_calendar.ics',
}

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

USE_FOLDER_AS_CATEGORY = True
TYPOGRIFY = True

INDEX_SAVE_AS = 'blog/index.html'

STATIC_PATHS = [ 'images' ]

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
