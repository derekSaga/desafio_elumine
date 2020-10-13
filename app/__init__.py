from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(
    app, db, compare_type=True, comper_server_default=True, render_as_batch=False
)
api = Api(app)
ma = Marshmallow(app)

from .view import upload_view, user_view
from .model import user_model
