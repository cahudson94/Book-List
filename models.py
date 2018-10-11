"""Model objects for book app."""
from app import db
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """User model."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    books = db.Column(JSON)

    def set_password(self, password):
        """Set users password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verify password."""
        return check_password_hash(self.password, password)


class Book(db.Model):
    """Book model."""

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    isbn = db.Column(db.String())
    date_of_publication = db.Column(db.String())
    users = db.Column(JSON)
