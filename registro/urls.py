
from django.urls import path
from . import views

urlpatterns = [
    path('equipamentos/', views.registrar, name="registrar" )
]