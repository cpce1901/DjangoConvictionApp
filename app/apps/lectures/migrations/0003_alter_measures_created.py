# Generated by Django 5.0.6 on 2024-07-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measures',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
