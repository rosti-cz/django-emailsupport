from __future__ import unicode_literals

from django.conf import settings


EMAIL_HOST = getattr(settings, 'EMAIL_HOST', None)
EMAIL_HOST_PASSWORD = getattr(settings, 'EMAIL_HOST_PASSWORD', None)
EMAIL_HOST_USER = getattr(settings, 'EMAIL_HOST_USER', None)
EMAIL_PORT = getattr(settings, 'EMAIL_PORT', None)
EMAIL_USE_SSL = getattr(settings, 'EMAIL_USE_SSL', False)

NOTIFICATION_EMAIL_LIST = getattr(settings, 'NOTIFICATION_EMAIL_LIST', None)
