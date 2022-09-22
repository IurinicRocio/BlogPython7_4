from django import forms
from Autores.models import Autor

# from Blog.models import Post

class form_nuevoAutor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=60)
    fotoPerfil = forms.ImageField()
    sobreMi = forms.CharField(max_length=300)