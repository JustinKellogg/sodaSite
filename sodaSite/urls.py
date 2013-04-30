from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'sodaSite.views.home', name='home'),
                       # url(r'^sodaSite/', include('sodaSite.foo.urls')),
                       url(r'^', include('sodaSite.home.urls')),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^', include('sodaSite.home.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('sodaSite.polls.urls', namespace='polls')),
                       url(r'^blog/', include('sodaSite.blog.urls', namespace='blog')),
                       url(r'^api/', include('sodaSite.api.urls', namespace='api')),
                       url(r'^chart/', include('sodaSite.chart.urls', namespace='chart')),
                       url(r'^home/', include('sodaSite.home.urls', namespace='home')),
                       url(r'^inventory/', include('sodaSite.inventory.urls', namespace='inventory')),
)
