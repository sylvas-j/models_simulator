from .common import *
###############
## configuration for heroku
# import dj_database_url
# import django_heroku
####################

DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1','localhost','localhost:8282','devarchive.org','www.devarchive.org','devarchive.org:8181','www.devarchive.org:8181']
ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8181',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8181',
    'http://www.devarchive.org:8181',
    'http://193.203.167.210:8181',
    'http://193.203.167.210',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8181',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8181',
    'http://www.devarchive.org:8181',
    'http://193.203.167.210:8181',
    'http://193.203.167.210',
]


# TEST/DEVELOPMENT REMOTE DATABASE
# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'admin_mod_sim',
#         'USER': 'admin_root',
#         'PASSWORD': 'admin_sylvas',
#         'HOST': '104.37.191.201',
#         # 'HOST': 'devarchive.org',
#         'PORT': '3306',
#         # 'OPTIONS': {
#         #   'init_command': "set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'"
#         # },
#     },
# }


# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': os.environ.get('MYSQL_ENGINE'),
#         'NAME': os.environ.get('MYSQL_DATABASE'),
#         'USER': os.environ.get('MYSQL_USER'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
#         'HOST': os.environ.get('MYSQL_HOST'),
#         'PORT': os.environ.get('MYSQL_PORT'),
#         'OPTIONS': {
#             'auth_plugin': 'mysql_native_password'
#         }

#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


