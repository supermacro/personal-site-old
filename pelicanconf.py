#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Giorgio Delgado'
SITENAME = 'Example Pelican website using GitLab Pages!'
SITEURL = 'http://localhost:8000'

DESCRIPTION = 'Thoughts and ramblings from way up north in Canada, eh!'

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

MENUITEMS = [('About', 'pages/about')]

THEME = './theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
