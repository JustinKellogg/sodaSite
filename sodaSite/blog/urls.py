from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from sodaSite.blog.models import *

urlpatterns = patterns('',
   url(r'^$',
      ListView.as_view(
          queryset=BlogPost.objects.filter().order_by("-timestamp"),
          context_object_name='blog_list',
          template_name='blog/index.html'),
      name = 'index')
 )
