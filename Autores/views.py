from django.shortcuts import render
from Autores.forms import form_nuevoAutor
from Autores.models import Autor

# Create your views here.

def autores(request):
    return render(request,'autores.html')

def create_autor(request):

    if request.method == "POST":
        formulario = form_nuevoAutor(request.POST, request.FILES)
        print({formulario.is_valid()})
        print(formulario.errors)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            autor = Autor(nombre = informacion["nombre"],apellido = informacion["apellido"], fotoPerfil = informacion["fotoPerfil"], sobreMi = informacion["sobreMi"])
            autor.save()
            return render(request,'autores.html')
    
    formulario = form_nuevoAutor()
    return render(request, 'create_autor.html',{'formulario': formulario})
