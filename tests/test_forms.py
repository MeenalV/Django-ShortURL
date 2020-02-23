from django.test import SimpleTestCase
from url_shortning.forms import Url

class TestForms(SimpleTestCase) :
	def test_form(self) :
		form = Url(data={
			'targetURL' : "www.youtube.come"
			})

		self.assertTrue(form.is_valid())	