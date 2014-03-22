import os

PROJECT_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = os.getenv("SECRET_KEY", 'booh')
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", '*')

STATIC_URL = '/static/'

ROOT_URLCONF = 'friendlyplaces.urls'

TEMPLATE_DIRS = (PROJECT_PATH,)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'leaflet',
    'friendlyplaces',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, '..', 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
