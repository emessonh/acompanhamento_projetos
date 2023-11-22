from django import forms
from django.forms import ModelForm
from .models import Projeto, Setor, Status

class ProjectForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobre = forms.CharField(required=False, label='Descrição', widget=forms.Textarea)
    status_id = forms.ModelChoiceField(queryset=Status.objects.all(), to_field_name='descricao', empty_label=None) # revisar
    situacao_atual = forms.CharField(required=False, label='Situação Atual')
    prioridade = forms.ChoiceField(choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')])
    prazo = forms.DateField(label='Prazo', widget=forms.DateInput(attrs={'type': 'date'})) # revisar
    link = forms.CharField(label='Link', max_length=100)
    proximos_passos = forms.CharField(required=False, label='Próximos passos')
    impedimentos = forms.CharField(required=False, label='Impedimentos')
    sistema_critico = forms.ChoiceField(label='Sistema Crítico', choices=[(True, 'Sim'), (False, 'Não')]) # revisar
    setor_id = forms.ModelChoiceField(queryset=Setor.objects.all(), to_field_name='nome', empty_label=None) # revisar
    pasta_responsavel = forms.ChoiceField(label='Pasta Responsável', choices=[('gabinete', 'Gabinete'), ('SEGP', 'SEGP'), ('SEGI', 'SEGI'), ('SEPOGD', 'SEPOGD')])
    
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ('nome',)

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('descricao', 'cor')