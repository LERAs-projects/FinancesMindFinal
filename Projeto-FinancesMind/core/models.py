from django.db import models

class Pin():
    texto = models.TextField(max_length=300)
    fontes = models.CharField()


class Video():
    capa = models.ImageField(null=True, blank=True)
    titulo = models.CharField()
    canal = models.CharField()

    def __str__(self):
        return self.titulo + " --- " + self.canal