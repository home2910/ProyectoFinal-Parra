from django.db import models

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












