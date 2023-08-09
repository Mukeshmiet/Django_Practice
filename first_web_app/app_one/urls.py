from django.urls import path
from app_one import views

#app_one/
urlpatterns = [
    path('<str:topic>/', views.app_one_view, name='topic_page'),
    path('<int:num_page>', views.page_number_view),
]