"""
URL configuration for PreentregaTres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import inicio, add_form, busqueda_producto, buscar_producto, read_product, borrar_producto,edit_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inicio/', inicio, name='inicio'),
    path('Agregar-producto/', add_form, name='agg'),
    path('Busqueda-producto/', busqueda_producto, name='busqueda-producto'),
    path('Buscar-producto/', buscar_producto, name='buscar-producto'),
    path('Leer-productos/', read_product, name='leer-producto'),
    path('Borrar-productos/<producto_nombre>', borrar_producto, name='eliminar-producto'),
    path('Actualizar_producto/<producto_nombre>', edit_products, name='editar-producto'),
]
  