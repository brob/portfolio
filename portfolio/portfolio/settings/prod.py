# Base settings for all environments
DEBUG = True
TEMPLATE_DEBUG = True
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'portfolio',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'bryanrobinson',
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/bryanlrobinson/webapps/static_port/media/portfolio-media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://media.bryanlrobinson.com/media/portfolio-media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/bryanlrobinson/webapps/static_port/media/portfolio-static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = 'http://media.bryanlrobinson.com/media/portfolio-collection/'




# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.	
	'/home/bryanlrobinson/webapps/static_port/media/django-media/static',
	'/home/bryanlrobinson/webapps/static_port/static-portfolio/portfolio-static',

)



EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'fourwheelfood'
EMAIL_HOST_PASSWORD = 'Asheron1'
DEFAULT_FROM_EMAIL = 'contact@bryanlrobinson.com'
SERVER_EMAIL = 'contact@bryanlrobinson.com'




TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'/home/bryanlrobinson/webapps/customport/portfolio-templates/',

)
