from django.shortcuts import render

# Create your views here.
def car_add(request):
    return render(request, 'app_cars/add.html')

def car_list(request):
    return render(request, 'app_cars/list.html')

def car_delete(request):
    return render(request, 'app_cars/delete.html')