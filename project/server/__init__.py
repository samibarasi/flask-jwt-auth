# project/server/__init__.py
import os
import sys
from logging.config import dictConfig

from dotenv import load_dotenv

from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

# import eventlet

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

CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)

import project.server.ws.events

@app.route('/')
def hello():
    return render_template("index.html")

