import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'bla-bla-bla': {
        'task': 'apps.users.tasks.send_email_task',
        # 'schedule': 1.0, Это каждую секунду
        'schedule': crontab(hour=1, minute=1),
        'kwargs': {}
    },
    'bla-bla-bla-2': {
        'task': 'apps.users.tasks.send_tg_message_crontab',
        'schedule': 10.0,
        'kwargs': {}
    }
}