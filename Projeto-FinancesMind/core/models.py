from django.db import models


class Pin(models.Model):
    texto = models.TextField(max_length=300)
    fontes = models.CharField(max_length=255)

    def __str__(self):
        return self.texto[:50]


class Video(models.Model):
    capa = models.ImageField(null=True, blank=True)
    titulo = models.CharField(max_length=200)
    canal = models.CharField(max_length=150)

    def __str__(self):
        return self.titulo + " --- " + self.canal