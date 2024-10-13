from django.contrib import admin
from .models import Cliente, Empleado, Producto, Avatar


# Register your models here.

admin.site.register(Cliente)

admin.site.register(Empleado)

admin.site.register(Producto)

admin.site.register(Avatar)
