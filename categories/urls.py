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
    path('categories/', views.categories, name='categories'),
    path('categories/<str:type>/', views.categories, name='categories_type'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/<str:tweetid>/', views.tweet, name='tweet_detail'),

    path('user/', views.user_dashboard, name='user_dashboard'),
    path('user/<str:username>/', views.user_dashboard, name='user_dashboard'),
]
