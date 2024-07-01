from django.db import models

class LectureManager(models.Manager):
    def full(self):
        return self.all()

   