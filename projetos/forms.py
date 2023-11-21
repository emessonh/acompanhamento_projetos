from django import forms
from .models import Projeto, Setor, Status

def lista_status():
    todos_status = Status.objects.all().order_by('id')
    lista = []
    
    for status in todos_status:
        lista.append((f'{status.id}', f'{status.descricao}'))
    return lista

def lista_setores():
    setores = Setor.objects.all().order_by('nome')
    lista = []

    for setor in setores:
        lista.append((f'{setor.id}', f'{setor.nome}'))
    return lista

class ProjectForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobre = forms.CharField(label='Descrição', required=False, widget=forms.Textarea)
    status_id = forms.ChoiceField(choices=lista_status(), label='Status ID') # revisar
    situacao_atual = forms.CharField(label='Situação Atual')
    prioridade = forms.ChoiceField(choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')])
    prazo = forms.DateField(label='Prazo') # revisar
    link = forms.CharField(label='Link', max_length=100)
    proximos_passos = forms.CharField(label='Próximos passos')
    impedimentos = forms.CharField(label='Impedimentos')
    sistema_critico = forms.BooleanField(label='Sistema Crítico') # revisar
    setor_id = forms.ChoiceField(label='Setor ID', choices=lista_setores()) # revisar
    pasta_responsavel = forms.ChoiceField(label='Pasta Responsável', choices=[('1', 'Gabinete'), ('2', 'SEGP'), ('3', 'SEGI'), ('4', 'SEPOGD')])

    
    # class Meta:
    #     model = Projeto
    #     fields = ('nome', 'sobre', 'status_id', 'situacao_atual', 'prioridade', 'prazo', 'link', 'proximos_passos', 
    #               'impedimentos', 'sistema_critico', 'setor_id', 'pasta_responsavel')
        
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ('nome',)

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('descricao', 'cor')