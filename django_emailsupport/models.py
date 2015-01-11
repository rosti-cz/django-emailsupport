from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.html import strip_tags
from django_emailsupport.tasks import send_mail
from django_emailsupport.manager import EmailManager


User = settings.AUTH_USER_MODEL

EMAIL_STATES = (
    (2, 'Assign'),
    (1, 'New'),
    (0, 'Closed'),
)


class Submitter(models.Model):
    address = models.EmailField(db_index=True, unique=True)
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.address


class Email(models.Model):
    submitter = models.ForeignKey(Submitter)
    subject = models.CharField(max_length=256)
    body = models.TextField()
    body_html = models.TextField(blank=True)
    state = models.IntegerField(choices=EMAIL_STATES, default=1)

    created = models.DateTimeField(auto_now=True)

    objects = EmailManager()

    class Meta:
        ordering = ('-created', '-state')

    def __str__(self):
        return '{} <{}>'.format(self.subject, self.submitter)

    def mark_as_closed(self):
        self.state = 0

    def get_body(self):
        return self.body or strip_tags(self.body_html)


class Resolution(models.Model):
    user = models.ForeignKey(User)
    email = models.ForeignKey(Email)
    content = models.TextField()

    created = models.DateTimeField(auto_now=True)

    def create_email_params(self):
        return {'subject': 'Re: {}'.format(self.email.subject),
                'message': self.get_message_content(),
                'from_email': settings.DEFAULT_FROM_EMAIL,
                'recipient_list': [self.email.submitter.address]}

    def get_message_content(self):
        content = self.email.get_body()
        content = '\r\n> '.join(content.splitlines())
        content = '\r\n> {}'.format(content)
        return '{}\r\n\r\n{}'.format(self.content, content)


def resolution_save_handler(sender, instance, created, **kwargs):
    if created:
        parameters = instance.create_email_params()
        send_mail(**parameters)
        instance.email.mark_as_closed()
        instance.email.save()


models.signals.post_save.connect(resolution_save_handler, Resolution, dispatch_uid='send_email')
