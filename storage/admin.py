#coding:utf-8
from django.contrib import admin
from django.contrib import messages
from storage.models import App, Tag, Graph

admin.site.register(App)
admin.site.register(Tag)
admin.site.register(Graph)