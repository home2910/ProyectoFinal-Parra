from django.http import HttpResponse
from .models import Producto
from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

def inicio(req):

    return render(req, 'inicio.html', {})


def add_form(req):

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
      return render(req, 'add_form.html', { 'mi_form':mi_form })
   
def busqueda_producto(req):
   return render(req, 'busqueda_producto.html')


def buscar_producto(req):
   
 precio = req.GET["precio"]
 print(req.GET)
 productos = Producto.objects.filter(precio__icontains = precio)

 return render(req, 'resultado_busqueda.html', { 'precio': precio, 'productos':productos })

def read_product(req):
  productos = Producto.objects.all()

  return render(req, 'leer_productos.html', {'productos':productos})

def borrar_producto(req, producto_nombre):
   producto = Producto.objects.get(nombre=producto_nombre)
   producto.delete()
   
   productos = Producto.objects.all()

   return render(req, 'leer_productos.html' , {'productos':productos})

def edit_products(req, producto_nombre):
  
  producto = Producto.objects.get(nombre=producto_nombre)

  if req.method == 'POST':
    product_form = ProductForm(req.POST)

    if product_form.is_valid():

      info = product_form.cleaned_data

      producto.nombre = info['producto']
      producto.precio = info['precio']
      
      producto.save()

      return render(req, 'inicio.html')
  else:
    product_form = ProductForm(initial={'producto': producto.nombre, 'precio':producto.precio})


    return render(req, 'editar_producto.html', {'product_form':product_form, 'producto_nombre':producto_nombre})
      
