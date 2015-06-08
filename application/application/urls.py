from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ip/', 'application.views.ip', name='ip'),
    url(r'^loc/','application.views.country', name='loc'),
    url(r'^.*/$', 'application.views.allother')
)
