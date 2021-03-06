# coding: utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventos.views.home', name='home'),
    # url(r'^eventos/', include('eventos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventos/', include('eventos.workshop.urls', namespace="workshop")),
    # url(r'^evento/.+$', include('eventos.workshop.urls', namespace="workshop")),
    url(r'^$', "eventos.workshop.views.index", name='index'),
    # url(r'^ordenar/titulo/', eventos.workshop.views.titulo, name='titulo'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
