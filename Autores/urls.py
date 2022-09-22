import imp
from django.urls import path
from Autores.views import autores, create_autor

urlpatterns = [
    path('autores/',autores),
    path('create_autor/',create_autor)
]