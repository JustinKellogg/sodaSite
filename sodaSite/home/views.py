# Create your views here.

from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.template import *

def HomePageView(request):
    return render(request, 'home/home.html')