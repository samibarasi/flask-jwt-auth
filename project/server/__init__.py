# project/server/__init__.py

import os
import sys
from logging.config import dictConfig

from dotenv import load_dotenv

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)


app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)
