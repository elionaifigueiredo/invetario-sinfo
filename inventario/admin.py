from django.contrib import admin

# Register your models here.

from inventario.models import Material

@admin.register(Material)
class AdminMaterial(admin.ModelAdmin):
    list_display = ['id','itens','serie','bmp', 'modelo','secao_carga','data']
