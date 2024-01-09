from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Pessoa, Pessoa_Projeto
from .forms import PessoaForm, PessoaProjetoForm
from projetos.models import Projeto

# Create your views here.

# dev

def listagemDesenvolvedor(request):
    lista_desenvolvedores = Pessoa.objects.all().order_by('nome')

    paginator = Paginator(lista_desenvolvedores, 10)
    page = request.GET.get('page')
    desenvolvedores = paginator.get_page(page)

    return render(request, 'pessoa/desenvolvedores.html', {'desenvolvedores': desenvolvedores})

def addDesenvolvedor(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        caracteres_cpf = ['.', '-']
        cpf = request.POST.get('cpf').replace('.', '', 3)
        cpf = cpf.replace('-', '')
        # print(cpf)
        dev_existe = Pessoa.objects.filter(cpf=cpf)
        # print(form)
        if form.is_valid() and not dev_existe:
            # cpf = form.cleaned_data['cpf']
            nome = form.cleaned_data['nome']
            area = form.cleaned_data['area']
            pessoa = Pessoa(cpf=cpf, nome=nome, area=area)
            pessoa.save()
            messages.success(request, 'Desenvolvedor adicionado com sucesso')
            return redirect('/desenvolvedor/')
        elif dev_existe:
            messages.warning(request, 'Atenção! Desenvolvedor já cadastrado')
            return redirect('/desenvolvedor/')
        else:
            messages.warning(request, 'Erro ao adicionar desenvolvedor')
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
            messages.warning(request, 'Erro ao editar desenvolvedor')
            return redirect('/desenvolvedor/')
    else:
        form = PessoaForm(initial={'nome':dev.nome, 'area': dev.area})
        return render(request, 'pessoa/editdev.html', {'form': form})

# pessoa_projeto

def addDevToProjeto(request, id):
    dev = get_object_or_404(Pessoa, pk=id)
    if request.method == 'POST':
        projetos_sel = request.POST.getlist('projeto')
        # print(type(projetos_sel[0]))
        if len(projetos_sel) == 0:
            return redirect(f'/desenvolvedor/tirardev/{id}')
        else:
            for projeto in projetos_sel:
                projeto = get_object_or_404(Projeto, pk=projeto)
                objeto_p_p = Pessoa_Projeto(pessoa=dev, projeto=projeto)
                objeto_p_p.save()
                messages.success(request, f'{dev.nome} adicionado ao projeto: {projeto.nome}')        
            return redirect('/desenvolvedor/')
        
    else:
        projetos = Projeto.objects.all() 
        pessoa_is_projeto = Pessoa_Projeto.objects.filter(pessoa_id=id)
        id_projetos = []
        for projeto in pessoa_is_projeto:
            id_projetos.append(projeto.projeto_id)

        pessoa_is_not_projeto = []
        for projeto in projetos:
            if projeto.id not in id_projetos:
                pessoa_is_not_projeto.append(projeto)
        
        projetos = []
        for pessoa_projeto in pessoa_is_not_projeto:
            projeto = get_object_or_404(Projeto, pk=pessoa_projeto.id)
            projetos.append(projeto)
        return render(request, 'projeto/addevtoproject.html', {'projetos': pessoa_is_not_projeto, 'qtd_projetos':len(projetos), 'nome_projetos': projetos})
    
def tirarDev(request, id):
    if request.method == 'POST':
        projetos_sel = request.POST.getlist('projeto')
        print(projetos_sel)
        if len(projetos_sel) == 0:
            return redirect(f'/desenvolvedor/tirardev/{id}')
        else:
            for pessoa_projeto in projetos_sel:
                pessoa_projeto = int(pessoa_projeto)
                objeto_p_p = get_object_or_404(Pessoa_Projeto, pk=pessoa_projeto)
                dev = get_object_or_404(Pessoa, pk=objeto_p_p.pessoa_id)
                projeto = get_object_or_404(Projeto, pk=objeto_p_p.projeto_id)
                objeto_p_p.delete()
                messages.success(request, f'{dev.nome} excluído do projeto: {projeto.nome}')        
            return redirect('/desenvolvedor/')
       
    else:
        pessoa_projetos = Pessoa_Projeto.objects.filter(pessoa=id) # id, pessoa_id, projeto_id
        projetos = []
        for pessoa_projeto in pessoa_projetos:
            projeto = get_object_or_404(Projeto, pk=pessoa_projeto.projeto_id)
            projetos.append(projeto)
        return render(request, 'projeto/tirardevtoproject.html', {'projetos': pessoa_projetos, 'qtd_projetos':len(projetos), 'nome_projetos': projetos})
    
    