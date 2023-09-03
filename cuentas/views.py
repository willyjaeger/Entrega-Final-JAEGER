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

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html') 

def mensajes(request):
    return render(request, 'mensajes.html')

def perfil(request):
    return render(request, 'perfil.html')   
 
def usuario(request):
    return render(request, 'cuentas/usuario.html')

def about(request):
    return render(request, 'about.html')


