from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    email=models.EmailField()
    website = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.nombre