"""
WSGI config for sso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR), '..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sso.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
