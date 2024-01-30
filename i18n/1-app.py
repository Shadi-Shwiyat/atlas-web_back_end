#!/usr/bin/env python3
'''Basic flask app with one route'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

babel.init_app(app)
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def hello():
    '''Basic initial route
    returns hello world'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
