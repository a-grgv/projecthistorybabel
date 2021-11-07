from werkzeug.security import generate_password_hash

from models.database import db
from models.users import User


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user_by_id(userid):
    return User.query.filter_by(id=userid).first()


def create_new_user(username, password):
    user = User(
        username=username,
        password=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    return user
