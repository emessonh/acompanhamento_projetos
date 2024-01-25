from django.db import models
from pessoas.models import Pessoa
# from django.db.models.signals import pre_save
# from django.dispatch import receiver

# Create your models here.

class Contas(models.Model):
    cpf = models.CharField(unique=True, null=False, max_length=11)
    senha = models.CharField(null=True, max_length=50)

    # def save_cpf(self, *args, **kwargs):
    #     self.cpf = Pessoa
    #     super(Contas, self).save(*args, **kwargs)