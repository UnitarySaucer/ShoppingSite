from flask_restful import Resource
from flask import request
from models.product import Product
from models.db import db
from sqlalchemy.orm import joinedload


class ProductList(Resource):
    def get(self):
        data = Product.find_all()
        results = [u.json() for u in data]
        return results

    def post(self):
        data = request.get_json()
        product = Product(**data)
        product.create()
        return product.json(), 201


class IndividualProduct(Resource):
    def get(self, id):
        product = Product.query.options(joinedload(
            'reviews')).filter_by(id=id).first()
        reviews = [t.json() for t in product.reviews]
        return {**product.json(), "reviews": reviews}

    def delete(self, id):
        product = Product.find_by_id(id)
        db.session.delete(product)
        db.session.commit()
        return {'msg': 'Deleted'}

    def put(self, id):
        data = request.get_json()
        product = Product.find_by_id(id)
        for key in data:
            setattr(product, key, data[key])
        db.session.commit()
        return product.json()
