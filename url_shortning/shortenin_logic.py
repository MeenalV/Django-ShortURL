from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import URLData
import string


lst = list(string.ascii_lowercase)
lst = lst + list(string.ascii_uppercase)
for i in range(0,10) :
	lst.append(str(i))

# print(lst , len(lst))
def generate_id(id) :
	id = int(id)
	key_id =  id+1
	return key_id

def convert_to_base62(key):
	digits = []
	num = key
	while num > 0 :
		remainder = divmod(num , 62)[1]
		num = divmod(num , 62)[0]
		digits.append(remainder)
	digits.reverse()

	alpha = ''
	for i in digits :
		alpha = alpha+ lst[i]

	return alpha

def convert_to_base10(crypt) :
	lstcrypt = list(crypt)
	len_lstcrypt = len(lstcrypt)
	sumbase10 = 0 
	for i in range(len_lstcrypt) :
		sumbase10 = sumbase10 + lst.index(lstcrypt[i])*pow(62, len_lstcrypt - (i+1))

	return sumbase10	

def change_status() :
	data = URLData.objects.all().filter(dateExpired__lte = datetime.now())
	for value in data :
		value.status = "INACTIVE"
		value.save()	