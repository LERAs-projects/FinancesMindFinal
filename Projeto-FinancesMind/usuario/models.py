from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower

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


EMOCOES_CHOICES = [
    ('feliz', 'Feliz'),
    ('triste', 'Triste'),
    ('ansioso', 'Ansioso'),
    ('estressado', 'Estressado'),
    ('paz', 'Paz')
]

LANCAMENTO_CHOICES = [
    ('recorrente', 'Recorrente'),
    ('parcelado', 'Parcelado'),
    ('unico', 'Único')
]

class Transacao(models.Model):

    class Meta:
        abstract = True

    data = models.DateField(null=False)
    descricao = models.TextField(blank=True)
    emocao = models.CharField(choices=EMOCOES_CHOICES, null=False)

class Receita(Transacao):

    lancamento = models.CharField(choices=LANCAMENTO_CHOICES, null=False)

class Transferencia(Transacao):

    TIPOS_CONTAS_CHOICES = [
        ('corrente', 'Conta-Corrente'),
        ('poupanca', 'Conta Poupança'),
        ('salario', 'Conta Salário'),
        ('digital', 'Conta Digital'),
        ('empresarial', 'Conta PJ / Empresarial'),
        ('conjunta', 'Conta Conjunta'),
    ]

    conta_origem = models.CharField(choices=TIPOS_CONTAS_CHOICES, default='corrente', null=False)
    conta_destino = models.CharField(choices=TIPOS_CONTAS_CHOICES, null=False)

class Despesa(Transacao):

    CATEGORIA_CHOICES = [
        ('alimentacao', 'Alimentação'),
        ('moradia', 'Moradia'),
        ('transporte', 'Transporte'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('lazer', 'Lazer'),
        ('vestuario', 'Vestuário'),
        ('contas', 'Contas (água, luz, internet)'),
        ('compras', 'Compras'),
        ('higiene', 'Higiene pessoal'),
        ('impostos', 'Impostos e taxas'),
        ('dividas', 'Dívidas e empréstimos'),
        ('animais', 'Animais de estimação'),
        ('outros', 'Outros'),
    ]

    lancamento = models.CharField(choices=LANCAMENTO_CHOICES, null=False)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, null=False)

