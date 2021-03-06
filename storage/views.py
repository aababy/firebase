#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from storage.models import App, Category, Graph, Package, Feature
from django.contrib import messages
from django.http import HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from datetime import datetime,timedelta


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
                data['tag_order'] = query.category_order
                data['version'] = query.version
                data['force_update_version'] = query.force_update_version
                return HttpResponse(json.dumps(data), content_type='application/json')

    elif name == 'tag':
        for query in Category.objects.all():
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
            category_names = map(lambda x: x.name, query.category.all())
            data['tag'] = '|'.join(category_names)
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

def ajax_get_graphs(request):
    jsonData = []
    for query in Graph.objects.all():
        data = {}
        data['name'] = query.name
        jsonData.append(data)

    return HttpResponse(json.dumps(jsonData, sort_keys=True), content_type='application/json')

def ajax_batch_check_graph(request):
    data = request.GET.getlist('data')

    found = []
    for graph_name in data:
        for query in Graph.objects.all():
            if graph_name == query.name:
                found.append(graph_name)

    return HttpResponse(json.dumps(found, sort_keys=True), content_type='application/json')

def ajax_batch_graphs(request):
    name = str(request.GET.get('name'))
    thumb_url = str(request.GET.get('url'))
    original_url = str(request.GET.get('original_url'))

    date = datetime.now()
    for daily in Graph.objects.order_by('-date'):
        date = daily.date + timedelta(days=1)
        break

    graph = Graph(name=name, url=thumb_url, original_url=original_url, date=date)
    graph.save()

    category = name[0:name.find('_')].lower()
    for query in Category.objects.all():
        if query.name.lower() == category:
            graph.category.add(query)
            graph.save()
            break

    jsonData = []
    return HttpResponse(json.dumps(jsonData, sort_keys=True), content_type='application/json')