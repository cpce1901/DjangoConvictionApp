from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class Enterprise(models.Model):
    name = models.CharField('Nombre', max_length = 255, blank = True, null = True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __rpt__(self) -> str:
        return f"<Enterprise: {self.name}>"
    
    def __str__(self) -> str:
        return f"{self.name}"


class CustomUserManager(UserManager):
    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password,**extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True, blank=True, related_name='user_enterprise')
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nombre', max_length = 255, blank=True)
    last_name = models.CharField('Apellido', max_length = 255, blank=True)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default= False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = ['email']
    REQUIRED_FIELDS = ['name', 'last_name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
    