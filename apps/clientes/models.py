from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=50)
    data_de_nascimento = models.DateField('Data de Nascimento')
    email = models.CharField('E-mail', max_length=50)
   
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']


    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"