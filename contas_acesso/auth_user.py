from django.contrib.auth.backends import BaseBackend
from .models import Contas  

class Backend(BaseBackend):
    def authenticate(request, cpf=None, senha=None, **kwargs):
        try:
            user = Contas.objects.get(cpf=cpf)
            if senha == user.senha:
                return user
            else:
                return False
        except Contas.DoesNotExist:
            return None

    def get_user(cpf):
        try:
            return Contas.objects.get(cpf=cpf)
        except Contas.DoesNotExist:
            return None
