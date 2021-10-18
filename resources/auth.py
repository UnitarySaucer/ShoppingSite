from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password


class Login(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = User.find_user(username=data['username']).json()
            check_pw = compare_password(
                data['password'], user['password_digest'])
            if check_pw:
                payload = {
                    'id': user['id'],
                    'username': user['username'],
                    'email': user['email']
                }
                token = create_token(payload)
                return {'user': payload, 'token': token}, 200
            else:
                return {'msg': "Please Check Your Credentials"}, 404
        except:
            return {'msg': 'Error'}, 404

    def get(self):
        token = strip_token(request)
        return read_token(token)


class Register(Resource):
    def post(self):
        data = request.get_json()
        params = {
            "username": data['username'],
            "email": data['email'],
            "password_digest": gen_password(data['password'])
        }
        user = User(**params)
        user.create()
        return user.json(), 201
