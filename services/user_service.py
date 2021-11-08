"""
This module contains methods to interact with saved users
"""

from werkzeug.security import generate_password_hash

from utils.application_factories.database import db
from models.users import User


def get_user_by_username(username: str) -> User:
    """
    Gets user by their username
    :param username: Username
    :return: User
    """
    return User.query.filter_by(username=username).first()


def get_user_by_id(user_id: int) -> User:
    """
    Gets user by their id
    :param user_id: User id
    :return: User
    """
    return User.query.filter_by(id=user_id).first()


def create_new_user(username: str, password: str) -> User:
    """
    Creates new user
    :param username: Username
    :param password: Password
    :return: User
    """
    user = User(
        username=username,
        password=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    return user
