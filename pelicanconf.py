#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Ramsay'
SITENAME = '53-degrees-astro'
SITEURL = 'http://172.17.0.2'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URLs
# URL settings
## Makes article like: /posts/year/month/article-slug/
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
## Makes categories like: /categories
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
## Makes category like /category/category-name
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
## Makes tag like: /tag/tag-name
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
## Makes tags like: /tags
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
## Makes tag like: /tag/tag-name
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
## Makes page like: /pages/page-name
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
## Makes author like: /author/chrisramsay/
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
## Makes authors like: /author
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'
## Archives ordered newest at top, oldest at bottom
NEWEST_FIRST_ARCHIVES = True
## Yearly and monthly archives
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

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
    'post_stats',
    'minify',
    ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Specific to pelican-bootstrap theme
#TWITTER_USERNAME = 'chris_ramsay'
#TWITTER_WIDGET_ID = '508154314989137921'
#KEYBASE_USER = 'chrisramsay'
#KEYBASE_64BIT = 'AC94 F4DE 41C2 E99B'
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_AUTHOR = True
SHOW_SERIES = True
BOOTSTRAP_THEME = 'darkly'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static files
# Files
STATIC_PATHS = [
    'static/robots.txt',
    'static/keybase.txt',
    'static/favicon.ico',
    ]
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/keybase.txt': {'path': 'keybase.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    }

# Cache settings
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
