import os

from flask import Flask

from auth import auth
from doc import doc
from home import homes
from utils.application_factories.database import db
from services import user_service
from utils.application_factories.login import login_manager


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    db.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(homes)
    app.register_blueprint(auth)
    app.register_blueprint(doc)

    return app


@login_manager.user_loader
def load_user(user_id):
    return user_service.get_user_by_id(user_id)


def setup_database(app):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run(host="0.0.0.0")
