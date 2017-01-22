from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from db import db
from models.user import UserModel
from models.wine import WineModel

app = create_app()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('runserver', Server(port=5555))
manager.add_command('db', MigrateCommand)

@manager.command
def populatedb():
    with app.app_context():
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

if __name__ == '__main__':
    manager.run()
