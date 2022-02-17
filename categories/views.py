from django.shortcuts import render

# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from django import template
from django.http import JsonResponse

import datetime

from app.models import *


@login_required(login_url="/login/")
def categories(request, type=None):
    names = ['md5', 'sha1', 'sha256', 'ip', 'domain', 'url', 'mail']
    # if type:
    if type in names:
        ioc_type = type
        data = Dashboard.objects.filter(type=type).order_by("-date")[0].data
        count_total = Dashboard.objects.filter(type=type).order_by("-date")[0].totalcount
        query = [
                {
                    "$match": {type: {"$regex": ".+"}},
                },
                {"$unwind": "$" + type},
                {
                    "$group": {
                        "_id": {"date": "$date", "ioc": "$" + type, "tweet_id": "$tweet_id", "username": "$username"}

                    }},
                {
                    "$sort": {"_id.date": -1}
                },
                {
                    "$limit": 100
                },
                {
                    "$project": {
                        "id": "$_id",
                        "_id": 0}}
            ]
        iocs = list(Tweet.objects.mongo_aggregate(query))
    else:
        ioc_type = ""
        iocCounts = Dashboard.objects.filter(type="iocCounts").order_by("-date")[0]
        iocCounts = iocCounts.data[0]

    return render(request,
                  "categories.html",
                  locals())


@login_required(login_url="/login/")
def tweet(request, tweetid=None):
    if tweetid is None:
        return render(request,
                      "error-404.html",
                      status=404)
    else:
        tweet = Tweet.objects.filter(tweet_id=tweetid).get()
        if tweet:
            print(tweet)
            return render(request, "tweet.html", locals())
        else:
            return render(request,
                          "error-404.html",
                          status=404)


@login_required(login_url="/login/")
def researcher_dashboard(request, username=""):
    user_info = TwitterProfile.objects.filter(username=username)
    if user_info:
        user_info = user_info[0]
        if user_info:
            counts_days = [
                {
                    "$match": {"username": username},
                },
                {
                    "$project": {
                        "_id": 1,
                        "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}},

                    }
                },
                {"$group": {
                    "_id": {"date": "$date"},
                    "count": {"$sum": 1}}
                },
                {"$project": {
                    "name": "$_id",
                    "count": 1,
                    "_id": 0}
                },

                {
                    "$sort": {"name.date": -1}
                },
                {
                    "$limit": 100
                }
            ]
            counts_days = list(Tweet.objects.mongo_aggregate(counts_days))

            counts_ioctypes = [
                {
                    "$match": {"username": username},
                },
                {
                    "$group": {
                        "_id": 0,
                        "md5": {"$addToSet": "$md5"},
                        "sha1": {"$addToSet": "$sha1"},
                        "sha256": {"$addToSet": "$sha256"},
                        "ip": {"$addToSet": "$ip"},
                        "domain": {"$addToSet": "$domain"},
                        "url": {"$addToSet": "$url"},
                        "mail": {"$addToSet": "$mail"}
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "md5": {"$size": "$md5"},
                        "sha1": {"$size": "$sha1"},
                        "sha256": {"$size": "$sha256"},
                        "ip": {"$size": "$ip"},
                        "domain": {"$size": "$domain"},
                        "url": {"$size": "$url"},
                        "mail": {"$size": "$mail"}
                    }
                }
            ]
            counts_ioctypes = list(Tweet.objects.mongo_aggregate(counts_ioctypes))[0]

            object_list = Tweet.objects.filter(username=username).order_by('-date')[:500]
            object_list = list(object_list)

            return render(request, "researcher.html", locals())
    else:
        username = ""
        Dashboard.objects.filter(type="researchersYearly").order_by("-date")[0].data
        researchersDaily = Dashboard.objects.filter(type="researchersDaily").order_by("-date")[0].data
        researchersMonthly = Dashboard.objects.filter(type="researchersMonthly").order_by("-date")[0].data
        researchersYearly = Dashboard.objects.filter(type="researchersYearly").order_by("-date")[0].data
        return render(request, "researcher.html", locals())

