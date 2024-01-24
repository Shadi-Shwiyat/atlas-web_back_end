#!/usr/bin/env python3
'''Simple flask app'''
from flask import Flask, jsonify, request, abort, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


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
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''Uses email and password to log user in'''
    email = request.form.get('email')
    password = request.form.get('password')

    is_valid = AUTH.valid_login(email, password)

    if is_valid:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    '''Uses session id cookie to delete user session'''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('hello'))
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    '''Returns a user based on session id cookie'''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": f"{user.email}"}), 200
    else:
        abort(403)


@app.route('reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    '''Returns the users reset token'''
    email = request.form.get('email')
    try:
        user = AUTH._db.find_user_by(email=email)
        if user:
            reset_token = AUTH.get_reset_password_token()
            return jsonify({"email": f"{email}",
                            "reset_token": f"{reset_token}"}), 200
    except (NoResultFound, InvalidRequestError, ValueError):
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
