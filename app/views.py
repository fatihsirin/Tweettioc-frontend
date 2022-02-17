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
from django.http import JsonResponse

import datetime

from app.models import *


@login_required(login_url="/login/")
def index(request):
    # user_tweets = Tweet.objects.filter(date__gt=datetime.datetime.strptime("2021-12-25", "%Y-%m-%d"),
    #                                    date__lt=datetime.datetime.strptime("2021-12-30", "%Y-%m-%d"))

    iocCounts = Dashboard.objects.filter(type="iocCounts").order_by("-date")[0]
    iocCounts = iocCounts.data[0]

    counts_daily = Dashboard.objects.filter(type="daily").order_by("-date")[0].data
    counts_monthly = Dashboard.objects.filter(type="monthly").order_by("-date")[0].data
    daily_hashtags = Dashboard.objects.filter(type="hashtagsDaily").order_by("-date")[0].data
    all_hashtags = Dashboard.objects.filter(type="hashtagsAll").order_by("-date")[0].data

    object_list = Tweet.objects.filter(date__gt=datetime.datetime.now() - datetime.timedelta(days=3),
                                       date__lt=datetime.datetime.now()).order_by('-date')
    object_list = list(object_list)

    # paginator = Paginator(object_list, 5)
    # page = request.GET.get('page', 1)
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    #
    # page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=3)

    context = {
        'iocCounts': iocCounts, 'counts_weekly': counts_daily,
        'counts_monthly': counts_monthly, 'daily_hashtags': daily_hashtags,
        'all_hashtags': all_hashtags,
    }

    return render(request, "index.html", locals())


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


@login_required(login_url="/login/")
def entries(request):

    object_list = Tweet.objects.filter(date__gt=datetime.datetime.now() - datetime.timedelta(days=30),
                                       date__lt=datetime.datetime.now()).order_by('-date')[:500]
    return render(request,
                  "tables.html",
                  locals())
