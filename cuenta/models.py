# -*- coding: utf-8
"""
Modelo de datos de la app globales
"""
# Librerias Future
from __future__ import unicode_literals

# Librerias Standard
import os

# Librerias Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Librerias en carpetas locales
from .libSobreEscribirImagen import SobreEscribirAvatar


def image_path(instance, filename):
    return os.path.join('avatar', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])


class Persona(AbstractUser):
    SEXO_CHOICES = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )
    LETRACEDULA_CHOICES = (
        ('V', 'V'),
        ('E', 'E'),
    )
    password = models.CharField("Clave", max_length=128)
    last_login = models.DateTimeField("Último inicio de sesión:", default=timezone.now)
    is_superuser = models.BooleanField("Super Administrador", default=False, db_index=True)
    is_staff = models.BooleanField("Mantenimiento", default=False, db_index=True)
    is_active = models.BooleanField("Activo", default=False)
    username = models.CharField("Nombre de usuario", max_length=150, db_index=True, unique=True)
    first_name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)
    email = models.CharField("Correo Electrónico", max_length=254, null=False, db_index=True, unique=True)
    email_secundario = models.CharField("Correo Secundario", max_length=254, null=True, blank=True, db_index=True, unique=True)
    letra_cedula_identidad = models.CharField('Letra C.I.', max_length=1, choices=LETRACEDULA_CHOICES, default=LETRACEDULA_CHOICES[0][0], blank=True, null=True)
    cedula_identidad = models.IntegerField("Cédula de Identidad", blank=True, null=True, db_index=True)
    otros_nombres = models.CharField("Otros Nombres", max_length=90, null=True, blank=True)
    otros_apellidos = models.CharField("Otros Apellidos", max_length=255, null=True, blank=True)
    telefono = models.CharField("Teléfono Local", max_length=255, blank=True, null=True)
    celular = models.CharField("Teléfono Celular", max_length=255, blank=True, null=True)
    facebook = models.CharField("FaceBook", max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField("Fecha de Nacimiento", blank=True, null=True)
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICES, blank=True, null=True)
    avatar = models.ImageField(max_length=255, storage=SobreEscribirAvatar(), upload_to=image_path, blank=True, null=True, default='avatar/default_avatar.png')
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = ('Persona')
        verbose_name_plural = ('Personas')
        db_table = 'auth_user'
