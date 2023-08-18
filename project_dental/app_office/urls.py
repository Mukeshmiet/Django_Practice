from django.urls import path
from . import views

# domain.com/office/
urlpatterns = [
    path('', views.patients, name='patients'),
]
