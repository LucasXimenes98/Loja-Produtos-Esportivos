from django.db import models

# Create your models here.

class NotaFiscal(models.Model):
    valorNota = models.CharField(max_length=100)
    dadosDestinatario = models.CharField(max_length=100)
    descricaoProduto = models.CharField(max_length=100)
    codigoFiscal = models.CharField(max_length=100)
    quantidades = models.CharField(max_length=100)