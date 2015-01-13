#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Ad
from content.forms import CategoryContentForm


class AdForm(CategoryContentForm):
    class Meta:
        model = Ad
        exclude = ('allow_comments', )

