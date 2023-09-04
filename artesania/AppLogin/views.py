from typing import Self
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView

# Create your views here.
class LoginPagina(LoginView):
    template_name = 'AppLogin/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')

def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user= request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/imagenes/avatars/avatarpordefecto.png"


def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppArtesania/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppLogin/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppLogin/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar": obtenerAvatar(request)})
    
