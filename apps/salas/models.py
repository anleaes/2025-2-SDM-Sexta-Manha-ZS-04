from django.db import models
from cinemas.models import Cinema

# Create your models here.
class Sala(models.Model):
    lotacao_maxima = models.IntegerField('Lotação Máxima')
    assentos_normais = models.IntegerField('Assentos Normais')
    assentos_acessiveis = models.IntegerField('Assentos Acessíveis')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering =['id']

    def __str__(self):
        return self.lotacao_maxima