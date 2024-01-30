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
babel.init_app(app, locale_selector=get_locale)


def get_locale():
    '''Determine the best-matching language using request.accept_languages'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    '''Basic initial route
    returns hello world'''
    home_title = 'title'
    home_header = 'header'
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
