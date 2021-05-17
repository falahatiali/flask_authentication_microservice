from flask import Flask
from flask_restful import Api

from authz.config import Config

api=Api()

from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Config loads
    api.init_app(app)
    return app