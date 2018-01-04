#coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe

class App(models.Model):
    name = models.CharField(max_length=200)
    tag_order = models.CharField(max_length=400)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    image_order = models.CharField(max_length=400)

    app = models.ManyToManyField(App)   # app

    def __unicode__(self):
        return self.name

class Graph(models.Model):
    name = models.CharField(max_length=200)             # 姓名
    url = models.CharField(max_length=400, default="")  # URL

    def display(self):
        return mark_safe(u'<img src="%s" width="120px" />' % self.url)
    display.short_description = u'图片'

    tag = models.ManyToManyField(Tag)   # tag

    def __unicode__(self):
        return self.name