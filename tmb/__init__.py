from flask import Flask
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "CHANGE ME"
babel = Babel(app)

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../tmb.db"
db = SQLAlchemy(app)

import tmb.models
import tmb.views
