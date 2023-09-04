from django.shortcuts import render, redirect, get_object_or_404
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
from AppPerfiles.models import Profile 
from AppLogin.models import Avatar
from AppLogin.views import obtenerAvatar
from AppLogin.forms import AvatarForm

# Create your views here.


@login_required
def inicio(request):
    try:
        profile = Profile.objects.get(usuario=request.user)
        avatar = obtenerAvatar(request)
    except Profile.DoesNotExist:
        profile = None
        avatar = "/imagenes/avatars/avatarpordefecto.png"

    context = {
        'profile': profile,
        'avatar': avatar,
    }
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar_obj, created = Avatar.objects.update_or_create(
                usuario=request.user, defaults={"imagen": form.cleaned_data["imagen"]}
            )
            context['mensaje'] = "Avatar agregado correctamente"
            context['avatar'] = avatar_obj.imagen.url
        else:
            context['mensaje'] = "Error al agregar el avatar"
            context['form'] = form
    else:
        context['form'] = AvatarForm()

    return render(request, "AppArtesania/inicio.html", context)



# Mate

class MateList(LoginRequiredMixin, ListView):
    context_object_name = 'mates'
    queryset = Artesania.objects.filter(producto__startswith='mate')
    template_name = 'AppArtesania/mates.html'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class MateDetalle(LoginRequiredMixin, DetailView):
    model = Artesania
    context_object_name = 'mate'
    template_name = 'AppArtesania/mateDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class MateUpdate(LoginRequiredMixin, UpdateView):
    model = Artesania
    form_class = ActualizacionArtesania
    success_url = reverse_lazy('mates')
    context_object_name = 'mate'
    template_name = 'AppArtesania/mateEdicion.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class MateDelete(LoginRequiredMixin, DeleteView):
    model = Artesania
    success_url = reverse_lazy('mates')
    context_object_name = 'mate'
    template_name = 'AppArtesania/matesBorrar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context


# Vidrio

class VidrioList(LoginRequiredMixin, ListView):
    context_object_name = 'vidrios'
    queryset = Artesania.objects.filter(producto__startswith='vidrio')
    template_name = 'AppArtesania/vidrios.html'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class VidrioDetalle(LoginRequiredMixin, DetailView):
    model = Artesania
    context_object_name = 'vidrio'
    template_name = 'AppArtesania/vidrioDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class VidrioUpdate(LoginRequiredMixin, UpdateView):
    model = Artesania
    form_class = ActualizacionArtesania
    success_url = reverse_lazy('vidrios')
    context_object_name = 'vidrio'
    template_name = 'AppArtesania/vidrioEdicion.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class VidrioDelete(LoginRequiredMixin, DeleteView):
    model = Artesania
    success_url = reverse_lazy('vidrios')
    context_object_name = 'vidrio'
    template_name = 'AppArtesania/vidriosBorrar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context


# Joyeria

class JoyeriaList(LoginRequiredMixin, ListView):
    context_object_name = 'joyerias'
    queryset = Artesania.objects.filter(producto__startswith='joyeria')
    template_name = 'AppArtesania/joyerias.html'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class JoyeriaDetalle(LoginRequiredMixin, DetailView):
    model = Artesania
    context_object_name = 'joyeria'
    template_name = 'AppArtesania/joyeriaDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class JoyeriaUpdate(LoginRequiredMixin, UpdateView):
    model = Artesania
    form_class = ActualizacionArtesania
    success_url = reverse_lazy('joyerias')
    context_object_name = 'joyeria'
    template_name = 'AppArtesania/joyeriaEdicion.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class JoyeriaDelete(LoginRequiredMixin, DeleteView):
    model = Artesania
    success_url = reverse_lazy('joyerias')
    context_object_name = 'joyeria'
    template_name = 'AppArtesania/joyeriasBorrar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context


# Pintura

class PinturaList(LoginRequiredMixin, ListView):
    context_object_name = 'pinturas'
    queryset = Artesania.objects.filter(producto__startswith='pintura')
    template_name = 'AppArtesania/pinturas.html'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class PinturaDetalle(LoginRequiredMixin, DetailView):
    model = Artesania
    context_object_name = 'pintura'
    template_name = 'AppArtesania/pinturaDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class PinturaUpdate(LoginRequiredMixin, UpdateView):
    model = Artesania
    form_class = ActualizacionArtesania
    success_url = reverse_lazy('pinturas')
    context_object_name = 'pintura'
    template_name = 'AppArtesania/pinturaEdicion.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class PinturaDelete(LoginRequiredMixin, DeleteView):
    model = Artesania
    success_url = reverse_lazy('pinturas')
    context_object_name = 'pintura'
    template_name = 'AppArtesania/pinturasBorrar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context


# Especial

class EspecialList(LoginRequiredMixin, ListView):
    context_object_name = 'especiales'
    queryset = Artesania.objects.filter(producto__startswith='especial')
    template_name = 'AppArtesania/especiales.html'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class EspecialDetalle(LoginRequiredMixin, DetailView):
    model = Artesania
    context_object_name = 'especial'
    template_name = 'AppArtesania/especialDetalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class EspecialUpdate(LoginRequiredMixin, UpdateView):
    model = Artesania
    form_class = ActualizacionArtesania
    success_url = reverse_lazy('especiales')
    context_object_name = 'especial'
    template_name = 'AppArtesania/especialEdicion.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

class EspecialDelete(LoginRequiredMixin, DeleteView):
    model = Artesania
    success_url = reverse_lazy('especiales')
    context_object_name = 'especial'
    template_name = 'AppArtesania/especialesBorrar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context


# CREACION PRODUCTO

class ArtesaniaCreacion(LoginRequiredMixin, CreateView):
    model = Artesania
    form_class = FormularioNuevaArtesania
    success_url = reverse_lazy('inicio')
    template_name = 'AppArtesania/artesaniaCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtesaniaCreacion, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppArtesania/comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avatar"] = obtenerAvatar(self.request)
        return context

# LISTA DE BLOG


def buscar_artesanias(request):
    titulo = request.GET["titulo"]
    if titulo!="":
        artesanias = Artesania.objects.filter(titulo__icontains=titulo)     
        return render(request, 'AppArtesania/busqueda.html', {'artesanias': artesanias, "avatar":obtenerAvatar(request)})
    else:
       return render(request, 'AppArtesania/busqueda.html', {"mensaje": "No ingresaste información", "avatar":obtenerAvatar(request)})


def busqueda(request):
    return render(request, "AppArtesania/busqueda.html", {"avatar":obtenerAvatar(request)} )

def detalle_artesania(request, artesania_id):
    artesania = get_object_or_404(Artesania, pk=artesania_id)
    return render(request, 'AppArtesania/detalle_artesania.html', {'artesania': artesania, "avatar":obtenerAvatar(request)})