from .base import *

ALLOWED_HOSTS = ['localhost']

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'foodbook_test',
      'USER': 'postgres',
      'HOST': 'localhost',
    },
}
