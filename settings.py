#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

SITENAME = 'Tshepang logs'
SITEURL = 'http://tshepang.net'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'
PATH = 'content/'
THEME = '../elegant'
OUTPUT_PATH = '.output'
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
# http://fortawesome.github.io/Font-Awesome/icons/#brand
SOCIAL = [
    ('bitbucket', 'https://bitbucket.org/tshepang'),
    ('github', 'https://github.com/tshepang'),
    ('twitter-square', 'https://twitter.com/tshepang_dev'),
    ('gittip', 'https://gittip.com/tshepang'),
]
TWITTER_USERNAME = 'tshepang_dev'
STATIC_PATHS = ['images', 'CNAME']

# specific to Elegant theme:
# http://oncrashreboot.com/elegant-a-clean-theme-for-pelican-with-search-feature
SOCIAL_PROFILE_LABEL = 'Stay in Touch'
USE_FAVICON = True
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'neighbors']
SITEMAP = {'format': 'xml'}
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives',
                     'search', '404'))
STATIC_PATHS.append('theme/images')
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
SITE_LICENSE = '''<a rel="license"
href="http://creativecommons.org/licenses/by-sa/3.0/"><img
alt="Creative Commons License" style="border-width:0"
src="http://i.creativecommons.org/l/by-sa/3.0/80x15.png" /></a><br
/>This work is licensed under a <a rel="license"
href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons
Attribution-ShareAlike 3.0 Unported License</a>.'''
