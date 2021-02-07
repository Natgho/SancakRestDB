"""
Django settings for sancakRest project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import environ
import django_heroku
import dj_database_url

env = environ.Env()
environ.Env.read_env()
# if server cannot find .env file
# env.read_env(env.str('ENV_PATH', '/path/to/.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'admin_reorder',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sancakRestDB.apps.SancakrestdbConfig',
    'rest_framework',
]

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Sancak Chopper Club Admin",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Sancak Chopper MK",

    # # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # "site_logo": "books/img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Hosgeldin Sancak Beyi",

    # Copyright on the footer
    "copyright": "Sancak Chopper MK",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Facebook", "url": "https://www.facebook.com/bursachopper/", "new_window": True},
        {"name": "Instagram", "url": "https://www.instagram.com/sancakchopperbursa/", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Facebook", "url": "https://www.facebook.com/bursachopper/", "new_window": True},
        {"name": "Instagram", "url": "https://www.instagram.com/sancakchopperbursa/", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": ["Meclis", "Stok", "Meclis.konu"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "books": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": True,
}
JAZZMIN_UI_TWEAKS = {
    "theme": "slate",
    "dark_mode_theme": "slate",
    "accent": "accent-lime",
    "brand_colour": "navbar-danger",
    "navbar_small_text": True,
    "navbar": "navbar-dark",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "sidebar_nav_flat_style": True,
}

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sancakRest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'sancakRest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }
db = f'mysql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}'

DATABASES = {'default': dj_database_url.parse(db, )}

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

LANGUAGE_CODE = 'tr-TR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Activate Django-Heroku.
django_heroku.settings(locals())

ADMIN_REORDER = (
    # Keep original label and models
    # 'sites',

    # Rename app
    # {'app': 'SancakRestDB', 'label': 'Tum '},

    # Reorder app models
    {'app': 'sancakRestDB', 'label': 'Sayman',
     'models': ('sancakRestDB.Sayman',
                'sancakRestDB.Harcamalar',
                'sancakRestDB.Deviraldigim',
                'sancakRestDB.Kasaborc',
                'sancakRestDB.Stok')},

    # Exclude models
    {'app': 'sancakRestDB', 'label': 'Koc',
     'models': ('sancakRestDB.Kunye',
                'sancakRestDB.Kmtakip',
                'sancakRestDB.Images'
                )},
    {'app': 'sancakRestDB', 'label': 'Yol Kaptani',
     'models': ('sancakRestDB.Surushatirlat',
                'sancakRestDB.Etkinliksurus')},
    {'app': 'sancakRestDB', 'label': 'Disiplin',
     'models': ('sancakRestDB.Disiplin',
                'sancakRestDB.Meclis')},
    {'app': 'sancakRestDB', 'label': 'Teknik Yonetim',
     'models': ('sancakRestDB.Giris',
                'sancakRestDB.Girislog',
                'sancakRestDB.DjangoAdminLog')
     }

    # # Cross-linked models
    # {'app': 'auth', 'models': ('auth.User', 'sites.Site')},
    #
    # # models with custom name
    # {'app': 'auth', 'models': (
    #     'auth.Group',
    #     {'model': 'auth.User', 'label': 'Staff'},
    # )},
)
