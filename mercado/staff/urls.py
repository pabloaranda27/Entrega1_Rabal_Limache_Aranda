from django.urls import path

from staff.views import Crear_staff, Lista_staff

urlpatterns = [
    path('nuevo-personal/', Crear_staff.as_view(), name='nuevo_personal'),
    path('lista-personal/', Lista_staff.as_view(), name='lista_personal'),
]