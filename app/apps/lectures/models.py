from django.db import models
from apps.sensors.models import Sensor
from django.conf import settings
from .managers import LectureManager

# Create your models here.
class Measures(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Sensor N°', db_index=True)
    Va = models.FloatField('V L1 - N')
    Vb = models.FloatField('V L2 - N')
    Vc = models.FloatField('V L3 - N')

    Vca = models.FloatField('V L1 - L3')
    Vab = models.FloatField('V L1 - L2')
    Vbc = models.FloatField('V L2 - L3')

    Ia = models.FloatField('I L1')
    Ib = models.FloatField('I L2')
    Ic = models.FloatField('I L3')

    Pa = models.FloatField('P L1')
    Pb = models.FloatField('P L2')
    Pc = models.FloatField('P L3')

    energy = models.FloatField('Consumo')
    FP = models.FloatField('FP')
    Hz = models.FloatField('Hz')

    created = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'
    
    objects = LectureManager()

    def __str__(self):
        return f'{self.sensor}'