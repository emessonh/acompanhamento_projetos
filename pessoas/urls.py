"""
URL configuration for to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    # Pessoas
    path('desenvolvedor/', views.listagemDesenvolvedor),
    path('desenvolvedor/addesenvolvedor/', views.addDesenvolvedor),
    path('desenvolvedor/deldev/<int:id>', views.delDev),
    path('desenvolvedor/editdev/<int:id>', views.editDev),
    # Pessoa_Projeto
    path('desenvolvedor/add_dev_projeto/<int:id>', views.addDevToProjeto),
    path('desenvolvedor/tirardev/<int:id>', views.tirarDev),
    
]
