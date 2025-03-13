from rest_framework import serializers
from .models import Usuario  # Alterado para 'Usuario'

class UsuarioSerializer(serializers.ModelSerializer):  # Alterado para 'Usuario'
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_nome(self, nome):
        if len(nome) < 3:
            raise serializers.ValidationError("O nome deve ser maior que 3 caracteres.")
        return nome

    def validate_email(self, email):
        if not email.endswith("@gmail.com") and not email.endswith("@hotmail.com") and not email.endswith("@outlook.com") and not email.endswith("@yahoo.com"):
            raise serializers.ValidationError("O email informado não é válido.")
        return email

    def validate_idade(self, idade):
        if idade < 1:
            raise serializers.ValidationError("A idade não pode ser menor que 1.")
        return idade

    def validate_telefone(self, telefone):
        if len(telefone) != 11:
            raise serializers.ValidationError("Número de telefone incorreto.")
        return telefone
