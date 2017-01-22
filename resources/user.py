from flask_restful import Resource, reqparse
from db import db
from models.user import UserModel


class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username')
    parser.add_argument('email')

    def get(self, user_id):
        user = UserModel.find_by_id(user_id)

        if user:
            return user.json(), 200

        return {"message": "User not found"}, 404

    def put(self, user_id):
        data = self.parser.parse_args()

        user = UserModel.find_by_id(user_id)

        if user:
            user.update(**data)

        return user.json()

    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)

        if user:
            try:
                user.delete_from_db()
            except:
                return {"message": "An error occured deleting user."}, 500

            return {"message": "User deleted"}, 204

        return {"message": "User not found"}, 404


class UserList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        help="This field cannot left be blank.")
    parser.add_argument('email',
                        required=True,
                        help="This field cannot left be blank.")
    parser.add_argument('password',
                        required=True,
                        help="This field cannot left be blank.")

    def get(self):
        users = UserModel.query.all()
        return {"users": [user.json() for user in users]}

    def post(self):
        data = self.parser.parse_args()

        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {"message": "An error ocured inserting user."}, 500

        return user.json(), 201
