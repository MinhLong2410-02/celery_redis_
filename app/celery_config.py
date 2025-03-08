from celery import Celery
from config.settings import REDIS_URL
from celery.schedules import crontab
celery_app = Celery("app", broker=REDIS_URL)

# Explicitly auto-discover tasks
celery_app.autodiscover_tasks(["app"])
celery_app.conf.beat_schedule = {
    "log_every_2_minutes": {
        "task": "app.tasks.log_one",
        "schedule": crontab(minute="*/2"),  # Runs every 2 minutes
    },
}

celery_app.conf.timezone = "UTC"