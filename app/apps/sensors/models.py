from typing import Iterable
from django.db import models
from django.utils.text import slugify
from apps.users.models import Enterprise
from .managers import SensorsManager, LocatesManager

class Tag(models.Model):
    name = models.CharField("Nombre de marca", max_length=50, unique=True)
    created = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return f"{self.name}"


class Device(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="Marca", related_name="device_tag")
    code = models.CharField("Modelo", max_length=50, unique=True)
    description = models.CharField("Descripción", max_length=255)
    image = models.ImageField("Imagen de equipo",unique=True,upload_to="media/device")
    created = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return f"{self.tag} - {self.code}"

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"


class Located(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True,related_name='located_enterprise')
    name = models.CharField("Lugar de instalación", max_length=50)
    image = models.ImageField("Imagen de lugar", unique=True, upload_to="media/located", blank=True)
    created = models.DateTimeField("Fecha de creación", auto_now_add=True)
    slug = models.SlugField(editable=False, unique=True, max_length=255)

    class Meta:
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"

    objects = LocatesManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.enterprise.name}_{self.name}' )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.enterprise} - {self.name}"  


class Sensor(models.Model):
    code = models.CharField("Codigo", max_length=32, unique=True, blank=True, db_index=True)
    topic = models.CharField("Topico", max_length=64, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Equipo", related_name="sensor_device")
    located = models.ForeignKey(Located, on_delete=models.CASCADE,verbose_name="Ubicación",related_name="sensor_located")
    detail = models.CharField("Detalle", max_length=256, blank=True)
    created = models.DateTimeField("Fecha de creación", auto_now_add=True)


    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"

    objects = SensorsManager()


    def __str__(self):
        return f"{self.code}"


