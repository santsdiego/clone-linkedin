from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    idade = models.PositiveIntegerField()  # Usando PositiveIntegerField para garantir valores não negativos
    telefone = models.CharField(max_length=15)

    cargo = models.CharField(max_length=255, null=True, blank=True)
    
    formacao_academica = models.JSONField(null=True, blank=True)
    xp_profissional = models.JSONField(null=True, blank=True)
    interesse = models.JSONField(null=True, blank=True)
    idioma = models.JSONField(null=True, blank=True)
    competencias = models.JSONField(null=True, blank=True)
    atividade = models.JSONField(null=True, blank=True)
    certificado = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Usuário Customizado'  # Definindo o nome do modelo para a interface de admin
        verbose_name_plural = 'Usuários Customizados'  # Definindo o nome plural para a interface de admin
