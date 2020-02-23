from django import forms
from django.utils import timezone


class Url(forms.Form) :
	targetURL  = forms.CharField(max_length = 128 , widget = forms.TextInput(
		attrs = (
			{'class' :'form-control' ,
			  'placeholder' : 'Enter URL'	
				}
			) 
		))
		
	# shortenURL = forms.CharField(max_length = 128 , required = False)
	# dateCreated = forms.DateTimeField(required = False)