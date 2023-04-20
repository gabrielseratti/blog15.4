import os
from pathlib import Path

DEBUG = True

ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = None
SESSION_COOKIE_SECURE = None
CSRF_COOKIE_SECURE = None
