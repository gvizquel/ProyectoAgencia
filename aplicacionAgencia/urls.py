"""Rutas de nuestra aplicación empresa
"""
# Librerias Django
from django.contrib.auth.decorators import permission_required
from django.urls import include, path
from django.views.generic import ListView

# Librerias de terceros
from aplicacionAgencia.models import *

# from django.views.generic.detail import DetailView


app_name = 'agencia'

urlpatterns = [

    ##########################################################################
    path( # Listar
        'viajero/listar',
        ListView.as_view(
            model=Viajero,
            template_name='viajero_listar.html'
        ),
        name='listar-viajero'),
]
