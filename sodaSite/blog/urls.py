__author__ = 'Justin'

from django.conf.urls.defaults import *
from sodaSite.blog.views import archive

urlpatterns = patterns('',
                       url(r'^$' , archive),
                       )
