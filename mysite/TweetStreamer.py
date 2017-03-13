from twython import TwythonStreamer
from elasticsearch import Elasticsearch, RequestsHttpConnection
from datetime import datetime

import random, requests, json

from requests_aws4auth import AWS4Auth
'''
host = 'https://search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com/twittmap/data'
awsauth = AWS4Auth('AKIAJ36PBOCUOTUL4TUQ', 'sPatz8yeckYNOjtELEZv6B5QhG0UOlnJi0UIjoz+', 'us-east-1', 'es')
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print (es.info)
'''

APP_KEY='DCqdGQEBRmpsZyA0YM38jFvLD'
APP_SECRET='qd8SDvqJLr239sxXXgAr0DOHIGAM1YN56OT8SsEgsUApbTv9z3'
OAUTH_TOKEN='716831862941847552-HbxSaNfmj93h2VqdFfhTvzEhpOSBvJf'
OAUTH_TOKEN_SECRET='q4mOw6u9lHEVfUkdVQBosqQYqE9pbN9IBC9DCvdmoqODb'

HOST = 'search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com'


class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			try:
				geo_coords = data['coordinates']['coordinates']
			except:
				geo_coords = [
					random.uniform(-180.0,180.0),
					random.uniform(-90.0,90.0)
				]
			time = data['created_at']
			#time1 = datetime.strptime(time,"%a %b %d %H:%M:%S %z %Y")
			#time1 = time1.strftime("%Y-%m-%d %H:%M:%S")
			tweet = {
				'user': data['user']['name'],
				'coords': {
					'latitude': geo_coords[1],
					'longitude': geo_coords[0]
				},
				'time': time,
				'text': data['text']
			}
			
			#print (tweet['time'])
			#print (tweet['coords'])
			#print (tweet['text'].encode('utf-8'))
			
			#es = Elasticsearch(['search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com'])
			response = requests.post('https://search-twittmap-x3dpgzermwimqntgwel5amlwve.us-east-1.es.amazonaws.com/twittmap/tweets/',json=tweet)
			print (response.text)
	def on_error(self, status_code, data):
		print (status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
while True:
	try:
		stream.statuses.filter(track='twitter')
	except:
		continue


