
INSTALLED_APPS = ['adinv']

_optional = ['django_jenkins', 'south']
for app in _optional:
    try:
        __import__(app)
    except ImportError:
        pass
    else:
        INSTALLED_APPS.append(app)

PROJECT_APPS = ['adinv']

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
        }
}

