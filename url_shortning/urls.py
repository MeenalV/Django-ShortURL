
from django.urls import path 
from url_shortning import views

urlpatterns = [
	# path('home/', views.home),
    path('home', views.url_shortner , name = 'home'),
    path('<slug:hashid>', views.get_targetURL , name = 'redirecting_url'),
    # path('shortner/<int:id>', views.retrieve_data , name = 'work') , 
]
