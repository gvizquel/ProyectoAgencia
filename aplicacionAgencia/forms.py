# Librerias Django
from django import forms
from django.utils.safestring import mark_safe
from django.forms import ModelForm

# Librerias en carpetas locales
from .models import Viajero


class ViajeroForm(ModelForm):
    """Clase para actualizar el perfil del usuario en el sistema
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