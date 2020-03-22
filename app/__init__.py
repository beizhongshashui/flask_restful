from flask import Flask



def register_bluepeints(app):

    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/v1')
    print('register_bluepeints')

def register_plugin(app):
    from app.model.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    print('register_plugin')


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.secure')

    register_bluepeints(app)
    register_plugin(app)

    return app
