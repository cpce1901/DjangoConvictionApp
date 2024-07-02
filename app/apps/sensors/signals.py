from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Sensor

def generate_code(enterprise_name, place, pk):
    words = place.split()
    if len(words) == 1:
        place_code = words[0][:4].upper()
    else:
        place_code = words[0][0].upper() + words[1][:4].upper()
    return f'{enterprise_name[:4].upper()}-{place_code}-{pk}'

# Guarda el codigo del sensor
@receiver(post_save, sender=Sensor)
def review_lecture_for_alert(sender, instance, created, **kwargs):
    if created:
        instance.code = generate_code(
            str(instance.located.enterprise.name),
            str(instance.located.name),
            instance.pk
        )
        instance.save()