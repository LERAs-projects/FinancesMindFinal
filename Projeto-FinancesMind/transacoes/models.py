from django.db import models
from usuario.models import Usuario

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

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='Receita',
    )
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

    usuario = models.ForeignKey(
            Usuario,
            on_delete=models.CASCADE,
            related_name='Transferencia',
        )
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

    usuario = models.ForeignKey(
            Usuario,
            on_delete=models.CASCADE,
            related_name='Despesa',
        )
    lancamento = models.CharField(choices=LANCAMENTO_CHOICES, null=False)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, null=False)

