# Create your views here.
from sodaSite.api.models import *
from django.http import HttpResponse
from sodaSite.api.sodaTypes import SODA_TYPE_CHOICES, TYPE_DICT
from django.utils import simplejson, timezone
from pychart import *
from django.template import loader, Context
from django.shortcuts import render_to_response


def example(request):
    return render_to_response("chart/example.html")


def salesByType(request):
    dewSales = SodaTransaction.objects.filter(Soda__name=TYPE_DICT[1])
    data = {'data': 'stuff'}
    return render_to_response("chart/example.html")


def salesByTime(request):
    pass


def salesByMachine(request):
    pass


def salesByBuilding(request):
    pass


