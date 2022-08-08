from django.urls import path

from sucursales.views import Crear_store, Lista_store

urlpatterns = [
    path('nueva-sucursal/', Crear_store.as_view(), name='nueva_sucursal'),
    path('lista-sucursales/', Lista_store.as_view(), name='lista_sucursales'),
]