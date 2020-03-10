from .base import *

ALLOWED_HOSTS = ['localhost']


DEBUG = True

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'foodbook_dev',
      'USER': 'postgres',
      'HOST': 'localhost',
    },
}
