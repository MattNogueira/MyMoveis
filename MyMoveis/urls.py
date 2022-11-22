"""MyMoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from MyMoveis.views import auth, pages

urlpatterns = [
    path('', pages.home, name='home'),
    path('home', pages.home, name='home'),
    path('redsenha', pages.redSenha, name="redSenha"),
    
    #urls of auth
    path('login', auth.login, name='login'),
    path('logout', auth.logout, name='logout'),
    path('cadastro', auth.cadastro, name='cadastro'),
    path('anunciante', auth.anunciante, name='anunciante')
]