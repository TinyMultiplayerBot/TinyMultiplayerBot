from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash

from tmb import db

class User(db.Model):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True)
    email = Column(String(128), unique=True)
    password = Column(String(256))
    openid = Column(String(64), unique=True)

    def __init__(self, username, password, openid):
        self.username = username
        self.password = generate_password_hash(
            password=password,
            method="pbkdf2:sha512",
            salt_longth=128
        )
        self.openid = openid

    def __repr__(self):
        return "<User %s>" % self.username
