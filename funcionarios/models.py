from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)