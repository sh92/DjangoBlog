# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog, Category, UserInfo

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(UserInfo)
