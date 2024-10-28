import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: Disable track modifications to save resources
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Use the DATABASE_URL from .env
    SECRET_KEY = os.getenv('SECRET_KEY')  # Set the secret key from .env

class DevelopmentConfig(Config):
    """Development configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

