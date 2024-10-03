from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre = models.CharField( max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Producto(models.Model):
    nombre = models.CharField( max_length=50)
    precio = models.IntegerField()












