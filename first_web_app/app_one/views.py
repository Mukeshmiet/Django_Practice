from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.urls import reverse
# Create your views here.

def simple_view(request):
    dict_name = {"name": "User_name"}
    return render(request, 'app_one/index.htm', context=dict_name)
