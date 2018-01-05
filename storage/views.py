#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from storage.models import App, Tag, Graph
from django.contrib import messages
from django.http import HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

def ajax_publish(request):
    name = str(request.GET.get('filename'))

    jsonData = []
    if name == 'app':
        app = str(request.GET.get('appname'))
        # apps
        for query in App.objects.all():
            if query.name == app:
                data = {}
                data['name'] = query.name
                data['tag_order'] = query.tag_order
                data['version'] = query.version
                return HttpResponse(json.dumps(data), content_type='application/json')

    elif name == 'tag':
        for query in Tag.objects.all():
            data = {}
            data['name'] = query.name
            data['display_name'] = query.display_name
            data['image_order'] = query.image_order
            app_names = map(lambda x: x.name, query.app.all())
            data['app'] = '|'.join(app_names)
            jsonData.append(data)

    elif name == 'graph':
        for query in Graph.objects.all():
            data = {}
            data['name'] = query.name
            data['url'] = query.url
            tag_names = map(lambda x: x.name, query.tag.all())
            data['tag'] = '|'.join(tag_names)
            data['date'] = str(query.date)
            jsonData.append(data)  
    
    pack = {}
    pack['version'] = getVersion(request)
    pack['data'] = jsonData
    return HttpResponse(json.dumps(pack), content_type='application/json')

def getVersion(request):
    app = str(request.GET.get('appname'))
    # apps
    for query in App.objects.all():
        if query.name == app:
            return query.version
    return '1'

def ajax_message(request):
    msg = str(request.GET.get('msg'))
    path = str(request.GET.get('path'))
    messages.add_message(request, messages.INFO, msg)           #显示message

    return render_to_response('messages.html', locals(), context_instance = RequestContext(request)) 
    # return HttpResponseRedirect(path)
