from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField('Título', max_length=50)
    sinopse = models.TextField('Sinopse', max_length=400)
    genero = models.CharField('Gênero', max_length=50, default='acao', choices=[
        ('acao', 'Ação'),
        ('animacao', 'Animação'),
        ('aventura', 'Aventura'),
        ('comedia', 'Comédia'),
        ('documentario', 'Documentário'),
        ('drama', 'Drama'),
        ('fantasia', 'Fantasia'),
        ('ficcao', 'Ficção Científica'),
        ('romance', 'Romance'),
        ('suspense', 'Suspense'),
        ('terror', 'Terror'),
    ]
)
    duracao = models.TimeField('Duração')

    class Meta:
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'
        ordering =['id']


    def __str__(self):
        return f"{self.titulo} (Duração: {self.duracao})"