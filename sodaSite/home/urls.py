__author__ = 'Justin'
from sodaSite.api.models import *

from django.conf.urls import *  # patterns, url
from django.views.generic import ListView
from sodaSite.home import views

#urlpatterns = patterns('',
#    url(r'^$', views.HomePageView,name='home'),
#    )

urlpatterns = patterns('',
        url(r'^$', views.HomePageView,name='home'),
        url(r'^transactions/$',
            ListView.as_view(
                queryset=Transaction.objects.order_by('-date_time')[:10],
                context_object_name='object_list',
                template_name='home/api_update.html'),
            name='api_update'),
)
