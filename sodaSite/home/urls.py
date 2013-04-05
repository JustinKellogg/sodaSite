__author__ = 'Justin'

from django.conf.urls.defaults import patterns, url

from sodaSite.home import views

urlpatterns = patterns('',
    url(r'^$', views.HomePageView,name='home'),
    )

