"""Rutas de nuestra aplicación empresa
"""
# Librerias Django
from django.contrib.auth.decorators import permission_required
from django.urls import include, path
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Librerias de terceros
from aplicacionAgencia.models import *
from aplicacionAgencia.views import *
from aplicacionAgencia.forms import *

from .views import *


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
    path(  # Agregar
        'viajero/agregar',
        CreateView.as_view(
            model=Viajero,
            form_class=ViajeroForm,
            template_name='formulario.html',
            success_url=reverse_lazy('agencia:listar-viajero'),
            extra_context={'titulo': 'Viajero'}
        ),
        name='agregar-viajero'),
    path(  # Detalle
        'viajero/detalle/<int:pk>',
        DetailView.as_view(
            model=Viajero,
            template_name='detalle.html',
            extra_context={'titulo': 'Viajero'}
        ),
        name='detalle-viajero'),
    path(  # Agregar
        'viajero/editar/<int:pk>',
        UpdateView.as_view(
            model=Viajero,
            form_class=ViajeroForm,
            template_name='formulario.html',
            success_url=reverse_lazy('agencia:listar-viajero'),
            extra_context={'titulo': 'Viajero'}
        ),
        name='editar-viajero'),
    path(  # Eliminar
        'ieu/tipo-ayuda-economica/eliminar/<int:pk>',
        EliminarModeloSimple.as_view(
            model=Viajero,
            template_name='eliminar.html',
            success_url=reverse_lazy('agencia:listar-viajero'),
            relacion=Itinerario,
            relacion_id='viajero',
            success_message='¡El viajero se eliminó de manera exitosa!',
            extra_context={'titulo': 'Viajero'}
        ),
        name='eliminar-viajero'),
]
