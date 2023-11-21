from django import forms
from .models import Projeto, Setor, Status

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('nome', 'sobre', 'status_id', 'situacao_atual', 'prioridade', 'prazo', 'link', 'proximos_passos', 
                  'impedimentos', 'sistema_critico', 'setor_id', 'pasta_responsavel')
        
class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ('nome',)

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('descricao', 'cor')