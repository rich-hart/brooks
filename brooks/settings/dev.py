from .base import *
ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    'michaelbrooks.herokuapp.com',
]

try:
    from .local import *
except ImportError:
    pass

