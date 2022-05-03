from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Material(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    itens = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    serie = models.CharField(max_length=30, blank=True )
    bmp = models.CharField(max_length=30, blank=True)
    secao_carga = models.CharField(max_length=30)
    descricao = models.TextField()
    status = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'material'
    

    def __str__(self):
        return self.itens
    
    