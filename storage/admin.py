#coding:utf-8
from django.contrib import admin
from django.contrib import messages
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from storage.models import App, Tag, Graph, Package, Feature
from storage.forms import TagForm

class AppAdmin(admin.ModelAdmin):
    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/app_admin.js")

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'apps')
    list_filter = ['app']
    filter_horizontal = ('app',)
    search_fields = ['app__name']

    def apps(self, tag):
        app_names = map(lambda x: x.name, tag.app.all())
        return ' | '.join(app_names)

class GraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'tags', 'subscription', 'date')
    readonly_fields = ('display',)
    list_filter = ['tag']
    filter_horizontal=('tag',)
    search_fields = ['tag__name']
    actions = ['add_tags', 'delete_tags', 'modify_subscription']

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    def tags(self, graph):
        tag_names = map(lambda x: x.name, graph.tag.all())
        return ' | '.join(tag_names)

    class tags_form(forms.forms.Form):  
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)  
        data_src = forms.ModelChoiceField(Tag.objects)

    def add_tags(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            modeladmin.message_user(request, u'Action canceled.')
            return
        elif 'data_src' in request.POST:
            form = modeladmin.tags_form(request.POST)
            if form.is_valid():
                data_src = form.cleaned_data['data_src']
                for selected in queryset:
                    selected.tag.add(data_src)
                    selected.save()
                modeladmin.message_user(request, "%s item(s) successfully updated." % queryset.count())
                return HttpResponseRedirect(request.get_full_path())
            else:
                messages.warning(request, u"Tags must be selected. ")
                form = None

        if not form:  
            form  = modeladmin.tags_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'add_tags', 'title': u'Add tags'},  
                                  context_instance=RequestContext(request))  
    add_tags.short_description = u'Add tags'

    def delete_tags(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            modeladmin.message_user(request, u'Action canceled.')
            return
        elif 'data_src' in request.POST:
            form = modeladmin.tags_form(request.POST)
            if form.is_valid():
                data_src = form.cleaned_data['data_src']
                for selected in queryset:
                    selected.tag.remove(data_src)
                    selected.save()
                modeladmin.message_user(request, "%s item(s) successfully updated." % queryset.count())
                return HttpResponseRedirect(request.get_full_path())
            else:
                messages.warning(request, u"Tags must be selected. ")
                form = None

        if not form:
            form  = modeladmin.tags_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'delete_tags', 'title': u'Delete tags'},  
                                  context_instance=RequestContext(request))
    delete_tags.short_description = u'Delete tags'

    def modify_subscription(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            for selected in queryset:
                selected.subscription = False
                selected.save()
            modeladmin.message_user(request, "%s item(s) successfully remove subscription." % queryset.count())
            return HttpResponseRedirect(request.get_full_path())
        elif 'data_src' in request.POST:
            for selected in queryset:
                selected.subscription = True
                selected.save()
            modeladmin.message_user(request, "%s item(s) successfully add subscription." % queryset.count())
            return HttpResponseRedirect(request.get_full_path())

        form  = modeladmin.tags_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'modify_subscription', 'title': u'Modify subscription'},  
                                  context_instance=RequestContext(request))
    modify_subscription.short_description = u'Modify subscription'

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/graph_admin.js")

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'graphs', )
    filter_horizontal=('graph',)

    def graphs(self, package):
        graph_names = map(lambda x: x.name, package.graph.all())
        return ' | '.join(graph_names)

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/package_admin.js")

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', )
    readonly_fields = ('display',)

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/feature_admin.js")

admin.site.register(App, AppAdmin)
admin.site.register(Tag, TagAdmin, form = TagForm)
admin.site.register(Graph, GraphAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Feature, FeatureAdmin)

admin.site.site_title = 'Firebase Storage admin'
admin.site.site_header = 'Firebase Storage'