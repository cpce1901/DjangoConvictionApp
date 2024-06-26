# Generated by Django 5.0.6 on 2024-07-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v1', models.FloatField(verbose_name='V L1 - N')),
                ('v2', models.FloatField(verbose_name='V L2 - N')),
                ('v3', models.FloatField(verbose_name='V L3 - N')),
                ('v13', models.FloatField(verbose_name='V L1 - L3')),
                ('v12', models.FloatField(verbose_name='V L1 - L2')),
                ('v23', models.FloatField(verbose_name='V L2 - L3')),
                ('i1', models.FloatField(verbose_name='I L1')),
                ('i2', models.FloatField(verbose_name='I L2')),
                ('i3', models.FloatField(verbose_name='I L3')),
                ('p1', models.FloatField(verbose_name='P L1')),
                ('p2', models.FloatField(verbose_name='P L2')),
                ('p3', models.FloatField(verbose_name='P L3')),
                ('energy', models.FloatField(verbose_name='Consumo')),
                ('fp', models.FloatField(verbose_name='FP')),
                ('hz', models.FloatField(verbose_name='Hz')),
                ('created', models.DateTimeField(verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Medida',
                'verbose_name_plural': 'Medidas',
            },
        ),
    ]
