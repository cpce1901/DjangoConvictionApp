# Generated by Django 5.0.6 on 2024-07-01 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0005_alter_located_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='slug',
        ),
    ]