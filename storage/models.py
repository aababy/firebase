#coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone

class App(models.Model):
    name = models.CharField(max_length=50)
    tag_order = models.CharField(max_length=200, default="", blank=True)
    version = models.CharField(max_length=10, default="1")

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, default="")
    image_order = models.CharField(max_length=400, blank=True)

    app = models.ManyToManyField(App)   # app

    def __unicode__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     repeat = False
    #     for query in Tag.objects.all():
    #         if query.name == self.name:
    #             repeat = True

    #     if repeat == False:
    #         super(Tag, self).save(*args, **kwargs) # Call the "real" save() method.

class Graph(models.Model):
    name = models.CharField(max_length=200)                         # 姓名
    url = models.CharField(max_length=400, default="", blank=True)  # URL
    date = models.DateTimeField('upload date', default=timezone.now())

    def display(self):
        return mark_safe(u'<img src="%s" width="120px" />' % self.url)
    display.short_description = u'graph'

    tag = models.ManyToManyField(Tag, blank=True)   # tag

    def __unicode__(self):
        return self.name