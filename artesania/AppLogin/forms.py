from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from AppArtesania.models import *

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")