from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField('Título', max_length=50)
    sinopse = models.TextField('Sinopse', max_length=100)
    genero = models.CharField('Gênero', max_length=50)
    duracao = models.TimeField('Duração')

    class Meta:
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'
        ordering =['id']


    def __str__(self):
        return self.titulo