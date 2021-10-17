from datetime import datetime

from sqlalchemy.orm import backref
from models.db import db


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    product = db.relationship(
        "Product", backref=db.backref('products', lazy=True))

    def __init__(self, title, content):
        self.title = title
        self.content = content
