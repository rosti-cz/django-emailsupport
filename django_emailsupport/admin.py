# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Email, Resolution, Submitter


class ResolutionInline(admin.StackedInline):
    model = Resolution
    max_num = 1


class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'submitter',  'created', 'get_state_display')
    inlines = [ResolutionInline]
    ordering = ('-state', '-created')
    change_form_template = 'admin/email_change_form.html'
    readonly_fields = ('submitter', 'subject', 'body', 'body_html')

    fieldsets = (
        ('Question', {
            'fields': ('submitter', 'subject', 'body', 'body_html', 'state')
        }),
    )

    class Media:
        css = {
            "all": ("admin/css/admin.css",)
        }

    def render_change_form(self, *args, **kwargs):
        response = super(EmailAdmin, self).render_change_form(*args, **kwargs)
        email = response.context_data['original']
        if email:
            response.context_data['previous_email'] = self.get_previous_email(email)
            response.context_data['next_email'] = self.get_next_email(email)
        return response

    def get_previous_email(self, email):
        return Email.objects.get_previous_email(email)

    def get_next_email(self, email):
        return Email.objects.get_next_email(email)


admin.site.register(Email, EmailAdmin)
admin.site.register(Submitter)
