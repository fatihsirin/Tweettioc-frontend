# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from categories import views


urlpatterns = [
    # Matches any html file
    #path('testing',views.categories, name="testing"),
    path('categories/', views.categories, name='categories'),
    path('categories/<str:type>/', views.categories, name='categories_type'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/<str:tweetid>/', views.tweet, name='tweet_detail'),

    path('researcher/', views.researcher_dashboard, name='researcher_dashboard'),
    path('researcher/<str:username>/', views.researcher_dashboard, name='researcher_dashboard'),
]
