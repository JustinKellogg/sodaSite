# Create your views here.
from sodaSite.api.models import *
from django.http import HttpResponse
from sodaSite.api.sodaTypes import SODA_TYPE_CHOICES, TYPE_DICT
from django.utils import simplejson, timezone
from django.shortcuts import render_to_response


def example(request):
    sales = {'Title': 'pizza example', 'Mushrooms': 55, 'Onions': 13, 'Olives': 15, 'Zucchini': 31, 'Pepperoni': 2, 'Cheese': 44}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/pieChart.html", {'sales': sales})


def salesByType(request):
    title = "Sales by Type"
    dewSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[1]))
    docSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[2]))
    pepSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[3]))
    cokSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[4]))
    sales = {'Title': title, 'Mountain Dew': dewSales, 'Doctor Pepper': docSales, 'Pepsi': pepSales, 'Coke': cokSales}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/pieChart.html", {'sales': sales})


def salesByTime(request):
    pass


def salesByMachine(request):
    pass


def salesByBuilding(request):
    pass


