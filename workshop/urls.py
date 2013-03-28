from django.conf.urls import patterns, urls
import views

urlpatterns = patterns(url(r'^$', views.index, name='index'),                    
                      )
