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
    # Projetos
    path('', views.listagemProjetos),
    path('addprojeto/', views.addProjeto),
    path('editprojeto/<int:id>', views.editProjeto),
    path('delprojeto/<int:id>', views.delProjeto),
    # Setores
    path('setores/', views.listarSetores),
    path('setores/addsetor/', views.addSetor),
    path('setores/delsetor/<int:id>', views.delSetor),
    path('setores/editsetor/<int:id>', views.editSetor),
    # Status
    path('status/', views.listaStatus),
    path('status/addstatus/', views.addStatus),
    path('status/delstatus/<int:id>', views.delStatus),
    path('status/editstatus/<int:id>', views.editStatus),
]
