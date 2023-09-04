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
from AppLogin.models import Avatar
from AppLogin.views import obtenerAvatar
from AppLogin.forms import AvatarForm

# Create your views here.
class RegistroPagina(FormView):
    template_name = 'AppRegister/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(RegistroPagina, self).get(*args, **kwargs)
 
    

def about(request):
    return render(request, 'AppRegister/acercaDeMi.html', {"avatar":obtenerAvatar(request) })
 