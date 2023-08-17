from django.urls import path
from app_one import views

urlpatterns = [
    path('', views.simple_view),
]
