from .base import *

DEBUG = False

ALLOWED_HOSTS = ['167.71.181.254', 'localhost']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DB_NAME,  
        "USER": DB_USER,  
        "PASSWORD": DB_PASS,  
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

STATIC_URL = "static/"
STATIC_ROOT = [BASE_DIR / "static/"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_local/"