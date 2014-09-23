from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash

from tmb import db

class User(db.Model):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    steamid = Column(String(64), unique=True)

    @staticmethod
    def get_or_create(steamid):
        user = User.query.filter_by(steamid=steamid).first()
        if user is None:
            user = User()
            user.steamid = steamid
            db.session.add(user)
        return user

    def __repr__(self):
        return "<User %s>" % self.username
