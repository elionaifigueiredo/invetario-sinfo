from django.urls import path

from . import views

urlpatterns = [
    path('chamados/', views.chamados, name="chamados"),
    path('solucionador/', views.solucionador, name="solucionador"),


]

