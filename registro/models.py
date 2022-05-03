from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class registro(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=2)
    serie = models.CharField(max_length=30)
    nome_fornecedor = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    cpf = models.CharField(max_length=15)
    quantidade = models.IntegerField()

    class Meta:
        db_table = "registro"
    def __str__(self) -> str:
        return self.nome