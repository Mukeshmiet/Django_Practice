import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Dashboard
from django.db.models.functions import ExtractYear
from .forms import FilterForm


def formFilters(request):
    form = FilterForm(request.POST)
    if form.is_valid():
        end_year=form.cleaned_data['end_year']
        country = form.cleaned_data['country']
        topic = form.cleaned_data['topic']
        region = form.cleaned_data['region']
        pestle = form.cleaned_data['pestle']
        sector = form.cleaned_data['sector']
        source = form.cleaned_data['source']

        filter_kwargs = {}
        if end_year:
            filter_kwargs['end_year'] = end_year
        if country:
            filter_kwargs['country'] = country
        if topic:
            filter_kwargs['topic'] = topic
        if region:
            filter_kwargs['region'] = region
        if pestle:
            filter_kwargs['pestle'] = pestle
        if sector:
            filter_kwargs['sector'] = sector
        if source:
            filter_kwargs['source'] = source
        
    return filter_kwargs

# Create your views here.
def intensity(request):
    if request.method == 'GET':
        filter_kwargs = formFilters(request)
        records = Dashboard.objects.filter(intensity__isnull=False, **filter_kwargs).values('intensity').distinct()
    else:
        records = Dashboard.objects.filter(intensity__isnull=False).values('intensity').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def likelihood(request):
    if request.method == 'GET':
        filter_kwargs = formFilters(request)
        records = Dashboard.objects.filter(likelihood__isnull=False, **filter_kwargs).values('likelihood').distinct()
    else:
        records = Dashboard.objects.filter(likelihood__isnull=False).values('likelihood').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def relevance(request):
    if request.method == 'GET':
        filter_kwargs = formFilters(request)
        records = Dashboard.objects.filter(relevance__isnull=False, **filter_kwargs).values('relevance').distinct()
    else:
        records = Dashboard.objects.filter(relevance__isnull=False).values('relevance').distinct()
    records_json = json.dumps(list(records))
    return JsonResponse(records_json, safe=False)

def year(request):
    if request.method == 'GET':
        filter_kwargs = formFilters(request)
        distinct_years = Dashboard.objects.filter(published__isnull=False, **filter_kwargs).annotate(year=ExtractYear('published')).values('year').distinct()
        print(distinct_years)
    else:
        distinct_years = Dashboard.objects.filter(published__isnull=False).annotate(year=ExtractYear('published')).values('year').distinct()
    years = [entry['year'] for entry in distinct_years]
    records_json = json.dumps(list(years))
    return JsonResponse(records_json, safe=False)

def index(request):
    form = FilterForm(request.GET)
    context = {'form': form}
    return render(request, 'index.html', context)
