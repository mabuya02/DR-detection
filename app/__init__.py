from flask import Flask
from .extensions import db, migrate
from .models import *  # Import your models
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()  # Optional

        # Import and register routes
        from .routes import bp as routes_bp
        app.register_blueprint(routes_bp)

    return app