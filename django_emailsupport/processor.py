# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django_emailsupport.utils.imap import get_unread_messages, mark_seen
from django_emailsupport.settings import NOTIFICATION_EMAIL_LIST
from django_emailsupport.tasks import send_mail

from models import Email, Submitter


def sanitize_email(email):
    return email


def notify_users(email):
    content = email.get_body()
    send_mail(email.subject, content, settings.DEFAULT_FROM_EMAIL, NOTIFICATION_EMAIL_LIST)


def get_submitter_by_email(email, name):

    return Submitter.objects.get_or_create(address=sanitize_email(email),
                                           defaults={'name': name})


def download_and_save():
    email_list = []
    uid_list = []
    for uid, message in get_unread_messages():
        submitter_data = message.sent_from[-1]

        submitter, created = get_submitter_by_email(submitter_data['email'],
                                                    submitter_data['name'])

        email = Email()
        email.submitter = submitter
        email.subject = message.subject
        try:
            email.body = message.body['plain'][-1]
        except IndexError:
            pass
        try:
            email.body_html = message.body['html'][-1]
        except IndexError:
            pass

        email_list.append(email)
        uid_list.append(uid)

    Email.objects.bulk_create(email_list)
    mark_seen(uid_list)

    for email in email_list:
        notify_users(email)
