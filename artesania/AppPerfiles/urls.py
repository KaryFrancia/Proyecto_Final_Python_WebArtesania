from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('accounts/profile/', ProfileDetailView.as_view(), name='profile'),
    path('crearPerfil/', CrearPerfil.as_view(), name='crear_perfil'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('borrarPerfil/<int:pk>/', UsuarioDelete.as_view(), name='borrar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
]
