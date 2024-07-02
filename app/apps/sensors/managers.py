from django.db import models

class SensorsManager(models.Manager):
    def full(self):
        return self.all()
    
    def get_by_locate(self, slug_located):
        return self.filter(located__slug=slug_located)
    
    def get_by_code(self, code):
        return self.get(code=code)
    

class LocatesManager(models.Manager):
       
    def get_by_user(self, user):
        return self.filter(enterprise=user.enterprise)
    
    def get_by_slug(self, slug):
        return self.get(slug=slug).name

    