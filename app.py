from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from models.user import User
from models.product import Product
from models.review import Review
from resources.auth import Login, Register
from resources.Users import UserList, IndividualUser
from resources.Reviews import ReviewList, IndividualReview
from resources.Products import ProductList, IndividualProduct

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/shopping_db'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

api = Api(app)
migrate = Migrate(app, db)

api.add_resource(Login, '/auth/login')
api.add_resource(Register, '/auth/register')

api.add_resource(UserList, '/api/users')
api.add_resource(IndividualUser, '/api/users/<int:id>')

api.add_resource(ReviewList, '/api/reviews')
api.add_resource(IndividualReview, '/api/reviews/<int:id>')

api.add_resource(ProductList, '/api/products')
api.add_resource(IndividualProduct, '/api/products/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
