
from django.urls import path
from . import views

urlpatterns = [

    path('cad_inventario/', views.cad_inventario, name="cad_inventario"),
    path('edit/<int:id_material>', views.edit_inventario, name="edit_inventario"),
    path('lista_material/', views.lista_material, name="lista_material"),
    path('delete/<int:material_id>/', views.delete, name="delete")

]