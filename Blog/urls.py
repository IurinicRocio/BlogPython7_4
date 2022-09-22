from django.urls import path
from Blog.views import buscar_publicacion, create_tematica, publicaciones, create_publicacion

urlpatterns = [
    path('publicaciones/',publicaciones),
    path('create_publicacion/',create_publicacion),
    path('create_tematica/',create_tematica),
    path('buscar_publicacion/<tematica_nombre>',buscar_publicacion)
]