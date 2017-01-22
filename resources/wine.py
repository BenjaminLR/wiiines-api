from flask_restful import Resource, reqparse

from models.wine import WineModel


class Wine(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        help="Set name for wine.")
    parser.add_argument('description',
                        help="Set description for wine.")

    def get(self, user_id, wine_id):
        wine = WineModel.find_by_id(wine_id)

        if wine:
            return wine.json(), 200

        return {"message": "Wine not found."}, 404

    def put(self, user_id, wine_id):
        data = self.parser.parse_args()

        wine = WineModel.find_by_id(wine_id)

        if wine:
            wine.update(**data)

            return wine.json(), 200

        return {"message": "Wine not found"}, 404



    def delete(self, user_id, wine_id):
        wine = WineModel.find_by_id(wine_id)

        if wine is None:
            return {"message": "Wine not found."}, 404

        try:
            wine.delete_from_db()
        except:
            return {"message": "An error occured deleting wine."}, 500

        return {"message": "Wine deleted."}, 200


class WineList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="A wine required a name.")
    parser.add_argument('description',
                        help="Put a description for wine.")

    def get(self, user_id):
        wines = WineModel.find_by_user(user_id)

        return {"wines": [wine.json() for wine in wines]}, 200

    def post(self, user_id):
        data = self.parser.parse_args()
        data['user_id'] = user_id

        wine = WineModel(**data)

        try:
            wine.save_to_db()
        except:
            return {"message": "An error occured inserting wine."}, 500

        return wine.json(), 201
