#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django import forms
from django.utils.translation import ugettext as _

from models import Ad
from content.forms import ContentForm

class AdForm(ContentForm):
    class Meta:
    	model = Ad
    	exclude = ('comment_status', )

