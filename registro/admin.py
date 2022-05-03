from django.contrib import admin

from registro.models import registro
# Register your models here.

@admin.register(registro)
class registroAdmin(admin.ModelAdmin):
    list_display =["nome"]

