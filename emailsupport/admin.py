from django.contrib import admin

from models import Email, Resolution


class ResolutionInline(admin.StackedInline):
    model = Resolution
    max_num = 1


class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'submitter', 'get_state_display')
    inlines = [ResolutionInline]
    ordering = ('-state', '-created')

admin.site.register(Email, EmailAdmin)
admin.site.register(Resolution)
