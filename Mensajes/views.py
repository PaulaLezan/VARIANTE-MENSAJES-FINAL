from email import message
from django.shortcuts import render 
from django.http import HttpResponse
from Mensajes.models import * 
from Mensajes.forms import *


# Create your views here.

def mensajes(request):   
    if (request.method=='POST'):
        form= MensajeForm(request.POST) 
        if form.is_valid():   
            info=form.cleaned_data
            emisor=info['emisor']
            receptor=info['receptor']
            message=info['message']
            fecha=info['fecha']
            hora=info['hora']
            mensaje=Mensajes(emisor=emisor,receptor= receptor, message=message, fecha=fecha, hora=hora ) 
            mensaje.save()
            comentario = "Su mensaje se ha enviado exitosamente"
            return render(request, 'Blog/inicio.html') 
    else:
        form=MensajeForm() 
    return render(request, 'Mensajes/inbox.html', {"form":form})


def leerUsuarios (request):
    user=Mensajes.objects.all()
    return render (request, "Mensajes/leerUsuarios.html", {"user":user})


def inbox (request):
    if request.method == "GET":
        mensaje_recibido= Mensajes.objects.filter(receptor=request.user)
        
        return render(request, 'Mensajes/inbox.html',{'users': User.objects.exclude(username=request.user.username)})

def crearMensajes(request):
    if (request.method=='POST'):
        form= MensajeForm(request.POST) 
        if form.is_valid():   
            info=form.cleaned_data
            emisor=info['emisor']
            receptor=info['receptor']
            message=info['message']
            created_at=info['created_at']
            mensaje=Mensajes(emisor=emisor,receptor= receptor, message=message, created_at=created_at ) 
            mensaje.save()
            comentario = "Su mensaje se ha enviado exitosamente"
            return render(request, 'Blog/inicio.html',{'comentario':comentario}) 
    else:
        form=MensajeForm() 
    return render(request, 'Mensajes/inbox.html', {"form":form})

def leerMensajes (request, emisor, receptor):
       if request.method == "GET":
        return render(request, "chat/messages.html",{'users': User.objects.exclude(username=request.user.username),'receiver': User.objects.get(id=receiver),
                       'messages': Mensajes.objects.filter(sender_id=emisor, receiver_id=receptor) |
                                  Mensajes.objects.filter(sender_id=receptor, receiver_id=emisor)})

