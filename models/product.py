from datetime import datetime
from models.db import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    reviews = db.relationship("Review", cascade='all',
                              backref=db.backref('reviews', lazy=True))

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def json(self):
        return {"id": self.id, "name": self.name, "price": self.price, "description": self.description, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Product.query.all()

    @classmethod
    def find_by_id(cls, product_id):
        user = Product.query.filter_by(id=product_id).first()
        return user
