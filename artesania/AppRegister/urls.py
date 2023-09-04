from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    
    path('accounts/signup/', RegistroPagina.as_view(template_name='AppRegister/registro.html'), name='registro'),
    path('about/', views.about, name='acercaDeMi'),
]