# Local imports
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f4jd#_bvborz%*#55c^1k&zb&ev(@!0nqrhhsq3l@@u$^1le!y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed host who can make request
ALLOWED_HOSTS = ['*']


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}