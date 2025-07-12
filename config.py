import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), "app", "uploads")
CONVERTED_FOLDER = os.path.join(os.getcwd(), "app", "converted")

# CELERY_BROKER_URL = 'redis://redis:6379/0'
# CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'