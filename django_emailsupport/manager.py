from __future__ import unicode_literals

from django.db.models import manager


class EmailManager(manager.Manager):

    def get_previous_email(self, email):
        """

        :param email:
        :type email: emailsupport.models.Email
        """

        lookup_params = {'submitter_id': email.submitter_id, 'pk__lt': email.pk}
        try:
            result = self.get_queryset().filter(**lookup_params).order_by('-pk')[:1][0]
        except IndexError:
            result = None

        return result

    def get_next_email(self, email):
        """

        :param email:
        :type email: emailsupport.models.Email
        """

        lookup_params = {'submitter_id': email.submitter_id, 'pk__gt': email.pk}
        try:
            result = self.get_queryset().filter(**lookup_params).order_by('pk')[:1][0]
        except IndexError:
            result = None

        return result
