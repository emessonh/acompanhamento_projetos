from django.db import models
from projetos.models import Projeto


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    area = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
    # a class Meta é onde passamos os metadados da tabela
    #ex: nome da tabela
    class Meta:
        ...
        # db_table = 'projeto'
    
    def _str_(self):
        return self.nome
    
class Pessoa_Projeto(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
