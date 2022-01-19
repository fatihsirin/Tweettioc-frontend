from django.shortcuts import render

# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.http import JsonResponse

import datetime

from app.models import *


@login_required(login_url="/login/")
def categories(request, type=None):
    names = ['md5', 'sha1', 'sha256', 'ip', 'domain', 'url', 'mail']
    if type:
        if type in names:
            data_type = Dashboard.objects.filter(type=type).order_by("-date")[0].data
            count_total = Dashboard.objects.filter(type=type).order_by("-date")[0].totalcount
            query = [
                {
                    "$match": {type: {"$regex": ".+"}},
                },
                {"$unwind": "$" + type},
                {
                    "$group": {
                        "_id": {"date": "$date", "ioc": "$" + type, "tweet_id": "$tweet_id"}

                    }},
                {
                    "$sort": {"_id.date": +1}
                },
                {
                    "$limit": 15
                },
            ]
            iocs = list(Tweet.objects.mongo_aggregate(query))

    print("")

    return render(request,
                  "tables.html",
                  locals())
