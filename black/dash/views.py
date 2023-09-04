from django.shortcuts import render
from .models import Dashboard

# Create your views here.
def index(request):
    records = Dashboard.objects.all()[:5]
    context = {
        'records': records
    }
    return render(request, 'index.html', context=context)