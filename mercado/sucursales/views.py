from django.views.generic import CreateView, ListView

from django.shortcuts import render
from sucursales.models import Store

class Lista_store(ListView):
    model= Store
    template_name= 'sucursales/lista_sucursales.html'

class Crear_store(CreateView):
    model= Store
    template_name= 'sucursales/nueva_sucursal.html'
    fields = '__all__'
    success_url = '/sucursales/lista-sucursales/'