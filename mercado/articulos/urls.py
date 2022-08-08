from django.urls import path

from articulos.views import nuevo_articulo, buscar_articulo, lista_articulos

urlpatterns = [
    path('nuevo-articulo/', nuevo_articulo, name='nuevo_articulo'),
    path('lista-articulos/', lista_articulos, name='lista_articulos'),
    path('buscar-articulo/', buscar_articulo, name='buscar_articulo'),
]