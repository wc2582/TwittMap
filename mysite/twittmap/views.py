from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch, RequestsHttpConnection
# Create your views here.
from .models import Tweet
import requests, json
HOST = 'https://search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com'
template = 'twittmap/index.html'



def index(request):    
	#es = Elasticsearch(HOST)
	#print (es.info)
	req = {
		"query": {
			"match_all":{}
			},
		"size": 1
		#"sort": [{"time": {"order": "desc"}}]
		}
	search_addr = '%s/twittmap/tweets/_search' % (HOST)
	response = requests.post(search_addr, data = json.dumps(req))
	print (response.text)
	return render(request, 'twittmap/index.html')

def search(request):
    #searchtext = request.POST['searchtext']
    searchtext = request.POST.get('searchtext', False)
    print (searchtext)
    #response = '<h1>test<h1>'


    req = {
    	"query": {
    		"match_all":{}
    		},
    	"size": 1
    	#"sort": [{"time": {"order": "desc"}}]
    	}
    search_addr = '%s/twittmap/tweets/_search' % (HOST)
    response = requests.post(search_addr, data = json.dumps(req))


    return HttpResponse(response)
    #return HttpResponse(response, content_type='application/json')
