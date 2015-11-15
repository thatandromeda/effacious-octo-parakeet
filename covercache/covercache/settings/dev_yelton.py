"""
Local development settings for Andromeda Yelton. Feel free to copy/modify
or outright use for local development.

*** not suitable for production ***
"""

import os

from covercache.settings.base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE':     'django.db.backends.postgresql_psycopg2',
        'NAME':     'covercache',
        'HOST':     'localhost',
        'PORT':     '5432',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(funcName)s]: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'logs', 'covercache.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'brief',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}
