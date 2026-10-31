from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    saldo = models.DecimalField(max_digits=17,decimal_places=2)
    profissao = models.CharField(max_length=200, blank=True, null=True)
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #password herdado

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Na hora de criar um superuser, será pedido apenas o username (que agora será o e-mail) e a senha

    def __str__(self):
        return self.nome

    def primeiro_nome(self):
        nomes = self.nome.split()
        return nomes[0] if nomes else ""