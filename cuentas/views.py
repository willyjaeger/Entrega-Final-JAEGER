from django.shortcuts import render
from .models import Usuario, Perfiles, Mensajes, EntradasBlog
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy      

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
 


def about(request):
    return render(request, 'about.html')

def usuarioregistro(request):
    if request.method=="POST":
        nombreusuario=request.POST["nombreusuario"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        contraseña=request.POST["contraseña"]
        email=request.POST["email"]
        usuario=Usuario(nombreusuario=nombreusuario,nombre=nombre,apellido=apellido,contraseña=contraseña,email=email)
        usuario.save()

        return render(request,"usuarioregistro.html",{"mensaje":"Usuario Registrado"})
    else:

        return render(request,"usuarioregistro.html")   
    return render(request, 'usuarioregistro.html')

def usuarioeditar(request):
    return render(request, 'usuarioeditar.ntml')

class UsuarioLista(ListView):
    model = Usuario
    template_name = 'usuariolista.html'

class UsuarioCrear(CreateView):
    model = Usuario

    fields = ['nombreusuario','nombre','apellido','contraseña','email']
    template_name = 'usuarioeditar.html'
    success_url = reverse_lazy('usuariolista' )

class UsuarioDetalle(DetailView):
    model = Usuario
    template_name = 'usuariodetalle.html'

class UsuarioBorrar(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuariolista.html' )

class UsuarioEditar(UpdateView):
    model = Usuario
    fields = ['nombreusuario','nombre','apellido','contraseña','email']
    template_name = 'usuarioeditar.html'
    success_url = reverse_lazy('usuariolista' )

