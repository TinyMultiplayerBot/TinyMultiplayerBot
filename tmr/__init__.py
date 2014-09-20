from flask import Flask
from flask.ext.babel import Babel

# Initialize the app
app = Flask(__name__)
babel = Babel(app)
