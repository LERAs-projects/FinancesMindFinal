from django.db import models
from usuario.models import Usuario
from django.core.validators import MinValueValidator
from decimal import Decimal

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

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='%(class)ss')
    valor = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    data = models.DateField()
    descricao = models.TextField(blank=True)
    emocao = models.CharField(max_length=20, choices=EMOCOES_CHOICES)
    lancamento = models.CharField(max_length=20, choices=LANCAMENTO_CHOICES, default='unico')

    class Meta:
        abstract = True


class Receita(Transacao):
    pass
    
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

    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

