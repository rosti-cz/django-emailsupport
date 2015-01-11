from django.core.mail import send_mail as email_sender


def send_mail(subject, message, from_email, recipient_list, **kwargs):
    return email_sender(subject, message, from_email, recipient_list, **kwargs)
