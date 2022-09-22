from django.shortcuts import render
from Autores.models import Autor
from Blog.models import Post, Tematica
from Blog.forms import form_nuevaPublicacion, form_nuevaTematica

# Create your views here.

def publicaciones(request): 
    
    return render(request, 'publicaciones.html')

def create_publicacion(request):

    if request.method == "POST":
        formulario = form_nuevaPublicacion(request.POST, request.FILES)
        print({formulario.is_valid()})
        print(formulario.errors)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            publicacion = Post(titulo = informacion["titulo"],subtitulo = informacion["subtitulo"], autor = informacion['autor'], imagen = informacion["imagen"], contenido = informacion["contenido"], resumen = informacion["resumen"], tematica = informacion["tematica"])
            publicacion.save()
            print (publicacion.autor.apellido)
            return render(request,'publicaciones.html')
    else:
        formulario = form_nuevaPublicacion()

    autores = Autor.objects.all()
    tematicas = Tematica.objects.all()
    
    return render(request, 'CRUDpublicacion/create_publicacion.html',{'formulario': formulario,'autores':autores, 'tematicas' : tematicas})

def create_tematica(request):

    if request.method == "POST":
        formulario = form_nuevaTematica(request.POST)
        print({formulario.is_valid()})
        print(formulario.errors)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tematica = Tematica(nombre = informacion["nombre"])
            tematica.save()
            return render(request,'publicaciones.html')
    else:
        formulario = form_nuevaTematica()
    return render(request, 'CRUDpublicacion/create_publicacion.html',{'formulario': formulario})
    