# Create your views here.
from sodaSite.api.models import *
from sodaSite.api.sodaTypes import TYPE_DICT
from django.utils import simplejson, timezone
from django.shortcuts import render_to_response
import datetime
from django.utils import timezone


def example(request):
    sales = {'Title': 'pizza example', 'X': 'Toppings', 'Y': 'Slices', 'Mushrooms': 55, 'Onions': 13, 'Olives': 15, 'Zucchini': 31, 'Pepperoni': 2, 'Cheese': 44}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/pieChart.html", {'sales': sales})


def salesByType(request):
    title = "Sales by Type"
    X = 'Type'
    Y = 'Sales'
    dewSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[1]))
    docSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[2]))
    pepSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[3]))
    cokSales = len(SodaTransaction.objects.filter(Soda__name=TYPE_DICT[4]))
    sales = {'Title': title, 'X': X, 'Y': Y, 'Mountain Dew': dewSales, 'Doctor Pepper': docSales, 'Pepsi': pepSales, 'Coke': cokSales}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/pieChart.html", {'sales': sales})


def salesByTime(request):
    title = "Sales by Time"
    X = 'Time'
    Y = 'Sales'
    allTrans = SodaTransaction.objects.all()
    today = len([soda for soda in allTrans if soda.timeWindow(0, 1)])
    yesterday = len([soda for soda in allTrans if soda.timeWindow(1, 2)])
    lastWeek = len([soda for soda in allTrans if soda.timeWindow(2, 7)])
    lastMonth = len([soda for soda in allTrans if soda.timeWindow(7, 31)])
    prior = len([soda for soda in allTrans if soda.timeWindow(31, 100000)])
    sales = {'Title': title, 'X': X, 'Y': Y, 'today': today, 'yesterday': yesterday, 'lastWeek': lastWeek, 'lastMonth': lastMonth, 'prior': prior}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/LineChart.html", {'sales': sales})


def sugarSales(request):
    title = "Sugar per Soda"
    X = 'Type'
    Y = 'Sugar'
    allTrans = SodaTransaction.objects.all()
    MD = sum([trans.Soda.sugar for trans in allTrans if trans.Soda.name == 'MD'])
    PS = sum([trans.Soda.sugar for trans in allTrans if trans.Soda.name == 'PS'])
    CK = sum([trans.Soda.sugar for trans in allTrans if trans.Soda.name == 'CK'])
    DP = sum([trans.Soda.sugar for trans in allTrans if trans.Soda.name == 'DP'])

    sales = {'Title': title, 'X': X, 'Y': Y, 'MD': MD, 'PS': PS, 'CK': CK, 'DP': DP}
    sales = simplejson.dumps(sales)
    return render_to_response("chart/PieChart.html", {'sales': sales})


def salesByMachine(request):
    pass


def salesByBuilding(request):
    pass


