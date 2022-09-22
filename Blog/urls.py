from django.urls import path
from Blog.views import create_tematica, publicaciones, create_publicacion

urlpatterns = [
    path('publicaciones/',publicaciones),
    path('create_publicacion/',create_publicacion),
    path('create_tematica/',create_tematica),
]