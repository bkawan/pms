"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ho2n7ik^9+^2*#!#cx3v)mz6xkh4sb*qj3qu0#%w=27c0f5pe6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
LOCAL_APPS = [
    'apps.core',
    'apps.users',
    'apps.company',
    'apps.product',
    'apps.gallery',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    # 'sorl.thumbnail',
    'easy_thumbnails',
]

INSTALLED_APPS = LOCAL_APPS + INSTALLED_APPS + THIRD_PARTY_APPS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS' : [
            os.path.join(BASE_DIR, '..', 'templates'),
        ],
        'APP_DIRS' : True,
        'OPTIONS' : {
            'context_processors' : [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'pmsnew',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : 'localhost'

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME' : 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME' : 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

AUTH_USER_MODEL = 'users.User'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'static'),
]
# by default the is a folder saticfiles  created by django, you can create another folder too manually
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
MEDIA_URL = '/media/'
THUMBNAIL_ALIASES = {
    '' : {
        'product_image_thumb' : {"size" : (64, 64), 'crop' : False, 'quality' : 90},
        '100-100' : {"size" : (100, 100), 'crop' : False, 'quality' : 90},
        '600-400' : {"size" : (600, 500), 'crop' : False, 'quality' : 90},
        '84-84' : {"size" : (84, 84), 'crop' : False, 'quality' : 90},
        'product_list' : {"size" : (256, 180), 'crop' : False, 'quality' : 90},
        'product_image_slider' : {"size" : (600, 400), 'crop' : False, 'quality ' : 90},
        'banner_slider' : {"size" : (1400, 600), 'crop' : False, 'quality ' : 90},

    },
}
