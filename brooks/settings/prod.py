import os
from .base import *

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    'michaelbrooks.herokuapp.com',
    'www.kardashevweb.com',
]

STATIC_ROOT = os.path.join(BASE_DIR,'static') 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
