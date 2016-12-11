import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    'michaelbrooks.herokuapp.com',
    'www.kardashevweb.com',
]

try:
    from .local import *
except ImportError:
    pass
