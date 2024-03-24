from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
# def index(request):
    # return HttpResponse('isitIndependenceDay/index.html')

def isitIndependenceDay(request):
    now = datetime.datetime.now()
    return render(request, 'isitIndependenceDay/index.html', {'isitIndependenceDay': now.month == 8 and now.day == 15})