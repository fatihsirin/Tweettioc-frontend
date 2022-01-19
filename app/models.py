# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

from django.utils.timezone import now
from djongo import models as djongo_models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Tweet(djongo_models.Model):
    id = djongo_models.BigIntegerField(primary_key=True, db_column="_id")
    tweet_id = djongo_models.TextField(db_column="tweet_id")
    name = djongo_models.TextField(db_column="name")
    username = djongo_models.TextField(db_column="username")
    postdate = djongo_models.TextField(db_column="postdate")
    timestamp = djongo_models.BigIntegerField(null=True, blank=True,db_column="timestamp")
    date = djongo_models.DateTimeField(db_column="date")
    text = djongo_models.TextField(db_column="text")
    link = djongo_models.TextField(db_column="link")
    reference = ArrayField(models.TextField(), db_column="reference")
    md5 = ArrayField(models.TextField(), db_column="md5")
    sha1 = ArrayField(models.TextField(), db_column="sha1")
    sha256 = ArrayField(models.TextField(), db_column="sha256")
    mail = ArrayField(models.TextField(), db_column="mail")
    ip = ArrayField(models.TextField(), db_column="ip")
    domain = ArrayField(models.TextField(), db_column="domain")
    url = ArrayField(models.TextField(), db_column="url")
    mentions = ArrayField(models.TextField(), db_column="mentions")
    hashtags = ArrayField(models.TextField(), db_column="hashtags")
    images = ArrayField(models.TextField(), db_column="images")

    objects = djongo_models.DjongoManager()

    class Meta:
        managed = True
        db_table = "tweets"


class Dashboard(djongo_models.Model):
    id = djongo_models.BigIntegerField(primary_key=True, db_column="_id")
    type = djongo_models.TextField(db_column="type")
    totalcount = djongo_models.BigIntegerField(db_column="totalcount")
    data = ArrayField(models.TextField(), db_column="data")
    date = djongo_models.DateTimeField(db_column="date")

    objects = djongo_models.DjongoManager()

    class Meta:
        managed = True
        db_table = "dashboards"
