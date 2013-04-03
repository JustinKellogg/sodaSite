__author__ = 'Justin'
from django.conf.urls import patterns, url
from sodaSite.polls import views
urlpatterns = patterns('',
            #ex /polls/
            url(r'^$', views.index, name = 'index'),
            #ex: /polls/5/
            url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
            #ex: /polls/5/results
            url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
            #ex: /polls/5/vote/
            url(r'^(?P<poll_id>\d+)/votes/$', views.vote, name='vote'),
)