# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

def HomePageView(request):
    return render(request, 'home/home.html')