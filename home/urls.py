from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name="home"),
    path('home/', views.home_msg, name="home_msg"),
    path('', views.index, name="index"),
    path('cancelar/<int:id_cancelar>', views.cancelar, name="cancelar")

    ]

