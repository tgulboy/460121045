from django.contrib import admin
from .models import Menu, Reservation, Gallery, Subscription, Chef, Contact

@admin.register(Menu)
class Menus(admin.ModelAdmin):
  list_display = ['name', 'desc', 'kind', 'price']

@admin.register(Reservation)
class Reservations(admin.ModelAdmin):
  list_display = ['fullname', 'email', 'phone_number', 'people', 'date', 'time', 'message']

@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
  list_display = ['image', 'type']

@admin.register(Subscription)
class Subscriptions(admin.ModelAdmin):
  list_display = ['email']

@admin.register(Chef)
class Chefs(admin.ModelAdmin):
  list_display = ['fullname', 'photo', 'facebook', 'twitter', 'linkedin']

#@admin.register(Blog)
#class Blogs(admin.ModelAdmin):
#  list_display = ['title', 'author', 'banner', 'release_date', 'contact']

@admin.register(Contact)
class Contact(admin.ModelAdmin):
  list_display = ['name', 'email', 'subject', 'message']
