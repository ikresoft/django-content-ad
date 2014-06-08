#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URL definitions for news pages
"""
try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #ad detail
    url(
        r'^(?P<slug>[-\w]+)/$',
        'content_ad.views.ad_detail',
        name='ad_detail'
    ),

)
