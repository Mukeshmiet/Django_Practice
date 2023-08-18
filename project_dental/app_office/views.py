from django.shortcuts import render
from . models import Patient


# Create your views here.
def patients(request):
    all_patients = Patient.objects.all()
    context = {'all_patients': all_patients}   # list into dict object
    return render(request, 'app_office/patients.html', context = context)