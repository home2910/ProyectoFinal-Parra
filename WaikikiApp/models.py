from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
      return f'Nombre: {self.nombre} - Apellido: {self.apellido}'
    

class Cliente(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
      return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}'

class Producto(models.Model):
    nombre = models.CharField( max_length=50)
    precio = models.IntegerField()

    def __str__(self):
      return f'Producto: {self.nombre} - Precio: ${self.precio}'

class Avatar(models.Model):
   
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   imagen = models.ImageField(upload_to='avatares', null = True, blank = True)










