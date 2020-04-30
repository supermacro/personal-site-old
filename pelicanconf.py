#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


import os
import sys

sys.path.append(os.curdir)

from jinjafilters import datetimeformat, tagsort

AUTHOR = 'Giorgio Delgado'
SITENAME = 'Giorgio Delgado'
SITEURL = 'http://localhost:8080'

USE_FOLDER_AS_CATEGORY = False

SUMMARY_MAX_LENGTH = 50

DESCRIPTION = 'Thoughts, ramblings, and randomness.'

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# MENUITEMS = [('About', 'pages/about')]

THEME = './theme'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['assets']

JINJA_FILTERS = {
    'datetimeformat': datetimeformat,
    'tagsort': tagsort
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/', 'pelican-thing'),
         ('Python.org', 'http://python.org/', 'pythong-thing'),
         ('Jinja2', 'http://jinja.pocoo.org/', 'jinja-thing'),
         ('You can modify those links in your config file', '#', 'other-thing'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/_gdelgado'),
          ('GitHub', 'https://github.com/concatmap'),
          ('LinkedIn', 'https://linkedin.com/in/giorgiodelgado'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
