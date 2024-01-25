from django.shortcuts import render, redirect
from django.contrib import messages
from pessoas.models import Pessoa
from contas_acesso.models import Contas

# Create your views here.

def login(request, msg_sucesso=None):
    if request.method == 'POST':
        cpf = request.POST.get('cpf').replace('.', '', 3)
        cpf = cpf.replace('-', '')
        senha_input = request.POST.get('password')
        dev = Contas.objects.filter(cpf=cpf)
        if dev:
            dev = dev.get()
            if dev.cpf == cpf and dev.senha == senha_input:
                return redirect('/')
            else:
                return render(request, 'login.html', {'msg_login': 'CPF e ou Senha incorretos', 'cpf':cpf})
        else:
            return render(request, 'login.html', {'msg_login': 'Usuário não cadastrado', 'cpf': cpf})
    else:
        return render(request, 'login.html', {'msg_sucesso': msg_sucesso})

def alterar_senha(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf').replace('.', '', 3)
        cpf = cpf.replace('-', '')
        nova_senha = request.POST.get('nova-senha')
        confirmacao_senha = request.POST.get('confirmacao-senha')
        dev = Contas.objects.filter(cpf=cpf)
        if dev:
            dev = dev.get()
            if nova_senha == dev.senha:
                return render(request, 'alterar_senha.html', {'msg': 'Digite uma senha diferente da anterior', 'cpf': cpf})
            else:
                if nova_senha != confirmacao_senha:
                    return render(request, 'alterar_senha.html', {'msg': 'Atenção! Senhas diferentes, tente novamante', 'cpf': cpf})
                else:
                    dev.senha = confirmacao_senha
                    dev.save()
                    return redirect('login', msg_sucesso='Senha alterada com sucesso')       
        else:
            return render(request, 'alterar_senha.html', {'msg': 'Usuário não cadastrado', 'cpf': cpf})
    else:
        return render(request, 'alterar_senha.html')

def criar_login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf').replace('.', '', 3)
        cpf = cpf.replace('-', '')
        senha_input = request.POST.get('password')
        confirmacao_senha = request.POST.get('confirm-password')
        dev = Pessoa.objects.filter(cpf=cpf)
        conta_dev = Contas.objects.filter(cpf=cpf)
        if not dev:
            return render(request, 'criar-login.html', {'msg':'CPF não cadastrado', 'cpf':cpf})
        elif cpf == dev.get().cpf and not conta_dev:
            if senha_input == confirmacao_senha:
                conta_dev = Contas(cpf=cpf, senha=senha_input)
                conta_dev.save()
                return redirect('login', msg_sucesso='Login criado com sucesso')
            else:
                return render(request, 'criar-login.html', {'msg_senha':'Senhas diferentes', 'cpf':cpf})
        else:
            return render(request, 'criar-login.html', {'msg': 'CPF já cadastrado', 'cpf': cpf})
    else:
        return render(request, 'criar-login.html')
    