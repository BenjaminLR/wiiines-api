from datetime import datetime
from db import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    created_at = db.Column(db.DateTime())
    wines = db.relationship('WineModel', backref='users', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        self.created_at = datetime.now()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "created": self.created_at.strftime("%d/%m/%y - %H:%M:%S"),
            "wines": [wine.json() for wine in self.wines.all()]
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **kwargs):
        if kwargs['username']:
            self.username = kwargs['username']
        if kwargs['email']:
            self.email = kwargs['email']

        db.session.commit()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()
