from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def registrar(request):
    return render(request, 'alterar_senha.html')

def criar_login(request):
    return render(request, 'criar-login.html')