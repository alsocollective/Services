from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'application.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ip/', 'application.views.ip', name='ip'),
    url(r'^loc/','application.views.country', name='loc')
    # url(r'^admin/', include(admin.site.urls)),
)
