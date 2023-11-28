from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Pessoa, Pessoa_Projeto
from .forms import PessoaForm, PessoaProjetoForm

# Create your views here.

# dev

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

# pessoa_projeto

def addDevToProjeto(request, id):
    dev = get_object_or_404(Pessoa, pk=id)
    if request.method == 'POST':
        form = PessoaProjetoForm(request.POST)
        if form.is_valid() and form.has_changed():
            projetos = form.cleaned_data
            for projeto in projetos['projetos']:
                pessoa_projeto = Pessoa_Projeto(projeto=projeto, pessoa=dev)
                print(projeto)
                print(dev)
                pessoa_projeto.save()
            messages.success(request, 'Dev adicionado a(os) projeto(os)')
            return redirect('/desenvolvedor/')
        elif form.is_valid() == False and form.has_changed() == False:
            return redirect(f'/desenvolvedor/add_dev_projeto/{id}')
        else:
            messages.warning(request, 'Erro ao adicionar dev ao projeto')
            return redirect('/desenvolvedor/')
    else:
        # dev_to_projetos = Pessoa_Projeto.objects.filter(pessoa=f'{id}')
        # all_projetos = Pessoa_Projeto.objects.all()
        # show_projetos = []
        # dados_projeto = {'nome': projeto.nome, 'sobre': projeto.sobre, 'status_id': projeto.status_id, 'situacao_atual': projeto.situacao_atual, 'prioridade': projeto.prioridade,
        # 'prazo': projeto.prazo, 'link': projeto.link, 'proximos_passos': projeto.proximos_passos, 'impedimentos': projeto.impedimentos, 'sistema_critico': projeto.sistema_critico,
        # 'setor_id': projeto.setor_id, 'pasta_responsavel': projeto.pasta_responsavel}
        # form = ProjectForm(initial=dados_projeto)

        form = PessoaProjetoForm()
        return render(request, 'projeto/addevtoproject.html', {'form':form, 'dev':dev})
    
def tirarDev(request, id):
    if request.method == 'POST':
        dev = get_object_or_404(Pessoa, pk=id)
        form = PessoaProjetoForm(request.POST)

        if form.is_valid() and form.has_changed():
            projetos = form.cleaned_data
            ids_projetos_pessoa = get_list_or_404(Pessoa_Projeto, pessoa=dev.id)
            c = 0
            for projeto in projetos['projetos']:
                pessoa_projeto = Pessoa_Projeto(pk=ids_projetos_pessoa[c].id)
                pessoa_projeto.delete()
                messages.success(request, f'{dev.nome} excluído do projeto {projeto.nome}')
                c += 1
            return redirect('/desenvolvedor/')
        
        elif form.is_valid() == False and form.has_changed() == False:
            return redirect(f'/desenvolvedor/tirardev/{id}')
        
        else:
            messages.warning(request, 'Erro ao adicionar dev ao projeto')
            return redirect('/desenvolvedor/')
        
    else:
       
        form = PessoaProjetoForm()
        return render(request, 'projeto/tirardevtoproject.html', {'form':form})