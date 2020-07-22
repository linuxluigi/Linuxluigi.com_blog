#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Steffen Exler"
SITENAME = "Linuxluigi.com"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "de"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("github", "https://github.com/linuxluigi"),
    ("rss", "//linuxluigi.com/feeds/all.atom.xml"),
    ("twitter", "https://twitter.com/linuxluigi"),
    ("reddit", "https://www.reddit.com/user/linuxluigi"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
