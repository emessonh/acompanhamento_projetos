from django.db import models
from pessoas.models import Pessoa

# Create your models here.

class Contas(models.Model):
    cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE, primary_key=True, to_field='cpf')
    senha = models.CharField(null=True, max_length=50)