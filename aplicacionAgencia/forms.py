"""Formularios para la agencia de viajes
"""
# Librerias Django
from django import forms
from django.utils.safestring import mark_safe
from django.forms import ModelForm

# Librerias en carpetas locales
from .models import *


class ViajeroForm(ModelForm):
    """Formulario para la gestión de los viajeros
    """
    class Meta:
        model = Viajero
        fields = (
            'nombre',
            'apellido',
            'letra_cedula_identidad',
            'cedula_identidad',
            'telefono',
        )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'letra_cedula_identidad': forms.Select(attrs={'class': 'form-control'}),
            'cedula_identidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': mark_safe("'mask': ['+58 (999) 999-99-99']"), ' data-mask': True}),
        }


class ViajeForm(ModelForm):
    """Formularios para la gestión de los viajes
    """
    class Meta:
        model = Viaje
        fields = (
            'origen',
            'destino',
            'plaza',
            'precio',
        )
        widgets = {
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'plaza': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ItinerarioForm(ModelForm):
    """Formulario para la gestion de los itinerarios de viajes sería
    conveniente agregar las fechas del itenerario para asi poder tener un
    mejor mayor control
    """
    class Meta:
        model = Itinerario
        fields = (
            'viajero',
            'viaje',
            # 'salida',
            # 'retorno',
        )
        widgets = {
            'viajero': forms.Select(attrs={'class': 'form-control'}),
            'viaje': forms.Select(attrs={'class': 'form-control'}),
            # 'salida': forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': mark_safe("'alias': 'dd/mm/yyyy'"), ' data-mask': True}),
            # 'retorno': forms.TextInput(attrs={'class': 'form-control', 'data-inputmask': mark_safe("'alias': 'dd/mm/yyyy'"), ' data-mask': True}),
        }
