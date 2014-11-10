"""
Django settings for mothra project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# jpb, 8/20/2014 added for heroku db
import dj_database_url

# jpb, 8/19/2014, commented below and added new BASE_DIR per HEROKU instructions
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_PATH=os.path.dirname(os.path.abspath(__file__))

#  Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = <insert secret key here>

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# jpb, 8/30 added TEMPLATE_DIRS
TEMPLATE_DIRS = (
     PROJECT_PATH + '/templates/'
)


# jpb, 8/28, added EMAIL setup
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = os.environ.get('MANDRILL_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MANDRILL_APIKEY')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'no-reply@dataium.com'
# print EMAIL_HOST_USER
# print EMAIL_HOST_PASSWORD

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # jpb, 2014-08-20, added humanize
    'django.contrib.humanize',
    # jpb, 2014-09-30, added bootstapform
    'bootstrapform',
    # third party 
    # jpb, 2014-08-20, added south
    'south',
    # jpb 2014-08-27, added tasteypie
    # 'tastypie',
    # jpb, 2014-09-29 added python-social-auth
    'social.apps.django_app.default',
    # internal
    # jpb, 2014-08-20, added reports
    'reports',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'mothra.urls'

WSGI_APPLICATION = 'mothra.wsgi.application'

# jpb, 9/29/2014, addded LOGIN_REDIRECT_URL

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'mothra',
	'USER': '<user>',
	'PASSWORD': '<password>',
	'HOST': 'localhost',
	'PORT': '3306',
        'STORAGE_ENGINE':'MyISAM',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Static asset configuration for Heroku
 
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR,'static'),
# )

STATICFILES_DIRS = (
   os.path.join(PROJECT_PATH,'static'),
)


# jpb, 8/19/2014
# ADDED for Django/Heroku Support
# Parse database configuration from $DATABASE_URL


if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config()


# Honor the 'X-Forwareded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

# Allow all host headers
    ALLOWED_HOSTS = ['*']

# jpb, end of Django DB Support

TEMPLATE_CONTEXT_PROCESSORS = (
'django.core.context_processors.request',
'django.contrib.auth.context_processors.auth',
)

