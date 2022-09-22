from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fotoPerfil = models.ImageField(upload_to='image/porfil/')
    sobreMi = models.TextField()


