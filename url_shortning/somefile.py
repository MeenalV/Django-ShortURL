import redis
# import Redis
import requests
import json


# print(dir(redis))
redis = redis.Redis()
# redis = redis.Redis()
def fetch_data(username) :
	result = requests.get("https://www.linkedin.com/in/" + username)
	print(
		json.dumps(
			{
				"cached" :False ,
				"profile" : "Hello"
			}
		) )
 
	redis.setex(username , 90 , "hello " + username)

def get_data(username) :
	result = redis.get(username)

	print(result)

fetch_data('meenal-verma')	
get_data('meenal-verma')