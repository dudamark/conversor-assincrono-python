from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from .tasks import convert_docx_to_pdf_task
from app.tasks import celery  
from config import UPLOAD_FOLDER, CONVERTED_FOLDER
import os

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".docx"):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            task = convert_docx_to_pdf_task.delay(filename)
            return redirect(url_for("main.task_status", task_id=task.id))
        else:
            flash("Apenas arquivos .docx são permitidos.")
    return render_template("index.html")

@main.route("/status/<task_id>")
def task_status(task_id):
    task = celery.AsyncResult(task_id)
    
    if task.state == "SUCCESS":
        
        return render_template("status.html", task_id=task_id, state=task.state, result=task.result)
    elif task.state == "FAILURE":
        return render_template("status.html", task_id=task_id, state=task.state, result=None)
    else:
        return render_template("status.html", task_id=task_id, state=task.state, result=None)

@main.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(CONVERTED_FOLDER, filename, as_attachment=True)
