from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch, RequestsHttpConnection
# Create your views here.
from .models import Tweet
import requests, json
HOST = 'https://search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com'
template = 'twittmap/index.html'

def index(request):    
    req = {
            "query": {
                "match_all":{}
                },
            "size": 100
            #"sort": [{"time": {"order": "desc"}}]
            }
    search_addr = '%s/twittmap/test1/_search' % (HOST)
    response = requests.post(search_addr, data = json.dumps(req))
    #print (response.text)
    return render(request, 'twittmap/index.html')

def search(request):
    searchtext = request.POST['searchtext']
    print (searchtext)
    #searchtext = request.POST.get('searchtext', False)
    #print (searchtext)
    #response = '<h1>test<h1>'
    #searchtext = 'test'
    
    req = {
            "query": {
                "match":{
                    "text": searchtext
                    }
                },
            "size": 100
            #"sort": [{"time": {"order": "desc"}}]
            }
    search_addr = '%s/twittmap/test1/_search' % (HOST)
    response = requests.post(search_addr, data = json.dumps(req))
    #print (response.text)
    #test = response['hits']['hits']
    #print (test.text)
    #return render(response, 'twittmap/index.html')
    return HttpResponse(response, content_type='application/json')
