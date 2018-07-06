#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from storage.models import App, Tag, Graph, Package, Feature
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
                query.version += 1
                query.save()

                data = {}
                data['name'] = query.name
                data['tag_order'] = query.tag_order
                data['version'] = query.version
                data['force_update_version'] = query.force_update_version
                return HttpResponse(json.dumps(data), content_type='application/json')

    elif name == 'tag':
        for query in Tag.objects.all():
            data = {}
            data['name'] = query.name
            data['display_name'] = query.display_name
            app_names = map(lambda x: x.name, query.app.all())
            data['app'] = '|'.join(app_names)
            data['cover'] = str(query.cover)
            jsonData.append(data)

    elif name == 'graph':
        for query in Graph.objects.order_by("-date"):
            data = {}
            data['name'] = query.name
            tag_names = map(lambda x: x.name, query.tag.all())
            data['tag'] = '|'.join(tag_names)
            data['date'] = str(query.date)
            data['subscription'] = query.subscription
            data['original'] = not query.starting
            jsonData.append(data)

    elif name == 'package':
        for query in Package.objects.order_by("name"):
            data = {}
            data['name'] = query.name
            data['thumb_name'] = query.thumb_name
            graph_names = map(lambda x: x.name, query.graph.all())
            data['graph'] = '|'.join(graph_names)
            app_names = map(lambda x: x.name, query.app.all())
            data['app'] = '|'.join(app_names)
            jsonData.append(data)      

    elif name == 'feature':
        for query in Feature.objects.all():
            data = {}
            data['name'] = query.name
            data['order'] = query.order
            jsonData.append(data)               
    
    pack = {}
    pack['version'] = getVersion(request)
    pack['data'] = jsonData
    return HttpResponse(json.dumps(pack, sort_keys=True), content_type='application/json')

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
