# project/server/__init__.py

import os
import sys

from dotenv import load_dotenv

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

load_dotenv()



print("FLASK_ENV: ", os.getenv('FLASK_ENV'))

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

@app.before_first_request
def before_first_request():
    app.logger.debug("main debug")
    app.logger.info("main info")
    app.logger.warning("main warning")
    app.logger.error("main error")
    app.logger.critical("main critical")

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)
