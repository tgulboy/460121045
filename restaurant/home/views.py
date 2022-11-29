from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Menu

def index(request):
  mymenu = Menu.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'menus': mymenu,
  }
  return HttpResponse(template.render(context, request))