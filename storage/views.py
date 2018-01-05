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
                data['version'] = '1'
                jsonData.append(data)
                break
        return HttpResponse(json.dumps(jsonData), content_type='application/json')

    elif name == 'tag':
        queryset = Tag.objects.all()
        json_serializer = serializers.get_serializer("json")()
        data = json_serializer.serialize(queryset, ensure_ascii=False)        
        return HttpResponse(data, content_type="application/json")

    elif name == 'graph':
        queryset = Graph.objects.all()
        json_serializer = serializers.get_serializer("json")()
        data = json_serializer.serialize(queryset, ensure_ascii=False)        
        return HttpResponse(data, content_type="application/json")

def ajax_message(request):
    msg = str(request.GET.get('msg'))
    path = str(request.GET.get('path'))
    messages.add_message(request, messages.INFO, msg)           #显示message

    return render_to_response('messages.html', locals(), context_instance = RequestContext(request)) 
    # return HttpResponseRedirect(path)
