#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from storage.models import App
from django.contrib import messages
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
    jsonData = []
    for query in App.objects.all():
        data = {}
        data['name'] = query.name
        data['tag_order'] = query.tag_order
        jsonData.append(data)

    msg = str(request.GET.get('msg'))
    messages.add_message(request, messages.INFO, msg)           #显示message
    # return HttpResponse('abc', content_type='text/plain')
    return HttpResponse(json.dumps(jsonData), content_type='application/json')
