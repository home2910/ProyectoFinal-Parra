from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Producto
from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.

@login_required
def inicio(req):

    return render(req, 'inicio.html', {})


class ProductCreateView(LoginRequiredMixin ,CreateView):
  model = Producto
  template_name = 'add_form.html'
  success_url = reverse_lazy('leer-producto')
  fields = ['nombre', 'precio']

   
def busqueda_producto(req):
   return render(req, 'busqueda_producto.html')


def buscar_producto(req):
   
 precio = req.GET["precio"]
 print(req.GET)
 productos = Producto.objects.filter(precio__icontains = precio)

 return render(req, 'resultado_busqueda.html', { 'precio': precio, 'productos':productos })

class ProductsListView(ListView):
  model = Producto
  context_object_name = 'productos'
  template_name= 'leer_productos.html'



class ProductDeleteView(LoginRequiredMixin ,DeleteView):
  model = Producto
  template_name = 'eliminar_producto.html'
  success_url = reverse_lazy('leer-producto')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
  model = Producto
  template_name = 'editar_producto.html'
  success_url = reverse_lazy('leer-producto')
  fields = ['nombre', 'precio']
      

def user_login(req):
  if req.method == 'POST':
    form = AuthenticationForm(req, data=req.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      user = authenticate(username=username, password=password)

      if user is not None:
        auth_login(req, user)
        return render(req, 'inicio.html', {'mensaje': f'Bienvenido {username}'})
      
      else:
        return render(req, 'login.html', {'mensaje': 'Error, datos incorrectos'})
      
    else:
      return render(req, 'login.html' , {'mensaje': 'Error, formulario incorrecto'})
   
  form = AuthenticationForm()
  return render(req, 'login.html', {'form':form})

def register(req):
  if req.method == 'POST':
    
      form = UserRegistrationForm(req.POST)
      if form.is_valid():
        
          username = form.cleaned_data['username']
          form.save()
          return render(req, 'inicio.html', {'mensaje':'Usuario Creado'})
      else:
         return render(req, 'registro.html', {'form': form, 'mensaje': 'Error en el formulario'})

      
  else: 
   form = UserRegistrationForm()

  return render(req,'registro.html', {'form':form})
