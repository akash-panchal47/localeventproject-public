"""
WSGI config for localeventproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

"""
WSGI config for localeventproject project.

It exposes the WSGI callable as a module-level variable named 'app'
for Vercel deployment.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localeventproject.settings')

# Default Django WSGI application
application = get_wsgi_application()

# Add this line so Vercel can find the app
app = application



