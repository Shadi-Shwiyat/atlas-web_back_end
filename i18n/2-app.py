#!/usr/bin/env python3
'''Basic flask app with one route'''
from flask import Flask, render_template
from flask_babel import Babel
from requests import request


class Config:
    '''Setup configuration for flask babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Determine the best-matching language using request.accept_languages'''
    return request.accept_languages.best_match(app.config['BABEL_LANGUAGES'])


@app.route('/')
def hello():
    '''Basic initial route
    returns hello world'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
