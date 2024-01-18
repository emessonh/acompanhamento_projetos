from django.shortcuts import render, redirect
from django.contrib import messages
from pessoas.models import Pessoa
from contas_acesso.models import Contas

# Create your views here.

def login(request):
    return render(request, 'login.html')

def registrar(request):
    return render(request, 'alterar_senha.html')

def criar_login(request, cpf=None):
    # devs = Pessoa.objects.all()
    # print(cpf)
    if request.method == 'POST':
        # print('entrou no if')
        dev = Pessoa.objects.filter(cpf=cpf)
        if dev:
            return redirect('/login/criar-login/')
        else:
            # print('cpf nao cadastrado')
            messages.warning(request, 'CPF não cadastrado!')
            print(cpf)
            return redirect(f'/login/criar-login/')
    else:
        return render(request, 'criar-login.html')