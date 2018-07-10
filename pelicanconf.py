#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Giorgio Delgado'
SITENAME = 'Giorgio Delgado'
SITEURL = 'http://localhost:8000'

USE_FOLDER_AS_CATEGORY = False

SUMMARY_MAX_LENGTH = 40

DESCRIPTION = 'Thoughts, ramblings, and randomness.'

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# MENUITEMS = [('About', 'pages/about')]

THEME = './theme'

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
SOCIAL = (('twitter', 'https://twitter.com/_gdelgado'),
          ('github', 'https://github.com/gDelgado14'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
