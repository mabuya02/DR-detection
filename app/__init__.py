import os
from flask import Flask
from .extensions import db, migrate, mail
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    return app
