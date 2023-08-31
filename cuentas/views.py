from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse

# Create your views here.
def  crear_usuario(request):
    nombreusuario = "Willy"
    apellidousuario ="Jaeger"
    contraseñausuario = "1234"
    print("creando usuario")
    usuario = Usuario(nombre=nombreusuario,apellido=apellidousuario,contraseña=contraseñausuario)       
    usuario.save()
    respuesta =f"Usuario Creado: {usuario.nombre} - {usuario.contraseña}"
    return HttpResponse(respuesta)
 
def  listar_usuarios(request):
    usuarios = Usuario.objects.all()
    respuesta = ""
    for usuario in usuarios:
        respuesta += f"{usuario.nombre} - {usuario.apellido} <br>"
    return HttpResponse(respuesta)