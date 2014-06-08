#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings as site_settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content import settings
from models import Ad
from forms import AdForm

from content.admin import ChildAdmin

class AdAdmin(ChildAdmin):
    base_model = Ad
    fieldsets = (
        (None, {
            'fields': ('title', 'body')
        }),
        (_('Ad data'), {
            'fields': ('url', 'start_showing', 'stop_showing',
                       'advertiser', )
        }),
        ('Categories', {
            'fields': ('categories',),
        }),
        (_('Page data'), {
            'fields': ('authors', 'non_staff_author',
                       'status', 'origin', )
        }),
    )

    fieldsets = fieldsets + ((_('Advanced Options'), {
            'fields': ('slug', 'date_modified', 'site', ),
            'classes': ('collapse',),
        }),)
    form = AdForm

