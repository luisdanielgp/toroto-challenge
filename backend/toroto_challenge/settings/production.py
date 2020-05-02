import os
import dj_database_url

from toroto_challenge.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# Update database configuration with $DATABASE_URL.
DATABASES['default'] = dj_database_url.config(conn_max_age=500)


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ['https://secret-shelf-40223.herokuapp.com/']

INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "../", "frontend", "build")]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "../", "frontend", "build", "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
WHITENOISE_ROOT = os.path.join(BASE_DIR, "../", "frontend", "build", "root")