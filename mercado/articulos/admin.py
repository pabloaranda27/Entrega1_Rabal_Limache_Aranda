from django.contrib import admin
from articulos.models import Articles

@admin.register(Articles)
class Articles_admin(admin.ModelAdmin):
    list_display=['name','price','stock']
