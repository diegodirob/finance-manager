from main.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'database',
        'PORT': 5432,
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'NAME': 'finance-manager',
    }
}


# Mail

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
