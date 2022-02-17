# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from navigation import views


urlpatterns = [
    # Matches any html file
    path('contribute',views.contribute, name="contribute"),
]
