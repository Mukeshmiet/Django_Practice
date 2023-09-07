import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Dashboard

# Create your views here.
def get_dashboard_data(request):
    # records = Dashboard.objects.all()   
    records = Dashboard.objects.filter(intensity__isnull=False).values('intensity').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def index(request):
    return render(request, 'index.html')

