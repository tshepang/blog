#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

SITENAME = 'Tshepang logs'
SITEURL = 'http://tshepang.net'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'
PATH = 'content/'
SUMMARY_MAX_LENGTH = 0
THEME = '../pelican-themes/elegant'
OUTPUT_PATH = os.path.expanduser('~/tmp/blog')
ARTICLE_URL = '{slug}'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}'
TIMEZONE = 'Africa/Johannesburg'
AUTHOR = 'Tshepang Lekhonkhobe'
DISQUS_SITENAME = 'tshepanglogs'
GOOGLE_ANALYTICS = 'UA-16685250-3'
TWITTER_USERNAME = 'tshepang_dev'
STATIC_PATHS = ['images', 'CNAME']

# specific to Elegant theme:
# http://oncrashreboot.com/elegant-a-clean-theme-for-pelican-with-search-feature
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives',
                     'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

