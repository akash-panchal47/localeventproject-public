"""
WSGI config for localeventproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localeventproject.settings')

# rename to `app` (Vercel expects this public variable)
app = get_wsgi_application()

