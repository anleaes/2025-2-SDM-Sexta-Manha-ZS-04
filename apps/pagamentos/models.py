from django.db import models

# Create your models here.
class Pagamento(models.Model):
    nome = models.CharField('Nome', max_length=50)
    tipo = models.CharField('Tipo', max_length=50, default='À Vista', choices=[
        ('a_vista', 'À Vista'),
        ('parcelado', 'Parcelado'),
        ('voucher', 'Voucher'),
    ]
    )
    desconto = models.DecimalField('Desconto (%)', max_digits=5, decimal_places=2, default=0)
    ativo = models.BooleanField('Ativo')
 
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['id']

    def __str__(self):
        return f"{self.nome} - {self.tipo})"