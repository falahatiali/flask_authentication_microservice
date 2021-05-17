from flask import Flask
from flask_restful import Api

from authz.config import Config

api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Load Configs
    api.init_app(app)
    return app