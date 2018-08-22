"""Vistas para el LOEU
"""
# Librerias Django
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView


##############################################################################
class Eliminar(SuccessMessageMixin, DeleteView):
    relacion = None
    relacion_id = None

    def __init__(self, *args, **kwargs):
        super(Eliminar, self).__init__(*args, **kwargs)
        # Para almacenar el código activo e inactivo
        self.relacionado = None
        self.object = None

    def get_context_data(self, **kwargs):
        contexto = super(Eliminar, self).get_context_data(**kwargs)
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
