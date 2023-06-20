from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.getenv("DB_NAME")),
        'USER': str(os.getenv("DB_USER")),
        'PASSWORD': str(os.getenv("DB_PASS")),
        'HOST': str(os.getenv("DB_HOST")),
        'PORT': str(os.getenv("DB_PORT")),
    }
}

MEDIA_ROOT = str(os.getenv("MEDIA_ROOT"))
MEDIA_URL = str(os.getenv("MEDIA_URL"))

STATIC_ROOT = str(os.getenv("STATIC_ROOT"))
STATIC_URL = str(os.getenv("STATIC_URL"))

# CSRF_TRUSTED_ORIGINS = [str(os.getenv("TRUST1")), ] # for https session auth
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
