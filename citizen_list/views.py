from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .models import Citizen

# Create your views here.

def menu(request):
    return render(request, 'citizen_list/title.html')

def my_contacts(request):
    return render(request, 'citizen_list/contacts.html')

def all_citizen(request):
    citizen_list = Citizen.objects.all()
    return render(request, 'citizen_list/all_citizen.html', {'citizen_list': citizen_list})

def get_info_citizen_city(request, id_citizen: int):
    citizen = get_object_or_404(Citizen, id=id_citizen)
    citizen_list = Citizen.objects.all()
    boss = citizen.boss
    boss_name = citizen_list.get(id=boss)
    return render(request, 'citizen_list/citizen_info.html', {'citizen': citizen, 'boss_name': boss_name})
