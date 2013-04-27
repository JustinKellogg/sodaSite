from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from sodaSite.api.models import *


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Machine.objects.all,
            context_object_name='machine_list',
            template_name='inventory/index.html'),
        name = 'index')
)