from twython import TwythonStreamer

import random 


APP_KEY='DCqdGQEBRmpsZyA0YM38jFvLD'
APP_SECRET='qd8SDvqJLr239sxXXgAr0DOHIGAM1YN56OT8SsEgsUApbTv9z3'
OAUTH_TOKEN='716831862941847552-HbxSaNfmj93h2VqdFfhTvzEhpOSBvJf'
OAUTH_TOKEN_SECRET='q4mOw6u9lHEVfUkdVQBosqQYqE9pbN9IBC9DCvdmoqODb'


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
			tweet = {
				'user': data['user']['name'],
				'coords': {
					'latitude': geo_coords[1],
					'longitude': geo_coords[0]
				},
				'time': time,
				'text': data['text']
			}
			print (tweet['time'].encode('utf-8'))
			print (tweet['coords'])
			print (tweet['text'].encode('utf-8'))

	def on_error(self, status_code, data):
		print (status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='twitter')