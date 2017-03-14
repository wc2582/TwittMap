from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch, RequestsHttpConnection
# Create your views here.
from .models import Tweet
import requests, json
HOST = 'https://search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com'
template = 'twittmap/index.html'



def index(request):    
	'''	
	req = {
		"settings": {
		"number_of_shards": 5,
		"number_of_replicas": 1
		},
		"mappings": {
			"tweets": {
				"properties": {
					"user": { "type" : "text" },
					"coords": { "type": "geo_point"},
					"time": { "type": "text"},
					"text": { "type": "text"}
				}
			}
		}
	}
	search_addr = '%s/twittmap' % (HOST)
	response = requests.post(search_addr, data = json.dumps(req))
	print (response.text)
	'''


	req = {
		"query": {
			"match_all":{}
			},
		"size": 100
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
			"match":{
				"text": searchtext
			}
		},
		"size": 100
    	#"sort": [{"time": {"order": "desc"}}]
	}
	search_addr = '%s/twittmap/tweets/_search' % (HOST)
	response = requests.post(search_addr, data = json.dumps(req))

	print (response.text)
	return render(request, 'twittmap/index.html')
    #return HttpResponse(response, content_type='application/json')
