import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Dashboard
from .forms import FilterForm

# Create your views here.
def intensity(request):
    # records = Dashboard.objects.all()   
    records = Dashboard.objects.filter(intensity__isnull=False).values('intensity').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def likelihood(request):
    # records = Dashboard.objects.all()   
    records = Dashboard.objects.filter(likelihood__isnull=False).values('likelihood').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def relevance(request):
    # records = Dashboard.objects.all()   
    records = Dashboard.objects.filter(relevance__isnull=False).values('relevance').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def year(request):
    # records = Dashboard.objects.all()   
    records = Dashboard.objects.values('start_year', 'end_year')
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def index(request):
    form = FilterForm(request.GET)
    queryset = Dashboard.objects.all()
    
    if form.is_valid():
        
        end_year = form.cleaned_data['end_year']
        country = form.cleaned_data['country']
        topic = form.cleaned_data['topic']
        region = form.cleaned_data['region']
        pestle = form.cleaned_data['pestle']
        sector = form.cleaned_data['sector']
        source = form.cleaned_data['source']
        
    if end_year:
        queryset = queryset.filter(end_year=end_year)
    if country:
        queryset = queryset.filter(country=country)
    if topic:
        queryset = queryset.filter(topic=topic)
    if region:
        queryset = queryset.filter(region=region)
    if pestle:
        queryset = queryset.filter(pestle=pestle)
    if sector:
        queryset = queryset.filter(sector=sector)
    if source:
        queryset = queryset.filter(source=source)
    
    intensity = queryset.filter(intensity__isnull=False).values('intensity').distinct()
    context = {
        'form': form,
        'queryset': queryset,
    }
    print(context)
    return render(request, 'index.html', context)


