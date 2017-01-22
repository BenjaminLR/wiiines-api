import os
from flask import Flask
from flask_restful import Api

from resources.user import UserList, User

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from db import db
    db.init_app(app)

    api = Api(app)
    api.add_resource(UserList, '/users')
    api.add_resource(User, '/users/<int:user_id>')

    return app
