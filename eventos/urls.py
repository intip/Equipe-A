from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from workshop import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventos.views.home', name='home'),
    # url(r'^eventos/', include('eventos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workshop/', views.index, name="workshop"),
)
