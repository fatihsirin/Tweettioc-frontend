# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Tweet)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "tweet_id", "username", "date")
    pass

@admin.register(Dashboard)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "date")
    pass

@admin.register(TwitterProfile)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "photo")
    pass