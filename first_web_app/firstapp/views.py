from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def first_app(request):
    return HttpResponse('<h1> My First Django App ... >|<  </h1>')

def dis_date(request):
    date=f'Current Date is {datetime.datetime.now()}'
    return HttpResponse(f'<h1>{date}</h1>')