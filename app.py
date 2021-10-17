from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from models.user import User
from models.product import Product
from models.review import Review

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/shopping_db'
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

api = Api(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
