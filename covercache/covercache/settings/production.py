"""
In future, this will be the production settings file.
"""

from covercache.settings.base import *

"""
Things we will want to set or override:
DEBUG
TEMPLATE_DEBUG
ALLOWED_HOSTS
DATABASES
LOGGING

Storages, probably
Static assets more generally (e.g. file compression, CDN serving, whatevs)
Cache, probably
Email sending, maybe
SSL, maybe
Celery
"""
