from django.shortcuts import render
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
		"size": 1000
		#"sort": [{"time": {"order": "desc"}}]
		}
	search_addr = '%s/twittmap/tweets/_search' % (HOST)
	response = requests.post(search_addr, data = json.dumps(req))
	print (response.text)
	return render(request, 'twittmap/index.html')
