from django.views.generic import CreateView, ListView

from django.shortcuts import render
from staff.models import Staff

class Lista_staff(ListView):
    model= Staff
    template_name: 'staff/lista_personal.html'

class Crear_staff(CreateView):
    model= Staff
    template_name: 'staff/nuevo_personal.html'
    fields = '__all__'
    success_url = '/staff/lista-staff/'
