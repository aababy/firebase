from django.shortcuts import render
from django.http import HttpResponse
from storage.models import App
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
