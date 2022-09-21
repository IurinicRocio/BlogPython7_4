from django.db import models
from Autores.models import Autor

# Create your models here.

class Post(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=60)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    imagen = models.ImageField()
    contenido = models.TextField()
    resumen = models.CharField(max_length=300)

class Tematica(models.Model):
    nombre=models.CharField(max_length=40)
