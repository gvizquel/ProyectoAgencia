"""Rutas de nuestra aplicación empresa
"""
# Librerias Django
from django.contrib.auth.decorators import permission_required
from django.urls import include, path
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.forms.models import model_to_dict

# Librerias de terceros
from aplicacionAgencia.models import *
from aplicacionAgencia.views import *
from aplicacionAgencia.forms import *

from .views import *


app_name = 'agencia'

urlpatterns = [

##############################################################################
    path( # Listar
        'viajero/listar',
        ListView.as_view(
            model=Viajero,
            template_name='viajero_listar.html'
        ),
        name='listar-viajero'),
    path(  # Detalle
        'viajero/detalle/<int:pk>',
        DetailView.as_view(
            model=Viajero,
            template_name='detalle.html',
            extra_context={'titulo': 'Viajero'}
        ),
        name='detalle-viajero'),
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
        'viajero/eliminar/<int:pk>',
        Eliminar.as_view(
            model=Viajero,
            template_name='eliminar.html',
            success_url=reverse_lazy('agencia:listar-viajero'),
            relacion=Itinerario,
            relacion_id='viajero',
            success_message='¡El viajero se eliminó de manera exitosa!',
            extra_context={'titulo': 'Viajero'}
        ),
        name='eliminar-viajero'),
##############################################################################
    path( # Listar
        'viaje/listar',
        ListView.as_view(
            model=Viaje,
            template_name='viaje_listar.html'
        ),
        name='listar-viaje'),
    path(  # Detalle
        'viaje/detalle/<int:pk>',
        DetailView.as_view(
            model=Viaje,
            template_name='detalle.html',
            extra_context={'titulo': 'Viaje'}
        ),
        name='detalle-viaje'),
    path(  # Agregar
        'viaje/agregar',
        CreateView.as_view(
            model=Viaje,
            form_class=ViajeForm,
            template_name='formulario.html',
            success_url=reverse_lazy('agencia:listar-viaje'),
            extra_context={'titulo': 'Viaje'}
        ),
        name='agregar-viaje'),
    path(  # Agregar
        'viaje/editar/<int:pk>',
        UpdateView.as_view(
            model=Viaje,
            form_class=ViajeForm,
            template_name='formulario.html',
            success_url=reverse_lazy('agencia:listar-viaje'),
            extra_context={'titulo': 'Viaje'}
        ),
        name='editar-viaje'),
    path(  # Eliminar
        'viaje/eliminar/<int:pk>',
        Eliminar.as_view(
            model=Viaje,
            template_name='eliminar.html',
            success_url=reverse_lazy('agencia:listar-viaje'),
            relacion=Itinerario,
            relacion_id='viaje',
            success_message='¡El viaje se eliminó de manera exitosa!',
            extra_context={'titulo': 'Viaje'}
        ),
        name='eliminar-viaje'),
##############################################################################
    path( # Listar
        'itinerario/listar',
        ListView.as_view(
            model=Itinerario,
            template_name='itinerario_listar.html'
        ),
        name='listar-itinerario'),
    path(  # Detalle
        'itinerario/detalle/<int:pk>',
        DetailView.as_view(
            model=Itinerario,
            template_name='detalle.html',
            extra_context={'titulo': 'Itinerario'}
        ),
        name='detalle-itinerario'),
    path(  # Agregar
        'itinerario/agregar',
        CreateView.as_view(
            model=Itinerario,
            form_class=ItinerarioForm,
            template_name='formulario.html',
            success_url=reverse_lazy('agencia:listar-itinerario'),
            extra_context={'titulo': 'Itinerario'}
        ),
        name='agregar-itinerario'),
    path(  # Agregar
        'itinerario/editar/<int:pk>',
        UpdateView.as_view(
            model=Itinerario,
            form_class=ItinerarioForm,
            template_name='formulario.html',
            success_url=reverse_lazy('agencia:listar-itinerario'),
            extra_context={'titulo': 'Itinerario'}
        ),
        name='editar-itinerario'),
    path(  # Eliminar
        'itinerario/eliminar/<int:pk>',
        Eliminar.as_view(
            model=Itinerario,
            template_name='eliminar.html',
            success_url=reverse_lazy('agencia:listar-itinerario'),
            relacion_id='itinerario',
            success_message='¡El itinerario se eliminó de manera exitosa!',
            extra_context={'titulo': 'Itinerario'}
        ),
        name='eliminar-itinerario'),
]
