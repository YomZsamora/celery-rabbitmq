# Import necessary modules
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
celery_app = Celery("core")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
celery_app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'