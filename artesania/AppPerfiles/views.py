from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
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
from django.shortcuts import get_object_or_404


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'AppPerfiles/perfil.html'
    model = Profile

    def get_object(self, queryset=None):
        try:
            return Profile.objects.get(usuario=self.request.user)
        except Profile.DoesNotExist:
            return None  # Devuelve None en lugar de levantar una excepción

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = obtenerAvatar(self.request)
        return context


class UsuarioEdicion(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'AppPerfiles/edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user.profile
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context


class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppPerfiles/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

def password_exitoso(request):
    return render(request, 'AppPerfiles/passwordExitoso.html', {})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'AppPerfiles/borrarPerfil.html'
    success_url = reverse_lazy('logout')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class CrearPerfil(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'AppPerfiles/crearPerfil.html'
    success_url = reverse_lazy('profile')
   
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context