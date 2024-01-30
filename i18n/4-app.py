#!/usr/bin/env python3
'''Basic flask app with one route'''
from flask import Flask, render_template, request
from flask_babel import Babel, _, get_locale


class Config:
    '''Setup configuration for flask babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    '''Determine the best-matching language using request.accept_languages'''
    locale = request.args.get('locale')
    if not locale or locale not in app.config['LANGUAGES']:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    else:
        return locale


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def hello():
    '''Basic initial route
    returns hello world'''
    home_title = 'title'
    home_header = 'header'
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
