from flask import Flask
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = "aosnetuhasoneuht"
babel = Babel(app)

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../tmb.db"
db = SQLAlchemy(app)

import tmb.models
import tmb.views
