# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from imbox import Imbox

from django_emailsupport import settings


def _create_connection():
    """
    Create new IMAP connection

    :rtype: imbox.Imbox
    """
    connection = Imbox(settings.EMAIL_HOST,
                       username=settings.EMAIL_HOST_USER,
                       password=settings.EMAIL_HOST_PASSWORD,
                       ssl=settings.EMAIL_USE_SSL)

    return connection


def get_unread_messages():
    connection = _create_connection()

    return connection.messages(unread=True)


def mark_seen(uid_list):
    connection = _create_connection()

    for uid in uid_list:
        connection.mark_seen(uid)
