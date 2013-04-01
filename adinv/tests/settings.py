
INSTALLED_APPS = ['adinv']

SECRET_KEY='django-adinv-test-key'

_optional = ['django_jenkins', 'south']
for app in _optional:
    try:
        __import__(app)
    except ImportError:
        pass
    else:
        INSTALLED_APPS.append(app)

PROJECT_APPS = ['adinv']

ADINV_IMAGE_PATH = '/tmp/adinv'

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
        }
}

