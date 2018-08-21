"""Rutas de nuestra aplicación empresa
"""
# Librerias Django
from django.contrib.auth.decorators import permission_required
from django.urls import include, path
from django.views.generic import TemplateView

# Librerias de terceros
from empresa.views import (
    AgregarEmpresa, DetalleEmpresa, EditarEmpresa, EliminarEmpresa,
    ListarEmpresa, arbol)

# Librerias en carpetas locales
from .routers import router

# from django.views.generic.detail import DetailView


app_name = 'agencia'

urlpatterns = [

    ##########################################################################
    path(
        '',
        (TemplateView.as_view(template_name='empresa.html')),
        name='empresa'),
]
