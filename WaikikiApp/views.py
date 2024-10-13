from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Avatar
from django.shortcuts import render
from .forms import UserRegistrationForm, UserEditForm, AvatarFormulario
from django.contrib.auth.models import User

# Create your views here.

@login_required
def inicio(req):
    
    avatares = Avatar.objects.filter(user=req.user.id)

    if avatares.exists():
        url = avatares[0].imagen.url  # Obtener la URL del primer avatar
    else:
        url = '/media/default_avatar.png'  # Imagen predeterminada si no hay avatar
    
    print(f'Mostrar url: {url}')

    return render(req, 'inicio.html', {'url':url})


class ProductCreateView(PermissionRequiredMixin, CreateView):
  model = Producto
  template_name = 'add_form.html'
  success_url = reverse_lazy('leer-producto')

  fields = ['nombre', 'precio']
  permission_required = ('WaikikiApp.add_producto', 'WaikikiApp.change_producto', 'WaikikiApp.delete_producto')

   
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



class ProductDeleteView(PermissionRequiredMixin, DeleteView):
  model = Producto
  template_name = 'eliminar_producto.html'
  success_url = reverse_lazy('leer-producto')
  permission_required = ('WaikikiApp.add_producto', 'WaikikiApp.change_producto', 'WaikikiApp.delete_producto')


class ProductUpdateView(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
  model = Producto
  template_name = 'editar_producto.html'
  success_url = reverse_lazy('leer-producto')
  fields = ['nombre', 'precio']
  permission_required = ('WaikikiApp.add_producto', 'WaikikiApp.change_producto', 'WaikikiApp.delete_producto')
      

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
          return render(req, 'login.html')
      else:
         return render(req, 'registro.html', {'form': form, 'mensaje': 'Error en el formulario'})

      
  else: 
   form = UserRegistrationForm()

  return render(req,'registro.html', {'form':form})


def editar_perfil(req):

  usuario = req.user

  if req.method == 'POST':
    miFormulario = UserEditForm(req.POST)
    if miFormulario.is_valid():

      info = miFormulario.cleaned_data

      usuario.email = info['email']
      usuario.password1 = info['password1']
      usuario.password2 = info['password2']
      usuario.save()

      return render(req, 'inicio.html')
    
  else:
    miFormulario = UserEditForm(initial={'email':usuario.email})
  

  return render(req, 'editar_perfil.html', {'miFormulario':miFormulario, "usuario":usuario})


@login_required
def agregar_avatar(req):
 if req.method == 'POST':
   miForm = AvatarFormulario(req.POST, req.FILES)

   if miForm.is_valid():
     
     u = User.objects.get(username = req.user)

     avatar = Avatar (user=u, imagen=miForm.cleaned_data['imagen'])

     avatar.save()

     return render(req, 'inicio.html')
   
 else:
   
    miForm = AvatarFormulario()

    return render(req, 'agregar_avatar.html', {'miForm': miForm})
 

def about_me(req):
   
   return render(req, 'about_me.html')