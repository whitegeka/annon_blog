import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*',]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_PATH_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'files')

if not os.path.isdir(STATIC_PATH_ROOT):
    os.mkdir(STATIC_PATH_ROOT, 0o776)

STATIC_ROOT = os.path.join(STATIC_PATH_ROOT, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
