from celery import shared_task
from django.core.mail import send_mail

from apps.users.utils import send_tg_message
from core import settings

@shared_task(queue='email')
def send_email_task():
    subject = "Welcome to our site"
    message = f"Hi "
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['snoopdas@mail.ru']
    send_mail(subject, message, email_from, recipient_list, fail_silently=False,)


@shared_task(queue='tg')
def send_tg_message_crontab():
    text = "HELLO"
    send_tg_message(text)
