from distutils.command.upload import upload
from django.db import models
from Autores.models import Autor


# Create your models here.
class Tematica(models.Model):
    nombre=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre

class Post(models.Model):
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=60)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='image/post/')
    contenido = models.TextField()
    resumen = models.CharField(max_length=300)
    tematica = models.ForeignKey(Tematica, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

