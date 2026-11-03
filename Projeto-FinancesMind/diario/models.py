from django.db import models

EMOTIONS_CHOICES = [
    ('ansioso','Ansioso'),
    ('cansado','Cansado'),
    ('empolgado','Empolgado'),
    ('feliz','Feliz'),
    ('irritado','Irritado'),
    ('normal','Normal'),
    ('triste','Triste'),
]

class MotivoDiario(models.Model):
    nome = models.CharField()
    img = models.ImageField()

    def __str__(self):
        return self.nome


class RegistroDiario(models.Model):
    data = models.DateField()
    motivos = models.ManyToManyField(MotivoDiario, blank=True)
    texto = models.TextField(blank=True)

    def __str__(self):
        return f'{self.data}: {self.emocao}' 


class Emocao(models.Model):
    nome = models.CharField()
    img = models.ImageField()
    registros = models.ForeignKey(
         RegistroDiario,
         related_name='Emocao',
         on_delete=models.PROTECT,
    )

    def __str__(self):
            return self.nome    