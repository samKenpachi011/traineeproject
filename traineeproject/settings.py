import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^aihy%i@7@tlj=e&je8q79#e*xyh!uk%-ysbf1xpm#fwg8sdo+'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

APP_NAME = 'traineeproject'
SITE_ID = 40
REVIEWER_SITE_ID = 1

ETC_DIR= os.path.join('/etc/', APP_NAME)

# KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'trainee-project.bhp.org.bw:8000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'django_crypto_fields.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_base.apps.AppConfig', 
    'edc_locator.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_calendar.apps.AppConfig',
    'traineeproject_visit_schedule.apps.AppConfig',
    'traineeproject_prn.apps.AppConfig',
    'traineeproject.apps.EdcProtocolAppConfig',
    'traineeproject.apps.EdcLabelAppConfig',
    'traineeproject.apps.EdcLabAppConfig',
    'traineeproject.apps.EdcDataManagerAppConfig',
    'traineeproject.apps.EdcAppointmentAppConfig',
    'traineeproject.apps.EdcMetadataAppConfig',
    'traineeproject.apps.EdcVisitTrackingAppConfig',
    'traineeproject.apps.EdcTimepointAppConfig',
    'traineeproject.apps.EdcFacilityAppConfig',
    'traineeproject.apps.AppConfig',
    'traineeproject_dashboard.apps.AppConfig',
    'traineeproject_validation.apps.AppConfig',
    'traineeproject_subject.apps.AppConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware', 
    'edc_lab_dashboard.middleware.DashboardMiddleware',

]

ROOT_URLCONF = 'traineeproject.urls'

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

WSGI_APPLICATION = 'traineeproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'traineeproject', 'static')

# dashboards
DASHBOARD_URL_NAMES = {
    'screening_listboard_url': 'traineeproject_dashboard:screening_listboard_url',
    'subject_listboard_url': 'traineeproject_dashboard:subject_listboard_url',
    'subject_dashboard_url': 'traineeproject_dashboard:subject_dashboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',

}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'traineeproject/base.html',
    'dashboard_base_template': 'traineeproject/base.html',
    'subject_dashboard_template': 'traineeproject_dashboard/subject/dashboard.html',
    'screening_listboard_template': 'traineeproject_dashboard/screening/listboard.html',
    'subject_listboard_template': 'traineeproject_dashboard/subject/listboard.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',

}

# Parent reference

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''