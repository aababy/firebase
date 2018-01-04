#coding:utf-8
from django.contrib import admin
from django.contrib import messages
from storage.models import App, Tag, Graph

class AppAdmin(admin.ModelAdmin):
    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/app_admin.js")

class TagAdmin(admin.ModelAdmin):
    search_fields = ['app']

class GraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'display')
    readonly_fields = ('display',)

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/graph_admin.js")



admin.site.register(App, AppAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Graph, GraphAdmin)