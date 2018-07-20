#!/usr/bin/env python

import sys

from django.conf import settings
from django.template import loader

sys.path.insert(0, '../')
sys.path.insert(0, '../blog/apps')

import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings.settings_dev'

import django
django.setup()

from index.crons import generate_index_page

if __name__ == '__main__':
     generate_index_page()