from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.activityview),
	url(r'register$', views.register),
]