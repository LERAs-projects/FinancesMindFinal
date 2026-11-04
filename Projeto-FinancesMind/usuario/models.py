from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower


from core.models import Pin
from .managers import UsuarioManager

class Usuario(AbstractUser):
    username = None
    first_name = None
    last_name = None

    nome = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    saldo = models.DecimalField(max_digits=17, decimal_places=2, null=False, blank=False, default=0)
    profissao = models.CharField(max_length=200, blank=True, null=False)
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    foto = models.ImageField(null=True, blank=True)
    pins_curtidos = models.ManyToManyField("Pin")

    #password herdado

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento'] # Na hora de criar um superuser, será pedido esses campos, além do email e senha.


    objects = UsuarioManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                name="usuario_email_ci_unique"
            )
        ]


    def __str__(self):
        return self.nome

    @property
    def primeiro_nome(self):
        nomes = self.nome.split()
        return nomes[0] if nomes else ""

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.primeiro_nome


class Analise():
    from transacoes.models import Despesa, Receita, Transferencia
    TOTALDIAS_CHOICES = [
        (7, "7 dias"),
        (15, "15 dias"),
        (30, "30 dias"),
        (60, "60 dias"),
        (90, "90 dias"),
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='Analise'
    )
    data = models.DateField()
    periodo_dias = models.IntegerField(choices=TOTALDIAS_CHOICES)
    despesas = models.ManyToManyField(Despesa,)
    receitas = models.ManyToManyField(Receita,)

    
