"""
Django settings for hoyai project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import platform

#host = os.environ['HOSTNAME']
host = platform.uname()[1]
CELERY_BROKER_URL =  'amqp://admin:mypass@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'db+postgresql://postgres:postgres@localhost'
CELERY_TASK_SERIALIZER = 'json'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#memcache server setting
#apt-get install memcached
#apt-get install python-memcache
#/etc/init.d/memcached start
CACHE_BACKEND = 'memcached://' + host + ':11211/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p8eici$0t2b!$=2xdb41o+bid)5qa^fs6ej-9&h8(n$x1(k^zf'

# Path Root
FILE_PATH = '/home/dev/tensormsaFile/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Celery Flag True = On, False = Off
CELERY_FLAG = False
# Rule init setup True = always setup, False = Once setup
RULE_FLAG = True
# GPU Multi Train or Predict Flag
GPU_FLAG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jenkins',
    'rest_framework',
    'rest_framework_swagger',
    'api.apps.ApiConfig',
    'cluster.apps.ClusterConfig',
    'common.apps.CommonConfig',
    'gui.apps.GuiConfig',
    'master.apps.MasterConfig',
    'chatbot.apps.ChatbotConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'hoyai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hoyai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD' : 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

CELERYD_HIJACK_ROOT_LOGGER = False
""" How to Logging

    log types :
        log level debug -> debug, info, error, critical
        log level info -> info, error, critical
        log level error -> error, critical
        log level critical -> critical
    log file path :
        /root/main_debug.log
    usages :
        import logging
        logging.debug("log leval : {0}".format('debug'))
        logging.info("log leval : {0}".format('info'))
        logging.error("log leval : {0}".format('error'))
        logging.critical("log leval : {0}".format('critical'))
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/root/main.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_false'],
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/root/main_debug.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/root/celery.log',
            'formatter': 'main_formatter',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', 'production_file', 'debug_file','celery'],
            'level': "DEBUG",
            'propagate': True,
        },

    }
}
#CELERYD_HIJACK_ROOT_LOGGER = False

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'ROK'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR , 'gui')
STATIC_URL = '/templates/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "gui/templates"),
]

CORS_ORIGIN_ALLOW_ALL = True

FLOWER_PORT = "5555"

TENSOR_FLOW_LOG_LEVEL = 'WARN' #DEBUG, INFO, WARN, ERROR, or FATAL