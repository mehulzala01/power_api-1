DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Each',
        'USER': 'robindu',
        'PASSWORD': 'Each2022',
        'HOST': 'postgis',
        'PORT': '5432'
    }
}