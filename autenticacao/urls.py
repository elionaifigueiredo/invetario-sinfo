from django.urls import path

from . import views

urlpatterns = [
    path('logar/', views.logar, name="logar"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('sair/', views.sair, name="sair")
]

