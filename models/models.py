from app import db
import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Contacts(db.Model):
    __tablename__ = "contacts"
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False, primary_key=True)
    sex = db.Column(db.String, nullable=False)
    add = db.Column(db.String, nullable=False)
    rel = db.Column(db.String, nullable=False)
    contact_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, name, phone, sex, add, rel):
        self.name = name
        self.phone = phone
        self.sex = sex
        self.add = add
        self.rel = rel


    def __repr__(self):
        return '<name {}'.format(self.name)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    contacts = relationship("Contacts", backref="user")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)