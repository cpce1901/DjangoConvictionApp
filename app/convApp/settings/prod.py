from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static/"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_local/"