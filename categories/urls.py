# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from categories import views


urlpatterns = [
    # Matches any html file
    path('testing',views.categories, name="testing"),
    path('categories', views.categories, name='controlserver'),
    path('categories/<str:type>/', views.categories, name='controlserverr'),
]
