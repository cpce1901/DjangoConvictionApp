from django.db import models

class SensorsManager(models.Manager):
    def full(self):
        return self.all()
    

class LocatesManager(models.Manager):
    def full(self):
        return self.all()
    
    def get_by_user(self, user):
        
        return self.filter(enterprise=user.enterprise)
