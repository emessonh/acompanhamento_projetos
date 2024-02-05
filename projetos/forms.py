from django import forms
from django.forms import ModelForm
from .models import Projeto, Setor, Status
import datetime


valores_situacao_atual = [('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')]
valores_sistema_critico = [(True, 'Sim'), (False, 'Não')]
valores_pastas_responsaveis = [('gabinete', 'Gabinete'), ('SEGP', 'SEGP'), ('SEGI', 'SEGI'), ('SEPOGD', 'SEPOGD')]
ano_atual = datetime.date.today()

class ProjectForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobre = forms.CharField(label='Descrição', widget=forms.Textarea)
    status_id = forms.ModelChoiceField(label='Status', queryset=Status.objects.all(), to_field_name='descricao', empty_label=None) # revisar
    situacao_atual = forms.CharField(required=False, label='Situação Atual')
    prioridade = forms.ChoiceField(choices=valores_situacao_atual)
    prazo = forms.DateField(required=False, label='Prazo', widget=forms.DateInput(attrs={'type': 'date'})) # revisar
    ano_desenvolvimento = forms.CharField(required=True, max_length=4, label='Ano Desenvolvimento', initial=ano_atual.year)
    link = forms.CharField(required=False, label='Link', max_length=100)
    proximos_passos = forms.CharField(required=False, label='Próximos passos')
    impedimentos = forms.CharField(required=False, label='Impedimentos')
    sistema_critico = forms.ChoiceField(label='Sistema Crítico', choices=valores_sistema_critico, initial=valores_sistema_critico[1]) # revisar
    setor_id = forms.ModelChoiceField(label='Setor', queryset=Setor.objects.all(), to_field_name='nome', empty_label=None) # revisar
    pasta_responsavel = forms.ChoiceField(label='Pasta Responsável', choices=valores_pastas_responsaveis, initial=valores_pastas_responsaveis[2])
    
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ('nome',)

# class StatusForm(forms.Form):
#     descricao = forms.CharField(label='descricao', max_length=100)
#     cor = forms.CharField(label='cor', max_length=10)

# class StatusForm(forms.ModelForm):
#     class Meta:
#         model = Status
#         fields = ('descricao', 'cor')