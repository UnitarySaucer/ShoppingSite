from datetime import datetime
from models.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    reviews = db.relationship("Review", cascade='all',
                              backref=db.backref('reviews', lazy=True))

    def __init__(self, username, email, password_digest):
        self.username = username
        self.email = email
        self.password_digest = password_digest

    def json(self):
        return {"id": self.id, "username": self.username, "email": self.email, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return User.query.all()

    @classmethod
    def find_by_id(cls, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user
