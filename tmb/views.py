from flask import g, render_template, request
from flask.ext.babel import gettext

from tmb import app, babel


@babel.localeselector
def get_locale():
    # This was taken from the flask-babel documentation
    user = getattr(g, 'user', None)

    if user is not None:
        return user.locale

    return request.accept_languages.best_match(['en'])

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
