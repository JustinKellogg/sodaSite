__author__ = 'Justin'

from sodaSite.api.models import adminable
from django.contrib import admin

for ad in adminable:
    admin.site.register(ad)


