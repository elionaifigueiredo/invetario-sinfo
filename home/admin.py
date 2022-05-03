from django.contrib import admin
from chamados.models import Chamados, Solucionador, Status

@admin.register(Chamados)
class ChamadosAdmin(admin.ModelAdmin):
    list_display = ['solucionador','id','status','date','militar','contato','subject','message']

@admin.register(Solucionador)
class SolucionadorAdmin(admin.ModelAdmin):
    list_display = ['nome','data_inicio','data_termino']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','status']


    
  
