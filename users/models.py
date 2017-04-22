from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi import Schema, fields
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class CRUD:
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Users(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    middle_name = db.Column(db.String(200), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    password = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(200), nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'password':
                setattr(self, str(key), str(generate_password_hash(value)))
            else:
                setattr(self, str(key), str(value))

    def __repr__(self):
        return 'User #{} - {} {}'.format(
            self.id, self.first_name, self.last_name)


class UsersSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    middle_name = fields.String()
    male = fields.String()
    password = fields.String()
    city = fields.String()

    class Meta:
        type_ = 'user'
