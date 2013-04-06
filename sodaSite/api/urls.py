__author__ = 'Justin'

from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from sodaSite.api.models import *

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Machine.objects.order_by('machineID'),
            context_object_name='machine_list',
            template_name='api/index.html'),
        name = 'index'),
)



