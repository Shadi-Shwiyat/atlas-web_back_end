#!/usr/bin/env python3
'''Simple flask app'''
from flask import Flask, jsonify, request, abort, make_response
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    '''Returns json paylod with message'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''Route that takes form data and registers users'''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        auth.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''Uses email and password to log user in'''
    email = request.form.get('email')
    password = request.form.get('password')

    is_valid = auth.valid_login(email, password)

    if is_valid:
        session_id = auth.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        return abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
