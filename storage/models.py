#coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone
from firebase import settings

class App(models.Model):
    name = models.CharField(max_length=50)
    category_order = models.CharField(max_length=200, default="", blank=True)
    version = models.IntegerField(default=1)
    force_update_version = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ["name",]

class Category(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, default="")

    app = models.ManyToManyField(App)   # app
    # cover = models.OneToOneField("Graph", related_name='cover')
    cover = models.ForeignKey("Graph", related_name='cover', default="", blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ["name",]

class Graph(models.Model):
    name = models.CharField(max_length=200)                                     # 姓名
    url = models.CharField(max_length=400, default="")                          # URL
    original_url = models.CharField(max_length=400, default="")                 # URL
    date = models.DateTimeField('upload date', default=timezone.now)

    def display(self):
        return mark_safe(u'<img src="%s%s%s" width="120px" />' %(settings.GRAPH_PATH, self.name, settings.GRAPH_END))
    display.short_description = u'graph'
    
    category = models.ManyToManyField(Category, blank=True)   # tag
    starting = models.BooleanField(default=False)
    subscription = models.BooleanField(default=True) #订阅

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ["name",]

class Package(models.Model):
    name = models.CharField(max_length=200, default="", blank=True)
    url = models.CharField(max_length=400, default="", blank=True)  # URL

    thumb_name = models.CharField(max_length=200, default="", blank=True)
    thumb_url = models.CharField(max_length=400, default="", blank=True)  # URL

    graph = models.ManyToManyField(Graph, blank=True)   # graph
    app = models.ManyToManyField(App, blank=True)   # app

    def __unicode__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=200, default="", blank=True)
    url = models.CharField(max_length=400, default="", blank=True) # URL
    order = models.IntegerField(default=1)
    click = models.ForeignKey(Category, blank=True, null=True)

    def display(self):
        return mark_safe(u'<img src="%s%s%s" width="120px" />' %(settings.FEATURE_PATH, self.name, settings.FEATURE_END))
    display.short_description = u'graph'

    def __unicode__(self):
        return self.name