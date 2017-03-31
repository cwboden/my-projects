"""
Definition of urls for website.
"""

from django.conf.urls import include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', website.views.home, name='home'),
    # url(r'^website/', include('website.website.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # leagues base
    url(r'^leagues/', include('leagues.urls')),

    # website homepage
    url(r'^', include('leagues.urls')),

]
