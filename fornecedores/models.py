from django.db import models

# Create your models here.

class Fornecedores(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    produto = models.CharField(max_length=100)