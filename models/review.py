from datetime import datetime
from models.db import db


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    product = db.relationship(
        "Product", backref=db.backref('products', lazy=True))
    user = db.relationship(
        "User", backref=db.backref('users', lazy=True))

    def __init__(self, title, content, product_id, user_id):
        self.title = title
        self.content = content
        self.product_id = product_id
        self.user_id = user_id

    def json(self):
        return {"id": self.id, "title": self.title, "content": self.content, "product_id": self.product_id, "user_id": self.user_id, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Review.query.all()

    @classmethod
    def find_by_id(cls, review_id):
        user = Review.query.filter_by(id=review_id).first()
        return user
