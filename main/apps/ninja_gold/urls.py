from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^ninja_gold$', views.index),
	url(r'^ninjado/(?P<action>\w{1,50})/$', views.ninjado)
]