from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    