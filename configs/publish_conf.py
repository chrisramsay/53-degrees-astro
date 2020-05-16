#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Main
AUTHOR = '53° Astro'
SITENAME = '53° Astro'
SITEURL = 'https://53-degrees-astro.com'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
	'author': '53° Astro',
}
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URLs
USE_FOLDER_AS_CATEGORY = True
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

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/53_astro'),
    ('instagram', 'https://www.instagram.com/53degreesastro'),
    ('flickr', 'https://www.flickr.com/people/53-degrees-astro'),
    )

# Theme and plugins
PLUGIN_PATHS = ['/plugins', ]
# Always put minify at the end of plugins list
PLUGINS = [
    'i18n_subsites',
    #'related_posts',
    'summary',
    'post_stats',
    'render_math',
    'series',
    'tag_cloud',
    'tipue_search',
    'minify',
    ]

# Specific to pelican-bootstrap theme
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
PYGMENTS_STYLE = 'solarazeddark'
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_AUTHOR = True
SHOW_SERIES = True
BOOTSTRAP_THEME = 'darkly'
BANNER = 'images/mammatus.jpg'

# Static files
# Files
STATIC_PATHS = [
    'static/robots.txt',
    'static/keybase.txt',
    'static/favicon.ico',
    'static/android-chrome-192x192.png',
    'static/android-chrome-512x512.png',
    'static/apple-touch-icon.png',
    'static/favicon-16x16.png',
    'static/favicon-32x32.png',
    'static/solarazeddark.css',
    'static/53_deg_logo_wbg.png',
    'static/mammatus.jpg',
    ]
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/keybase.txt': {'path': 'keybase.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'static/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'static/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'static/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'static/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'static/solarazeddark.css': {'path': 'theme/css/pygments/solarazeddark.css'},
    'static/53_deg_logo_wbg.png': {'path': 'images/53_deg_logo_wbg.png'},
    'static/mammatus.jpg': {'path': 'images/mammatus.jpg'},
    }

# Cache settings
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False
