from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto 
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ProjectForm, SetorForm, StatusForm
from .models import Setor, Status

# Projetos

def listagemProjetos(request):
    projects_list = Projeto.objects.all().order_by('data_criacao')

    paginator = Paginator(projects_list, 5)
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    return render(request, 'projetos/home.html', {'projetos':projects})

def addProjeto(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            projeto = form.save()
            messages.success(request, 'Tarefa adicionada com sucesso')
            return redirect('/')
        else:
            messages.error(request, 'Error ao adicionar tarefa')
            return redirect('/')
        
    else:
        form = ProjectForm()
        return render(request, 'projetos/addprojeto.html', {'form': form})
    
# Setores
    
def listarSetores(request):
    lista_setores = Setor.objects.all().order_by('nome')

    paginator = Paginator(lista_setores, 5)
    page = request.GET.get('page')
    setores = paginator.get_page(page)

    return render(request, 'setor/setores.html', {'setores':setores})

def addSetor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)

        if form.is_valid():
            task = form.save()
            messages.success(request, 'Tarefa adicionada com sucesso')
            return redirect('/setores/')
        
    else:
        form = SetorForm()
        return render(request, 'setor/addsetor.html', {'form': form})
    
def delSetor(request, id):
    task = get_object_or_404(Setor, pk=id)
    task.delete()
    messages.success(request, 'Setor excluído com sucesso')
    return redirect('/setores/')

def editSetor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(instance=setor)
    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            setor.save()
            messages.success(request, 'Setor editado com sucesso')
            return redirect('/setores/')
        else:
            messages.error(request, 'Erro ao editar o setor! Tente novamente!')
            return redirect('/setores/')
    else:
        return render(request, 'setor/editsetor.html', {'form': form})
    
# Status

def listaStatus(request):
    lista_status= Status.objects.all().order_by('descricao')

    paginator = Paginator(lista_status, 5)
    page = request.GET.get('page')
    lista_status = paginator.get_page(page)

    return render(request, 'status/status.html', {'lista_status':lista_status})

def addStatus(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)

        if form.is_valid():
            status = form.save()
            messages.success(request, 'Status adicionado com sucesso')
            return redirect('/status/')
        
    else:
        form = StatusForm()
        return render(request, 'status/addstatus.html', {'form': form})
    
def delStatus(request, id):
    status = get_object_or_404(Status, pk=id)
    status.delete()
    messages.success(request, 'Status excluído com sucesso')
    return redirect('/status/')

def editStatus(request, id):
    status = get_object_or_404(Status, pk=id)
    form = StatusForm(instance=status)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            status.save()
            messages.success(request, 'Status editado com sucesso')
            return redirect('/status/')
        else:
            messages.error(request, 'Erro ao editar o status! Tente novamente!')
            return redirect('/status/')
    else:
        return render(request, 'status/editstatus.html', {'form': form})
