from django.shortcuts import render, redirect
from django.urls import reverse
from . import models


# Create views for models
# Create your views here.
def car_list(request):
    all_cars = models.Cars.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'app_cars/list.html', context = context)

def car_add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Cars.objects.create(brand=brand, year=year)
        return redirect(reverse('app_cars:car_list'))
    else:
        return render(request, 'app_cars/add.html')

def car_delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Cars.objects.get(pk=pk).delete()
            return redirect(reverse('app_cars:car_list'))
        except:
            print('primary key not found')
            return redirect(reverse('app_cars:car_list'))
    else:
        return render(request, 'app_cars/delete.html')