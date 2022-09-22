from django import forms

from Blog.models import Tematica
from Autores.models import Autor

# from Blog.models import Post

class form_nuevaPublicacion(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=60)
    autor= forms.ModelChoiceField(queryset=Autor.objects.all())
    imagen = forms.ImageField()
    contenido = forms.CharField(max_length=2000)
    resumen = forms.CharField(max_length=300)
    tematica = forms.ModelChoiceField(queryset=Tematica.objects.all())

class form_nuevaTematica(forms.Form):
    nombre = forms.CharField(max_length=40)

