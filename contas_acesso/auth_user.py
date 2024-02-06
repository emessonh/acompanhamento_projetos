from django.contrib.auth.backends import BaseBackend
from .models import Contas  

class Backend(BaseBackend):
    def authenticate(request, cpf=None, senha=None, **kwargs):
        try:
            user = Contas.objects.get(cpf=cpf)
            if senha == user.senha:
                return user
            else:
                return None
        except Contas.DoesNotExist:
            return None

    def get_user(user_id):
        try:
            return Contas.objects.get(pk=user_id)
        except Contas.DoesNotExist:
            return None
