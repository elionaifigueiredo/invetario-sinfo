from statistics import mode
from django.db import models 

from datetime import datetime
# Create your models here.

from django.contrib.auth.models import User


class Solucionador(models.Model):
    id = models.AutoField(primary_key= True)
    nome = models.CharField(max_length=30)
    data_inicio = models.DateTimeField(auto_created=True)
    data_termino = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'solucionador'

    def __str__(self) -> str:
        return self.nome

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    choice_status = (('R', 'Resolvido'),('C','Cancelado'),('P','Processando'))
    status = models.CharField(max_length=1, choices=choice_status)

    class Meta:
        db_table = 'status'
    
    def __str__(self) -> str:
        return self.status



class Chamados(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    solucionador = models.ForeignKey(Solucionador,null=True, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, null=True, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    militar = models.CharField(max_length=30)
    contato = models.CharField(max_length=11)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    from_email = models.CharField(max_length=250)
    recipient_list = models.CharField(max_length=250)
    

    class Meta:
        db_table = 'chamados'

    def __str__(self) -> str:
        return self.subject













    
