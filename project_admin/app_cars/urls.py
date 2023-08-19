from django.urls import path
from . import views

app_name = 'app_cars'

urlpatterns = [
    path('list/', views.car_list, name='car_list'),
    path('add/', views.car_add, name='car_add'),
    path('delete/', views.car_delete, name='car_delete'),
]
