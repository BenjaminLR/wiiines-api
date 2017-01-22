import os
from flask import Flask
from flask_restful import Api

from models.user import UserModel
from models.wine import WineModel
from resources.user import UserList, User

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from db import db
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        user1 = UserModel('one', 'one@example.com', 'azerty')
        user2 = UserModel('two', 'two@example.com', 'azerty')
        user3 = UserModel('three', 'three@example.com', 'azerty')
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        wine1 = WineModel('wine1', 'description1', 1)
        wine2 = WineModel('wine2', 'description2', 1)
        wine3 = WineModel('wine3', 'description3', 2)
        db.session.add(wine1)
        db.session.add(wine2)
        db.session.add(wine3)
        db.session.commit()

    api = Api(app)
    api.add_resource(UserList, '/users')
    api.add_resource(User, '/users/<int:user_id>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5050)
