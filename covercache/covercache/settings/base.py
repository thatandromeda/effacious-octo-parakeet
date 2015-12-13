"""
Common (default) Django settings for covercache project.

This file is not intended to be used as-is. You should make a settings
file for your own environment, import * from here, and override as needed.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# ------------------------------------------------------------------------------
# ------------------------> core django configurations <------------------------
# ------------------------------------------------------------------------------

# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

COVERCACHE_APPS = (
    'covercache',
)

THIRD_PARTY_APPS = (
    'sorl.thumbnail',
)

INSTALLED_APPS = DJANGO_APPS + COVERCACHE_APPS + THIRD_PARTY_APPS



# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)



# DEBUG
# ------------------------------------------------------------------------------

# SECURITY WARNING: don't run with debug = True in production!
DEBUG = True



# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------

# (None)


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# Override this with real config in server and personal settings files.
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# MISC CONFIGURATION
# ------------------------------------------------------------------------------

WSGI_APPLICATION = 'covercache.wsgi.application'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', None)

# Set this in child settings files or Django will not run. For servers,
# this should contain ONLY the server hostname and, if necessary, other
# servers that must post to it for core functionality to work
# (looking at you, Paypal). For local development, '*' is an acceptable
# value.
ALLOWED_HOSTS = []


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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



# INTERNATIONALIZATION CONFIGURATION
# ------------------------------------------------------------------------------

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'



# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# (None: we don't have user-uploaded media.)



# URL CONFIGURATION
# ------------------------------------------------------------------------------

ROOT_URLCONF = 'covercache.urls'



# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------



# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------



# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------



# STORAGES CONFIGURATION
# ------------------------------------------------------------------------------



# CACHE CONFIGURATION
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# -----------------> third-party and covercache configurations <----------------
# ------------------------------------------------------------------------------

# Default size is the image size that will be returned if no other size
# is specified. It is a string of {width}x{height}.
THUMBNAIL_DEFAULT_SIZE = '100x100'

COVERCACHE_AUTH = {
    'SYNDETICS': {
        'CLIENT_CODE': os.environ.get('COVERCACHE_SYNDETICS_CLIENT_CODE', None)
    }
}
