from flask import Flask
from flask_restful import Api,abort,Resource
from flask_sqlalchemy import SQLAlchemy


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

api = Api(app)
db = SQLAlchemy(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.user_module.Controllers import UserApi, UsersApi
api.add_resource(UserApi, "/api/users/<user_id>")
api.add_resource(UsersApi, "/api/users")

from app.products_module.Controllers import ProductApi, ProductsApi
api.add_resource(ProductApi, "/api/products/<product_id>")
api.add_resource(ProductsApi, "/api/products")

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

#db.create_all()