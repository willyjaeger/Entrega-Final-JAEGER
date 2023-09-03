from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreusuario=models.CharField(max_length=40,null=False,default="") 
    nombre=models.CharField(max_length=40,null=False,default="")
    apellido=models.CharField(max_length=40,null=False,default="")     
    contraseña=models.CharField(max_length=40)
    email=models.EmailField(max_length=40,null=True,default="")
        
    def __str__(self):
        return f"{self.nombreusuario} - {self.email}"

class Perfiles(models.Model):
    imagen=models.CharField(max_length=40,null=False,default="") 
    nombre=models.CharField(max_length=40,null=False,default="")
    descripcion=models.CharField(max_length=100,null=False,default="")
    usuarioid=models.IntegerField()
    paginaweb=models.CharField(max_length=40,null=False,default="") 
    email=models.EmailField(max_length=40,null=True,default="") 
    contraseña=models.CharField(max_length=40)  
    def __str__(self):
        return f"{self.nombre} - {self.paginaweb}"   
    
class Mensajes(models.Model):
    mensaje=models.CharField(max_length=200,null=False,default="") 
    usuarioidemisor=models.IntegerField()
    usuarioidreceptor=models.IntegerField() 
    leido=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.mensaje} - {self.usuarioid}"