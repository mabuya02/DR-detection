import os
from dotenv import load_dotenv
from flask import Flask
from app.extensions import db, migrate
from app.routes import bp as test_bp

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# Register blueprints for routes
app.register_blueprint(test_bp)

if __name__ == '__main__':
    app.run(debug=True)