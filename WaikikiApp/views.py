from django.http import HttpResponse
from .models import Producto
from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

def inicio(req):

    return render(req, 'inicio.html', {})


def menu(req):

    return render(req, 'menu.html', {})


def form(req):

   if req.method == 'POST':

    mi_form = ProductForm(req.POST)

    if mi_form.is_valid():
     data = mi_form.cleaned_data

     producto = Producto(nombre= data['producto'], precio= data['precio'])
     producto.save()
 
     return render(req, "inicio.html")
    
    else:
       return render(req, "mi_form.html")
   
   else:
      mi_form = ProductForm()
      return render(req, 'form.html', { 'mi_form':mi_form })
   
def busqueda_producto(req):
   return render(req, 'busqueda_producto.html')


def buscar_producto(req):
   
 precio = req.GET["precio"]
 print(req.GET)
 productos = Producto.objects.filter(precio__icontains = precio)

 return render(req, 'resultado_busqueda.html', { 'precio': precio, 'productos':productos })



