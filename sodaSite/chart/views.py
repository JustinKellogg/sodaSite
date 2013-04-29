# Create your views here.
from sodaSite.api.models import *
from django.http import HttpResponse
from sodaSite.api.sodaTypes import SODA_TYPE_CHOICES, TYPE_DICT
from django.utils import simplejson, timezone
from django.shortcuts import render_to_response


def example(request):
    sales = {'Mushrooms': 55, 'Onions': 13, 'Olives': 15, 'Zucchini': 31, 'Pepperoni': 2, 'Cheese': 44}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/example.html", {'sales': sales})


def salesByType(request):
    dewSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[1]))
    docSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[2]))
    pepSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[3]))
    cokSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[4]))
    sales = {'dew': dewSales, 'doc': docSales, 'pep': pepSales, 'coke': cokSales}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/example.html", {'sales': sales})


def salesByTime(request):
    data = (('IO on eyedrops', 61), ('Haskel on Hovercrafts', 276),
            ('Lua on Linseed Oil', 99), ('Django', 1000))
    dataset = [(item[0],[[0,item[1]]]) for item in data]
    pass


def salesByMachine(request):
    pass


def salesByBuilding(request):
    pass


