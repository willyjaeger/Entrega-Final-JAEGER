from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=40,null=False,default="")
    apellido=models.CharField(max_length=40,null=False,default="")     
    contraseña=models.CharField(max_length=40)
    email=models.EmailField(max_length=40,null=True,default="")
        
    def __str__(self):
        return f"{self.nombreusuario} - {self.email}"

   