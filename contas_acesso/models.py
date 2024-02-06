from django.db import models
from pessoas.models import Pessoa
from django.contrib.auth.models import AbstractBaseUser

class Contas(models.Model):
    cpf = models.CharField(unique=True, null=False, max_length=11)
    senha = models.CharField(null=True, max_length=50)

    