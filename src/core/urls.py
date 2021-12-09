from django.urls import path

from .views import HomePageView, SamplePageView #import views

urlpatterns = [
	path('', HomePageView.as_view(), name="home"), 
	path('sample/', SamplePageView.as_view(), name="sample"),
]