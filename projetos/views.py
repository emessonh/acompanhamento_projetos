from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ProjectForm, SetorForm
# from .forms import StatusForm
from .models import Setor, Status, Projeto 

# Projetos

def listagemProjetos(request):
    search = request.GET.get('search')
    if search:
        lista_projetos = Projeto.objects.filter(nome__icontains=search).order_by('nome')
        paginator = Paginator(lista_projetos, 10)
        page = request.GET.get('page')
        projetos = paginator.get_page(page)
        return render(request, 'projetos/home.html', {'projetos': projetos, 'search': search})
    else:
        projects_list = Projeto.objects.all().order_by('data_criacao')

        paginator = Paginator(projects_list, 10)
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

            # Verifica se há um projeto com o mesmo nome e setor
            projetos_existentes = Projeto.objects.all()
            for p in projetos_existentes:
                # print(p.nome.upper(), nome.upper(), p.setor_id_id, setor_id.id)
                if (p.nome.upper() == nome.upper()) and (p.setor_id_id == setor_id.id):
                    messages.warning(request, 'Atenção! Projeto já cadastrado com mesmo nome e setor')
                    return redirect('/')

            # Instancia o projeto
            projeto = Projeto(nome=nome, sobre=sobre, status_id=status_id, situacao_atual=situacao_atual, 
                            prioridade=prioridade, prazo=prazo, link=link, proximos_passos=proximos_passos, impedimentos=impedimentos, sistema_critico=sistema_critico, 
                            setor_id=setor_id, pasta_responsavel=pasta_responsavel)

            # Salva  
            projeto.save()
            messages.success(request, 'Projeto adicionado com sucesso')
            return redirect('/')
        else:
            messages.warning(request, 'Erro ao adicionar projeto')
            return redirect('/')
        
    else:
        form = ProjectForm()
        return render(request, 'projetos/addprojeto.html', {'form': form})

def editProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    projetos = get_list_or_404(Projeto)
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
            
            # Verifica se a edição é possível
            for p in projetos:
                print(p.nome, projeto.nome)
                print(p.setor_id_id, projeto.setor_id.id)
                if p.nome.upper() == projeto.nome.upper() and p.setor_id_id == projeto.setor_id.id:
                    messages.warning(request, 'Atenção! Projeto já existe')
                    return redirect('/')

            # Salva  
            projeto.save()
            messages.success(request, 'Projeto editado com sucesso')
            return redirect('/')
        else:
            messages.warning(request, 'Erro ao editar projeto')
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
        paginator = Paginator(lista_setores, 10)
        page = request.GET.get('page')
        setores = paginator.get_page(page)
        return render(request, 'setor/setores.html', {'setores':setores, 'search':search})
    else:
        lista_setores = Setor.objects.all().order_by('nome')

        paginator = Paginator(lista_setores, 10)
        page = request.GET.get('page')
        setores = paginator.get_page(page)
    
        return render(request, 'setor/setores.html', {'setores':setores})

def addSetor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():

            # Verifica se o setor já existe
            setores = Setor.objects.all()
            print(setores)
            dados = form.cleaned_data
            for setor in setores:
                if setor.nome.upper() == dados['nome'].upper():
                    messages.warning(request, 'Atenção! Setor já cadastrado')
                    return redirect('/setores/')
                
            task = form.save()
            messages.success(request, 'Setor adicionado com sucesso')
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
        setores = get_list_or_404(Setor)
        form_enviado = SetorForm(request.POST, instance=setor)
        print(form_enviado)
        sigla_setor = form_enviado.cleaned_data['nome']
        # print(dados)
        # sigla_setor = dados['nome']
        # print(sigla_setor)
        if form_enviado.is_valid():
            # Verifica se o setor já existe
            for s in setores:
                if sigla_setor.upper() == s.nome.upper():
                    print(sigla_setor, s.nome)
                    messages.warning(request, 'Atenção! Setor já cadastrado')
                    return redirect('/setores/')
                
            # Salva
            setor.save()
            messages.success(request, 'Setor editado com sucesso')
            return redirect('/setores/')
        else:
            messages.warning(request, 'Erro ao editar o setor! Tente novamente!')
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
        descricao_status = request.POST.get('descricao')
        cor_status = request.POST.get('cor')
        # print(descricao_status, cor_status)

        # Verifica se o status já existe
        status = Status.objects.all()
        for s in status:
            if s.descricao.upper() == descricao_status.upper():
                messages.warning(request, "Atenção! Status já cadastrado")
                return redirect('/status/')

        status = Status(descricao=descricao_status, cor=cor_status)
        status = status.save()
        messages.success(request, 'Status adicionado com sucesso')
        return redirect('/status/')
            
    else:
        # form = StatusForm()
        return render(request, 'status/addstatus.html')
    
def delStatus(request, id):
    status = get_object_or_404(Status, pk=id)
    status.delete()
    messages.success(request, 'Status excluído com sucesso')
    return redirect('/status/')

def editStatus(request, id):
    status = get_object_or_404(Status, pk=id)
    
    # form = StatusForm(instance=status)
    if request.method == 'POST':
        status_banco = get_list_or_404(Status)
        
        # form = StatusForm(request.POST, instance=status)
        # if form.is_valid():
        nova_descricao = request.POST.get('descricao')
        nova_cor = request.POST.get('cor')
        
        # verifica se o status já existe 
        for s in status_banco:
            # print(s.descricao, nova_descricao)
            if s.descricao.upper() == nova_descricao.upper():
                messages.warning(request, 'Atenção! Status já cadastrado')
                return redirect('/status/')

        # Salva
        status.descricao = nova_descricao
        status.cor = nova_cor
        status.save()
        messages.success(request, 'Status editado com sucesso')
        return redirect('/status/')
        # else:
        #     messages.error(request, 'Erro ao editar o status! Tente novamente!')
        #     return redirect('/status/')
    else:
        descricao_status = status.descricao
        cor_status = status.cor
        return render(request, 'status/editstatus.html', {'descricao': descricao_status, 'cor': cor_status})
