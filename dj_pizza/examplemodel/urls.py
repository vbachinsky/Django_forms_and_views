from django.conf.urls import url
from django.urls import path
from . import views
from examplemodel.views import *

#It creates a scheme for ExampleModels
#examplemodel/urls.py

urlpatterns = [
	path('', ExampleTemplateView.as_view(), name='home'),
	path('listview/', ExampleListView.as_view(), name='list'),
	path('view/', ExampleView.as_view(), name='view'),
	path('post/', CreatePost.as_view(), name='post'),
]