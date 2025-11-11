from django.db import models
from clientes.models import Cliente
from filmes.models import Filme

# Create your models here.
class Avaliacao(models.Model):
    nota = models.IntegerField('Nota (0 a 10)')
    descricao = models.TextField('Descrição', max_length=400)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering =['id']


    def __str__(self):
        return f"{self.cliente.nome} - {self.nota} (Filme: {self.filme.titulo})"
