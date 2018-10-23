#coding:utf-8
from django.contrib import admin
from django.contrib import messages
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from storage.models import App, Category, Graph, Package, Feature
from storage.forms import CategoryForm

class AppAdmin(admin.ModelAdmin):
    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/firebase-jigsaw.js",
        "/static/app_admin.js")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'apps')
    list_filter = ['app']
    filter_horizontal = ('app',)
    search_fields = ['app__name']

    def apps(self, category):
        app_names = map(lambda x: x.name, category.app.all())
        return ' | '.join(app_names)

class GraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'categories', 'starting', 'subscription', 'date')
    readonly_fields = ('display',)
    list_filter = ['category']
    filter_horizontal=('category',)
    search_fields = ['name', 'category__name']
    actions = ['add_categories', 'delete_categories', 'modify_subscription', 'modify_starting']
    list_editable = ['date', ]

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    def categories(self, graph):
        category_names = map(lambda x: x.name, graph.category.all())
        return ' | '.join(category_names)

    class categories_form(forms.forms.Form):  
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)  
        data_src = forms.ModelChoiceField(Category.objects)

    def add_categories(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            modeladmin.message_user(request, u'Action canceled.')
            return
        elif 'data_src' in request.POST:
            form = modeladmin.categories_form(request.POST)
            if form.is_valid():
                data_src = form.cleaned_data['data_src']
                for selected in queryset:
                    selected.category.add(data_src)
                    selected.save()
                modeladmin.message_user(request, "%s item(s) successfully updated." % queryset.count())
                return HttpResponseRedirect(request.get_full_path())
            else:
                messages.warning(request, u"Categorys must be selected. ")
                form = None

        if not form:  
            form  = modeladmin.categories_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'add_categories', 'title': u'Add categories'},  
                                  context_instance=RequestContext(request))  
    add_categories.short_description = u'Add categories'

    def delete_categories(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            modeladmin.message_user(request, u'Action canceled.')
            return
        elif 'data_src' in request.POST:
            form = modeladmin.categories_form(request.POST)
            if form.is_valid():
                data_src = form.cleaned_data['data_src']
                for selected in queryset:
                    selected.category.remove(data_src)
                    selected.save()
                modeladmin.message_user(request, "%s item(s) successfully updated." % queryset.count())
                return HttpResponseRedirect(request.get_full_path())
            else:
                messages.warning(request, u"Categorys must be selected. ")
                form = None

        if not form:
            form  = modeladmin.categories_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'delete_categories', 'title': u'Delete categories'},  
                                  context_instance=RequestContext(request))
    delete_categories.short_description = u'Delete categories'

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

        form  = modeladmin.categories_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'modify_subscription', 'title': u'Modify subscription'},  
                                  context_instance=RequestContext(request))
    modify_subscription.short_description = u'Modify subscription'

    def modify_starting(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            for selected in queryset:
                selected.starting = False
                selected.save()
            modeladmin.message_user(request, "%s item(s) successfully turn off starting." % queryset.count())
            return HttpResponseRedirect(request.get_full_path())
        elif 'data_src' in request.POST:
            for selected in queryset:
                selected.starting = True
                selected.save()
            modeladmin.message_user(request, "%s item(s) successfully turn on starting." % queryset.count())
            return HttpResponseRedirect(request.get_full_path())

        form  = modeladmin.categories_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'modify_starting', 'title': u'Modify starting'},  
                                  context_instance=RequestContext(request))
    modify_starting.short_description = u'Modify starting'

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/firebase-jigsaw.js",
        "/static/graph_admin.js")

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'graphs', 'apps', )
    filter_horizontal=('graph', 'app', )

    def graphs(self, package):
        graph_names = map(lambda x: x.name, package.graph.all())
        return ' | '.join(graph_names)

    def apps(self, package):
        app_names = map(lambda x: x.name, package.app.all())
        return ' | '.join(app_names)

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/firebase-jigsaw.js",
        "/static/package_admin.js")

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'order')
    readonly_fields = ('display',)

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/firebase-jigsaw.js",
        "/static/feature_admin.js")

admin.site.register(App, AppAdmin)
admin.site.register(Category, CategoryAdmin, form = CategoryForm)
admin.site.register(Graph, GraphAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Feature, FeatureAdmin)

admin.site.site_title = 'Jigsaw admin'
admin.site.site_header = 'Jigsaw'