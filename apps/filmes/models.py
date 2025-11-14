from django.db import models
from generos.models import Genero

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField('Título', max_length=50)
    sinopse = models.TextField('Sinopse', max_length=400)
    genero = models.ManyToManyField(Genero, on_delete=models.CASCADE)
    duracao = models.TimeField('Duração')

    class Meta:
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'
        ordering =['id']


    def __str__(self):
        return f"{self.titulo} (Duração: {self.duracao})"