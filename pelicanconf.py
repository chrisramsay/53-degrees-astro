#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Ramsay'
SITENAME = '53-degrees-astro'
SITEURL = 'file:///media/data_1/web/sites/53-degrees-astro/output'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

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

DEFAULT_PAGINATION = 10

# Theme and plugins
PLUGIN_PATHS = ['/plugins', ]
# Always put minify at the end of plugins list
PLUGINS = [
    'i18n_subsites',
    'related_posts',
    'summary',
    'post_stats',
    'render_math',
    'series',
    'tag_cloud',
    'tipue_search',
     'minify',
    ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
BOOTSTRAP_THEME = 'darkly'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Cache settings
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
