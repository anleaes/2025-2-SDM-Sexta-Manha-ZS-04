from django.db import models
from sessoes.models import Sessao
from clientes.models import Cliente

# Create your models here.
class Ingresso(models.Model):
    tipo = models.CharField('Tipo', max_length=50, default='Inteira', choices=[
        ('inteira', 'Inteira'),
        ('meia_estudante', 'Meia — Estudante'),
        ('meia_pcd', 'Meia — PCD'),
        ('promocional', 'Promocional'),
        ('infantil', 'Infantil'),
        ('cortesia', 'Cortesia'),
    ])
    preco =  models.DecimalField('Preço', max_digits=5, decimal_places=2, default=0)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)   
   