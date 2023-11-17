from django.shortcuts import render
from .models import Projeto 
from django.core.paginator import Paginator

# Create your views here.

def listagemProjetos(request):
    projects_list = Projeto.objects.all().order_by('data_criacao')

    paginator = Paginator(projects_list, 5)
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    return render(request, 'projetos/home.html', {'projetos':projects})
