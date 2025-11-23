# backend/__init__.py

from flask import Flask
from .config import Config
from .database.db import db

def create_app():
    app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
    app.config.from_object(Config)

    db.init_app(app)  # Connect DB

    with app.app_context():
        db.create_all()  # Make tables

    return app