from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ProjectForm, SetorForm, StatusForm
from .models import Setor, Status, Projeto 

# Projetos

def listagemProjetos(request):
    search = request.GET.get('search')
    if search:
        lista_projetos = Projeto.objects.filter(nome__icontains=search).order_by('nome')
        paginator = Paginator(lista_projetos, 5)
        page = request.GET.get('page')
        projetos = paginator.get_page(page)
        return render(request, 'projetos/home.html', {'projetos': projetos, 'search': search})
    else:
        projects_list = Projeto.objects.all().order_by('data_criacao')

        paginator = Paginator(projects_list, 5)
        page = request.GET.get('page')
        projects = paginator.get_page(page)

        return render(request, 'projetos/home.html', {'projetos':projects})

def addProjeto(request):
    if request.method == 'POST':
        # Recebe o formulário
        form = ProjectForm(request.POST)

        # Verifica se é válido
        if form.is_valid():
            
            # Tratando os dados 
            dados_form = form.cleaned_data
            nome = dados_form['nome']
            sobre = dados_form['sobre']
            status_id = dados_form['status_id']
            situacao_atual = dados_form['situacao_atual']
            prioridade = dados_form['prioridade']
            prazo = dados_form['prazo']
            link = dados_form['link']
            proximos_passos = dados_form['proximos_passos']
            impedimentos = dados_form['impedimentos']
            sistema_critico = dados_form['sistema_critico']
            setor_id = dados_form['setor_id']
            pasta_responsavel = dados_form['pasta_responsavel']

            # Instancia o projeto
            projeto = Projeto(nome=nome, sobre=sobre, status_id=status_id, situacao_atual=situacao_atual, 
                            prioridade=prioridade, prazo=prazo, link=link, proximos_passos=proximos_passos, impedimentos=impedimentos, sistema_critico=sistema_critico, 
                            setor_id=setor_id, pasta_responsavel=pasta_responsavel)

            # Salva  
            projeto.save()
            messages.success(request, 'Tarefa adicionada com sucesso')
            return redirect('/')
        else:
            messages.error(request, 'Error ao adicionar tarefa')
            return redirect('/')
        
    else:
        form = ProjectForm()
        return render(request, 'projetos/addprojeto.html', {'form': form})

def editProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
             # Tratando os dados 
            dados_form = form.cleaned_data
            nome = dados_form['nome']
            sobre = dados_form['sobre']
            status_id = dados_form['status_id']
            situacao_atual = dados_form['situacao_atual']
            prioridade = dados_form['prioridade']
            prazo = dados_form['prazo']
            link = dados_form['link']
            proximos_passos = dados_form['proximos_passos']
            impedimentos = dados_form['impedimentos']
            sistema_critico = dados_form['sistema_critico']
            setor_id = dados_form['setor_id']
            pasta_responsavel = dados_form['pasta_responsavel']

            # modifica o projeto
            projeto.nome = nome
            projeto.sobre = sobre
            projeto.status_id = status_id
            projeto.situacao_atual = situacao_atual
            projeto.prioridade = prioridade
            projeto.prazo = prazo
            projeto.link = link
            projeto.proximos_passos = proximos_passos
            projeto.impedimentos = impedimentos
            projeto.sistema_critico = sistema_critico
            projeto.setor_id = setor_id
            projeto.pasta_responsavel = pasta_responsavel

            # Salva  
            projeto.save()
            messages.success(request, 'Projeto editado com sucesso')
            return redirect('/')
        else:
            messages.error(request, 'Error ao editar projeto')
            return redirect('/')

    else:
        dados_projeto = {'nome': projeto.nome, 'sobre': projeto.sobre, 'status_id': projeto.status_id, 'situacao_atual': projeto.situacao_atual, 'prioridade': projeto.prioridade,
        'prazo': projeto.prazo, 'link': projeto.link, 'proximos_passos': projeto.proximos_passos, 'impedimentos': projeto.impedimentos, 'sistema_critico': projeto.sistema_critico,
        'setor_id': projeto.setor_id, 'pasta_responsavel': projeto.pasta_responsavel}
        form = ProjectForm(initial=dados_projeto)
        return render(request, 'projetos/editprojeto.html', {'form':form})

def delProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    projeto.delete()
    messages.success(request, 'Projeto deletado com sucesso')
    return redirect('/')

# def showProjeto(request, id)
# Setores
    
def listarSetores(request):
    search = request.GET.get('search')
    if search:
        lista_setores = Setor.objects.filter(nome__icontains=search)
        paginator = Paginator(lista_setores, 5)
        page = request.GET.get('page')
        setores = paginator.get_page(page)
        return render(request, 'setor/setores.html', {'setores':setores, 'search':search})
    else:
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
    setor = get_object_or_404(Setor, pk=id)
    setor.delete()
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
