#coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe

class App(models.Model):
    name = models.CharField(max_length=200)
    tag_order = models.CharField(max_length=400, default="", blank=True)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, default="")
    image_order = models.CharField(max_length=400, blank=True)

    app = models.ManyToManyField(App)   # app

    def __unicode__(self):
        return self.name

class Graph(models.Model):
    name = models.CharField(max_length=200)                         # 姓名
    url = models.CharField(max_length=400, default="", blank=True)  # URL

    def display(self):
        return mark_safe(u'<img src="%s" width="120px" />' % self.url)
    display.short_description = u'graph'

    tag = models.ManyToManyField(Tag, blank=True)   # tag

    def __unicode__(self):
        return self.name