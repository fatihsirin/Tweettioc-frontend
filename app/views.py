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
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

import datetime


# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client.ioctest  # Select the database
# ioc = db.ioc



from app.models import *


@login_required(login_url="/login/")
def index(request):
    user_tweets = Tweet.objects.filter(date__gt=datetime.datetime.strptime("2021-12-25", "%Y-%m-%d"),
                                       date__lt=datetime.datetime.strptime("2021-12-30", "%Y-%m-%d"))

    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def tables(request):
#     testIOC = ioc.find({'tweet.date': {'$lt': datetime.datetime.now(), '$gt': datetime.datetime.now() - datetime.timedelta(days=50)}}
#                        , sort=[('tweet.date', pymongo.DESCENDING)]).limit(200)
#
#     counts = {}
#     if ioc.find_one():
#         for name, value in ioc.find_one().items():
#             counts[name] = 0
#             for x in ioc.find({name: {"$regex": ".+"}}):
#                 counts[name] += len(x[name])
#
#     return render(request, "tables.html",{'iocs': testIOC})


@login_required(login_url="/login/")
def tables(request):
    object_list = Tweet.objects.filter(date__gt=datetime.datetime.now() - datetime.timedelta(days=50),
                                       date__lt=datetime.datetime.now()).order_by('date')



    paginator = Paginator(object_list, 10)
    page = request.GET.get('page',1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=3)
    context = {
        'page_obj': page_obj, 'page_range': page_range,
        'page': page, 'paginator': paginator,
    }

    return render(request,
                  "tables.html",
                  context)

