from django.db import models

# Create your models here.
class Pagamento(models.Model):
    nome = models.CharField('Nome')
    tipo = models.CharField('Tipo', max_length=50, default='À Vista', choices=[
        ('a_vista', 'Vista'),
        ('parcelado', 'Parcelado'),
        ('voucher', 'Voucher'),
    ]
    )
    desconto = models.DecimalField('Desconto')
    ativo = models.BooleanField('Ativo')
 
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['id']

    def __str__(self):
        return f"{self.nome} - {self.tipo})"