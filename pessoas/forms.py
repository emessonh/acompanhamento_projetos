from django import forms

class PessoaForm(forms.Form):
    nome = forms.CharField(max_length=100)
    area = forms.ChoiceField(choices=[('Comissionado','Comissionado'), ('Conveniado', 'Conveniado'), ('Efetivo', 'Efetivo'), ('Estagiario', 'Estagiário')])