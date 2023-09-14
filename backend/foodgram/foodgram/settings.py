import os
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY',
                       default='p&l%385148kslhtyn^##a1)'
                               'ilz@4zqj=rq&agdol^##zgl9(dd')

DEBUG = (os.getenv('DEBUG', default='False') == 'True')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', default='*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework.authtoken',
    'rest_framework',
    'djoser',
    'api.apps.ApiConfig',
    'recipes.apps.RecipesConfig',
    'users.apps.UsersConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foodgram.urls'

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

WSGI_APPLICATION = 'foodgram.wsgi.application'

DB_ENGINE = os.getenv('DB_ENGINE', default='django.db.backends.postgresql')

if 'sqlite' in DB_ENGINE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': os.getenv('DB_NAME', default='postgres'),
            'USER': os.getenv('POSTGRES_USER', default='postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
            'HOST': os.getenv('DB_HOST', default='db'),
            'PORT': os.getenv('DB_PORT', default='5432')
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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 6,

}

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'users.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APPEND_SLASH = False

DJOSER = {
    'SERIALIZERS': {
        'user': 'api.serializers.CustomUserSerializer',
        'current_user': 'api.serializers.CustomUserSerializer',
    },
    'PERMISSIONS': {
        'user': ['rest_framework.permissions.AllowAny']
    }
}

CORS_ALLOW_ALL_ORIGINS = True
DATA_DIR = (BASE_DIR / 'static/data/')

MODEL_STR_LIMIT = 30
LENGTH254 = 254
LENGTH150 = 150
LENGTH200 = 200
LENGTH7 = 7
MINVALUE = 1
MUST_HAVE_FIELD = 'Обязательное поле.'
NOT_LIST_INGREDIENT = '{ingredients} должен быть не пустым списком!'
NOT_POSITIVE_INTEGER_TAG = '{tag} должен быть целым числом больше нуля!'
MUST_HAVE_FIELD_AMOUNT = ('amount обязательное поле для ингредиента '
                          '{ingredient}.')
MUST_HAVE_FIELD_ID = 'id обязательное поле для ингредиента {ingredient}.'
NOT_POSITIVE_INTEGER = ('Значение amount для ингредиента {ingredient} '
                        'должно быть целым и больше нуля!')
DUPLICATE_INGREDIENTS = 'Дублирование ингредиента {ingredient} в запросе!'
DUPLICATE_TAGS = 'Дублирование тега {tag} в запросе!'
NO_INGREDIENT = 'Такого ингредиента {ingredient} не существует!'
DUPLICATE_FAVORITES = 'Дублирование рецепта {recipe} в избранном!'
DUPLICATE_SUBSCRIPTION = 'Дублирование подписки на автора {author}!'
NO_SUBSCRIPTION = ('У пользователя {subscriber} нет подписки '
                   'на автора {author}!')
SELF_SUBSCRIPTION = ('Попытка самоподписки пользователя {subscriber} '
                     'на автора {author}!')
RECIPE_ALREADY_IN_CART = 'Рецепт {recipe} уже добавлен в корзину'
NO_RECIPE_FOR_DONWLOAD = 'У вас нет рецептов в корзине'
