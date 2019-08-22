from mysite.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['52.78.203.155']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}