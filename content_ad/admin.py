#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Ad
from forms import AdForm
import translation
from content.admin import ContentAdmin


class AdAdmin(ContentAdmin):
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

admin.site.register(Ad, AdAdmin)
