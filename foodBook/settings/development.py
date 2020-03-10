from .base import *

ALLOWED_HOSTS = ['localhost']


DEBUG = True

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'foodbook_development',
      'USER': 'postgres',
      'HOST': 'localhost',
    },
}
