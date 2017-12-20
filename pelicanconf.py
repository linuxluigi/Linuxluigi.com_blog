#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Steffen Exler'
SITEURL = 'https://linuxluigi.com'
SITENAME = 'Linuxluigi.com'
SITETITLE = 'Linuxluigi Blog'
SITESUBTITLE = 'Coding & Admin stuff'
SITEDESCRIPTION = 'Coding & admin stuff blog'
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

THEME = "pelican-themes/Flex"

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

MAIN_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins", "pelican-plugins"]
PLUGINS = ['assets', 'sitemap', 'i18n_subsites']

# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

# Translate to German.
DEFAULT_LANG = 'de'
OG_LOCALE = 'de_DE'
LOCALE = 'de_DE'

# Default theme language.
I18N_TEMPLATES_LANG = 'de'

# Sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# URL Settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
