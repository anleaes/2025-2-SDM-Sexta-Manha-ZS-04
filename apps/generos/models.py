from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=400)
    clasificacao_indicativa = models.CharField('Classificação Indicativa', max_length=50)
    pais_de_origem = models.CharField('País de Origem', max_length=50)

    class Meta:
            verbose_name = 'genero'
            verbose_name_plural = 'generos'
            ordering =['id']


    def __str__(self):
        return f"{self.nome} (Classificação Indicativa: {self.clasificacao_indicativa})"