# Local imports
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Ax82na2D@sdA2!8454_SAss23@45aWGsa@!lksUO54as2!D95e46AF'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed host who can make request
ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project_db',
        'USER': 'the_project',
        'PASSWORD': 'project01',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}