from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from datetime import datetime , timedelta

# Create your models here.
class URLData(models.Model) :
	targetURL  		= models.CharField(max_length = 256)
	shortenURL 		= models.CharField(max_length = 128)
	dateCreated 	= models.DateTimeField(default = datetime.now())
	dateExpired	 	= models.DateTimeField(default = datetime.now() + timedelta(minutes = 15))
	status 			= models.CharField(max_length = 64 , default = "ACTIVE")
	shortURLbase 	= models.CharField(max_length = 32 , default = 'a')

	def __str__(self):
		return self.targetURL



class ShortURLAnalytics(models.Model) :
	URLid 			= models.ForeignKey(URLData , null = True,on_delete = models.SET_NULL)
	targetURL  		= models.CharField(max_length = 256)
	shortenURL 		= models.CharField(max_length = 128)
	IPAddr			= models.CharField(max_length = 32)
	count_of_hits	= models.IntegerField(default = 0)
	# unique_hits		= models.IntegerField(default = 0)

	def __str__(self):
		return self.targetURL		