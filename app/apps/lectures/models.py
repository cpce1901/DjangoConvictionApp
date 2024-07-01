from django.db import models
from apps.sensors.models import Sensor
from django.conf import settings
from .managers import LectureManager

# Create your models here.
class Measures(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Sensor N°', db_index=True)
    v1 = models.FloatField('V L1 - N')
    v2 = models.FloatField('V L2 - N')
    v3 = models.FloatField('V L3 - N')

    v13 = models.FloatField('V L1 - L3')
    v12 = models.FloatField('V L1 - L2')
    v23 = models.FloatField('V L2 - L3')

    i1 = models.FloatField('I L1')
    i2 = models.FloatField('I L2')
    i3 = models.FloatField('I L3')

    p1 = models.FloatField('P L1')
    p2 = models.FloatField('P L2')
    p3 = models.FloatField('P L3')

    energy = models.FloatField('Consumo')
    fp = models.FloatField('FP')
    hz = models.FloatField('Hz')

    created = models.DateTimeField('Fecha de creación', auto_now_add= not settings.DEBUG)

    class Meta:
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'
    
    objects = LectureManager()

    def __str__(self):
        return f'{self.sensor}'