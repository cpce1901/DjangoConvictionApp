from django.apps import AppConfig


class SensorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sensors'
    verbose_name = "Sensores"

    def ready(self):
        from. import signals