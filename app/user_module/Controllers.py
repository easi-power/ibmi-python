from flask_restful import Resource, marshal_with, reqparse, fields, abort
from app import db
from app.user_module.Models import User

resource_fields = {
    'id' : fields.Integer,
    'firstname': fields.String,
    'lastname': fields.String,
    'email': fields.String,
    'phone': fields.String
}

user_args = reqparse.RequestParser()
user_args.add_argument("firstname", type=str, help="The firstname of the user is required", required=True)
user_args.add_argument("lastname", type=str, help="The lastname of the user is required", required=True)
user_args.add_argument("email", type=str, help="The email of the user is required", required=True)
user_args.add_argument("phone", type=str, help="The phone field is required", required=True)

filter_args = reqparse.RequestParser()
filter_args.add_argument('id', type=int, help="The id attribute should be an integer", required=False, location='args')
filter_args.add_argument('firstname', type=str, help="Invalid name attribute", required=False, location='args')

class UserApi(Resource):
    

    @marshal_with(resource_fields)
    def get(self, user_id=None):
        result = User.query.filter_by(id=user_id).first()
        if not result:
            abort(404,message="User does not exist")
        return result

    @marshal_with(resource_fields)
    def put(self, user_id):
        args = user_args.parse_args()
        user = User.query.filter_by(id=user_id)
        if not user.scalar():
            abort(404,message="User does not exist")
        user.update(args)
        db.session.commit()
        return user.first(), 202

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return '', 204

class UsersApi(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = filter_args.parse_args()
        result = User.query
        
        if(args.id):
            result = result.where(User.id == args.id)
        if(args.firstname):
            result = result.where(User.firstname == args.firstname)

        return result.all()

    @marshal_with(resource_fields)
    def post(self):
        args = user_args.parse_args()
        user = User(firstname=args['firstname'], lastname=args['lastname'], email=args['email'], phone=args['phone'])
        db.session.add(user)
        db.session.commit()
        return user, 201