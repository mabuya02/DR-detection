import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from .extensions import db, migrate, mail
from .models import *
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Ensure the logs folder exists
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Set up logging to capture all levels
    # Configure logging both in debug and production modes for testing purposes
    main_handler = RotatingFileHandler(
        app.config['LOG_FILE_PATH'], maxBytes=10240, backupCount=5
    )
    main_handler.setLevel(logging.DEBUG)  # Capture all log levels
    main_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )

    # Error-specific log handler for ERROR and higher levels
    error_handler = RotatingFileHandler(
        app.config['ERROR_LOG_FILE_PATH'], maxBytes=10240, backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )

    # Attach handlers to the app's logger
    app.logger.setLevel(logging.DEBUG) 
    app.logger.addHandler(main_handler)
    app.logger.addHandler(error_handler)

    with app.app_context():
        db.create_all()  # Optional

        # Import and register routes
        from .routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app
