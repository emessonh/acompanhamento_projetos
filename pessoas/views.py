from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Pessoa

# Create your views here.

def listagemUsuarios(request):
    lista_usuarios = Pessoa.objects.all().order_by('nome')

    paginator = Paginator(lista_usuarios, 5)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)

    return render(request, 'pessoa/desenvolvedores.html', {'usuarios': usuarios})


