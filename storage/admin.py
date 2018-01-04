#coding:utf-8
from django.contrib import admin
from django.contrib import messages
from storage.models import App, Tag, Graph

class GraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'url')
    readonly_fields = ('display',)


admin.site.register(App)
admin.site.register(Tag)
admin.site.register(Graph, GraphAdmin)