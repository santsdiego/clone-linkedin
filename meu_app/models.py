from django.db import models

class Usuario(models.Model):  # Alterado para 'Usuario'
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
