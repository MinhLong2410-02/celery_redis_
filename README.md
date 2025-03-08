# Pythonic project set up for periodically task using Celery + Redis, deploy on Docker

celery_project/
│── app/
│   ├── tasks.py          # Celery tasks
│   ├── celery_config.py  # Celery configuration
│── config/
│   ├── settings.py       # Configurations (Redis)
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── main.py               # Entry point for testing Celery task

