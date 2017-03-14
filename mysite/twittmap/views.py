from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch, RequestsHttpConnection
# Create your views here.
from .models import Tweet
import requests, json
HOST = 'https://search-twittmap1-q22wgseqgxjgys23kyp65eli4u.us-east-1.es.amazonaws.com'
template = 'twittmap/index.html'

def index(request):  
    req = {
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 1
                },
            "mappings": {
                "test": {
                    "properties": {
                        "user": {"type": "text"},
                        "coords": {"type": "geo_point"},
                        "time": {"type": "text","fielddata": True},
                        "text": {"type": "text"}
                        }
                    }
                }
            }
    mapping_addr = '%s/twittmap2/' % (HOST)
    try:
        response = requests.put(mapping_addr, data=json.dumps(req))
        #print (response.text)
    except:
        pass

        req = {
                "query": {
                    "match_all":{}
                    },
                "size": 100,
                "sort": [{"time": {"order": "desc"}}]
                }
        
    search_addr = '%s/twittmap2/test/_search' % (HOST)
    response = requests.post(search_addr, data = json.dumps(req))
    #print (response.text)
    return render(request, 'twittmap/index.html')

def search(request):
    searchtext = request.POST['searchtext']
    #print (searchtext)
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
            "size": 100,
            "sort": [{"time": {"order": "desc"}}]
            }
    search_addr = '%s/twittmap2/tweet/_search' % (HOST)
    response = requests.post(search_addr, data = json.dumps(req))
    #print (response.text)
    #test = response['hits']['hits']
    #print (test.text)
    #return render(response, 'twittmap/index.html')
    return HttpResponse(response, content_type='application/json')

def update(request):
    searchtext = request.POST['searchtext']
    #print(searchtext)
    req = {
            "query": {
                "match":{
                    "text": searchtext
                    }
                },
            "size": 100,
            "sort": [{"time": {"order": "desc"}}]
            }
    search_addr = '%s/twittmap2/test/_search' % (HOST)
    response = requests.post(search_addr, data = json.dumps(req))
    #print (response.text)
    return HttpResponse(response, content_type='application/json')


def geolocation(request):
	loc = request.POST['loc']
	radius = request.POST['radius']
	print (loc+"\n")
	print (radius+"\n")
	req = {
		"size": 100,
		"query": {
			"bool": {
				"must": {
					"match_all":{}
				},
				"filter": {
					"geo_distance": {
						"distance": '1000km',
						"coords": loc
					}
				}
			}
		}
	}
	search_addr = '%s/twittmap2/test/_search' % (HOST)
	response = requests.post(search_addr, data = json.dumps(req))
	print (response.text)
	return HttpResponse(response, content_type='application/json')


