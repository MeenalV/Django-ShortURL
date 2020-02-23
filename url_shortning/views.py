from django.shortcuts import render ,get_object_or_404 , redirect
from url_shortning.forms import Url
from url_shortning.models import URLData , ShortURLAnalytics
from django.utils import timezone
from datetime import datetime ,  timedelta
from url_shortning.shortenin_logic import * 
from django.urls import resolve
from django.http import HttpResponse
import redis
import json 
import socket

expTime 					= 900
hostname 					= socket.gethostname()
IPAddr 						= socket.gethostbyname(hostname)
count 						= 0
cache_redis 				= redis.Redis()
ip_hit_count 				= redis.Redis()
local_url 					= '//127.0.0.1:8000/'

def url_shortner(request) :
	
	form =  Url(request.POST)
	if  form.is_valid() :
		
		if URLData.objects.all().exists() :
			num 				= generate_id(URLData.objects.latest('id').id)
		else :
			num 				= generate_id(0)
		base62 					= convert_to_base62(num)
		base10 					= convert_to_base10(base62)
		
		obj 					= URLData()	
		analysis 				= ShortURLAnalytics.objects.all().filter(URLid = num , IPAddr = IPAddr) 
		
		obj.targetURL 			= form.cleaned_data['targetURL'].split("//")[1]
		targetURL 				= obj.targetURL
		obj.shortenURL 			= local_url + base62
		shortURL 				= obj.shortenURL
		obj.shortURLbase 		= base62
		obj.dateCreated 		= datetime.now() + timedelta(hours = 5 , minutes = 30)
		obj.dateExpired			= datetime.now() + timedelta(hours = 5 , minutes = 30 , seconds = expTime)
	
		obj.save()

		if not analysis :
			analysisObj 				= ShortURLAnalytics()
			analysisObj.URLid_id 		= num
			analysisObj.targetURL 		= obj.targetURL
			analysisObj.shortenURL	 	= obj.shortenURL
			analysisObj.IPAddr 			= IPAddr
		analysisObj.save()


		data = URLData.objects.all().filter(targetURL = targetURL).order_by('-id')	
		cache_redis.setex(num , expTime , targetURL)	

		if data.count() == 0 :
			context 			= {'form' : form }
		else :
			context 			= {'form' : form ,  'data' : data[0] ,  'shortURL' : shortURL }
		form =  Url()

	else :
		context 				= {'form' : form}	

	return render(request , 'url_shortning/forms.html', context)



def get_targetURL(request , hashid)	:
	global count
	count 						= count+1
	keyid 						= convert_to_base10(hashid)
	result 						= cache_redis.get(keyid)

	analysis 					= ShortURLAnalytics.objects.get(URLid = keyid , IPAddr = IPAddr)
	analysis.count_of_hits 		+= 1
	ip_hit_count.setex(IPAddr , 60 , analysis.count_of_hits)
	analysis.save()
	
	data = URLData().objects.get(id = keyid)

	if not ip_hit_count.get(IPAddr) and int(ip_hit_count.get(IPAddr).decode("utf-8"))>= 100 :
		return HttpResponse("<H1>The user is temporarily blocked</H1>")
	
	if not result :
		return HttpResponse("<H1>Sorry the page expired!! It exceeded the time Limit of 2 Mins</H1>")
	else :	
		change_status()
		str_result = result.decode("utf-8")
		return redirect("//"+str_result)