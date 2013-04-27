__author__ = 'Justin'
from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from sodaSite.api.models import SodaTransaction


urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=SodaTransaction.objects.all(),
            context_object_name='sales_list',
            template_name='chart/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
        model=SodaTransaction,
        template_name='chart/detail.html'),
        name='detail'),
    url(r'^type/$', 'sodaSite.chart.views.salesByType', name='type'),
    url(r'^example/$', 'sodaSite.chart.views.example',name='example'),
    )
