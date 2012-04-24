from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'popcorn_gallery.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# Playdoh ships with sha512 password hashing by default. Bcrypt+HMAC is safer,
# so it is recommended. Please read <https://github.com/fwenzel/django-sha2#readme>,
# then switch this to bcrypt and pick a secret HMAC key for your application.
PWD_ALGORITHM = 'bcrypt'
HMAC_KEYS = {  # for bcrypt only
    '2011-01-01': 'cheesecake',
}

# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# NOSE_ARGS = ['--failed', '--stop']

# NOSE_PLUGINS = []