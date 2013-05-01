from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
    url(r'^$',
        'sodaSite.purchase.views.index',
        name='index'),
    url(r'^login', 
        'sodaSite.purchase.views.my_login', 
        name='login'),
    url(r'^logout',
        'sodaSite.purchase.views.my_logout',
        name='logout'),
    url(r'^buy',
        'sodaSite.purchase.views.buy',
        name='buy'),
)