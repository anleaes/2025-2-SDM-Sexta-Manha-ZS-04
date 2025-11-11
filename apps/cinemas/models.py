from django.db import models


# Create your models here.
class Cinema(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereço', max_length=100)
    horario_de_abertura = models.TimeField('Horário de Abertura')
    horario_de_fechamento = models.TimeField('Horário de Fechamento')
   
    class Meta:
        verbose_name = 'cinema'
        verbose_name_plural = 'cinemas'
        ordering =['id']


    def __str__(self):
        return f"{self.nome} - ({self.endereco})"