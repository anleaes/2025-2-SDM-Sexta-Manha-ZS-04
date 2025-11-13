from .models import Pagamento
from rest_framework import serializers

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'

    def validate(self, data):
        desconto = data.get('desconto')

        if desconto is not None:
            if desconto < 0 or desconto > 100:
                raise serializers.ValidationError({
                    'Desconto': 'O desconto deve estar entre 0 e 100.'
                })
        return data