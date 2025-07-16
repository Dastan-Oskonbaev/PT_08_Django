from celery import shared_task
from django.core.mail import send_mail

from core import settings

@shared_task
def send_email_task():
    subject = "Welcome to our site"
    message = f"Hi "
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['snoopdas@mail.ru']
    send_mail(subject, message, email_from, recipient_list, fail_silently=False,)
