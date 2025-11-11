from django.db import models
from salas.models import Sala
from filmes.models import Filme

# Create your models here.
class Sessao(models.Model):
    horario_de_inicio = models.TimeField('Horário de Início')
    tipo_de_exibicao = models.CharField('Exibição', max_length=50, default='dublada', choices=[
        ('dublada', 'Dublada'),
        ('legendada', 'Legendada'),
        ('original', 'Áudio Original (Sem Legendas)'),
        ('3d_dublada', '3D Dublada'),
        ('3d_legendada', '3D Legendada'),
        ('imax_dublada', 'IMAX Dublada'),
        ('imax_legendada', 'IMAX Legendada'),
    ]
    )
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'
        ordering =['id']

    def __str__(self):
        return f"{self.filme.titulo} - {self.tipo_de_exibicao} (Início: {self.horario_de_inicio})"