# Django-ShortURL
creating a web-app to generate short urls once the user inputs long urls


Hello!!


To run this project please firstly clone the project to your local repository
Cloning URL "https://github.com/MeenalV/Django-ShortURL.git"

Now open the cmd and install
1. redis
2. resolve

use the following commands to run it properly :

1. navigate it to the project folder : ShortURL
2. check if manage.py is present (ls)
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver

Deployment File = Dockerfile

After this your localhost should be up and running :)


So this is basically a code walkthrough on how to generate a ShortURL when we are given the big ones eg : 
"https://www.youtube.com/watch?v=ll0mOXceOXM"

The name of my app is url_shortning.

The file contains some django generated files :
	1. views.py
	2. admin.py
	3. models.py
	4. apps.py
	5. urls.py
	6. __init__.py (the app wont run if one accidentally deletes it)

The files that I created are:
	1. shortenin_logic
	2. forms.py

As we know, most of the application business logic is written in view.py ( MVT - V (View))

My view.py contains 2 functions, who take the requests and return the respected responses. 

First Function : 
	url_shortner(request) : 
	1. it takes the requests from the html form that is displayed to the user. 
	2. checks whether the input value (form) is valid or not, then nly it proceeds.
	3. Then it uses its logics to calculate the id of the "MainURL" that will be stored in db and then converts this unique integer id to a base62 key, and then appends it to our domain and stores it as a shortenURL value in the DB (table : URLData which collets the URL related data) 
	4. This Short URL is then visible to the user, who can furthur either click the hyperlink and get redirected to the Main Site or they can copy it and use it on other browsers. 
	5. The time limit before this short URL expires is 900 seconds or 15 min. This could be changed with change variable expTime declared globally.

	get_targetURL(request) :	
	1. This function takes the request when the person clicks the hyperlink, or paste the short URL on the browser.
	2. The URL consists of the base62 key which is then extracted from the URL and is used to find the Main URL and then redirects it to the site. 
	3. The querying time is slow as the in-memory cache db : redis is used to fetch the Main URL and then redirect it.
	4. Redis is also used to monitor user hits in a minute. 

There are 2 models or tables created to complete the following requirements :
	URLData :
		targetURL
		shortenURL
		status				(only active and inactive)
		dateCreated
		dateExpired
		ShortURLbase		(base62 key stored)	

	ShortURLAnalytics :
		URLid				(foreignkey , stores targetURL value)
		URLid_id			(foreignkey using URLData id)
		targetURL
		shortenURL
		IPAddr
		count_of_hits

So this is the basic code overview.	