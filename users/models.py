from django.db import models


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)

    formacao_academica = models.JSONField(null=True, blank=True)
    xp_profissional = models.JSONField(null=True, blank=True)
    interesse = models.JSONField(null=True, blank=True)
    idioma = models.JSONField(null=True, blank=True)
    competencias = models.JSONField(null=True, blank=True)
    atividade = models.JSONField(null=True, blank=True)
    certificado = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.nome
    