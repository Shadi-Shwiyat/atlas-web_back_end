#!/usr/bin/env python3
'''Basic flask app with one route'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    '''Basic initial route
    returns hello world'''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
