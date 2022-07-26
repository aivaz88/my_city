from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='title'),
    path('all_citizen/', views.all_citizen, name='citizens_my_city'),
    path('citizen<int:id_citizen>/', views.get_info_citizen_city, name='citizen_info'),
    path('сontacts/', views.my_contacts, name='my-contacts')
]
