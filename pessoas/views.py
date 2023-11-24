from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

def listagemDesenvolvedor(request):
    lista_desenvolvedores = Pessoa.objects.all().order_by('nome')

    paginator = Paginator(lista_desenvolvedores, 5)
    page = request.GET.get('page')
    desenvolvedores = paginator.get_page(page)

    return render(request, 'pessoa/desenvolvedores.html', {'desenvolvedores': desenvolvedores})

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

def delDev(request, id):
    dev = get_object_or_404(Pessoa, pk=id) 
    dev.delete()
    messages.success(request, 'Desenvolvedor excluído com sucesso')
    return redirect('/desenvolvedor/')

def editDev(request, id):
    dev = get_object_or_404(Pessoa, pk=id) 
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            dev.nome = form.cleaned_data['nome']
            dev.area = form.cleaned_data['area']
            dev.save()
            messages.success(request, 'Edição realizada com sucesso')
            return redirect('/desenvolvedor/')
        else: 
            messages.error(request, 'Erro ao editar desenvolvedor')
            return redirect('/desenvolvedor/')
    else:
        form = PessoaForm(initial={'nome':dev.nome, 'area': dev.area})
        return render(request, 'pessoa/editdev.html', {'form': form})