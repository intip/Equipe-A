# coding: utf-8

from django.conf.urls import patterns, url
from eventos.workshop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^evento/(?P<evento>\d+)$', views.evento, name='evento'),
    url(r'^data/$', views.data, name='data'),
    url(r'^titulo/$', views.titulo, name='titulo'),
    url(r'^contact/$', views.contact, name='contact'),
)
