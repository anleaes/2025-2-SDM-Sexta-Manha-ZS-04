from .models import Sala
from rest_framework import serializers

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

    def validate(self, data):
        total_assentos = data.get('assentos_normais', 0) + data.get('assentos_acessiveis', 0)
        if total_assentos != data.get('lotacao_maxima', 0):
            # Aqui retorna só uma mensagem simples
            raise serializers.ValidationError("A soma dos assentos deve ser igual à lotação máxima.")
        return data