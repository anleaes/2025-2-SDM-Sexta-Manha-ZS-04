from .models import Avaliacao
from rest_framework import serializers

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

    def validate(self, data):
        nota = data.get('nota')
        if nota is not None and (nota < 0 or nota > 10):
            raise serializers.ValidationError({
                'nota': 'A nota deve estar entre 0 e 10.'
            })
        return data