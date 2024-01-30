#!/usr/bin/env python3
'''Basic flask app with one route'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_locale


class Config:
    '''Setup configuration for flask babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    '''Determine the best-matching language using request.accept_languages'''
    locale = request.args.get('locale')
    if not locale or locale not in app.config['LANGUAGES']:
        # print('default locale is:',
        # request.accept_languages.best_match(app.config['LANGUAGES']))
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    else:
        # print('locale is:',locale)
        return locale


def get_user():
    '''Returns user dictionary'''
    login_as = request.args.get('login_as')
    if not login_as:
        # print('No user found stupid, try again')
        return None
    else:
        # print('user found:', login_as)
        return users.get(int(login_as))


babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    '''Task handled before route request made'''
    user = get_user()
    if user:
        g.user = user
        # print(g.user.name)


@app.route('/')
def hello():
    '''Basic initial route
    returns hello world'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
