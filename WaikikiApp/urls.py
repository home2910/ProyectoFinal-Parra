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
from django.contrib.auth.views import LogoutView
from .views import inicio, busqueda_producto, buscar_producto, user_login, register, ProductsListView, ProductCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('Agregar-producto/', ProductCreateView.as_view(), name='agg'),
    path('Busqueda-producto/', busqueda_producto, name='busqueda-producto'),
    path('Buscar-producto/', buscar_producto, name='buscar-producto'),
    path('Leer-productos/', ProductsListView.as_view(), name='leer-producto'),
    path('Borrar-productos/<int:pk>/delete', ProductDeleteView.as_view(), name='eliminar-producto'),
    path('Actualizar_producto/<int:pk>/update', ProductUpdateView.as_view(), name='editar-producto'),
    path('login/', user_login, name='login' ),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
  