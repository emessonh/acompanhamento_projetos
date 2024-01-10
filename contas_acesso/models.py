from django.db import models

# Create your models here.

class Contas(models.Model):
    cpf = models.CharField(null=False, max_length=11, primary_key=True)
    senha = models.CharField(null=False, max_length=50)