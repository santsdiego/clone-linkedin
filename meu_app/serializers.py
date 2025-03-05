from rest_framework import serializers
from .models import Usuario  # Alterado para 'Usuario'

class UsuarioSerializer(serializers.ModelSerializer):  # Alterado para 'Usuario'
    class Meta:
        model = Usuario
        fields = '__all__'
