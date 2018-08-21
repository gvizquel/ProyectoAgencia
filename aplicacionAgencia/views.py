"""Vistas para el LOEU
"""
# Librerias Django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView





##############################################################################
class EliminarModeloSimple(SuccessMessageMixin, DeleteView):
    """Esta clase sirve para eliminar todos los modelos que son auxiliares a
    otros modelos, por ejemplo: TipoAyudaEconomica, TipoActividadCUltural,
    TipoCarrera, etc. Para ver su funcionamiento dirijase a las URL's.
    Siempre y cuando no tengo objetos dependientes.
    """

    relacion = None
    relacion_id = None

    def __init__(self, *args, **kwargs):
        super(EliminarModeloSimple, self).__init__(*args, **kwargs)
        # Para almacenar el código activo e inactivo
        self.relacionado = None
        self.object = None

    def get_context_data(self, **kwargs):
        contexto = super(EliminarModeloSimple, self).get_context_data(**kwargs)
        if self.relacion and self.relacion_id:

            filtro = {self.relacion_id: self.kwargs['pk']}
            self.relacionado = self.relacion.objects.filter(**filtro).exists()

        contexto['relacionado'] = self.relacionado

        return contexto

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.get_context_data(**kwargs)

        if not self.relacionado:
            messages.success(self.request, self.success_message)

            return self.delete(request, *args, **kwargs)

        return HttpResponseRedirect(self.get_success_url())
