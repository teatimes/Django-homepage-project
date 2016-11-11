import sys
from os.path import dirname, abspath, join, basename, normpath
import os
from socket import gethostname

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9wl5jq=fj+c$q0m1+_v(dexs#wt1wl0uj2yw)^u2p1blkyj^$6'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get('DEBUG') == 'True'
DEBUG = False

# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
PROJECT_DIR = dirname(dirname(dirname(abspath(__file__))))
APPLICATION_DIR = join(PROJECT_DIR, "src")
DATA_DIR = os.environ.get("OPENSHIFT_DATA_DIR", APPLICATION_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

ON_OPENSHIFT = False

if 'OPENSHIFT_REPO_DIR' in os.environ:
	ON_OPENSHIFT = True

ALLOWED_HOSTS = [
	# Originally domainname/url
	"localhost",
	"127.0.0.1"
	]

# For email in contactschema
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@test.no'
EMAIL_HOST_PASSWORD = '25d56704b6dfb898e382cd5c65d17530'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# For django-mailgun
"""
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'ACCESS-KEY'
MAILGUN_SERVER_NAME = 'SERVER-NAME'
"""
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			join(PROJECT_DIR, 'src/templates'),
			join(PROJECT_DIR, 'apps/homepage', 'templates'),
			join(PROJECT_DIR, 'apps/blog', 'templates'),
			join(PROJECT_DIR, 'apps/shared', 'templates'),
		],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if ON_OPENSHIFT:
	DEBUG = False
	#TEMPLATE_DEBUG = False
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': os.environ["OPENSHIFT_APP_NAME"],
			'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
			'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
			'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
			'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
		}
	}

else:
	DEBUG = True
	#TEMPLATE_DEBUG = True
	ALLOWED_HOSTS = [
		"localhost",
		"127.0.0.1"
	]
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': join(PROJECT_DIR, 'db.sqlite3'),
		}
	}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Application definition
PREREQ_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	#'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
]

PROJECT_APPS = [
	'src.apps.blog',
	'src.apps.homepage',
	'pagedown', 
	'markdown_deux',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [
	join(APPLICATION_DIR, "static"),
	join(os.environ.get('OPENSHIFT_REPO_DIR') or '', 'src', 'static'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if ON_OPENSHIFT:
    STATIC_ROOT = join(PROJECT_DIR, 'wsgi', "static")
    # STATIC_URL = '/openshift_static/'

if ON_OPENSHIFT:
    MEDIA_ROOT = join(os.environ.get('OPENSHIFT_DATA_DIR'), 'openshift_media')
else:
    MEDIA_ROOT = join("APPLICATION_DIR", "media")

# http://www.appsembler.com/blog/django-deployment-using-openshift/
# TODO

