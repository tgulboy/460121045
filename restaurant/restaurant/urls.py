"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import index, signup, login, about_us, blog, contact, gallery, menu, our_team, reservation, logout
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('about-us/', about_us, name='about_us'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('menu/', menu, name='menu'),
    path('our-team/', our_team, name='our_team'),
    path('reservation/', reservation, name='reservation'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  