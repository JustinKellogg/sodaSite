__author__ = 'Justin'

from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from sodaSite.api.models import *

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Machine.objects.order_by('id'),
            context_object_name='machine_list',
            template_name='api/index.html'),
        name='index'),
#    url(r'^transactions/$', 'sodaSite.api.views.transactions', name='transactions')
    url(r'^transactions/(?P<soda_id>\d+)/(?P<stid>\d+)/$', 'sodaSite.api.views.transactions', name='transactions'),
    url(r'^check/$', 'sodaSite.api.views.check_machine', name='check_machine'),
    url(r'^ping/$', 'sodaSite.api.views.ping_machine', name='ping'),
)

