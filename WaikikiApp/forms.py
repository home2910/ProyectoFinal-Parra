from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Avatar

class ProductForm(forms.Form):
    producto = forms.CharField()
    precio = forms.IntegerField()    

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'last_name', 'first_name']
        help_texts = {k:''for k in fields}


class UserEditForm(UserCreationForm):

    
    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Modificar Contraseña')
    password2 = forms.CharField(label='Repetir Contraseña')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']