"""
Django settings for OnlineExam project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h!@71twrzjx3ag6z+j8l)_(!^2*v!_ow)idqt-wtre1%o-*=@s'



AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',


    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'oauth2_provider',

    'admin_reorder',

    'import_export',

    'easy_thumbnails',
    'filer',
    'mptt',

    'rest_auth',
    'rest_auth.registration',
    'crispy_forms',

    'ckeditor',
    'ckeditor_uploader',
    'webpack_loader',

    'users',
    'questions',
    'exam_sessions',
]

ADMIN_REORDER = (
    # Keep original label and models
    'sites',

    # Rename app
    {'app': 'auth', 'label': 'Groups'},


    # Reorder app models
    {'app': 'users', 'label': 'Users', 'models': ('users.CustomUser',)},
    {'app': 'oauth2_provider', 'label': 'Oauth2', 'models': ('oauth2_provider.AccessToken',)},

    {'app': 'questions', 'models': ('questions.CourseModel', 'questions.SubjectModel', 'questions.QuestionModel',
                                    'questions.SubjectExamModel', 'questions.CourseExamModel')},

    {'app': 'exam_sessions', 'models': ('exam_sessions.SubjectExamSession', 'exam_sessions.CourseExamSession',
                                         'exam_sessions.FreeExamSession', 'exam_sessions.ExamResults')},

    


)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'core.middleware.CustomModelAdminReorder',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'exam_sessions.middleware.DisableCSRF'
]

ROOT_URLCONF = 'OnlineExam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'OnlineExam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = "bootstrap4"

# django-contrib-sites
SITE_ID = 1

# django-allauth
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = (True)


# django-import-export
IMPORT_EXPORT_USE_TRANSACTIONS = True

# django rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend', 'webpack-stats.json'),
    }
}

# thumbnails
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/'

# SESSION AGE 1 Minutes
# SESSION_EXPIRE_SECONDS = 5*60
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'errors.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }
