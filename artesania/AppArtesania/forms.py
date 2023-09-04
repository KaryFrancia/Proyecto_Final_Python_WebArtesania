from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from AppArtesania.models import *


class FormularioNuevaArtesania(forms.ModelForm):
    class Meta:
        model = Artesania
        fields = ('usuario', 'titulo', 'producto', 'modelo', 'descripcion', 'precio', 'imagenProducto')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizacionArtesania(forms.ModelForm):
    class Meta:
        model = Artesania
        fields = ('titulo', 'producto', 'modelo', 'descripcion', 'precio', 'imagenProducto')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }









