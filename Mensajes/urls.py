from django.urls import path
from .views import *

urlpatterns = [

    
    path('inbox/', inbox, name=inbox), 
    path('leerUsuarios/', leerUsuarios, name=leerUsuarios),
    path('verMensajes/', leerMensajes, name=leerMensajes),
    path('crearMensajes/', crearMensajes, name=crearMensajes),


]