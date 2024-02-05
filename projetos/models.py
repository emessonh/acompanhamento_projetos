from django.db import models
import datetime

ano_atual = datetime.date.today()

# Create your models here.

class Status(models.Model):
    descricao = models.CharField(max_length=100)
    cor = models.CharField(max_length=10)
    
    def __str__(self):
        return self.descricao

class Setor(models.Model):
    nome = models.CharField(max_length=100)
        
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    sobre = models.TextField(blank=False, null=False)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE) # revisar
    situacao_atual = models.TextField(blank=True, null=True)
    prioridade = models.CharField(max_length=5)
    prazo = models.DateField(blank=True, null=True) # revisar
    ano_desenvolvimento = models.CharField(null=False)
    link = models.CharField(blank=True, null=True, max_length=100)
    proximos_passos = models.TextField(blank=True, null=True)
    impedimentos = models.TextField(blank=True, null=True)
    sistema_critico = models.BooleanField(default=False) # revisar
    setor_id = models.ForeignKey(Setor, on_delete=models.CASCADE) # revisar
    pasta_responsavel = models.CharField(max_length=8)
    data_criacao = models.DateTimeField(auto_now=True)
    
    # a class Meta é onde passamos os metadados da tabela
    #ex: nome da tabela
    class Meta:
        ...
        # db_table = 'projeto'
    
    def __str__(self):
        return self.nome
