from .base import *


DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'productiondb'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
