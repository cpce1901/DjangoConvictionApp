# Generated by Django 5.0.6 on 2024-07-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0006_remove_sensor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='topic',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Topico'),
        ),
    ]
