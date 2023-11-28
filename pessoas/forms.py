from django import forms
from projetos.models import Projeto
from .models import Pessoa, Pessoa_Projeto

class PessoaForm(forms.Form):
    nome = forms.CharField(max_length=100)
    area = forms.ChoiceField(choices=[('Comissionado','Comissionado'), ('Conveniado', 'Conveniado'), ('Efetivo', 'Efetivo'), ('Estagiario', 'Estagiário')])

class PessoaProjetoForm(forms.Form):
    projetos = forms.ModelMultipleChoiceField(queryset=Projeto.objects.all(), to_field_name='nome', widget=forms.CheckboxSelectMultiple)

# class PessoaToProjetoForm(forms.Form):
#     projetos = forms.ModelMultipleChoiceField(queryset=Pessoa_Projeto.objects.filter(pessoa=id), to_field_name='nome', widget=forms.CheckboxSelectMultiple)

