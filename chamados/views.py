from datetime import datetime
from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.contrib import messages


from . models import Chamados, Solucionador, Status

@login_required(login_url='/auth/logar/')
def solucionador(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'solucionador.html')
        return redirect('/auth/logar.html')
    elif request.method == "POST":
        nome = request.POST.get('nome','')
        data_inicio = request.POST.get('data_inicio', datetime.now())
        data_termino = request.POST.get('data_inicio', datetime.now())
    # fazer o if dos fields blank or null
        formulario = Solucionador.objects.create(nome=nome, data_inicio=data_inicio, data_termino=data_termino)
        formulario.save()
        messages.error (request, 'Registrado o Solucionador')
        return render(request, 'home.html')

@login_required(login_url='/auth/logar/')
def chamados(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'chamados.html')
        return redirect('/auth/logar.html')
    
    elif request.method == 'POST':
        usuario = request.user
        date = datetime.now()
        militar = request.POST.get('militar','')
        contato = request.POST.get('contato','')
        subject = request.POST.get('assunto','')
        message = request.POST.get('descricao', '')
        from_email = request.POST.get('admin_email', '')
        recipient_list = request.POST.get('solicitante', '')

    if len(militar.strip()) == 0 or len(contato.strip()) == 0 or len(subject.strip()) == 0 or len(message.strip()) == 0 or len(from_email.strip()) == 0 or len(recipient_list.strip()) == 0:
        try:
            send_mail(subject, message,
                      from_email, [recipient_list])
                      
            formulario = Chamados.objects.create(date=date, usuario=usuario, militar=militar,contato=contato, subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
            formulario.save()
        except Exception:
            messages.error (request, 'Falha no Envio Contate o Administrador.')
            return redirect('chamados')
        return redirect('home')

    else:
        return HttpResponse('Email not send')








