# Copy to env.py
# Choose the environment: development, or production; uncomment the appropriate

from .prod import *
# from .dev import *

# Other developer custom settings may go below in env.py

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'pmsnew',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT' : '',  # Set to empty string for default.
    }
}