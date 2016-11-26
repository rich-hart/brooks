import os
from .base import *

ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
]

STATIC_ROOT = os.path.join(BASE_DIR,'static') 

try:
    from .local import *
except ImportError:
    pass
