from django import forms

class ProductForm(forms.Form):
    producto = forms.CharField()
    precio = forms.IntegerField()    
