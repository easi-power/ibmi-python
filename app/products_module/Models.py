from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    max_capacity = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(25), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    image_styling = db.Column(db.String(16000), nullable=False)
