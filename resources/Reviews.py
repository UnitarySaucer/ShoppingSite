from flask_restful import Resource
from flask import request
from models.review import Review
from models.db import db
from sqlalchemy.orm import joinedload


class ReviewList(Resource):
    def get(self):
        data = Review.find_all()
        results = [r.json() for r in data]
        return results

    def post(self):
        data = request.get_json()
        review = Review(**data)
        review.create()
        return review.json(), 201


class IndividualReview(Resource):
    def get(self, id):
        review = Review.query.options(
            joinedload('user'), joinedload('product')).filter_by(id=id).first()
        user = review.user.json()
        product = review.product.json()
        return {**review.json(), "user": user, "product": product}

    def delete(self, id):
        review = Review.find_by_id(id)
        db.session.delete(review)
        db.session.commit()
        return {'msg': 'Deleted'}

    def put(self, id):
        data = request.get_json()
        review = Review.find_by_id(id)
        for key in data:
            setattr(review, key, data[key])
        db.session.commit()
        return review.json()
