"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
import app_01.urls
from MyBlog.views import *


app_name='MyBlog'
urlpatterns = [
    path('blog/',include(app_01.urls,)),
    path('login/user/',login_view),
    path('register/user/',register_view),
    path('login/',login_page,name='login_page'),
    path('register/',register_page,name='register_page'),
    path('about/',get_about,name='about'),
    path('contact/',get_contact,name='contact'),
    path('admin/', admin.site.urls),
]
