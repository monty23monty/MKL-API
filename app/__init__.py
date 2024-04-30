from flask import Flask

from .extensions import api, db
from .resources import ns

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MKL.db'

    # Initialize the extensions
    api.init_app(app, version='0.1', title='MKL API', description='An API for the MKL database')
    db.init_app(app)

    #with app.app_context():
     #   db.create_all()

    # Add the namespace
    api.add_namespace(ns)

    return app