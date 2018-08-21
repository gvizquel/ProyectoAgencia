"""Entorno, filtros, pruebas y evaluaciones para jinja2
"""

# Librerias Standard
import locale

# Librerias Django
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

# Librerias de terceros
import jinja2

#Para ver la fecha y hora en español :-)
locale.setlocale(locale.LC_TIME, '')


def environment(**options):
    env = jinja2.Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_messages': messages.get_messages,
    })
    return env

def is_in_user_group(grupo, usuario):
    """Este test valida sin un usuario es miembro de un determinado grupo de
    usuarios.
    """
    return usuario.groups.filter(name=grupo).exists()
jinja2.tests.TESTS['in_user_group'] = is_in_user_group
