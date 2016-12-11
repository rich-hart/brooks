import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    'michaelbrooks.herokuapp.com',
    'www.kardashevweb.com',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


try:
    from .local import *
except ImportError:
    pass
