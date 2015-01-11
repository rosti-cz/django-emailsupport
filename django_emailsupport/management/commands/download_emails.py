# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.core.management.base import BaseCommand
from django_emailsupport.processor import download_and_save

logger = logging.getLogger('default')


class Command(BaseCommand):
    help = 'Download emails'

    def handle(self, *args, **options):
        try:
            download_and_save()
        except Exception, e:
            logger.error(str(e), extra={'exception': e, 'stack': True})
