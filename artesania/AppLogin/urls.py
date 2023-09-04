from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    
    path('accounts/login/', LoginPagina.as_view(template_name='AppLogin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppLogin/logout.html'), name='logout'),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
]