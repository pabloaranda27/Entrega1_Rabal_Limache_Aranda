from django.contrib import admin
from django.urls import path, include

from mercado.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('articulos/', include('articulos.urls')),
    path('staff/', include('staff.urls')),
]
