# Generated by Django 5.0.6 on 2024-07-01 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lectures', '0001_initial'),
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measures',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor', verbose_name='Sensor N°'),
        ),
    ]
