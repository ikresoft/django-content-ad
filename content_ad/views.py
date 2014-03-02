#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from content import settings
from models import Ad

def ad_detail(request, slug, extra_context={}):
    try:
        ad = Ad.objects.get(slug=slug)
    except Ad.DoesNotExist:
        if not settings.THROW_404:
            return render_to_response('content_ad/removed.html',
                                      {},
                                      context_instance=RequestContext(request))
        else:
            raise Http404
    context = {
        'object': ad,
    }
    if extra_context:
        context.update(extra_context)
    template_name = "content_ad/detail.html"
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

