import os
from celery import Celery

#because the manage.py server hasn't started as per config in the docker-compose.yml
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ecommapp.settings')
#initiation of the Celery app
celery_app = Celery(
    "ecommapp",    
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
    )
#look for celery in the settings with the name starting with CELERY
celery_app.config_from_object("django.conf:settings",namespace="CELERY")

celery_app.autodiscover_tasks()
