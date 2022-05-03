from email import header, utils
from tkinter.tix import Meter
from typing import Counter
from django.shortcuts import render, redirect
from chamados.models import Chamados
from inventario.models import Material
from chamados.models import Status
from django.contrib.auth.models import User

from .utils import get_plot

from django.db.models import Count
# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/logar/')
def home(request):
    lista_chamados = Chamados.objects.filter(usuario=request.user)
    context = {'lista_chamados': lista_chamados}
    return render(request,'home.html', context)

@login_required(login_url='/auth/logar/')
def home_msg(request):
    context = {'msg': "lista_chamados"}
    return render(request,'home.html', context)

def cancelar(request, id_cancelar):
    valor = 2
    status_cancelar = Status.objects.get(id=id_cancelar)
    status_cancelar.id = valor
    status_cancelar.save()
    return redirect('home')


def index(request):
    material = Material.objects.all()
    x = [x.itens for x in material]
    y = [y.serie for y in material ]
    chart = get_plot(x,y)
    return render(request, "index.html", {'chart': chart})











