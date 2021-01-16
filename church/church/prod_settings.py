from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nehr^!9q5+&-u-r_-znx5s!(ct#y!83%$h6x84p5d1ch=4ath)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "178.62.195.87"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'church',
        'USER': 'db_user',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
