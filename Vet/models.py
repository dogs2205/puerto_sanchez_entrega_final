from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    nombre_animal = models.CharField(max_length=100)
    tipo_animal = models.CharField(max_length=80)
    edad_animal = models.CharField(max_length=15)
    precio_tratamiento = models.FloatField()
    pre_diagnostico = models.CharField(max_length=120)
    imagen = models.ImageField(upload_to="menues", null=True, blank=True)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name="propietario")
    creado_el = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''

    def __str__(self):
        return f"{self.id} - {self.nombre_animal} - {self.propietario.id}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''


class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")

    
    
# Create your models here.
