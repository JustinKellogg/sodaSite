# Create your views here.

from django.shortcuts import render


def HomePageView(request):
    return render(request, 'home/home.html')

