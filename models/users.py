"""
This module contains the model object for users.
"""
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from utils.application_factories.database import db


class User(db.Model, UserMixin):
    """
    Postgres model for users
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(128))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)
