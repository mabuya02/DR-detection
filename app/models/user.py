from app.extensions import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing user ID
    username = db.Column(db.String(50), unique=True, nullable=False)  # Unique username
    email = db.Column(db.String(100), unique=True, nullable=False)  # Unique email address
    password = db.Column(db.String(255), nullable=False)  # User's hashed password
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Timestamp for creation
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Timestamp for updates

    def __repr__(self):
        return f'<User {self.username}>'