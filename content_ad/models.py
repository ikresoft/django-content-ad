#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides the Page model for reporting news, events, info etc.
"""

from django.db import models
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.conf import settings as site_settings
from slugify import slugify
from content import settings
from content.models import CategoryContent

import datetime

# Use a datetime a few days before the max to that timezone changes don't
# cause an OverflowError.
MAX_DATETIME = datetime.datetime.max - datetime.timedelta(days=2)
try:
    from django.utils.timezone import now, make_aware, utc
except ImportError:
    now = datetime.datetime.now
else:
    MAX_DATETIME = make_aware(MAX_DATETIME, utc)


class Advertiser(models.Model):
    """ A Model for our Advertiser.  """
    company_name = models.CharField(
        verbose_name=_(u'Company Name'), max_length=255)
    website = models.URLField(verbose_name=_(u'Company Site'))
    user = models.ForeignKey(site_settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = _(u'Ad Provider')
        verbose_name_plural = _(u'Advertisers')
        ordering = ('company_name',)

    def __unicode__(self):
        return self.company_name

    def get_website_url(self):
        return self.website


class Ad(CategoryContent):
    url = models.URLField(verbose_name=_(u'Advertised URL'), null=True, blank=True)
    start_showing = models.DateTimeField(verbose_name=_(u'Start showing'),
                                         default=now)
    stop_showing = models.DateTimeField(verbose_name=_(u'Stop showing'),
                                        default=MAX_DATETIME)

    # Relations
    advertiser = models.ForeignKey(Advertiser, verbose_name=_("Ad Provider"), null=True, blank=True)

    def get_slug(self):
        return slugify(self.title, ok='-_', only_ascii=True)

    def get_absolute_url(self):
        if self.url:
            return self.url
        return reverse('ad_detail', args=tuple(), kwargs={
            'slug': self.slug
        })


# Reversion integration
if settings.USE_REVERSION:
    rev_error_msg = 'Pages excepts django-reversion to be '\
                    'installed and in INSTALLED_APPS'
    try:
        import reversion
        if not 'reversion' in site_settings.INSTALLED_APPS:
            raise ImproperlyConfigured(rev_error_msg)
    except (ImportError, ):
        raise ImproperlyConfigured(rev_error_msg)

    reversion.register(Ad)
