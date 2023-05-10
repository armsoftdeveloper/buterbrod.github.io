from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
import geoip2.database

BASE_DIR = Path(__file__).resolve().parent.parent

from django.shortcuts import HttpResponse


#--------------------------------------------- Secret Key Dont Give Anyone ---------------------------------------------#

SECRET_KEY = 'WORK GREAT BUT I DONT GIVE KEY ANYONE'

#--------------------------------------------- Debug For Host/Localhost ---------------------------------------------#

DEBUG = True

#--------------------------------------------- Work With Gmail ---------------------------------------------#

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'WORK GREAT BUT I DONT GIVE KEY ANYONE'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#--------------------------------------------- Python Django App Host ---------------------------------------------#

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS = [
    'django_translation_flags',
    'modeltranslation',
    'jazzmin',
    'captcha',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'phonenumber_field',
]
    
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

#--------------------------------------------- Admin And Django Default Settings ---------------------------------------------#


LANGUAGE_CODE = 'hy'

TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True

USE_TZ = True

#--------------------------------------------- Work With i18n ---------------------------------------------#

gettext = lambda s: s

LANGUAGES = (
    ('hy', gettext('Armenian')),
    ('en', gettext('English')),
    ('ru', gettext('Russia')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)
#--------------------------------------------- Static And Media Urls/Roots ---------------------------------------------#

STATIC_URL = 'static/'
STATIC_ROOT = 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#--------------------------------------------- Work With Cache ---------------------------------------------#

CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR,'core_cache'),
    }
}

#--------------------------------------------- Work With ReCaptcha ---------------------------------------------#

RECAPTCHA_PUBLIC_KEY = 'WORK GREAT BUT I DONT GIVE KEY ANYONE'
RECAPTCHA_PRIVATE_KEY = 'WORK GREAT BUT I DONT GIVE KEY ANYONE'
RECAPTCHA_REQUIRED_SCORE = 0.85

#--------------------------------------------- Work With CKEDITOR ---------------------------------------------#

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
            'height': '100%',
            'width': '100%',
        'toolbar_Custom': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Youtube','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['CodeSnippet']},
            {'name': 'about', 'items': ['About']},
            '/',
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'Custom', 
        'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 400,
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
        ]),
    }
}

#--------------------------------------------- Custom Security  ---------------------------------------------#

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#--------------------------------------------- Block Countries ---------------------------------------------#

def get_country_by_ip(ip_address):
    reader = geoip2.database.Reader('geoip/GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip_address)
        return response.country.iso_code
    except geoip2.errors.AddressNotFoundError:
        return None


def block_turkey_middleware(get_response):
    def middleware(request):
        ip_address = request.META.get('REMOTE_ADDR')
        country_code = get_country_by_ip(ip_address)

        if country_code == 'TR':
            return HttpResponse("Access denied.")
        
        if country_code == 'AZ':
            return HttpResponse("Access denied.")

        return get_response(request)

    return middleware
