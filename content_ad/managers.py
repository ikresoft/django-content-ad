import datetime

from django.contrib.sites.models import Site

from django.db import models
from content.managers import CurrentSitePublishedManager
try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now


class AdManager(CurrentSitePublishedManager):
    """ A Custom Manager for ads """

    def get_random_ad(self, category=None, limit=1):
        """
        Returns a random advert that belongs for the specified ``ad_category``
        and ``ad_zone``.
        If ``ad_category`` is None, the ad will be category independent.
        """
        qs = self.get_query_set().filter(start_showing__lte=now(),
                                         stop_showing__gte=now(),
                                         sites=Site.objects.get_current().pk
                                         )
        if category:
            qs = qs.filter(categories=category)
        try:
            ad = qs.order_by('?')[:limit]
        except IndexError:
            return None
        return ad
