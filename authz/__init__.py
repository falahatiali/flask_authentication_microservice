from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from authz.config import Config

api = Api()
db  = SQLAlchemy()
mg  = Migrate()
ma  = Marshmallow()


from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Config loads
    db.init_app(app)
    mg.init_app(app , db)
    ma.init_app(app)
    api.init_app(app)
    return app