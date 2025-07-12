from flask import Flask
from config import UPLOAD_FOLDER, CONVERTED_FOLDER
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER
    app.secret_key = 'WFKvvrmrmrmrrREUUGKTRMBe5262vred5v2r4g5v1e41'

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(CONVERTED_FOLDER, exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app
