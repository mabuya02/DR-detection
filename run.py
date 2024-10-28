from flask import Flask
from app.extensions import db
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load config

    # Initialize the database and migrate
    db.init_app(app)
    migrate = Migrate(app, db)  # Initialize Migrate with the app and db

    # Register blueprints or routes here (if any)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()