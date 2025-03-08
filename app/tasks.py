import logging
from app.celery_config import celery_app

# Configure Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("celery_tasks.log")  
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

@celery_app.task
def log_one():
    logger.info("1")  # Log "1" to the log file
    return "Logged 1 successfully"
