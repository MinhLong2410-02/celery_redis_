import os

# Redis Configuration (Celery Broker)
REDIS_URL = os.getenv("REDIS_URL", "redis://celery_redis:6379/0")