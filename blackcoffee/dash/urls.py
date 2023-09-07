from django.urls import path
from .views import get_dashboard_data, index

urlpatterns = [
    path('api/dashboard_data/', get_dashboard_data, name='get_dashboard_data'),
    path('', index, name='index'),
]