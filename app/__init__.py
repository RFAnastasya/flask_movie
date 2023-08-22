from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

app = Flask(__name__)
app.config.from_object('config.Config')
BASEDIR = Path(__file__).parent
UPLOAD_FOLDER = BASEDIR / 'static' / 'images'

db = SQLAlchemy(app)

from . import models, views  #noqa
with app.app_context():
    db.create_all()
