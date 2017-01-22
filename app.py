import os
from flask import Flask
from flask_restful import Api

from resources.user import UserList, User
from resources.wine import WineList, Wine

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from db import db
    db.init_app(app)

    api = Api(app)
    api.add_resource(UserList, '/users')
    api.add_resource(User, '/users/<int:user_id>')
    api.add_resource(WineList, '/users/<int:user_id>/wines')
    api.add_resource(Wine, '/users/<int:user_id>/wines/<int:wine_id>')

    return app
