from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

def listagemDesenvolvedor(request):
    lista_usuarios = Pessoa.objects.all().order_by('nome')

    paginator = Paginator(lista_usuarios, 5)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)

    return render(request, 'pessoa/desenvolvedores.html', {'usuarios': usuarios})

def addDesenvolvedor(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            area = form.cleaned_data['area']
            pessoa = Pessoa(nome=nome, area=area)
            pessoa.save()
            messages.success(request, 'Desenvolvedor adicionado com sucesso')
            return redirect('/desenvolvedor/')
        else:
            messages.error(request, 'Erro ao adicionar desenvolvedor')
            return redirect('/desenvolvedor/')

    else:
        form = PessoaForm()
        return render(request, 'pessoa/adddesenvolvedor.html', {'form':form})

