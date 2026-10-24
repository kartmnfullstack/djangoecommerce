from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(email):

    c = {
        'email': email
    }

    email_subject = "Email Confirmation"
    email_body = render_to_string("email.txt",c)

    email_msg = EmailMessage(
        email_subject,
        email_body,
        settings.EMAIL_FROM,
        [email,],
    )

    return email_msg.send(fail_silently=True)

