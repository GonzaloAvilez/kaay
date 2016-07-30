"""
Django settings for socialhand project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
STATICFILES_DIRS = [join(BASE_DIR, 'static')]




# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                 'cart.context_processors.cart',
                 # Python Social Auth Context Processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = 'mnj=llx*oe9sp_l^g5dz5!!cn_y4&w488f1q6l-eyl_)kirrm$'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authtools',
    'crispy_forms',
    'easy_thumbnails',
    'social.apps.django_app.default',

    'paypal.standard.ipn',
    'payment',
    'profiles',
    'accounts',
    'orders',
    'shop',    
    'cart',
    'socialhand',
    'haystack',
    'djrill',
        
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Facebook
    'social.backends.facebook.FacebookOAuth2',
    # Twitter
    'social.backends.twitter.TwitterOAuth',
    # Google 
    'social.backends.google.GoogleOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
)

# Facebook Keys
SOCIAL_AUTH_FACEBOOK_KEY = '657778311046259'
SOCIAL_AUTH_FACEBOOK_SECRET = '95a709bc0b55e58dcb010d0ba45fcb54'


# Twitter Keys
SOCIAL_AUTH_TWITTER_KEY = 'wk2ccPNF6lc9T84xjgejYuqUE'
SOCIAL_AUTH_TWITTER_SECRET = 'IrK4vcEebnoDPNXEaIhyoDj64GuKNdxqANyBFViLM67U3MGIld'

# Google Keys 
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '913879562571-3prerlijc0i0ahp0plta7juieev02c7l.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'H7RVg5PlMgil9GxK0K0TvPn1'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

ROOT_URLCONF = 'socialhand.urls'

WSGI_APPLICATION = 'socialhand.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = join(BASE_DIR, '')

MEDIA_URL = "/media/"
MEDIA_ROOT = join(BASE_DIR, 'media')

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")


THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails
CART_SESSION_ID = 'cart'

#Contact Us features

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

MANDRILL_API_KEY='n6MKcMYN9KTbSPrZcl8sKA'
DEFAULT_FROM_EMAIL= "g.avilez.ig@gmail.com"

# EMAIL_HOST ='smtp.mandrillapp.com'
# EMAIL_PORT = 587
# EMAIL_HOST_PASSWORD= 'n6MKcMYN9KTbSPrZcl8sKA'
# EMAIL_HOST_USER= 'IKAAY'


# DEFAULT_FROM_EMAIL = "g.avilez.ig@gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'g.avilez.ig@gmail.com'
# EMAIL_HOST_PASSWORD = 'aiig890905hgrvgn04'



# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# SENDGRID_USER = "g.avilez.ig"
# SENDGRID_PASSWORD = "gonzalito"





# django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'g.avilez.ig-facilitator@gmail.com'
PAYPAL_TEST = True


#search engine adquired via pip 

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
# signal processor will enable signal processor that for every change in the models will run
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'