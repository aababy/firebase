#coding:utf-8
from django.contrib import admin
from django.contrib import messages
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from storage.models import App, Tag, Graph

class AppAdmin(admin.ModelAdmin):
    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/app_admin.js")

class TagAdmin(admin.ModelAdmin):
    list_filter = ['app']
    filter_horizontal=('app',)
    search_fields = ['app__name']

class GraphAdmin(admin.ModelAdmin):
    list_display = ('name', 'display')
    readonly_fields = ('display',)
    list_filter = ['tag']
    filter_horizontal=('tag',)
    search_fields = ['tag__name']
    actions = ['add_tags']

    class add_tags_form(forms.forms.Form):  
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)  
        data_src = forms.ModelChoiceField(Tag.objects)

    def add_tags(modeladmin, request, queryset):
        form = None
        if 'cancel' in request.POST:
            modeladmin.message_user(request, u'Action canceled.')
            return
        elif 'data_src' in request.POST:
            form = modeladmin.add_tags_form(request.POST)
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
            form  = modeladmin.add_tags_form(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})  
        return render_to_response('batch_update.html',  
                                  {'objs': queryset, 'form': form, 'path':request.get_full_path(), 'action': 'add_tags', 'title': u'Add tags'},  
                                  context_instance=RequestContext(request))  
  
    add_tags.short_description = u'Add tags'  

    class Media:
        js=("https://www.gstatic.com/firebasejs/4.2.0/firebase.js", 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-app.js', 
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-auth.js',
        'https://www.gstatic.com/firebasejs/4.2.0/firebase-storage.js',
        "/static/graph_admin.js")



admin.site.register(App, AppAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Graph, GraphAdmin)

admin.site.site_title = 'Firebase Storage admin'
admin.site.site_header = 'Firebase Storage'