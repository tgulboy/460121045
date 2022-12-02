from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Menu

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def about_us(request):
  template = loader.get_template('about-us.html')
  return HttpResponse(template.render())

def blog(request):
  template = loader.get_template('blog.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render())

def menu(request):
  menu = Menu.objects.all().values()
  context = {
    'menus': menu,
  }
  template = loader.get_template('menu.html')
  return HttpResponse(template.render(context, request))

def our_team(request):
  template = loader.get_template('our-team.html')
  return HttpResponse(template.render())

def reservation(request):
  template = loader.get_template('reservation.html')
  return HttpResponse(template.render())