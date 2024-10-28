from app.extensions import db
from datetime import datetime, timezone

class Profile(db.Model):
    __tablename__ = 'profiles'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing profile ID
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key referencing User
    bio = db.Column(db.String(255), nullable=True)  # User bio
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Timestamp for creation
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Timestamp for updates

    def __repr__(self):
        return f'<Profile user_id={self.user_id}>'