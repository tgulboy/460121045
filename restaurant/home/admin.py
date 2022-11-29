from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class Menus(admin.ModelAdmin):
  list_display = ['name', 'desc', 'kind', 'price']
