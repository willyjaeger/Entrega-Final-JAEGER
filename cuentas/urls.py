from django.urls import path    
from .views import *    

urlpatterns = [ 
    path("crear_usuario/",crear_usuario,name="crear_usuario"),
    path("listar_usuarios/",listar_usuarios,    name="listar_usuarios"),
    path("inicio/",inicio,name="inicio"),
    path("login/",login,name="login"),   
    path("mensajes/",mensajes,  name="mensajes"),     
    path("perfil/",perfil,  name="perfil"), 
    path("usuario/",usuario,  name="usuario"), 
    path("about/",about,  name="about"),


]   
