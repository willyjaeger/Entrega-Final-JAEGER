from django.urls import path    
from .views import *    

urlpatterns = [ 
    path("crear_usuario/",crear_usuario,name="crear_usuario"),
    path("listar_usuarios/",listar_usuarios,    name="listar_usuarios"),
    path("inicio/",inicio,name="inicio"),
    path("login/",login,name="login"),   
    path("mensajes/",mensajes,  name="mensajes"),     
    path("perfil/",perfil,  name="perfil"), 
    path("about/",about,  name="about"),

    path("usuario/lista/",UsuarioLista.as_view(),name="usuariolista"),
    path("usuario/crear/",UsuarioCrear.as_view(),name="usuariocrear"),         
    path("usuario/<pk>",UsuarioDetalle.as_view(),name="usuariodetalle"), 
    path("usuario/borrar/<pk>",UsuarioBorrar.as_view(),name="usuarioborrar"),   
    path("usuario/editar/<pk>",UsuarioEditar.as_view(),name="usuarioeditar"),
]   
