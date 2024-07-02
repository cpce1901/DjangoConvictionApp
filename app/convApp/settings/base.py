import os
from .top_secret import secret
from pathlib import Path

DB_NAME = secret.get("DB_NAME")
DB_USER = secret.get("DB_USER")
DB_PASS = secret.get("DB_PASS")
DB_HOST = secret.get("DB_HOST")
DB_PORT = secret.get("DB_PORT")

MQTT_BROKER = secret.get("MQTT_BROKER")
MQTT_PORT = secret.get("MQTT_PORT")
MQTT_USERNAME = secret.get("MQTT_USERNAME")
MQTT_PASSWORD = secret.get("MQTT_PASSWORD")
MQTT_ID = secret.get("MQTT_ID")

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-3^58wm2iasw(fc_r+zghc=y$+$ird*m^v_t7z3&q3u+6_4_)5o'

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.alerts',
    'apps.graphics',
    'apps.lectures',
    'apps.reports',
    'apps.sensors',
    'apps.users',
]

THIRTY_APPS = [
    'daphne',
    'django_htmx',
]

INSTALLED_APPS = THIRTY_APPS + BASE_APPS + LOCAL_APPS 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # HTMX
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'convApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'convApp.wsgi.application'
ASGI_APPLICATION = 'convApp.asgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
