from django.urls import path
from .views import index, intensity, likelihood,relevance, year

urlpatterns = [
    path('api/intensity/', intensity, name='intensity'),
    path('api/likelihood/', likelihood, name='likelihood'),
    path('api/relevance/', relevance, name='relevance'),
    path('api/year/', year, name='year'),
    path('', index, name='index'),
]