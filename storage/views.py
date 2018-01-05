#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from storage.models import App
from django.contrib import messages
from django.http import HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

def ajax_publish(request):
    jsonData = []
    for query in App.objects.all():
        data = {}
        data['name'] = query.name
        data['tag_order'] = query.tag_order
        jsonData.append(data)

    print u'data:' + json.dumps(jsonData)
    return HttpResponse(json.dumps(jsonData), content_type='application/json')

def ajax_message(request):
    msg = str(request.GET.get('msg'))
    path = str(request.GET.get('path'))
    messages.add_message(request, messages.INFO, msg)           #显示message

    return render_to_response('messages.html', locals(), context_instance = RequestContext(request)) 
    # return HttpResponseRedirect(path)
