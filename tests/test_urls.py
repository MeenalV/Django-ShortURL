from django.test import SimpleTestCase 
from django.urls import reverse, resolve
from url_shortning.views import *


# print("Heelo")

class TestUrls(SimpleTestCase) :

	def test_home_url_is_resolved(self):
		url = reverse('home')
		# print(resolve(url))
		self.assertEquals(resolve(url).func , url_shortner)

	def test_redirecting_url_url_is_resolved(self):
		url = reverse('redirecting_url' , args=['f'])
		# print(resolve(url))
		self.assertEquals(resolve(url).func , get_targetURL)	