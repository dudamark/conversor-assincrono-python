from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, UPLOAD_FOLDER, CONVERTED_FOLDER
from .utils import convert_to_pdf
import os

# celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

celery = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND 
)

celery.conf.update(
    task_track_started=True,
    task_ignore_result=False,  
    result_expires=3600        
)

@celery.task(bind=True)
def convert_docx_to_pdf_task(self, filename):
    docx_path = os.path.join(UPLOAD_FOLDER, filename)
    pdf_filename = filename.replace(".docx", ".pdf")
    pdf_path = os.path.join(CONVERTED_FOLDER, pdf_filename)
    convert_to_pdf(docx_path, pdf_path)
    return pdf_filename
