from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from flickr import urls as flickr_urls
import portfolio.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helleos.views.home', name='home'),
    # url(r'^helleos/', include('helleos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', portfolio.views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flickr/', include(flickr_urls)),
)
