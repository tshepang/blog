# -*- coding: utf-8 -*-

import re
import os
import datetime
import unicodedata

import jinja2

from liquidluck.readers.base import Post
from liquidluck.readers.restructuredtext import RestructuredTextReader
from liquidluck.utils import to_datetime


class MyReader(RestructuredTextReader):
    def _parse_meta(self, header):
        meta = super(MyReader, self)._parse_meta(header)
        if 'date' not in meta:
            mtime = os.stat(self.filepath).st_mtime
            date = datetime.datetime.fromtimestamp(mtime)
            meta['date'] = date.date().isoformat()
        return meta


class MyPost(Post):
    @property
    def category(self):
        return self.relative_filepath.split('/')[0]

    @property
    def date(self):
        if 'page' in self.tags:
            return None
        date = self.meta.get('date')
        if date:
            return to_datetime(date)
        return None

    @property
    def clean_title(self):
        value = jinja2.Markup(self.title).striptags()
        if type(self.title) == unicode:
            value = unicodedata.normalize('NFKD', value).encode('ascii',
                                                                'ignore')
        value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
        return re.sub('[-\s]+', '-', value)
