from celery import shared_task
from . email import send_email
@shared_task(name="send_email_celery")
def send_email_celery(email):
    return send_email(email)
