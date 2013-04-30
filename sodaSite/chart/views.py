# Create your views here.
from sodaSite.api.models import *
from sodaSite.api.sodaTypes import TYPE_DICT
from django.utils import simplejson, timezone
from django.shortcuts import render_to_response
import datetime
from django.utils import timezone

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
    title = "Sales by Time"
    allTrans = SodaTransaction.objects.all()
    today = len([soda for soda in allTrans if soda.timeWindow(0, 1)])
    yesterday = len([soda for soda in allTrans if soda.timeWindow(1, 2)])
    prior = len([soda for soda in allTrans if soda.timeWindow(2, 100)])
    sales = {'Title': title, 'today': today, 'yesterday': yesterday, 'prior': prior}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/pieChart.html", {'sales': sales})


def salesByMachine(request):
    pass


def salesByBuilding(request):
    pass


