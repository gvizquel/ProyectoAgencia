from django.db import models

# Create your models here.

# Librerias de terceros
from ckeditor.fields import RichTextField


class Viajero(models.Model):
    LETRACEDULA_CHOICES = (
        ('V', 'V'),
        ('E', 'E'),
    )
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    letra_cedula_identidad = models.CharField('Letra C.I.', max_length=1,
        choices=LETRACEDULA_CHOICES, default=LETRACEDULA_CHOICES[0][0])
    cedula_identidad = models.IntegerField("Cédula de Identidad", db_index=True)
    direccion = RichTextField()
    telefono = models.CharField("Teléfono Local", max_length=255)
    # viajes = models.ManyToManyField(
    #     'Viaje',
    #     through='Itinerario',
    #     related_name='viajes'
    # )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = ('Viajero')
        verbose_name_plural = ('Viajeros')
        db_table = 'viajero'


class Viaje(models.Model):
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    plaza = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return '%s - %s' % (self.origen, self.destino)

    class Meta:
        verbose_name = ('Viaje')
        verbose_name_plural = ('Viajes')
        db_table = 'viaje'


class Itinerario(models.Model):
    viajero = models.ForeignKey('Viajero', on_delete=models.PROTECT)
    persona = models.ForeignKey('viaje', on_delete=models.PROTECT)
    salida = models.DateField()
    retorno = models.DateField()

    class Meta:
        db_table = 'itinerario'