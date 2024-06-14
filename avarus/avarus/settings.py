import os
from pathlib import Path
import json
from django.utils.translation import gettext_lazy as _


def _read_env_str(name: str) -> str:
    return os.getenv(name, '')

def _read_env_bool(name: str) -> bool:
    return bool(os.getenv(name, 'False') == 'True')

def _read_env_list(name: str) -> list:
    return json.loads(os.getenv(name, '[]'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _read_env_str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://avarus.space']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'apps.authors',
    'apps.datasets',
    'apps.map_locations',
    'apps.publications',
    'apps.related_projects',
    'apps.profiles',
    'apps.feedback',
    'apps.statistics',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'avarus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'avarus.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'postgres19001-v2',
        'NAME': _read_env_str('POSTGRES_DB'),
        'PASSWORD': _read_env_str('POSTGRES_PASSWORD'),
        'PORT': '5432',
        'USER': _read_env_str('POSTGRES_USER'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('EN')),
    ('ru', _('RU')),
)

LOCALE_PATHS = (BASE_DIR, 'locale/', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = _read_env_str('EMAIL_HOST_USER')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = _read_env_str('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


FEEDBACK_SEND_EMAIL = _read_env_bool('FEEDBACK_SEND_EMAIL')
FEEDBACK_EMAIL_RECIPIENTS = _read_env_list('FEEDBACK_EMAIL_RECIPIENTS')


DATASET_REQUEST_SEND_EMAIL = _read_env_bool('DATASET_REQUEST_SEND_EMAIL')
DATASET_REQUEST_EMAIL_RECIPIENTS = _read_env_list('DATASET_REQUEST_EMAIL_RECIPIENTS')

SESSION_SAVE_EVERY_REQUEST = True

YANDEX_MAPS_TOKEN = _read_env_str('YANDEX_MAPS_TOKEN')
