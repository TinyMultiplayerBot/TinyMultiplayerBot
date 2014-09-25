import re
import urllib2

from flask import g, json, render_template, redirect, request, session
from flask.ext.babel import gettext
from werkzeug import url_encode

from tmb import app, babel, db, oid
from tmb.models import User

_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')

def get_steam_userinfo(steamid):
    options = {
        'key' : "YOUR KEY HERE",
        "steamids" : steamid
    }
    url = 'http://api.steampowered.com/ISteamUser/' \
              'GetPlayerSummaries/v0001/?%s' % url_encode(options)
    info = json.load(urllib2.urlopen(url))
    return info['response']['players']['player'][0] or {}


@babel.localeselector
def get_locale():
    # This was taken from the flask-babel documentation
    user = getattr(g, 'user', None)

    if user is not None:
        return user.locale

    return request.accept_languages.best_match(['en'])

@app.route('/login')
@oid.loginhandler
def login():
    if getattr(g, 'user', None) is not None:
        return redirect(oid.get_next_url())
    return oid.try_login('http://steamcommunity.com/openid')

@oid.after_login
def create_or_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    g.user = User.get_or_create(match.group(1))
    steamdata = get_steam_userinfo(g.user.steamid)
    g.user.nickname = steamdata['personaname']
    db.session.commit()
    session['user_id'] = g.user.id
    return redirect(oid.get_next_url())

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(oid.get_next_url())

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
