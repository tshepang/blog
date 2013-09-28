#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

SITENAME = 'Tshepang logs'
SITEURL = 'http://tshepang.net'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'
PATH = 'content/'
SUMMARY_MAX_LENGTH = 0
THEME = 'notmyidea'
OUTPUT_PATH = os.path.expanduser('~/tmp/blog')
ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}'
CATEGORY_URL = '{slug}'
TAG_URL = 'tag/{slug}'
AUTHOR_SAVE_AS = False
TIMEZONE = 'Africa/Johannesburg'
AUTHOR = 'Tshepang Lekhonkhobe'
DISQUS_SITENAME = 'tshepanglogs'
GOOGLE_ANALYTICS = 'UA-16685250-3'
TWITTER_USERNAME = 'tshepang_dev'
STATIC_PATHS = ['images', 'CNAME']
