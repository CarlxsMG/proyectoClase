# Local imports
from .base import *
import os
import django_heroku


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Ax82na2D@sdA2!8454_SAss23@45aWGsa@!lksUO54as2!D95e46AF'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed host who can make request
ALLOWED_HOSTS = ['proyecto-clase-b.herokuapp.com', '*']
CORS_ORIGIN_ALLOW_ALL = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['http://localhost','https://proyecto-clase-f.herokuapp.com/',]
CSRF_COOKIE_SECURE = False


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2va6ls79meckr',
        'USER': 'wawyjjkfglgbvo',
        'PASSWORD': '8cd4a78915d07d832afa5adf6ae1215345a4f491f6a0dff7c70d527c11c5e541',
        'HOST': 'ec2-52-212-228-71.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
django_heroku.settings(locals())
