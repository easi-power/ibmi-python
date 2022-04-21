from flask_restful import Resource, marshal_with, reqparse, fields, abort
from app import db
from app.products_module.Models import Product

resource_fields = {
    'id' : fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'stock': fields.Integer,
    'max_capacity': fields.Integer,
    'status': fields.String,
    'image_path': fields.String,
    'image_styling': fields.String,
}

class ProductApi(Resource):
    @marshal_with(resource_fields)
    def get(self, product_id=None):
        result = Product.query.filter_by(id=product_id).first()
        if not result:
            abort(404,message="Product does not exist")
        return result

class ProductsApi(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Product.query.all()

