from datetime import datetime
from db import db


class WineModel(db.Model):

    __tablename__ = 'wines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(140))
    created_at = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.user_id = user_id

    def json(self):
        return {
            "name": self.name,
            "description": self.description,
            "created": self.created_at.strftime("%d/%m/%y - %H:%M:%S")
        }
