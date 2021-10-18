from flask_restful import Resource
from flask import request
from models.user import User
from models.db import db
from sqlalchemy.orm import joinedload


class UserList(Resource):
    def get(self):
        data = User.find_all()
        results = [u.json() for u in data]
        return results


class IndividualUser(Resource):
    def get(self, id):
        user = User.query.options(joinedload(
            'reviews')).filter_by(id=id).first()
        reviews = [t.json() for t in user.reviews]
        return {**user.json(), "reviews": reviews}

    def delete(self, id):
        user = User.find_by_id(id)
        db.session.delete(user)
        db.session.commit()
        return {'msg': 'Deleted'}

    def put(self, id):
        data = request.get_json()
        user = User.find_by_id(id)
        for key in data:
            setattr(user, key, data[key])
        db.session.commit()
        return user.json()
