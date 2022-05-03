from itertools import count
from multiprocessing import context
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
# from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

from . models import Material
#FUNCIONALIDADE FUNCIONAL
@login_required(login_url='/auth/logar/')
def cad_inventario(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'cad_material.html')
        return redirect('/auth/logar.html')
    elif request.method == "POST":
        usuario = request.user
        itens = request.POST.get('itens','')
        modelo = request.POST.get('modelo','')
        serie = request.POST.get('serie','')
        bmp = request.POST.get('bmp','')
        secao_carga = request.POST.get('secao_carga','')
        descricao = request.POST.get('descricao','')
        status = request.POST.get('status','')
        data = datetime.now()
        id = request.POST.get('id')
        if id:
            Material.objects.filter(id=id).update( itens=itens, modelo=modelo, serie=serie, bmp=bmp, secao_carga=secao_carga, descricao=descricao, status=status)
        else:
            form = Material.objects.create(usuario=usuario, itens=itens, modelo=modelo, serie=serie, bmp=bmp, secao_carga=secao_carga, descricao=descricao, status=status, data=data)
            form.save()
    return redirect('/inventario/lista_material')

        
# FUNCIONALIDADE LISTA FUNCIONAL    
@login_required(login_url='/auth/logar/')
def lista_material(request):
    lista_material = Material.objects.filter(usuario = request.user)
    busca = request.GET.get('search')# REALIZA O PESQUISA
    if busca:
        lista_material = Material.objects.filter(itens__icontains = busca)
    context = {'lista_material': lista_material}
    return render(request, 'lista_material.html', context)


#FUNCIONALIDADE DELETE FUNCIONAL
@login_required(login_url='/auth/logar/')
def delete(request, material_id):
    usuario = Material.objects.get(id=material_id)
    if request.method == "POST": # como lista_material é um GET e não é um form POST é direcionado para o else
        usuario.delete()
        return redirect('/inventario/lista_material')
    else: # O material_id vai no form delete_material onde existe um POST
        return render(request, 'deletar_material.html', {'usuario':usuario})
    
    # usuario = request.user
    # try:
    #     # material = get_object_or_404(Material, id=material_id) ----tbm funciona
    #     material = Material.objects.get(id=material_id)
    # except Exception:
    #     raise Http404()
    
    # if usuario == material.usuario:
    #     material.delete()
    #     return redirect('/inventario/lista_material')
    # else:
    #     raise Http404()
    #     return redirect('/inventario/lista_material')

    # obj = get_object_or_404(Material, id=material_id)
    # if request == "POST":
    #     obj.delete()
    #     return redirect('/inventario/lista_material')
    # context = {
    #     "obj": obj
    # }
    # return render(request, 'deletar_material.html', context)

@login_required(login_url='/auth/logar/')
def edit_inventario(request, id_material):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'cad_material.html')
        return redirect('/auth/logar.html')
    elif request.method == "POST":
        itens = request.POST.get('itens','')
        modelo = request.POST.get('modelo','')
        serie = request.POST.get('serie','')
        bmp = request.POST.get('bmp','')
        secao_carga = request.POST.get('secao_carga','')
        descricao = request.POST.get('descricao','')
        status = request.POST.get('status','')
        id_material = request.POST.get('id')
        if id_material:
            Material.objects.filter(id=id_material).update( itens=itens, modelo=modelo, serie=serie, bmp=bmp, secao_carga=secao_carga, descricao=descricao, status=status)
        else:
            return redirect('/inventario/lista_material')
    return redirect('/inventario/lista_material')










        

