#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django import forms
from django.utils.translation import ugettext as _

from models import Ad
from category_content.forms import CategoryContentForm

class AdForm(CategoryContentForm):
    class Meta:
    	model = Ad
    	exclude = ('allow_comments', )

