from flask import g, request

from tmr import app, babel


@babel.localeselector
def get_locale():
    # This was taken from the flask-babel documentation
    user = getattr(g, 'user', None)

    if user is not None:
        return user.locale

    return request.accept_languages.best_match(['en'])


